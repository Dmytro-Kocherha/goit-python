import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
OTHER = []
UNKNOWN = set()
EXTENSION = set()

REGISTERED_EXTENSIONS = {
    'JPEG' : JPEG_IMAGES,
    'JPG' : JPG_IMAGES,
    'PNG' : PNG_IMAGES,
    'SVG' : SVG_IMAGES
}




def get_extension(file_name) -> str:
    return Path(file_name).suffix[1:].upper()


def scan(folder: Path):
    for item in folder.interdir():
        if item.is_dir():
            scan(item)
            continue
        extension = get_extension(item.name)
        new_name = folder / item.name
        if not extension:
            OTHER.append(new_name)
        else:
            try:
                current_container = REGISTERED_EXTENSIONS[extension]
                EXTENSION.add(extension)
                current_container.append(new_name)
            except KeyError:
                UNKNOWN.add(extension)
                OTHER.append(new_name)
            

if __name__ == '__main__':
    scan_path = sys.argv[1]
    print(f'Starts in folder {scan_path}')

    search_folder = Path(scan_path)
    scan(search_folder)
    print(f'Images JPEG: {JPEG_IMAGES}')
    print(f'Images JPG: {JPG_IMAGES}')
    print(f'Images SVG: {SVG_IMAGES}')
    print(f'Images PNG: {PNG_IMAGES}')
    print(f'Unknown files: {OTHER}')
    print(f'There are file of types: {EXTENSION}')
    print(f'Unknown files: {OTHER}')
