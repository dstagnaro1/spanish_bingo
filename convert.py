import glob, os
from PIL import Image

def convert():
    print("convert entered")
    # Get a list of all EPS files in the current directory

    # Define the directory path
    # eps_directory = os.path.join(os.getcwd(), "eps files")

    # Get a list of all EPS files inside the "eps_files" directory
    # all_files = glob.glob(os.path.join(eps_directory, "*.eps"))

    all_files = glob.glob("*.eps")
 
    # Iterate through the EPS files and convert them to PDF
    for image_eps in all_files:
        # Open the EPS file using Pillow (PIL)
        im = Image.open(image_eps)

        # Convert the image to the RGB mode
        rbg_im = im.convert('RGB')

        # Save the LAB mode image as a PDF file
        pdf_filename = image_eps.replace(".eps", ".pdf")
        rbg_im.save(pdf_filename)

    print("Conversion complete.")

if __name__ == "__main__":
    convert()