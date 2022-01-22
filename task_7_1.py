import os


with open('task1.cfg', 'r', encoding='utf-8') as f1:
    folders_list = f1.readlines()
root_folder = ''
for folder in folders_list:
    folder = folder.strip('\n')
    if folder[0] != '-':
        root_folder = folder
    else:
        folder = os.path.join(root_folder, folder.strip('-'))
    if not os.path.exists(folder):
        os.mkdir(folder)
