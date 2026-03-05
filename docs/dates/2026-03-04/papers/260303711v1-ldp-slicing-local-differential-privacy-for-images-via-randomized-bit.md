---
layout: default
title: LDP-Slicing: Local Differential Privacy for Images via Randomized Bit-Plane Slicing
---

# LDP-Slicing: Local Differential Privacy for Images via Randomized Bit-Plane Slicing
**arXiv**：[2603.03711v1](https://arxiv.org/abs/2603.03711) · [PDF](https://arxiv.org/pdf/2603.03711.pdf)  
**作者**：Yuanming Cao, Chengqi Li, Wenbo He  

**一句话要点**：提出LDP-Slicing框架，通过位平面分解解决图像本地差分隐私应用中的高维效用损失问题。

**关键词**：本地差分隐私, 图像隐私保护, 位平面分解, 隐私预算分配, 感知混淆

## 3 点简述
- 核心问题：传统LDP机制应用于高维像素空间导致严重效用下降，阻碍图像隐私保护。
- 方法要点：将像素值分解为二进制位平面，结合感知混淆模块和隐私预算优化策略，实现像素级ε-LDP。
- 实验或效果：在人脸识别和图像分类任务中优于现有DP/LDP基线，计算开销可忽略。

## 摘要（原文）

> Local Differential Privacy (LDP) is the gold standard trust model for privacy-preserving machine learning by guaranteeing privacy at the data source. However, its application to image data has long been considered impractical due to the high dimensionality of pixel space. Canonical LDP mechanisms are designed for low-dimensional data, resulting in severe utility degradation when applied to high-dimensional pixel spaces. This paper demonstrates that this utility loss is not inherent to LDP, but from its application to an inappropriate data representation. We introduce LDP-Slicing, a lightweight, training-free framework that resolves this domain mismatch. Our key insight is to decompose pixel values into a sequence of binary bit-planes. This transformation allows us to apply the LDP mechanism directly to the bit-level representation. To further strengthen privacy and preserve utility, we integrate a perceptual obfuscation module that mitigates human-perceivable leakage and an optimization-based privacy budget allocation strategy. This pipeline satisfies rigorous pixel-level $\varepsilon$-LDP while producing images that retain high utility for downstream tasks. Extensive experiments on face recognition and image classification demonstrate that LDP-Slicing outperforms existing DP/LDP baselines under comparable privacy budgets, with negligible computational overhead.

