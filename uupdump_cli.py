from queue import Empty
import sys
from zipfile import ZipFile
import py7zr
import requests, re, os
from requests.models import HTTPError
from sys import platform

prefer_py7zr = False

# Welcome
print("UUPDump CLI\n")

# Definitions
API_URL = "https://api.uupdump.net/"
DOWNLOAD_PATH = None

# Figure out what OS the script is running on, and use that to determine the execution path
OS_StringName = "OS: "
if platform == "linux" or platform == "linux2":
    # Linux
    OS_StringName += "Linux ("+platform+")"
    DOWNLOAD_PATH = os.path.dirname(os.path.realpath(__file__)) + "/"
elif platform == "darwin":
    # OS X
    OS_StringName += "macOS X ("+platform+")"
    DOWNLOAD_PATH = os.path.dirname(os.path.realpath(__file__)) + "/"
elif platform == "win32":
    # Windows
    OS_StringName += "Windows ("+platform+")"
    DOWNLOAD_PATH = os.path.dirname(os.path.realpath(__file__)) + "\\"

print (OS_StringName) # Print the OS name

# Print the path where downloaded files will be saved
print ("Files will be downloaded to " + DOWNLOAD_PATH + "\n")

def HomePage():
    print("\n \nUUP Dump --------------------")
    print("1. Download latest update")
    if(AskRange(1,1) == "1"):
        LatestUpdatePage()

def LatestUpdatePage():
    print("\nGet Latest Update")
    release_type = AskForReleaseType()
    architecture = AskForArchitecture()
    def_language = AskForLanguage()
    print("Selected:", "ring=" + release_type, "arch=" + architecture)
    print("\nGetting update(s)...")

    # Start request
    payload = {'arch': architecture, 'ring': release_type}
    
    try:
        length = 0
        selectedId = ""
        latest_update_request = requests.get(API_URL+"/fetchupd.php", params=payload)
        response = latest_update_request.json()
        updates = response['response']['updateArray']

        while True:
            length = 0
            print("")
            for f in updates: 
                length += 1
                print (str(length) + ": " + f['updateTitle'], "("+f['foundBuild']+")")
            
            int_selection = int(AskRange(1, length))
            selectedUpdate = updates[int_selection-1]

            # Print summary of selected update
            print("")
            print("Selected:")
            print (selectedUpdate['updateTitle'])
            print("UUID: " + selectedUpdate['updateId'])
            print("Build "+ selectedUpdate['foundBuild'])
            print(""+ selectedUpdate['arch'])
            print("")

            if (AskYesNo("Is this correct? [y/n]: ") == True):
                selectedId = selectedUpdate['updateId']
                break
        
        # Get editions
        edition_count = 0
        print("Getting available editions...")
        request_payload = {'id': selectedId, 'lang': def_language}
        request_editions = requests.get(API_URL + "/listeditions.php", params=request_payload)
        response = request_editions.json()
        editions = response['response']['editionFancyNames']

        selectedEdition = ""

        while True:
            print("\nChoose Edition")
            print("1.", editions['CORE'])
            print("2.", editions['COREN'])
            print("3.", editions['PROFESSIONAL'])
            print("4.", editions['PROFESSIONALN'])

            int_selection = int(AskRange(1, 4))

            ed_sel = ""

            if(int_selection == 1):
                ed_sel = "CORE"
            if(int_selection == 2):
                ed_sel = "COREN"
            if(int_selection == 3):
                ed_sel = "PROFESSIONAL"
            if(int_selection == 4):
                ed_sel = "PROFESSIONALN"

            print("")
            print("Selected:", editions[ed_sel])
            # print("")

            if (AskYesNo("Is this correct? [y/n]: ") == True):
                selectedEdition = ed_sel
                break

        print("")
        print("Downloading converter...")
#autodl=2 : download aria2 package
#autodl=2 : download aria2 + convert package
        res = download(selectedId, def_language, selectedEdition)
        if(res != Empty):
            if(AskYesNo("Decompress and execute? [y/n]: ")):
                extract(res, True)
        # print (response)
        #link = response['response']['files']['string']['url']

    except HTTPError:
        print("Error connecting to the UUPDump API. Please try again later.")
        exit()

def download(id, language, edition):
    try:
        request_payload = {'id': id, 'pack': language, 'edition': edition, 'autodl':"2"}
        r = requests.get("https://uupdump.net/get.php", params=request_payload, allow_redirects=True)
        #print(r.url)
        d = r.headers['content-disposition']
        filename = re.findall("filename=(.+)", d)[0].replace('"', '')
        filepath = os.path.join(DOWNLOAD_PATH, filename)
        with open(os.path.join(DOWNLOAD_PATH, filename), 'wb') as f:
            f.write(r.content)
        return filepath
    except:
        return Empty

def extract(file, execute):
    if(file != Empty):
        if(prefer_py7zr):
            archive = py7zr.SevenZipFile(file, mode='r')
            archive.extractall(os.path.splitext(file)[0])
        else:
            sz = ZipFile(file)
            sz.extractall(os.path.splitext(file)[0])

        directory = os.path.splitext(file)[0]
        filepath = os.path.join(os.path.splitext(file)[0], getExFileForOS())

        if platform == "linux" or platform == "linux2" or platform == "darwin":
            # Linux or OS X
            os.system("chmod -R +rx " + directory)
            os.system(filepath)
        elif platform == "win32":
            # Windows
            os.startfile(filepath)
       
def AskYesNo(prompt):
    regexFN = re.compile('^(?:y|n)$', re.IGNORECASE)
    while True:
        answer = input(prompt)
        if regexFN.match(answer):
            break
        else:
            print("Invalid input.")

    if(answer == "Y" or answer == "y"):
        return True
    else:
        return False

def AskRange(minF, maxF):
    regexF = re.compile('^[1-' + str(maxF) + ']\S*$', re.IGNORECASE)
    while True:
        selection = input("Enter selection ["+str(minF)+"-"+str(maxF)+"]: ")
        if regexF.match(selection):
            break
        else:
            print("Invalid input.")
    return selection

def AskForLanguage():
    return "en-us"

def AskForReleaseType():
    print("\nChoose Release Type")
    print("1. Public Release")
    print("2. Release Preview")
    print("3. Beta Channel")
    print("4. Dev Channel")
    regexF = re.compile('^[1-4]\S*$', re.IGNORECASE)
    while True: 
        selection = input("Enter selection [1-4]: ")
        if regexF.match(selection):
            break
        else:
            print("Invalid input.")
    print("")
    if(selection == "1"):
        return "Retail"
    if(selection == "2"):
        return "ReleasePreview"
    if(selection == "3"):
        return "Beta"
    if(selection == "4"):
        return "Dev"

def AskForArchitecture():
    print("\nChoose Architecture")
    print("1. AMD64")
    print("2. x86")
    print("3. ARM64")
    print("4. All")
    regexF = re.compile('^[1-4]\S*$', re.IGNORECASE)
    while True: 
        selection = input("Enter selection [1-4]: ")
        if regexF.match(selection):
            break
        else:
            print("Invalid input.")
    print("")
    if(selection == "1"):
        return "amd64"
    if(selection == "2"):
        return "x86"
    if(selection == "3"):
        return "arm64"
    if(selection == "4"):
        return "all"

def getExFileForOS():
    if platform == "linux" or platform == "linux2":
        # linux
        return "uup_download_linux.sh"
    elif platform == "darwin":
        # OS X
        return "uup_download_macos.sh"
    elif platform == "win32":
        # Windows...
        return "uup_download_windows.cmd"

#----------------------------------
#------Everything starts here------
#----------------------------------

# Start by making sure we can connect to the API
print("Testing connection...")
try:
    # Attempt to get the API version
    test_request = requests.get(API_URL)

    # Check response code
    if test_request.status_code == 429:
        print("error\nYou are being rate limited. Try again later.")
        exit()

    # Get & print API version
    api_version = test_request.json()['response']['apiVersion']
    print("API version " + api_version)
    print("Returned response code", str(test_request.status_code))
    #HomePage()

    if(len(sys.argv) > 1):
        release_type = sys.argv[1]
        architecture = sys.argv[2]
        selectedEdition = sys.argv[3]

        payload = {'arch': architecture, 'ring': release_type}
        try:
            length = 0
            selectedId = ""
            latest_update_request = requests.get(API_URL+"/fetchupd.php", params=payload)
            response = latest_update_request.json()
            updates = response['response']['updateArray']
            length = 0
            print("")
            for f in updates: 
                length += 1
                print (str(length) + ": " + f['updateTitle'], "("+f['foundBuild']+")")
            selectedUpdate = updates[0]
            selectedId = selectedUpdate['updateId']
            print("")
            print(selectedId)
            print(selectedEdition)
            print(selectedUpdate)
            print("Downloading converter...")
            res = download(selectedId, 'en-us', selectedEdition)
            extract(res, True)
            # print (response)
            #link = response['response']['files']['string']['url']

        except HTTPError:
            print("Error connecting to the UUPDump API. Please try again later.")
            exit()
    else:
        LatestUpdatePage()

except HTTPError:
    print("error connecting\nCould not connect to the UUPDump API.")
    exit()