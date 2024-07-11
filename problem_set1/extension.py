file_name = input("File name:")
file_name = file_name.lower()
if ".gif" in file_name:
    print("image/gif")
elif ".jpg" in file_name:
    print("image/jpeg")
elif ".png" in file_name:
    print("image/png")
elif ".txt" in file_name:
    print("text/txt")
else:
    print("application/octet-stream")