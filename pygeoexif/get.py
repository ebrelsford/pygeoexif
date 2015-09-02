from PIL.ExifTags import TAGS, GPSTAGS


def get_exif_data(image):
    """
    Returns a dictionary from the exif data of an PIL Image item. Also 
    converts the GPS Tags
    """
    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for t in value:
                    sub_decoded = GPSTAGS.get(t, t)
                    gps_data[sub_decoded] = value[t]
                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value
    return exif_data


def _to_degrees(value):
    """
    Helper function to convert the GPS coordinates stored in the EXIF to 
    degrees in float format
    """
    (degrees, minutes, seconds) = value
    d = float(degrees[0]) / float(degrees[1])
    m = float(minutes[0]) / float(minutes[1])
    s = float(seconds[0]) / float(seconds[1])
    return d + (m / 60.0) + (s / 3600.0)


def get_lat_lon(exif_data):
    """
    Returns the latitude and longitude, if available, from the provided 
    exif_data (obtained through get_exif_data above)
    """
    try:
        gps_info = exif_data['GPSInfo']

        lat = _to_degrees(gps_info['GPSLatitude'])
        if gps_info['GPSLatitudeRef'] == "S":                     
            lat = -lat

        lon = _to_degrees(gps_info['GPSLongitude'])
        if gps_info['GPSLongitudeRef'] == "W":
            lon = -lon
        return lat, lon
    except KeyError:
        return None, None
