# GPT OCR Entropy Analysis

**Python code for assessing GPT model uncertainty in mathematical OCR tasks via entropy analysis.**

## Introduction

This repository contains the Python scripts used in the research paper:

- **Title:** Assessing GPT Model Uncertainty in Mathematical OCR Tasks via Entropy Analysis
- **Author:** Alexei Kaltchenko
- **Journal:** Journal of Applied Mathematics and Computing (Submitted)

The project investigates the uncertainty of GPT models when extracting mathematical equations from images of varying resolutions and converting them into LaTeX code. By employing concepts of entropy and mutual information, we assess the model's uncertainty in this specialized OCR task.

## Prerequisites

- **Python 3.x**
- **Required Python libraries:**
  - `openai==1.51.2`
  - Any other dependencies specified in `requirements.txt`

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/YourUsername/gpt-ocr-entropy-analysis.git
   cd gpt-ocr-entropy-analysis
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Data Preparation

The images used in this study are derived from a publicly available PDF document on arXiv:

- **Title:** Asymptotic Equipartition Property for Nonidentically Distributed States
- **Authors:** Kun Wang, Xiaoming Sun
- **arXiv Link:** [arXiv:2106.13823](https://arxiv.org/abs/2106.13823)

### Steps to Recreate the Images:

1. **Download the PDF:**

   - Visit the arXiv page at [https://arxiv.org/abs/2106.13823](https://arxiv.org/abs/2106.13823).
   - Download the PDF file.

2. **Select the Relevant Page:**

   - Open the PDF and navigate to the page used in the experiments (e.g., **Page 3**).

3. **Convert the Page to Images:**

   - Use a PDF conversion tool (e.g., Adobe Acrobat, ImageMagick) to convert the selected page to JPEG format.
   - Perform the conversion at the following resolutions: **72, 96, 150, and 300 dpi**.
   - Save the images with descriptive filenames, such as `page3_72dpi.jpg`, `page3_96dpi.jpg`, etc.

4. **Place the Images in the Repository:**

    - Place the generated images inside the repository folder.

## Usage

1. **Set Up OpenAI API Access:**

   - Obtain an API key from OpenAI.
   - Set the API key as an environment variable or include it in a configuration file as required by the code.

2. **Run the Script:**

   ```bash
   python image-entropy.py
   ```


3. **Results:**

   - The script will perform entropy analysis on the GPT model outputs for the given images.
   - Results will be displayed in the console or saved to output files, as configured.



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

The data used in this study are derived from:

- **Title:** Asymptotic Equipartition Property for Nonidentically Distributed States
- **Authors:** Kun Wang, Xiaoming Sun
- **arXiv Link:** [https://arxiv.org/abs/2106.13823](https://arxiv.org/abs/2106.13823)

The use of this material is for research and educational purposes.

## Contact Information

For any questions or issues, please contact:

- **Author:** Alexei Kaltchenko
- **Email:** [akaltchenko@wlu.ca](mailto:akaltchenko@wlu.ca)
