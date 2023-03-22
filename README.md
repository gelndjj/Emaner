# Emaner
_Emaner can batch rename your files. It also has the ability to replace any string you want in your files name using Regular Expressions._

```
88888888888                                                                  
88                                                                           
88                                                                           
88aaaaa     88,dPYba,,adPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88"""""     88P'   "88"    "8a ""     `Y8 88P'   `"8a a8P_____88 88P'   "Y8  
88          88      88      88 ,adPPPPP88 88       88 8PP""""""" 88          
88          88      88      88 88,    ,88 88       88 "8b,   ,aa 88          
88888888888 88      88      88 `"8bbdP"Y8 88       88  `"Ybbd8"' 88          
            
```

### SUMMARY
Emaner grabs files from a folder you select and then gives you the option to replace a character or a character sequence in the files name.<br />
The soft allows you to use Regular Expressions and has an windows showing you some examples to  use them.<br />
Finally you have the option to batch rename your files by typing the name you want; if the chosen name is identical to other files you are renaming, a number sequence will be added at final.<br />

### SCREENSHOTS

![Screenshot](https://github.com/gelndjj/Emaner/blob/main/img/main.png)

![Screenshot](https://github.com/gelndjj/Emaner/blob/main/img/main_browse.png)

### HOW IT WORKS 
1. Select a folder by clicking on the Browse button.
2. Type an string or an string sequence you want to change from the current file name in the Old String field.
3. And type the new string by which you want the file to be modified in the New String field.
4. Click on Replace, the result is automatically shown in the window above. 

* In the example below, we replace the string "Screenshot" by "Capture".

![Screenshot](https://github.com/gelndjj/Emaner/blob/main/img/main_replace_1.png)

![Screenshot](https://github.com/gelndjj/Emaner/blob/main/img/main_replace_2.png)

### USING REGULAR EXPRESSIONS
The soft contains instructions to get familiar with RE; click on the Regular Exp. Examples button to display them.<br />

![Screenshot](https://github.com/gelndjj/Emaner/blob/main/img/re_examples.png)

We can use them the same way than replacing a string or an sequence in the file name.<br />

* Here is an example using RE to replace a pattern.<br /> 
The pattern will be represented as an hour format "HH.MM.SS"<br />
According to the instructions the RE will be:<br /><br />

> \d{2}\.\d{2}\.\d{2}<br />

>- \d{2} #look for 2 digits<br />
>- .\ #look for an '.'<br />


![Screenshot](https://github.com/gelndjj/Emaner/blob/main/img/main_re_1.png)

* Let's replace the above quoted pattern by the following {date}
  
> \d{2}\.\d{2}\.\d{2}<br />

> {date}<br/>
> 
![Screenshot](https://github.com/gelndjj/Emaner/blob/main/img/main_re2.png)

### BATCH RENAME FEATURE
On the last field, type a name you want your files to have and click on the rename button.<br />
All the present files will be named with this name and a number will be added at final.

* Here is an example below where "Capture" will be the new name of every files. 

![Screenshot](https://github.com/gelndjj/Emaner/blob/main/img/main_rename_1.png)

![Screenshot](https://github.com/gelndjj/Emaner/blob/main/img/main_rename_2.png)

### ROLLBACK BUTTON

If you made a mistake renaming a file, click on the button Rollback and it will reverse the action.<br />
##### However, it only works with the first Replace feature so far.<br />

### REQUIREMENTS INSTALLATION

> pip install requirements.txt