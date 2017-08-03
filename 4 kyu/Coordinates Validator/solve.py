import re


def is_valid_coordinates(coordinates):
    try:
        lat, long = re.split(r', ?', coordinates)
        pattern = re.compile(r'[-+]?\d+\.?\d*')
        return re.fullmatch(pattern, lat) is not None and re.fullmatch(pattern, long) is not None and -90 <= float(lat) <= 90 and -180 <= float(long) <= 180
    except:
        return False
