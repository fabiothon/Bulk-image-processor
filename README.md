# Bulk image processor
## Description

This Python script is designed for batch image processing. It identifies and processes all JPEG images in a specified folder, detects "blue" regions in the images, and replaces these regions with black pixels. The processed images are then saved to a designated output directory.

## Application Overview


This application automates the following tasks:

- Detects regions in images that match a specific "blue" color range.
- Changes the blue regions to black.
- Outputs the modified images into a new folder.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) and the provided requirments.txt file to install this script.

```bash
pip install -r /path/to/requirements.txt
`````

## Usage

1. Download of all necessary files (main.py, requirements.txt)
2. Install necessary libraries on your local environment or virtual environment via the requirement.txt
3. Run application

## Contributing

Pull requests are welcome! For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Licenses
This script uses the [MIT](https://choosealicense.com/licenses/mit/) License.
