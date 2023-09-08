# Facefusion-Bulk

This repository contains Python scripts designed to automate bulk face swapping operations using a running instance of the [Facefusion](https://github.com/facefusion/facefusion) application. It leverages SeleniumBase to programmatically control the web UI, enabling users to process a large number of target images against a single source image without manual intervention.

## Features

-   **Bulk Processing**: Automate face swapping for an entire directory of target images.
-   **Web Automation**: Uses SeleniumBase to interact with the Facefusion Gradio web interface.
-   **Configurable Settings**: The script sets options like Face Enhancer, Frame Enhancer, and output quality before starting the process.
-   **File Renaming Utility**: Includes a helper script to sequentially rename image files for organized processing.

## Files

-   `Facefusion.py`: The main automation script. It navigates to the Facefusion URL, uploads a source image, and then iterates through a directory of target images, performing a face swap for each one.
-   `Rename.py`: A utility script to rename all `.jpeg` files in a directory to a sequential format (e.g., `1.jpeg`, `2.jpeg`, `3.jpeg`, etc.).

## Prerequisites

-   Python 3.x
-   A running instance of Facefusion accessible via a URL.
-   `seleniumbase` library. Install it via pip:
    ```bash
    pip install seleniumbase
    ```

## Setup and Usage

### 1. Prepare Your Images

-   Create a directory for your target images (the images you want to swap faces onto).
-   Place a single source image (the face you want to use) in a separate, easily accessible location.

### 2. Rename Target Images (Optional)

The `Facefusion.py` script processes files sorted by name. To ensure a predictable order, you can use the `Rename.py` utility.

1.  Copy `Rename.py` into the directory containing your target `.jpeg` images.
2.  Navigate to that directory in your terminal.
3.  Run the script:
    ```bash
    python Rename.py
    ```
    This will rename your files to `1.jpeg`, `2.jpeg`, and so on.

### 3. Configure the Automation Script

Open `Facefusion.py` in a text editor and modify the following variables:

1.  **Facefusion URL**: Change the placeholder URL to the live URL of your Facefusion instance.
    ```python
    self.open("https://Your facefusion url/")
    ```

2.  **Source Image Path**: Update `file_path1` with the absolute path to your source image.
    ```python
    # Example for Windows
    file_path1 = r"C:\path\to\your\source_face.png"
    # Example for macOS/Linux
    # file_path1 = r"/path/to/your/source_face.png"
    ```

3.  **Target Directory Path**: Update `target_dir` with the absolute path to the folder containing your target images.
    ```python
    # Example for Windows
    target_dir = r"C:\path\to\your\target_images\"
    # Example for macOS/Linux
    # target_dir = r"/path/to/your/target_images/"
    ```

### 4. Run the Script

Execute the script from your terminal. SeleniumBase will launch a browser, connect to the Facefusion instance, and begin the automation process.

```bash
python Facefusion.py
```

The script will:
- Enable the "face_enhancer" and "frame_enhancer".
- Set the pixel boost to "1024x1024".
- Upload the source image.
- Loop through each target image, upload it, set output quality to 100, and click the start/download buttons.

### Important Notes

-   **UI Selectors**: This script relies on component IDs (e.g., `button#component-113`) from the Gradio interface. If your version of Facefusion has a different UI layout, these selectors might need to be updated. You can find the correct selectors using your browser's developer tools.
-   **Processing Time**: The `sleep()` timers are included to give the web application time to process uploads and generate images. You may need to adjust these values based on your machine's performance and network speed.
-   **Google Colab**: As noted in the script, this workflow is well-suited for environments like Google Colab. Mounting your Google Drive allows the output files to be saved directly to cloud storage.
