<head>
  <script type="text/javascript" async
    src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
  </script>
</head>

# GPT OCR Entropy Analysis

**Python code for assessing GPT model uncertainty in mathematical OCR tasks via entropy analysis.**

## Introduction

This repository contains the Python scripts used in the research paper:

- **Title:** Assessing GPT Model Uncertainty in Mathematical OCR Tasks via Entropy Analysis
- **Author:** Alexei Kaltchenko

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

# Appendix

## Experiment 1: 300 dpi Resolution

**Original document:** [arXiv:2106.13823] Page-3

**Image file:** `2106.13823v3-P3-300.jpg`

**Image resolution:** 300 dots per inch (dpi)

**Number of output tokens:** 453

**Total Entropy:** 7.77 bits

**Normalized Entropy:** 0.0171 bits

---

### Recognized Math Equations:

$$
Q(N, \rho, \epsilon) = \sum_{x \in \epsilon\text{-strong-typical}} |i_1\rangle \langle i_1| \otimes |i_2\rangle \langle i_2| \otimes \cdots \otimes |i_N\rangle \langle i_N|. \tag{11}
$$

$$
\text{tr} \left( Q(N, \rho, \epsilon) \rho^{\otimes N} \right) \geq 1 - \delta. \tag{12}
$$

$$
\text{tr} \left( Q(N, \rho, \epsilon) \rho^{\otimes N} \right) = \sum_{x \in \epsilon\text{-strong-typical}} P(i_1) P(i_2) \cdots P(i_N) = \sum_{x \in \epsilon\text{-strong-typical}} P(x). \tag{13}
$$

$$
\langle l \rangle = \sum_{i=1}^{D} p_i l_i = \sum_{i=1}^{D} p_i \log \frac{1}{q_i} = H(p, q). \tag{16}
$$

$$
H(p, q) \leq \langle l \rangle < H(p, q) + 1. \tag{17}
$$

$$
\sigma = \sum_{i=1}^{D} q_i |a_i\rangle \langle a_i|, \quad \rho = \sum_{i=1}^{D} p_i |b_i\rangle \langle b_i|, \quad \{q_i\} \neq \{p_i\}, \quad \{|a_i\rangle\} \neq \{|b_i\rangle\}. \tag{15}
$$

---

## Experiment 2: 150 dpi Resolution

**Original document:** [arXiv:2106.13823] Page-3

**Image file:** `2106.13823v3-P3-150.jpg`

**Image resolution:** 150 dpi

**Number of output tokens:** 434

**Total Entropy:** 12.28 bits

**Normalized Entropy:** 0.028 bits

---

### Recognized Math Equations:

$$
Q(N, \rho, \epsilon) = \sum_{|i\rangle \in \epsilon\text{-strong-typical}} |i_1\rangle \langle i_1| \otimes |i_2\rangle \langle i_2| \otimes \cdots \otimes |i_N\rangle \langle i_N|. \tag{11}
$$

$$
\text{tr} \left( Q(N, \rho, \epsilon) \rho^{\otimes N} \right) \geq 1 - \delta. \tag{12}
$$

$$
\text{tr} \left( Q(N, \rho, \epsilon) \rho^{\otimes N} \right) = \sum_{x \in \epsilon\text{-strong-typical}} P(i_1) P(i_2) \cdots P(i_N) = \sum_{x \in \epsilon\text{-typical}} P(x). \tag{13}
$$

$$
H(p, q) = \sum_{i=1}^{D} p_i \log \frac{1}{q_i} = H(q, p). \tag{16}
$$

$$
H(p, q) \leq \langle l \rangle < H(p, q) + 1. \tag{17}
$$

$$
\sigma = \sum_{i=1}^{D} q_i |a_i\rangle \langle a_i|, \quad \rho = \sum_{i=1}^{D} p_i |b_i\rangle \langle b_i|, \quad \{a_i\} \neq \{p_i\}, \quad \{a_i\} \neq \{b_i\}. \tag{15}
$$

---

## Experiment 3: 96 dpi Resolution

**Original document:** [arXiv:2106.13823] Page-3

**Image file:** `2106.13823v3-P3-96.jpg`

**Image resolution:** 96 dpi

**Number of output tokens:** 476

**Total Entropy:** 18.27 bits

**Normalized Entropy:** 0.038 bits

---

### Recognized Math Equations:

$$
Q(N, \rho, \epsilon) = \sum_{|i\rangle \, \epsilon\text{-strongly typical}} |i\rangle \langle i| \otimes |i_2\rangle \langle i_2| \otimes |i_N\rangle \langle i_N|. \tag{11}
$$

$$
\text{tr} \left( Q(N, \rho, \epsilon) \rho^{\otimes N} \right) \geq 1 - \delta. \tag{12}
$$

$$
\text{tr} \left( Q(N, \rho, \epsilon) \rho^{\otimes N} \right) = \sum_{x \, \epsilon\text{-strongly typical}} P(i_1) P(i_2) \cdots P(i_N) = \sum_{x \, \epsilon\text{-strongly typical}} P(x). \tag{13}
$$

$$
(1 - \delta)^2 2^{N(S(\rho) - \epsilon)} \leq T(N, \rho, \epsilon) \leq 2^{N(S(\rho) + \epsilon)}. \tag{14}
$$

$$
\sigma = \sum_{i=1}^{D} q_i |a_i\rangle \langle a_i|, \quad \rho = \sum_{i=1}^{D} p_i |b_i\rangle \langle b_i|, \quad \{q_i\} \neq \{p_i\}, \quad \{|a_i\rangle\} \neq \{|b_i\rangle\}. \tag{15}
$$

$$
l(x) = \left\lceil \log \frac{1}{q_x} \right\rceil = H(p, q). \tag{16}
$$

$$
H(p, q) \leq l(x) < H(p, q) + 1. \tag{17}
$$

---

## Experiment 4: 72 dpi Resolution

**Original document:** [arXiv:2106.13823] Page-3

**Image file:** `2106.13823v3-P3-72.jpg`

**Image resolution:** 72 dpi

**Number of output tokens:** 473

**Total Entropy:** 38.91 bits

**Normalized Entropy:** 0.082 bits

---

### Recognized Math Equations:

$$
Q(\mathcal{N}, \rho, \epsilon) = \sum_{k: \langle k | \rho | k \rangle \geq \epsilon} |k\rangle \langle k| \otimes |k\rangle \langle k| \otimes |k\rangle \langle k|. \tag{11}
$$

$$
\operatorname{tr} (Q(\mathcal{N}, \rho, \epsilon) \rho^{\otimes n}) \geq 1 - \delta. \tag{12}
$$

$$
\operatorname{tr} (Q(\mathcal{N}, \rho, \epsilon) \rho^{\otimes n}) = \sum_{x \in \epsilon\text{-strong-typical}} P(x) \cdot P(x) \cdot \ldots \cdot P(x) = \sum_{x \in \epsilon\text{-strong-typical}} P(x). \tag{13}
$$

$$
(1 - \delta) 2^{n(S(\rho) - \epsilon)} \leq P(\mathcal{N}, \rho, \epsilon) \leq 2^{n(S(\rho) + \epsilon)}. \tag{14}
$$

$$
\langle \ell \rangle = \sum_{x} P(x) \cdot \left\lceil \log \frac{1}{P(x)} \right\rceil = H(P, q). \tag{16}
$$

$$
H(q) \leq \langle \ell \rangle \leq H(q) + 1. \tag{17}
$$

$$
\sigma = \sum_{i} \lambda_{i} |\phi_{i}\rangle \langle \phi_{i}| = \sum_{i} p_{i} |\psi_{i}\rangle \langle \psi_{i}|. \tag{18}
$$
