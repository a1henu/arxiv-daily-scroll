---
layout: default
title: Free-RBF-KAN: Kolmogorov-Arnold Networks with Adaptive Radial Basis Functions for Efficient Function Learning
---

# Free-RBF-KAN: Kolmogorov-Arnold Networks with Adaptive Radial Basis Functions for Efficient Function Learning
**arXiv**：[2601.07760v1](https://arxiv.org/abs/2601.07760) · [PDF](https://arxiv.org/pdf/2601.07760.pdf)  
**作者**：Shao-Ting Chiu, Siu Wun Cheung, Ulisses Braga-Neto, Chak Shing Lee, Rui Peng Li  

**一句话要点**：提出Free-RBF-KAN，通过自适应径向基函数提升KAN的计算效率与精度平衡

**关键词**：Kolmogorov-Arnold网络, 径向基函数, 自适应网格, 函数逼近, 计算效率

## 3 点简述
- 原KAN使用B样条基函数导致计算开销大，RBF-KAN虽高效但精度不足
- Free-RBF-KAN引入自适应学习网格和可训练平滑度，动态对齐激活模式
- 实验显示在函数逼近、物理信息机器学习等任务中，精度媲美原KAN且训练推理更快

## 摘要（原文）

> Kolmogorov-Arnold Networks (KANs) have shown strong potential for efficiently approximating complex nonlinear functions. However, the original KAN formulation relies on B-spline basis functions, which incur substantial computational overhead due to De Boor's algorithm. To address this limitation, recent work has explored alternative basis functions such as radial basis functions (RBFs) that can improve computational efficiency and flexibility. Yet, standard RBF-KANs often sacrifice accuracy relative to the original KAN design. In this work, we propose Free-RBF-KAN, a RBF-based KAN architecture that incorporates adaptive learning grids and trainable smoothness to close this performance gap. Our method employs freely learnable RBF shapes that dynamically align grid representations with activation patterns, enabling expressive and adaptive function approximation. Additionally, we treat smoothness as a kernel parameter optimized jointly with network weights, without increasing computational complexity. We provide a general universality proof for RBF-KANs, which encompasses our Free-RBF-KAN formulation. Through a broad set of experiments, including multiscale function approximation, physics-informed machine learning, and PDE solution operator learning, Free-RBF-KAN achieves accuracy comparable to the original B-spline-based KAN while delivering faster training and inference. These results highlight Free-RBF-KAN as a compelling balance between computational efficiency and adaptive resolution, particularly for high-dimensional structured modeling tasks.

