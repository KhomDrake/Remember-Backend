import os
import base64


def image_as_base64(image_file):
    """
    :param `image_file` for the complete path of image.
    """
    if not os.path.isfile(image_file):
        return None

    encoded_string = ''
    with open(image_file, 'rb') as img_f:
        encoded_string = base64.b64encode(img_f.read())
    return encoded_string
