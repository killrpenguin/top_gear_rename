import os
import subprocess
from dataclasses import dataclass


@dataclass
class Episode:
   season: str
   ep_num: str
   title: str


@dataclass
class File:
    parent_dir: str
    file_nm: str

 
episode_obj = {}
folders_obj = {}
hm = os.path.expanduser('~/Videos/Top_Gear')

sub_folders = []
folders = os.listdir(hm)
folders = [a for a in folders if "Season" in a]
folders = sorted([int(a[7:]) for a in folders]) 
folders = [f'Season_{a}' for a in folders]
 
for folder in folders:
    contents = os.listdir(f'{hm}/{folder}')
    contents = [a for a in contents if ".vsmeta" not in a]
    contents = [a.split('.') for a in contents]
    contents = sorted([int(a[0]) for a in contents])
    contents = [f'{a}.mp4' for a in contents]
    sub_folders.extend(contents)

with open('TG_names', "r") as file:
    labels = file.read().strip().split('\n')

    
for item in labels:
    label = item.split(',')
    episode_obj.update({label[0] :
                        Episode(
                            season=label[1],
                            ep_num=label[2],
                            title=label[4]
                        )
                        })

for item in labels:
    label = item.split(',')
    folders_obj.update({label[0]:
                        File(
                            parent_dir="",
                            file_nm="",
                        )
                        })


if __name__ == '__main__':
    pass
