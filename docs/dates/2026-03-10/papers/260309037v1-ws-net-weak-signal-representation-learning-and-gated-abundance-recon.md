---
layout: default
title: WS-Net: Weak-Signal Representation Learning and Gated Abundance Reconstruction for Hyperspectral Unmixing via State-Space and Weak Signal Attention Fusion
---

# WS-Net: Weak-Signal Representation Learning and Gated Abundance Reconstruction for Hyperspectral Unmixing via State-Space and Weak Signal Attention Fusion
**arXiv**：[2603.09037v1](https://arxiv.org/abs/2603.09037) · [PDF](https://arxiv.org/pdf/2603.09037.pdf)  
**作者**：Zekun Long, Ali Zia, Guanyiman Fu, Vivien Rolland, Jun Zhou  

**一句话要点**：提出WS-Net，通过状态空间建模和弱信号注意力融合解决高光谱解混中的弱信号崩溃问题。

**关键词**：高光谱解混, 弱信号增强, 状态空间模型, 注意力机制, 多分辨率编码, 丰度重建

## 3 点简述
- 核心问题：高光谱图像中弱光谱响应被主导端元和噪声掩盖，导致丰度估计不准确。
- 方法要点：结合多分辨率小波融合编码器、Mamba状态空间分支和弱信号注意力分支，自适应融合表示。
- 实验或效果：在模拟和真实数据集上优于六个基线，RMSE和SAD分别降低达55%和63%，低信噪比下保持稳定。

## 摘要（原文）

> Weak spectral responses in hyperspectral images are often obscured by dominant endmembers and sensor noise, resulting in inaccurate abundance estimation. This paper introduces WS-Net, a deep unmixing framework specifically designed to address weak-signal collapse through state-space modelling and Weak Signal Attention fusion. The network features a multi-resolution wavelet-fused encoder that captures both high-frequency discontinuities and smooth spectral variations with a hybrid backbone that integrates a Mamba state-space branch for efficient long-range dependency modelling. It also incorporates a Weak Signal Attention branch that selectively enhances low-similarity spectral cues. A learnable gating mechanism adaptively fuses both representations, while the decoder leverages KL-divergence-based regularisation to enforce separability between dominant and weak endmembers. Experiments on one simulated and two real datasets (synthetic dataset, Samson, and Apex) demonstrate consistent improvements over six state-of-the-art baselines, achieving up to 55% and 63% reductions in RMSE and SAD, respectively. The framework maintains stable accuracy under low-SNR conditions, particularly for weak endmembers, establishing WS-Net as a robust and computationally efficient benchmark for weak-signal hyperspectral unmixing.

