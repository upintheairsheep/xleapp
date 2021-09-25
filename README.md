# xLEAPP
iOS Logs, Events, And Plists Parser  
Details in blog post here: https://abrignoni.blogspot.com/2019/12/xleapp-ios-logs-events-and-properties.html

Supports iOS/iPadOS 11, 12, 13 and 14.
Select parsing directly from a compressed .tar/.zip file, or a decompressed directory, or an iTunes/Finder backup folder.

## Features

Parses:  
&#9881; Mobile Installation Logs  
&#9881; iOS 12 & 13 Notifications  
&#9881; Build Info (iOS version, etc.)  
&#9881; Wireless cellular service info (IMEI, number, etc.)  
&#9881; Screen icons list by screen and in grid order.  
&#9881; ApplicationState.db support for app bundle ID to data container GUID correlation.   
&#9881; User and computer names that the iOS device connected to. Function updated by Jack Farley (@JackFarley248, http://farleyforensics.com/).  
&#9881; KnowledgeC + Powerlog artifacts.
And many, many more...


## Pre-requisites:
This project requires you to have Python > 3.7.4 installed on your system. **Ideally use Python 3.9 (significantly faster processing!)**

## Installation

To install dependencies, run:

```
pip install -r requirements.txt
```

To run on **Linux**, you will also need to install `tkinter` separately like so:

```
sudo apt-get install python3-tk
```

## Compile to executable

To compile to an executable so you can run this on a system without python installed.

To create xleapp.exe, run:

```
pyinstaller --onefile xleapp.spec
````

To create xleappGUI.exe, run:

```
pyinstaller --onefile --noconsole xleappGUI.spec
```

## Usage

### CLI

```
$ python xleapp.py -t <zip | tar | fs | gz | itunes> -i <path_to_extraction> -o <path_for_report_output>
```

### GUI

```
$ python xleappGUI.py 
```

### Help

```
$ python xleapp.py --help
```

The GUI will open in another window.  <br><br>


## Acknowledgements

This tool is the result of a collaborative effort of many people in the DFIR community.

This product includes software developed by Sarah Edwards (Station X Labs, LLC, @iamevltwin, mac4n6.com) and other contributors as part of APOLLO (Apple Pattern of Life Lazy Output'er).
