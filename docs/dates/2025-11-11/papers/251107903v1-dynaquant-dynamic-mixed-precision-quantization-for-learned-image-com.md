---
layout: default
title: DynaQuant: Dynamic Mixed-Precision Quantization for Learned Image Compression
---

# DynaQuant: Dynamic Mixed-Precision Quantization for Learned Image Compression
**arXiv**：[2511.07903v1](https://arxiv.org/abs/2511.07903) · [PDF](https://arxiv.org/pdf/2511.07903.pdf)  
**作者**：Youneng Bao, Yulong Cheng, Yiping Liu, Yichen Yang, Peng Qin, Mu Li, Yongsheng Liang  

**一句话要点**：提出动态混合精度量化框架以优化学习图像压缩的性能与效率平衡

**关键词**：学习图像压缩, 动态量化, 混合精度, 率失真优化, 内容感知, 比特宽度选择

## 3 点简述
- 静态统一比特宽度无法适应学习图像压缩模型的多样数据分布和敏感性
- 结合内容感知量化和动态比特宽度选择器，实现端到端训练
- 实验显示在保持率失真性能的同时显著降低计算和存储需求

## 摘要（原文）

> Prevailing quantization techniques in Learned Image Compression (LIC) typically employ a static, uniform bit-width across all layers, failing to adapt to the highly diverse data distributions and sensitivity characteristics inherent in LIC models. This leads to a suboptimal trade-off between performance and efficiency. In this paper, we introduce DynaQuant, a novel framework for dynamic mixed-precision quantization that operates on two complementary levels. First, we propose content-aware quantization, where learnable scaling and offset parameters dynamically adapt to the statistical variations of latent features. This fine-grained adaptation is trained end-to-end using a novel Distance-aware Gradient Modulator (DGM), which provides a more informative learning signal than the standard Straight-Through Estimator. Second, we introduce a data-driven, dynamic bit-width selector that learns to assign an optimal bit precision to each layer, dynamically reconfiguring the network's precision profile based on the input data. Our fully dynamic approach offers substantial flexibility in balancing rate-distortion (R-D) performance and computational cost. Experiments demonstrate that DynaQuant achieves rd performance comparable to full-precision models while significantly reducing computational and storage requirements, thereby enabling the practical deployment of advanced LIC on diverse hardware platforms.

