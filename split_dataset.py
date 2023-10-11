import os
import shutil
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


BASE_DIR = os.path.join(BASE_DIR, 'dataset')
print(BASE_DIR)
def make_dir(folder_name):
    if not os.path.exists(os.path.join(BASE_DIR, folder_name)):
        os.makedirs(os.path.join(BASE_DIR, folder_name))
make_dir(os.path.join('train', 'images'))
make_dir(os.path.join('train', 'labels'))
make_dir(os.path.join('val', 'images'))
make_dir(os.path.join('val', 'labels'))

def split_files(folder_name):

    folder_path = os.path.join(BASE_DIR, folder_name)
    file_list = os.listdir(folder_path)
    
    for i, file_name in enumerate(file_list):
        if i % 10 == 0:
            shutil.copy(os.path.join(folder_path, file_name), os.path.join(BASE_DIR, os.path.join('val', folder_name)))
        else:
            shutil.copy(os.path.join(folder_path, file_name), os.path.join(BASE_DIR, os.path.join('train', folder_name)))
split_files('images')
split_files('labels')