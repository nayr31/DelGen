import os, json
from packaging.version import Version

home_dir = os.getcwd()
filesHere = os.listdir()
filesHere.remove("DelGen.py")

print("Working in " + home_dir)

dependencies = {
    "h3vr.otherloader.deli": "0.3.0",
    "h3vr.tnhtweaker.deli": "1.6.7"
}

str = """
{
    "guid": "",
    "version": "",
    "require": "0.4.1",
    "dependencies": {
    },
    "name": "",
    "description": "",
    "authors": [
    ],
    "assets": {
    }
}
"""

json_data = json.loads(str)

print()
string_name = input("Please input the name of your mod: ")
string_description = input("Please input a description: ")

list_authors = []
print("\nPlease list authors of the mod. Type \"0\" to stop listing authors.")
while True:
    string_author = input()
    if string_author != "0":
        list_authors.append(string_author)
    else:
        break

if list_authors.count != 0:
    string_author = list_authors[0]
else:
    string_author = "unknown"

json_data["guid"] = "h3vr." + string_author + "." + string_name.replace(" ", "").lower()
json_data["authors"] = list_authors

print("Please input your mod version (x.x.x format)")
while True:
    string_version = input()
    try:
        Version(string_version)
        json_data["version"] = string_version
        break
    except:
        print("This is not a correct version string, try again.")

print("\nPlease select loading perameters for your files.\nFile list:")

print(filesHere)

for file in filesHere:
    print("Do you want to include \"" + file + "" if os.path.isfile(file) == True else "/" + "\"? (y/n)")
    while True:
        conf = input()
        if conf != "y" and conf != "n":
            print("Incorrect input, try again.")
        elif conf == "y":
            break
        elif conf == "n":
            continue
    filename = file
    print("Do you need to change the name of this? (only use for globing files in custom characters) (y/n)")
    while True:
        conf = input()
        if conf != "y" and conf != "n":
            print("Incorrect input, try again.")
        elif conf == "y":
            filename = input("Input glob: ")
            break
        elif conf == "n":
            break
    stage = input("Please select a loading stage. Otherloader items should be in runtime, character assets in runtime.\n[1] - \"patcher\"\n[2] - \"setup\"\n[3] - \"runtime\"\n")
    while True:
        if not (stage == "1" or stage == "2" or stage == "3"):
            print("Please input a valid number.")
        else:
            if stage == "1":
                stage = "patcher"
            elif stage == "2":
                stage = "setup"
            else:
                stage = "runtime"
            break
    asset_type = "unknown"
    print("What type of asset is this?\n[1] - Otherloader\n[2] - TnHTweaker (character)\n[3] - TnHTweaker (sosig)\n[4] - TnHTweaker (vault)")
    while True:
        conf = input()
        if conf <= "1" or conf > "4":
            print("Incorrect input, try again.")
        elif conf == "1":
            asset_type = "lmao"
            break
        elif conf == "2":
            asset_type = "lmao"
            break
        elif conf == "3":
            asset_type = "lmao"
            break
        elif conf == "4":
            asset_type = "lmao"
            break


    print("Adding \"" + filename + "\" to \"" + stage + "\" asset loading stage for \"" + asset_type + "\" loading method.")

print("Finished creating data, writing...")

input("Finished.")