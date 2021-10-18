# uupdump_cli
#### A simple experimental command-line-interface for UUP Dump written in Python that uses the UUP Dump JSON API.

[![Compile Python script](https://github.com/JosephM101/uupdump_cli/actions/workflows/python-compile.yml/badge.svg)](https://github.com/JosephM101/uupdump_cli/actions/workflows/python-compile.yml)

## Requirements
**Developed and tested on Python 3.8**

To install requirements, run `pip install requests` in your terminal of choice. If you get an error like `pip: command not found`, then try `pip3`instead.


## How to use

#### Simply run the script, and if UUPDump is not down (that happens sometimes), the script will display instructions to help you quickly get the update package you need.
All downloaded files will be saved in the same directory as the python script.

------

## Compiled Builds
GitHub Actions is set up to compile binaries for Windows, macOS and Linux. You can find them as downloadable artifacts [here](https://github.com/JosephM101/uupdump_cli/actions).

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
