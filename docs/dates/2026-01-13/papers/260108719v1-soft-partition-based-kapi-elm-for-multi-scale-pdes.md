---
layout: default
title: Soft Partition-based KAPI-ELM for Multi-Scale PDEs
---

# Soft Partition-based KAPI-ELM for Multi-Scale PDEs
**arXiv**：[2601.08719v1](https://arxiv.org/abs/2601.08719) · [PDF](https://arxiv.org/pdf/2601.08719.pdf)  
**作者**：Vikas Dwivedi, Monica Sigovan, Bruno Sixou  

**一句话要点**：提出基于软分区的KAPI-ELM方法，以解决多尺度偏微分方程求解中的谱偏差和计算成本问题。

**关键词**：物理信息机器学习, 多尺度偏微分方程, 核自适应, 软分区, 极端学习机, 线性求解

## 3 点简述
- 现有物理信息机器学习方法在处理振荡、多尺度或奇异扰动PDE时，面临谱偏差、反向传播成本高和手动调参等挑战。
- KAPI-ELM通过软分区长度联合控制配置中心和核宽度，实现连续粗到细分辨率，无需傅里叶特征或硬边界。
- 在八个基准测试中，该方法匹配或超越先进PINN和TFC变体，仅需单次线性求解，展示了快速、架构无关的潜力。

## 摘要（原文）

> Physics-informed machine learning holds great promise for solving differential equations, yet existing methods struggle with highly oscillatory, multiscale, or singularly perturbed PDEs due to spectral bias, costly backpropagation, and manually tuned kernel or Fourier frequencies. This work introduces a soft partition--based Kernel-Adaptive Physics-Informed Extreme Learning Machine (KAPI-ELM), a deterministic low-dimensional parameterization in which smooth partition lengths jointly control collocation centers and Gaussian kernel widths, enabling continuous coarse-to-fine resolution without Fourier features, random sampling, or hard domain interfaces. A signed-distance-based weighting further stabilizes least-squares learning on irregular geometries. Across eight benchmarks--including oscillatory ODEs, high-frequency Poisson equations, irregular-shaped domains, and stiff singularly perturbed convection-diffusion problems-the proposed method matches or exceeds the accuracy of state-of-the-art Physics-Informed Neural Network (PINN) and Theory of Functional Connections (TFC) variants while using only a single linear solve. Although demonstrated on steady linear PDEs, the results show that soft-partition kernel adaptation provides a fast, architecture-free approach for multiscale PDEs with broad potential for future physics-informed modeling. For reproducibility, the reference codes are available at https://github.com/vikas-dwivedi-2022/soft_kapi

