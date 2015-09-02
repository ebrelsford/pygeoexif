pygeoexif
=========

A python module for reading latitude and longitude from an image's EXIF data.

Heavily based on [this gist](https://gist.github.com/erans/983821), packaged
here for ease of installation and use.

Requires PIL.


Install
-------

Use pip: `pip install pygeoexif`


Usage
-----

```python
from PIL import Image
from pygeoexif import get_exif_data, get_lat_lon

image = Image.open(<path_to_image>)
lat, lon = get_lat_lon(get_exif_data(image))
```


License
-------

MIT, as permitted by [this comment](https://gist.github.com/erans/983821#gistcomment-882766)
in the original.
