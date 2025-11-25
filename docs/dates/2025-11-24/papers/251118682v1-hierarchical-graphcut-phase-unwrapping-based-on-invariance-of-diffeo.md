---
layout: default
title: Hierarchical GraphCut Phase Unwrapping based on Invariance of Diffeomorphisms Framework
---

# Hierarchical GraphCut Phase Unwrapping based on Invariance of Diffeomorphisms Framework
**arXiv**：[2511.18682v1](https://arxiv.org/abs/2511.18682) · [PDF](https://arxiv.org/pdf/2511.18682.pdf)  
**作者**：Xiang Gao, Xinmu Wang, Zhou Zhao, Junqi Huang, Xianfeng David Gu  

**一句话要点**：提出基于微分同胚不变性的分层GraphCut相位展开框架，以提升实时3D扫描精度与速度

**关键词**：相位展开, GraphCut算法, 微分同胚不变性, 实时3D扫描, 像素标记, 多数投票融合

## 3 点简述
- 核心问题：相位展开因噪声和遮挡而病态，需从模2π值估计真实相位，现有方法难以兼顾速度与精度。
- 方法要点：将GraphCut重构为像素标记问题，利用微分同胚不变性，通过多数投票融合分层结果。
- 实验或效果：实验显示速度提升45.5倍且L2误差降低，适用于实时应用如4D面部动态捕捉。

## 摘要（原文）

> Recent years have witnessed rapid advancements in 3D scanning technologies, with applications spanning VR/AR, digital human creation, and medical imaging. Structured-light scanning with phase-shifting techniques is preferred for its use of low-intensity visible light and high accuracy, making it well suited for capturing 4D facial dynamics. A key step is phase unwrapping, which recovers continuous phase values from measurements wrapped modulo 2pi. The goal is to estimate the unwrapped phase count k in the equation Phi = phi + 2pi k, where phi is the wrapped phase and Phi is the true phase. Noise, occlusions, and complex 3D geometry make recovering the true phase challenging because phase unwrapping is ill-posed: measurements only provide modulo 2pi values, and estimating k requires assumptions about surface continuity. Existing methods trade speed for accuracy: fast approaches lack precision, while accurate algorithms are too slow for real-time use. To overcome these limitations, this work proposes a phase unwrapping framework that reformulates GraphCut-based unwrapping as a pixel-labeling problem. This framework improves the estimation of the unwrapped phase count k through the invariance property of diffeomorphisms applied in image space via conformal and optimal transport (OT) maps. An odd number of diffeomorphisms are precomputed from the input phase data, and a hierarchical GraphCut algorithm is applied in each domain. The resulting label maps are fused via majority voting to robustly estimate k at each pixel. Experimental results demonstrate a 45.5x speedup and lower L2 error in real experiments and simulations, showing potential for real-time applications.

