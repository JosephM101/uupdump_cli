# uupdump_cli
## NOTE:
As of December 17, 2022, this repository is, until further notice, not being maintained.
Not only has it been a while since I've worked on this project, but it seems as though uupdump.net has been a bit unstable, fairly frequently going offline. Unfortunately, these are issues that are out of my control, and that is why, at least until further notice, I will be archiving this repository. 
In the meantime, please do not try to use this tool. I'd suggest trying [gus33000's UUPMediaCreator](https://github.com/gus33000/UUPMediaCreator) tool.

<hr>

#### A simple experimental command-line-interface for UUP Dump written in Python that uses the UUP Dump JSON API.

[![Compile Python script](https://github.com/JosephM101/uupdump_cli/actions/workflows/python-compile.yml/badge.svg)](https://github.com/JosephM101/uupdump_cli/actions/workflows/python-compile.yml)

## Requirements
**Developed and tested on Python 3.8. Newer versions should work as well.** To check what version of Python you're running, open a terminal and type `python --version` or `python3 --version` (depending on your install). If Python is not installed on your machine, you can download it from the [official website](https://www.python.org/downloads/). Alternatively, you can [download an automatically compiled binary](#automatically-compiled-builds) of the script.

The script requires `requests`. To install the requirements, run `pip install requests` in your terminal of choice. If you get an error like `pip: command not found`, then try `pip3` instead.


## How to use

#### Simply run the script, and if UUPDump is not down (that happens sometimes), the script will display instructions to help you quickly get the update package you need.
All downloaded files will be saved in the same directory as the Python script.

------

## Automatically compiled builds
GitHub Actions is set up to compile binaries for Windows and Linux (macOS is not currently supported) using Nuitka. Useful if you don't have Python installed on your machine. You can find the binaries as downloadable artifacts [here](https://github.com/JosephM101/uupdump_cli/actions).

------

# One-Line Run

To automate the download and execution process, you need to call the script from a terminal. In that terminal, enter the following:
`python uupdump_cli.py [arguments]` See [Arguments](#arguments) below.

## Arguments

#### You can pass through arguments to the script to make the download process autonomous, but they must all be used for proper functionality. The arguments are as follows, respectively:

### **Ring**
  Accepted input: `Dev`, `Beta`, `ReleasePreview`, `Retail`
  
### **Architecture**
  Accepted input: `amd64`, `x86`, `arm64`, `all`
  
### **Edition**
  Accepted input: `CORE`, `COREN`, `PROFESSIONAL`, `PROFESSIONALN
  
  
  For example, `uupdump_cli.py Dev amd64 PROFESSIONAL` would automatically download the latest update package from the Dev channel, and start the download process.
