import re


BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
END = '\033[0m'
BOLD = '\038[1m'
UNDERLINE = '\033[4m'
INVISIBLE = '\033[08m'
REVERCE = '\033[07m'


def sizeof_fmt(num, suffix='B'):
    # http://stackoverflow.com/questions/1094841/reusable-library-to-get-human-readable-version-of-file-size
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


IMAGE_TAG_PATTERN = r'(?P<image>[^:]+)(:)?(?P<tag>[^/:]*)'
PORT_PATTERN = r'(?P<source>\d+):(?P<dest>\d+)'


# return (registry, image, tag)
def parse_image_opt(option) -> (str, str, str):
    match = re.match(IMAGE_TAG_PATTERN, option)
    if not match:
        print('invalid image name')
        return None
    image = match.group('image')
    tag = match.group('tag') if match.group('tag') else 'latest'

    if '/' in image:
        last_idx = image.rfind('/')
        return image[:last_idx], image[last_idx + 1:], tag
    else:
        return 'library', image, tag
