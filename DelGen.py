import os, json
from packaging.version import Version

home_dir = os.getcwd()
filesHere = os.listdir()
filesHere.remove("DelGen.py")

print("Working in " + home_dir)

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

json_data["name"] = string_name
json_data["description"] = string_description
json_data["guid"] = "h3vr." + string_author.replace(" ", "").lower() + "." + string_name.replace(" ", "").lower()
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

def add_asset_entry(stage, filename, asset_type):
    print("Adding \"" + filename + "\" to \"" + stage + "\" asset loading stage for \"" + asset_type + "\" loading method.")
    while True:
        try:
            json_data["assets"][stage].update({filename : asset_type})
            break
        except:
            json_data["assets"][stage] = { }

def add_assets_otherloader():
    json_data["dependencies"].update({ "h3vr.otherloader.deli": "0.3.0" })
    for file in filesHere:
        file_split = file.split(".")
        if len(file_split) == 1 and os.path.isfile(file):
            add_asset_entry("runtime", file, "h3vr.otherloader.deli:item") 

def add_assets_tnhtweaker():
    json_data["dependencies"].update({ "h3vr.tnhtweaker.deli": "1.6.7" })
    character_folder = ""
    for file in filesHere:
        if not os.path.isfile(file):
            character_folder = file
            break
    if character_folder == "":
        input("Could not find characer folder. Please make sure its next to me.")
        quit()
    else:
        print("Adding character folder...")
        add_asset_entry("setup", character_folder + "/", "h3vr.tnhtweaker.deli:character")
        add_asset_entry("setup", character_folder + "/*sosig*.json", "h3vr.tnhtweaker.deli:sosig")
        add_asset_entry("setup", character_folder + "/*vault*.json", "h3vr.tnhtweaker.deli:vault_file")

def add_assets_assembly():
    print("Adding assembly files...")
    for file in filesHere:
        file_split = file.split(".")
        try:
            if file_split[1] == "dll":
                add_asset_entry("setup", file, "deli:assembly")
        except:
            continue
    
prompt = True
while prompt:
    print("What kind of files do you need to add?\n[0] - Stop adding files\n[1] - Otherloader items\n[2] - TnHTweaker Character\n[3] - Assembly")
    while True:
        conf = int(input())
        if conf < 0 and conf > 3:
            print("Incorrect input, try again.")
        elif conf == 0:
            prompt = False
            break
        elif conf == 1:
            add_assets_otherloader()
            break
        elif conf == 2:
            add_assets_tnhtweaker()
            break
        elif conf == 3:
            add_assets_assembly()
            break

print("\nFinished creating data, writing...")

with open("manifest.json", "w+") as f:
    json.dump(json_data, f, indent=2)

input("Finished.")