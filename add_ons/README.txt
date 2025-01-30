# A Guide To Making Add Ons

The structure of how your add on needs to be build is very percise and needs to be exactly how I describe it here (sorry about that).
The general rule is that all add ons are treated as python packages, so you should program you add_on with that in mind.

In order for an add_on to be considered a package, it must have an init file.
Currently as of 2025 Jan 18, the program requred you to put your "__init__.py" file in the closest possible space to the root of your add on as you can.

Heres an example:

add_ons/
├── Your Add On/
│   ├── __init__.py
│   ├── scripts
│   │   ├── main.py

The init file is the entry point into your code.


---!#RULES FOR UPLOADING FILES HERE#!---

THIS IS A CHECKLIST THAT YOU MUST FOLLOW BEFORE UPLOADING ANYTHING HERE

1. The file names in here cannot be already exisiting names. for example i named a file "test" but it doesent work since that already exists in python
2. All __init__ files should contain a function called "main"
3. Files posted in the add_ons folder may NEVER have invalid syntax. I tried to handle invalid syntax in the program but you cant even handle
  wrong syntax modules in python while importing

SOMETHING TO NOTE
  -The raw file takes a little bit of time to actually update so yeah keep that in mind
  -Github api can be a little slow to update stuff

  -It is safe for this txt file to be here because the program only looks for python files.

  -If you manually delete an add_on, and the add_on is still in the pycache folder, then if you make changes on the github website to the file and try to download again, changes will not be made,
  it will just load the pycache thing instead of actually donwloading it anew. This means that if we make a delete and update function, that we will have to either delete the enitire pycache folder, or just the cache file
  idk if this is true 100% tho. also maybe add to the clear command a clear chache option.
  