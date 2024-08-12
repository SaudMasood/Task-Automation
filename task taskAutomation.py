#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os
import shutil

def organize_files(source_dir):
    extensions = {
        'documents': ['.pdf', '.doc', '.docx', '.txt'],
        'images': ['.jpg', '.jpeg', '.png', '.gif'],
        'videos': ['.mp4', '.avi', '.mkv'],
        'audios': ['.mp3', '.wav'],
        'archives': ['.zip', '.rar'],
        'others': []
    }

    for file in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, file)):
            _, ext = os.path.splitext(file)
            ext = ext.lower()

            for category, ext_list in extensions.items():
                if ext in ext_list:
                    dest_dir = os.path.join(source_dir, category)
                    if not os.path.exists(dest_dir):
                        os.makedirs(dest_dir)
                    shutil.move(os.path.join(source_dir, file), os.path.join(dest_dir, file))
                    break
            else:
                dest_dir = os.path.join(source_dir, 'others')
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                shutil.move(os.path.join(source_dir, file), os.path.join(dest_dir, file))

    print("File organization completed.")

if __name__ == "__main__":
    source_directory = input("Enter the path of the directory to organize: ")
    organize_files(source_directory)


# In[16]:


import os
import shutil

def organize_files(source_dir):
    if not os.path.exists(source_dir):
        print(f"Error: Directory '{source_dir}' does not exist.")
        return
    
    extensions = {
        'documents': ['.pdf', '.doc', '.docx', '.txt'],
        'images': ['.jpg', '.jpeg', '.png', '.gif'],
        'videos': ['.mp4', '.avi', '.mkv'],
        'audios': ['.mp3', '.wav'],
        'archives': ['.zip', '.rar'],
        'others': []
    }

    try:
        for file in os.listdir(source_dir):
            if os.path.isfile(os.path.join(source_dir, file)):
                _, ext = os.path.splitext(file)
                ext = ext.lower()

                for category, ext_list in extensions.items():
                    if ext in ext_list:
                        dest_dir = os.path.join(source_dir, category)
                        if not os.path.exists(dest_dir):
                            os.makedirs(dest_dir)
                        shutil.move(os.path.join(source_dir, file), os.path.join(dest_dir, file))
                        print(f"Moved '{file}' to '{category}' directory.")
                        break
                else:
                    dest_dir = os.path.join(source_dir, 'others')
                    if not os.path.exists(dest_dir):
                        os.makedirs(dest_dir)
                    shutil.move(os.path.join(source_dir, file), os.path.join(dest_dir, file))
                    print(f"Moved '{file}' to 'others' directory.")

        print("File organization completed.")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    source_directory = input("Enter the full path of the directory to organize: ").strip()
    organize_files(source_directory)


# In[ ]:





# In[ ]:




