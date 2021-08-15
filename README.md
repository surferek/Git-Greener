# Git-Greener
#### A simple script that user can implement to control git contribution activity

----

### Requirements
Python 2.7 or higher  
`pip` installed  
`gitpython` library installed  
`git installed locally` 
( to install configure git locally follow the [tutorial](https://www.computerhope.com/issues/ch001927.htm) )  
Admin privileges 

### UPDATE (15.08.2021)  
As since 13.08.2021 you need to use github personal access token to perform remote operations.   
For your local purposes follow [PAT Create](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) tutorial

Once you generate your PAT token open `CMD` and run command within pattern below  
`git remote add origin https://[USERNAME]:[PAT TOKEN]@github.com/[USERNAME]/[REPO].git`

----
## Instruction

Go to `windows + R`  
Type `shell:startup`  
Create `wrapper.txt` file  
Add: `python path/to/script path/to/stampler`  
Rename file to `wrapper.bat` 