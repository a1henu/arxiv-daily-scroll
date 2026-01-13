---
layout: default
title: Anatomy Aware Cascade Network: Bridging Epistemic Uncertainty and Geometric Manifold for 3D Tooth Segmentation
---

# Anatomy Aware Cascade Network: Bridging Epistemic Uncertainty and Geometric Manifold for 3D Tooth Segmentation
**arXiv**：[2601.07499v1](https://arxiv.org/abs/2601.07499) · [PDF](https://arxiv.org/pdf/2601.07499.pdf)  
**作者**：Bing Yu, Liu Shi, Haitao Wang, Deran Qi, Xiang Cai, Wei Zhong, Qiegen Liu  

**一句话要点**：提出AACNet以解决CBCT中牙齿粘连导致的3D分割边界模糊问题

**关键词**：3D牙齿分割, CBCT图像处理, 边界模糊处理, 几何约束, 级联网络, 临床应用

## 3 点简述
- 核心问题：CBCT扫描中低对比度和边界不清晰导致牙齿粘连，影响3D分割精度。
- 方法要点：采用粗到细框架，结合AGBR处理高不确定性区域和SDMAA增强几何一致性。
- 实验或效果：在125个CBCT数据集上Dice系数达90.17%，HD95为3.63mm，优于现有方法。

## 摘要（原文）

> Accurate three-dimensional (3D) tooth segmentation from Cone-Beam Computed Tomography (CBCT) is a prerequisite for digital dental workflows. However, achieving high-fidelity segmentation remains challenging due to adhesion artifacts in naturally occluded scans, which are caused by low contrast and indistinct inter-arch boundaries. To address these limitations, we propose the Anatomy Aware Cascade Network (AACNet), a coarse-to-fine framework designed to resolve boundary ambiguity while maintaining global structural consistency. Specifically, we introduce two mechanisms: the Ambiguity Gated Boundary Refiner (AGBR) and the Signed Distance Map guided Anatomical Attention (SDMAA). The AGBR employs an entropy based gating mechanism to perform targeted feature rectification in high uncertainty transition zones. Meanwhile, the SDMAA integrates implicit geometric constraints via signed distance map to enforce topological consistency, preventing the loss of spatial details associated with standard pooling. Experimental results on a dataset of 125 CBCT volumes demonstrate that AACNet achieves a Dice Similarity Coefficient of 90.17 \% and a 95\% Hausdorff Distance of 3.63 mm, significantly outperforming state-of-the-art methods. Furthermore, the model exhibits strong generalization on an external dataset with an HD95 of 2.19 mm, validating its reliability for downstream clinical applications such as surgical planning. Code for AACNet is available at https://github.com/shiliu0114/AACNet.

