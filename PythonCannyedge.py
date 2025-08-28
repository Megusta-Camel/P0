
#Dette script implementerer en simpel Canny edge detection-algoritme ved hjælp af OpenCV. 
#Canny edge detection bruges til at identificere kanter i billeder
#Der gør det nemmere at object detection og image segmention.
#ved at analysere ændringer i pixelintensitet.
#Jeg brugte det fordi jeg var nysgerrig på, ift kongekronerne p0 projektet om man kunne  
#identificere dem på billederne sammen med den gulebaggrund. 


#Der er en trackbars til dynamisk at justere minimums- og maksimumsværdierne for Canny edge detection.

#inspiration fra
#https://www.youtube.com/watch?v=PS7zHKwXWRM
#  
#
import cv2 as cv
import os

# Define a callback function for the trackbars
def callback(x):
    pass

def cannyEdge():
    # Construct the image path
    root = os.getcwd()
    image_path = os.path.join(root, 'P0', '27.jpg')

    # Load the image
    img = cv.imread(image_path, cv.IMREAD_GRAYSCALE)  # Load as grayscale for Canny edge detection
    if img is None:
        print(f"Error: Image not found at {image_path}")
        return

    # Create a window and trackbars
    winname = 'Canny'
    cv.namedWindow(winname)
    cv.createTrackbar('minVal', winname, 0, 255, callback)
    cv.createTrackbar('maxVal', winname, 0, 255, callback)

    while True:
        # Exit the loop if 'q' is pressed
        if cv.waitKey(1) == ord('q'):
            break

        # Get the trackbar positions
        min_val = cv.getTrackbarPos('minVal', winname)
        max_val = cv.getTrackbarPos('maxVal', winname)

        # Apply Canny edge detection
        edges = cv.Canny(img, min_val, max_val)

        # Display the edges
        cv.imshow(winname, edges)

    # Destroy all OpenCV windows
    cv.destroyAllWindows()

# Ensure the function runs only when the script is executed directly
if __name__ == "__main__":
    cannyEdge()