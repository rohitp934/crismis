# crismis
CRISMIS
Implemented using Python 3.

This project is to detect Cosmic Ray Artifacts in interstellar imagery, taken by the NASA Messenger expedition of Mercury.
This is implemented using a Neural Network to classify the images into two classes, yes, or no. Where yes denotes that there are cosmic ray artifacts in the image.

## Step 1: Collecting the data
We use beautiful soup to scrape the images from the NASA public dataset.

## Step 2: Plot the images to verify they are not corrupted
We use a module called RasterIO for python to display the images as a plot using Matplotlib, since the image data are in the form of .IMG files.

## Step 3: Creating the Dataset
We need to sort the dataset into train and test splits and place them in their respective class label.
The initial idea was to use Manual Annotation, but there was a new Module called Astroscrappy which is based on this research paper: https://arxiv.org/pdf/1909.01929.pdf

## Step 4: Training the Neural Network
We use Keras to create a CNN to classify the images.

## Future updates: 
Making a web dashboard to test the model on user input images.

