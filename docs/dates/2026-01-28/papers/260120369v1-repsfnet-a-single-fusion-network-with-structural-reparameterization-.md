---
layout: default
title: RepSFNet : A Single Fusion Network with Structural Reparameterization for Crowd Counting
---

# RepSFNet : A Single Fusion Network with Structural Reparameterization for Crowd Counting
**arXiv**：[2601.20369v1](https://arxiv.org/abs/2601.20369) · [PDF](https://arxiv.org/pdf/2601.20369.pdf)  
**作者**：Mas Nurul Achmadiah, Chi-Chia Sun, Wen-Kai Kuo, Jun-Wei Hsieh  

**一句话要点**：提出RepSFNet，通过结构重参数化和单融合网络解决人群计数中的尺度变化与高计算成本问题。

**关键词**：人群计数, 结构重参数化, 特征融合, 轻量级网络, 实时计算, 边缘计算

## 3 点简述
- 核心问题：人群计数在变密度场景中面临尺度变化、遮挡和现有模型计算成本高的挑战。
- 方法要点：使用RepLK-ViT骨干网络和特征融合模块，结合ASPP与CAN进行密度自适应上下文建模，避免注意力机制以降低复杂度。
- 实验或效果：在多个数据集上实现竞争性精度，推理延迟降低达34%，适用于实时和低功耗边缘计算。

## 摘要（原文）

> Crowd counting remains challenging in variable-density scenes due to scale variations, occlusions, and the high computational cost of existing models. To address these issues, we propose RepSFNet (Reparameterized Single Fusion Network), a lightweight architecture designed for accurate and real-time crowd estimation. RepSFNet leverages a RepLK-ViT backbone with large reparameterized kernels for efficient multi-scale feature extraction. It further integrates a Feature Fusion module combining Atrous Spatial Pyramid Pooling (ASPP) and Context-Aware Network (CAN) to achieve robust, density-adaptive context modeling. A Concatenate Fusion module is employed to preserve spatial resolution and generate high-quality density maps. By avoiding attention mechanisms and multi-branch designs, RepSFNet significantly reduces parameters and computational complexity. The training objective combines Mean Squared Error and Optimal Transport loss to improve both count accuracy and spatial distribution alignment. Experiments conducted on ShanghaiTech, NWPU, and UCF-QNRF datasets demonstrate that RepSFNet achieves competitive accuracy while reducing inference latency by up to 34 percent compared to recent state-of-the-art methods, making it suitable for real-time and low-power edge computing applications.

