'''
SwitchFolderSorter
-------
Script that sorts Nintendo Switch Album files to picture and 
    video directories for .jpg and .mp4 files, respectively 

Assumes that switch_path directory is formatted in same order 
    as the Switch Album directory
'''

import os, shutil

if __name__ == '__main__':
    switch_path = "" # Replace with highest level directory path
    
    switch_video_path = "" # Replace with destination path for .mp4 files
    switch_picture_path = "" # Replace with destination path for .jpg files
    #os.chdir(switch_path) 
    #print(os.listdir())
    
    for month_dir in os.listdir(switch_path):
        #print(os.path.join(switch_path, month_dir))
        month_path = os.path.join(switch_path, month_dir)
        
        for day_dir in os.listdir(month_path):
            day_path = os.path.join(month_path, day_dir)
            
            for media_file in os.listdir(day_path):
                origin_media_path = os.path.join(day_path, media_file)
                
                if media_file.endswith(".jpg"):
                   
                    print("JPG: {}".format(media_file))
                    shutil.move(origin_media_path, os.path.join(switch_picture_path, media_file))
                elif media_file.endswith(".mp4"):
                    print("MP4: {}".format(media_file))
                    shutil.move(origin_media_path, os.path.join(switch_video_path, media_file))
    print("Done with sorting")
    #shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")