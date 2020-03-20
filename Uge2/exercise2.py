import utils

# 1.
utils.write_filenames("./", "folderfiles.csv")

# 2.
utils.write_all_filenames("./", "folderfiles2.csv")

# 3.
utils.print_first_line(["./folderfiles2.csv", "./folderfiles.csv", "./newfile.csv"])

# 4.
utils.print_email_lines(["./folderfiles2.csv", "./folderfiles.csv", "./file_containing_emails.csv"])

#5.
utils.write_headlines_to_file(["./utils.py", "./folderfiles.csv", "./file_containing_emails.csv"], "./headlinesfile.csv")