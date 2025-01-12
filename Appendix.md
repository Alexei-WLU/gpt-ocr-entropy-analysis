<head>
  <script type="text/javascript" async
    src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
  </script>
</head>


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
