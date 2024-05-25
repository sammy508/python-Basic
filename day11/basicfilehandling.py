
# import os

# def list_files_in_folder(folder_path):
#     try:
#         files = os.listdir(folder_path)
#         return files, None
#     except FileNotFoundError:
#         return None, "Folder not found"
#     except PermissionError:
#         return None, "Permission denied"

# def main():
#     folder_paths = input("Enter a list of folder paths separated by spaces: ").split()
    
#     for folder_path in folder_paths:
#         files, error_message = list_files_in_folder(folder_path)
#         if files:
#             print(f"Files in {folder_path}:")
#             for file in files:
#                 print(file)
#         else:
#             print(f"Error in {folder_path}: {error_message}")

# if __name__ == "__main__":
# #     main()




# # well structured format
# import os
# def file_list(folderpath):

#  try:
#   files = os.listdir(folderpath)
#  except PermissionError:
#   print(f"we don't have permission ")

# def main():
#  folderpath = input("enter folder name : ") .split()
#  print("Folder paths entered:", folderpath)

#  for folder in folderpath:
#   files, errormessage = file_list(folderpath)
  
#   if files :
#    file_list(folderpath)
#    for file in files:
#     print(file)
# main()    
