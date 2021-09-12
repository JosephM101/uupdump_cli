# uupdump_cli
#### A simple in-development command-line-interface for UUPDump written in Python that utilizes the UUPDump JSON API.

## Requirements
#### Developed and tested on Python 3.8
To install requirements, run `pip install requests` in your terminal of choice.

## How to use

#### Simply run the script, and if UUPDump is not down, the script will display instructions to help you quickly get the update package you need.

## Arguments

#### You can pass through arguments to the script to make it autonomous, but they must all be used. The arguments are as follows (in order):
- `Ring`
  
  Accepted input: `Dev`, `Beta`, `ReleasePreview`, `Retail`
  
- `Architecture`
  
  Accepted input: `amd64`, `x86`, `arm64`, `all`
  
- `Edition`

  Accepted input: `CORE`, `COREN`, `PROFESSIONAL`, `PROFESSIONALN
  
  
  For example, `uupdump_cli.py Dev amd64 PROFESSIONAL` would automatically download the latest update package from the specified update ring, and automatically start the download process.
