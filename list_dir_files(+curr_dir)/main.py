import os

cwd = os.getcwd()
print("The current working directory is:", cwd)

files_list = [
    f for f in os.listdir("/Users") if os.path.isfile(os.path.join("/Users", f))
]

print(f"\n {files_list}")
