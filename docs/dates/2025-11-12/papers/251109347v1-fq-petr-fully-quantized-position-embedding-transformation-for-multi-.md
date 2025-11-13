---
layout: default
title: FQ-PETR: Fully Quantized Position Embedding Transformation for Multi-View 3D Object Detection
---

# FQ-PETR: Fully Quantized Position Embedding Transformation for Multi-View 3D Object Detection
**arXiv**：[2511.09347v1](https://arxiv.org/abs/2511.09347) · [PDF](https://arxiv.org/pdf/2511.09347.pdf)  
**作者**：Jiangyong Yu, Changyong Shu, Sifan Zhou, Zichen Yu, Xing Hu, Yan Chen, Dawei Yang  

**一句话要点**：提出FQ-PETR全量化框架以解决多视图3D检测部署中的精度与效率问题

**关键词**：多视图3D检测, 神经网络量化, 位置嵌入优化, 非线性算子近似, 自动驾驶视觉

## 3 点简述
- 核心问题：PETR系列模型量化后精度严重下降，源于多模态特征尺度差异和非线性算子量化误差
- 方法要点：引入量化友好位置嵌入、双查找表近似非线性函数、量化后数值稳定化
- 实验或效果：W8A8量化下精度损失仅1%，延迟降低75%，优于现有量化方法

## 摘要（原文）

> Camera-based multi-view 3D detection is crucial for autonomous driving. PETR and its variants (PETRs) excel in benchmarks but face deployment challenges due to high computational cost and memory footprint. Quantization is an effective technique for compressing deep neural networks by reducing the bit width of weights and activations. However, directly applying existing quantization methods to PETRs leads to severe accuracy degradation. This issue primarily arises from two key challenges: (1) significant magnitude disparity between multi-modal features-specifically, image features and camera-ray positional embeddings (PE), and (2) the inefficiency and approximation error of quantizing non-linear operators, which commonly rely on hardware-unfriendly computations. In this paper, we propose FQ-PETR, a fully quantized framework for PETRs, featuring three key innovations: (1) Quantization-Friendly LiDAR-ray Position Embedding (QFPE): Replacing multi-point sampling with LiDAR-prior-guided single-point sampling and anchor-based embedding eliminates problematic non-linearities (e.g., inverse-sigmoid) and aligns PE scale with image features, preserving accuracy. (2) Dual-Lookup Table (DULUT): This algorithm approximates complex non-linear functions using two cascaded linear LUTs, achieving high fidelity with minimal entries and no specialized hardware. (3) Quantization After Numerical Stabilization (QANS): Performing quantization after softmax numerical stabilization mitigates attention distortion from large inputs. On PETRs (e.g. PETR, StreamPETR, PETRv2, MV2d), FQ-PETR under W8A8 achieves near-floating-point accuracy (1% degradation) while reducing latency by up to 75%, significantly outperforming existing PTQ and QAT baselines.

