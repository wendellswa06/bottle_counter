import os
import albumentations as A
from pathlib import Path
import cv2
import glob


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

img_folder_path = './dataset/images/'
annot_folder_path = './dataset/labels/'

def transformer(img_folder_path, annot_folder_path):
    
    img_paths = Path(img_folder_path).glob('*.jpg')
    print('--------------------label path--------------------')
    for img_path in img_paths:
        # print(img_path)
        img_name = str(img_path).split('\\')[-1].split('.')[:-1]
        img_name = '.'.join(img_name)
        label_name = img_name + '.txt'
        label_path = annot_folder_path + label_name
        
        print(label_path)
        result = horizontalFlip(str(img_path), label_path, img_name)

    # return    
    print('--------------------------------------------------')
    return

def horizontalFlip(img_path, label_path, save_name):
    
    transformerHorizontalFlip = A.Compose([A.HorizontalFlip(always_apply=True)], bbox_params=A.BboxParams(format='yolo'))
    print(label_path)
    with open(label_path) as f:
        lines = f.readlines()
        
    bbox = []
    for line in lines:
        l = line.split(' ')
        bbox.append([float(l[1]), float(l[2]), float(l[3]), float(l[4]), float(l[0])])
        
    img = cv2.imread(img_path)
    
    try:
        trns = transformerHorizontalFlip(image=img, bboxes=bbox)
        print("------------------1------------------------")
        img_transformed = trns['image']
        boxes = trns['bboxes']
        print("------------------2------------------------")
        print(save_name)
        cv2.imwrite(os.path.join(img_folder_path, save_name+'_hf.jpg'), img_transformed)
        print("------------------3------------------------")
        with open(os.path.join('./labels', save_name+'_hf.txt'), 'w') as f:
            for box in boxes:
                f.write(str(box[-1]))
                f.write(' '+str(box[0]))
                f.write(' '+str(box[1]))
                f.write(' '+str(box[2]))
                f.write(' '+str(box[3]))
                f.write('\n')
        return
    except:
        print('Failed:', save_name)
        return
    # print(img_paths)
transformer(img_folder_path, annot_folder_path)