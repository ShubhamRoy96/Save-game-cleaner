import pathlib as p
import os
import shutil
import datetime
import sys

source = p.Path.cwd()
destination = source / 'remove this'
game_list = os.listdir(source)
# date = "2018-09-08"
print("Welcome to save game cleaner !")

try:
    year = int(input("Please enter the year of save games that you want to remove as YYYY (eg: 2018): "))
    month = int(input("Please enter the month of save games that you want to remove as mm (eg: 09): "))
    day = int(input("Please enter the day of save games that you want to remove as dd (eg: 08): "))
    date_info = datetime.datetime(year, month, day)
    date = date_info.strftime("%Y-%m-%d")
    print("Date entered : ", date)
except ValueError:
    print("Please enter correct date format!\nExiting the program...")
    sys.exit(1)

select = input("Enter d for permanently deleting the files or\nEnter m for moving file to temporary folder :\n")

if select == "d":
    for data in game_list:
        if date in data:
            source_file = source / data
            os.remove(source_file)
elif select == "m":
    try:
        p.Path.mkdir(destination, parents=True)
    except FileExistsError:
        print("Destination folder already exists!\nSkipping folder creation...")
        pass

    for data in game_list:
        if date in data:
            source_file = source / data
            destination_file = destination / data
            try:
                shutil.move(source_file, destination_file)
            except FileExistsError:
                print("File already exists !")
else:
    print("Incorrect value entered, exiting ... ")
    sys.exit(1)

print("Process finished !")
