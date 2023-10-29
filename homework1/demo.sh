#!/bin/bash
echo -e "a. List all files in the present working directory\n
b. Display today's date and time\n
c. Display whether a file is a \"simple\" file or a \"directory\"\n
d. Create a backup for a file\n
e. Start an ftp session\n
f. Start your LED control program\n
x. Exit\n
Please input a character to invoke an option: " 

read option

case $option in
    a)
        ls -al
        ;;
    b)
        date
        ;;
    c)
        echo "Please input a filename: "
        read filename
        if [ -d $filename ]; then
            echo $filename" is a directory"
        else
            echo $filename" is a simple file"
        fi
        ;;
    d)
        echo "Please input a filename: "
        read filename
        cp $filename "backup_"$filename
        ;;
    e)
        ftp
        ;;
    f)
        python draft.py
        ;;
    x)
        ;;
    esac