---
layout: default
title: Deep Learning-Driven Inversion Framework for Shear Modulus Estimation in Magnetic Resonance Elastography (DIME)
---

# Deep Learning-Driven Inversion Framework for Shear Modulus Estimation in Magnetic Resonance Elastography (DIME)
**arXiv**：[2512.13010v1](https://arxiv.org/abs/2512.13010) · [PDF](https://arxiv.org/pdf/2512.13010.pdf)  
**作者**：Hassan Iftikhar, Rizwan Ahmad, Arunark Kolipaka  

**一句话要点**：提出深度学习驱动的反演框架DIME，以增强磁共振弹性成像中剪切模量估计的鲁棒性。

**关键词**：磁共振弹性成像, 剪切模量估计, 深度学习反演, 有限元模拟, 鲁棒性增强

## 3 点简述
- 核心问题：传统MMDI算法基于均匀介质假设，对噪声敏感，影响刚度估计的准确性。
- 方法要点：DIME基于有限元模拟生成的位移场-刚度图对训练，采用小图像块捕获局部波行为，提升鲁棒性。
- 实验或效果：在合成和真实肝脏数据中，DIME相比MMDI显示更高相关性、更低偏差和更准确边界描绘。

## 摘要（原文）

> The Multimodal Direct Inversion (MMDI) algorithm is widely used in Magnetic Resonance Elastography (MRE) to estimate tissue shear stiffness. However, MMDI relies on the Helmholtz equation, which assumes wave propagation in a uniform, homogeneous, and infinite medium. Furthermore, the use of the Laplacian operator makes MMDI highly sensitive to noise, which compromises the accuracy and reliability of stiffness estimates. In this study, we propose the Deep-Learning driven Inversion Framework for Shear Modulus Estimation in MRE (DIME), aimed at enhancing the robustness of inversion. DIME is trained on the displacement fields-stiffness maps pair generated through Finite Element Modelling (FEM) simulations. To capture local wave behavior and improve robustness to global image variations, DIME is trained on small image patches. We first validated DIME using homogeneous and heterogeneous datasets simulated with FEM, where DIME produced stiffness maps with low inter-pixel variability, accurate boundary delineation, and higher correlation with ground truth (GT) compared to MMDI. Next, DIME was evaluated in a realistic anatomy-informed simulated liver dataset with known GT and compared directly to MMDI. DIME reproduced ground-truth stiffness patterns with high fidelity (r = 0.99, R^2 = 0.98), while MMDI showed greater underestimation. After validating DIME on synthetic data, we tested the model in in vivo liver MRE data from eight healthy and seven fibrotic subjects. DIME preserved physiologically consistent stiffness patterns and closely matched MMDI, which showed directional bias. Overall, DIME showed higher correlation with ground truth and visually similar stiffness patterns, whereas MMDI displayed a larger bias that can potentially be attributed to directional filtering. These preliminary results highlight the feasibility of DIME for clinical applications in MRE.

