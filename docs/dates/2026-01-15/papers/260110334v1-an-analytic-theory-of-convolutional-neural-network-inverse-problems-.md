---
layout: default
title: An analytic theory of convolutional neural network inverse problems solvers
---

# An analytic theory of convolutional neural network inverse problems solvers
**arXiv**：[2601.10334v1](https://arxiv.org/abs/2601.10334) · [PDF](https://arxiv.org/pdf/2601.10334.pdf)  
**作者**：Minh Hai Nguyen, Quoc Bao Do, Edouard Pauwels, Pierre Weiss  

**一句话要点**：提出局部等变最小均方误差理论以解析监督卷积神经网络在成像逆问题中的求解机制

**关键词**：卷积神经网络, 逆问题求解, 最小均方误差估计, 平移等变性, 局部性约束, 成像分析

## 3 点简述
- 核心问题：监督CNN在成像逆问题中缺乏理论理解，常被视为黑箱
- 方法要点：基于最小均方误差估计器，结合平移等变性和局部性约束推导解析公式
- 实验或效果：通过多实验验证理论匹配网络输出，并分析物理感知与物理无关估计器差异

## 摘要（原文）

> Supervised convolutional neural networks (CNNs) are widely used to solve imaging inverse problems, achieving state-of-the-art performance in numerous applications. However, despite their empirical success, these methods are poorly understood from a theoretical perspective and often treated as black boxes. To bridge this gap, we analyze trained neural networks through the lens of the Minimum Mean Square Error (MMSE) estimator, incorporating functional constraints that capture two fundamental inductive biases of CNNs: translation equivariance and locality via finite receptive fields. Under the empirical training distribution, we derive an analytic, interpretable, and tractable formula for this constrained variant, termed Local-Equivariant MMSE (LE-MMSE). Through extensive numerical experiments across various inverse problems (denoising, inpainting, deconvolution), datasets (FFHQ, CIFAR-10, FashionMNIST), and architectures (U-Net, ResNet, PatchMLP), we demonstrate that our theory matches the neural networks outputs (PSNR $\gtrsim25$dB). Furthermore, we provide insights into the differences between \emph{physics-aware} and \emph{physics-agnostic} estimators, the impact of high-density regions in the training (patch) distribution, and the influence of other factors (dataset size, patch size, etc).

