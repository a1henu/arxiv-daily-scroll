---
layout: default
title: Temporal-Spatial Tubelet Embedding for Cloud-Robust MSI Reconstruction using MSI-SAR Fusion: A Multi-Head Self-Attention Video Vision Transformer Approach
---

# Temporal-Spatial Tubelet Embedding for Cloud-Robust MSI Reconstruction using MSI-SAR Fusion: A Multi-Head Self-Attention Video Vision Transformer Approach
**arXiv**：[2512.09471v1](https://arxiv.org/abs/2512.09471) · [PDF](https://arxiv.org/pdf/2512.09471.pdf)  
**作者**：Yiqun Wang, Lujun Li, Meiru Yue, Radu State  

**一句话要点**：提出基于时空管状嵌入的ViViT框架，用于云覆盖多光谱图像重建，提升农业监测鲁棒性。

**关键词**：多光谱图像重建, 时空融合, 视频视觉Transformer, 云鲁棒性, 农业监测

## 3 点简述
- 核心问题：云覆盖导致多光谱图像信息损失，影响早期作物制图准确性。
- 方法要点：采用非重叠时空管状嵌入，结合3D卷积约束时间跨度，增强局部时序一致性。
- 实验或效果：在Traill County数据上，SAR融合方案使SMTS-ViViT比基线MSE降低10.33%。

## 摘要（原文）

> Cloud cover in multispectral imagery (MSI) significantly hinders early-season crop mapping by corrupting spectral information. Existing Vision Transformer(ViT)-based time-series reconstruction methods, like SMTS-ViT, often employ coarse temporal embeddings that aggregate entire sequences, causing substantial information loss and reducing reconstruction accuracy. To address these limitations, a Video Vision Transformer (ViViT)-based framework with temporal-spatial fusion embedding for MSI reconstruction in cloud-covered regions is proposed in this study. Non-overlapping tubelets are extracted via 3D convolution with constrained temporal span $(t=2)$, ensuring local temporal coherence while reducing cross-day information degradation. Both MSI-only and SAR-MSI fusion scenarios are considered during the experiments. Comprehensive experiments on 2020 Traill County data demonstrate notable performance improvements: MTS-ViViT achieves a 2.23\% reduction in MSE compared to the MTS-ViT baseline, while SMTS-ViViT achieves a 10.33\% improvement with SAR integration over the SMTS-ViT baseline. The proposed framework effectively enhances spectral reconstruction quality for robust agricultural monitoring.

