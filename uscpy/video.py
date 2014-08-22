"""
A collection of flags and functions for video input and output with OpenCV.
"""

import cv2

FORMAT_TABLE = {}

# RAW RGB format, BI_RGB, see http://www.fourcc.org/rgb.php
FORMAT_RAWRGB = 0x0
FORMAT_TABLE["rawrgb"] = FORMAT_RAWRGB

FORMAT_MJPEG = cv2.cv.FOURCC("m", "j", "p", "g")
FORMAT_TABLE["mjpeg"] = FORMAT_MJPEG

FORMAT_MPEG4 = cv2.cv.FOURCC("m", "4", "s", "2")
FORMAT_TABLE["mpeg4"] = FORMAT_MPEG4

# alternative mpeg4 outputs
FORMAT_FFMPEG_MPEG4 = cv2.cv.FOURCC("f", "m", "p", "4")
FORMAT_DIVX_MPEG4 = cv2.cv.FOURCC("d", "x", "5", "0")

FORMAT_H263 = cv2.cv.FOURCC("h", "2", "6", "3")
FORMAT_TABLE["h263"] = FORMAT_H263

FORMAT_H264 = cv2.cv.FOURCC("h", "2", "6", "4")
FORMAT_APPL_H264 = cv2.cv.FOURCC("a", "v", "c", "1")
FORMAT_TABLE["h264"] = FORMAT_H264

def fourcc(string):
    """
    Return the fourcc encoded integer for a fourcc string.

    Args:
        string: the fourcc string to encode. Must be 4 characters, typically
                tailing space padded.

    References:
     [1] http://www.fourcc.org/codecs.php
     [2] http://msdn.microsoft.com/en-us/library/cc250415.aspx
    """
    if len(string) != 4:
        raise Exception("Invalid fourcc string: '%s'" % string)
    return cv2.cv.FOURCC(string[0], string[1], string[2], string[3])
