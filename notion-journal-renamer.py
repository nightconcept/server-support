import os
from datetime import datetime


# handle parsing
# parser = argparse.ArgumentParser()
# parser.add_argument("path", help="path that will be renamed")
# args = parser.parse_args()
# print("Path to parse through: " + args.path)
# dirpath = args.path
# print(f"dirpath:{dirpath}")
# os.chdir(dirpath)

directory = os.fsencode(os.getcwd())

today = datetime.now()
today_str = str(today.strftime("%Y-%m-%d")).strip()

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".md"):
        print(f"filename:{filename}")
        with open(filename, encoding="utf-8") as filereader:
            # Extract date
            lines = filereader.readlines()
            date = ''
            new_date = ''
            new_file_name = ''
            for line in lines:
                if "Created: " in line:
                    date = line[9:].strip()
                    date_object = datetime.strptime(date, "%B %d, %Y %I:%M %p")
                    new_date = str(date_object.strftime("%Y-%m-%d")).strip()
                    new_file_name = new_date + ".md"
                    print(f"new_file_name:{new_file_name}")
                    break

            with open(new_file_name, "w", encoding="utf-8") as newfile:
                # Add frontmatter
                newfile.write("---\n")
                newfile.write(f"title: {new_date}\n")
                newfile.write("tags: my/journal\n")
                newfile.write(f"startDate: {new_date}\n")
                newfile.write(f"updated: {today_str}\n")
                newfile.write("---\n")
                for line in lines:
                    if not ("Created: " in line):
                        if not ("Tags: " in line):
                            newfile.write(line)