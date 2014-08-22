"""
Functions called on a per frame basis.
"""
import cv2

def greyscale(frame):
    """
    Returns a greyscale image from a color frame.
    """
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def cell_contours(frame, threshold=10):
    """
    Returns an array of polygons that contain the perimeter of cell contours.
    
    Args:
        frame: the cv2 greyscale image to process
        threshold: the absolute value to threshold the median

    NOTE: This method is a work in progress and may not provide robust results.

    The current process improves image contrast and attempts to remap the intensity
    values to an absolute range for thresholding. A median filter is applied before
    thresholding to reduce noise.

    After thresholding, a Canny edge detector is used and provides input into a 
    contour detector.

    References:
     [1] http://docs.opencv.org/doc/tutorials/imgproc/histograms/histogram_equalization/histogram_equalization.html
     [2] http://docs.opencv.org/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html#findcontours
    """
    height, width = frame.shape[0:2]
    image = cv2.equalizeHist(frame)
    image = cv2.medianBlur(image, 7)
    _, image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    edges = cv2.Canny(image, width, height)
    contours, heirarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours
