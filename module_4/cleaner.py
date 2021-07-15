import sys
from pathlib import Path


def sort():
    images, video, docs, music, archives = [], [], [], [], []
    try:
        p = Path()
        for i in p.iterdir():
            if i.suffix in ('.jpeg', '.png', '.jpg', '.svg'):
                images.append(i.name)
            elif i.suffix in ('.avi', '.mp4', '.mov', '.mkv'):
                video.append(i.name)
            elif i.suffix in ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'):
                docs.append(i.name)
            elif i.suffix in ('.mp3', '.ogg', '.wav', '.amr'):
                music.append(i.name)
            elif i.suffix in ('.zip', '.gz', '.tar'):
                archives.append(i.name)
            else:
                p = Path()
    except:
        IndexError
    print(images, video, docs, music, archives, sep = '\n')


if __name__ == '__main__':
    sort()
