# Image to ASCII art generator
This simple generator uses the OpenCV library to manipulate the image imput as a 2D matrix.

# The Process
After fetching the file path, we remove the double-quotes at the ends and feed the remaining string into the parameters of the imread function with 0 passed to represent only black-and-white form.

This function returns an OpenCV matrix of the image, containing the values of each pixel in range [0,255]

Corresponding to each member of the the matrix, print an appropriate ASCII character, as shown below

![pic](https://github.com/user-attachments/assets/086cecd4-5e29-439c-95f0-387d32e54ca5)


![66f8de4ecf1eb_download](https://github.com/user-attachments/assets/1a184482-da38-40fd-b940-b649cdfefd5a)
