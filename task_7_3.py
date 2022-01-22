import os
import shutil

prj_dir = 'my_project'
tmplts_dir = 'templates'

root_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), prj_dir)
template_dir = os.path.join(root_dir, tmplts_dir)

for root, dirs, files in os.walk(root_dir):
    for dr in dirs:
        if dr == 'templates':
            rel_path = os.path.join(root, dr)
            shutil.copytree(rel_path, template_dir, dirs_exist_ok=True)
