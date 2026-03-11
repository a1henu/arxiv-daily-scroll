---
layout: default
title: Rotation Equivariant Mamba for Vision Tasks
---

# Rotation Equivariant Mamba for Vision Tasks
**arXiv**：[2603.09138v1](https://arxiv.org/abs/2603.09138) · [PDF](https://arxiv.org/pdf/2603.09138.pdf)  
**作者**：Zhongchen Zhao, Qi Xie, Keyu Huang, Lei Zhang, Deyu Meng, Zongben Xu  

**一句话要点**：提出EQ-VMamba以解决视觉Mamba模型缺乏旋转等变性、影响鲁棒性的问题。

**关键词**：旋转等变性, 视觉Mamba, 图像分类, 语义分割, 超分辨率, 参数效率

## 3 点简述
- 当前视觉Mamba模型未考虑旋转对称性，导致对图像旋转敏感，限制鲁棒性和泛化能力。
- 引入旋转等变性交叉扫描策略和组Mamba块，构建首个旋转等变性视觉Mamba架构EQ-VMamba。
- 实验表明EQ-VMamba在多个任务中性能优越或竞争，参数减少约50%，增强鲁棒性和效率。

## 摘要（原文）

> Rotation equivariance constitutes one of the most general and crucial structural priors for visual data, yet it remains notably absent from current Mamba-based vision architectures. Despite the success of Mamba in natural language processing and its growing adoption in computer vision, existing visual Mamba models fail to account for rotational symmetry in their design. This omission renders them inherently sensitive to image rotations, thereby constraining their robustness and cross-task generalization. To address this limitation, we propose to incorporate rotation symmetry, a universal and fundamental geometric prior in images, into Mamba-based architectures. Specifically, we introduce EQ-VMamba, the first rotation equivariant visual Mamba architecture for vision tasks. The core components of EQ-VMamba include a carefully designed rotation equivariant cross-scan strategy and group Mamba blocks. Moreover, we provide a rigorous theoretical analysis of the intrinsic equivariance error, demonstrating that the proposed architecture enforces end-to-end rotation equivariance throughout the network. Extensive experiments across multiple benchmarks - including high-level image classification task, mid-level semantic segmentation task, and low-level image super-resolution task - demonstrate that EQ-VMamba achieves superior or competitive performance compared to non-equivariant baselines, while requiring approximately 50% fewer parameters. These results indicate that embedding rotation equivariance not only effectively bolsters the robustness of visual Mamba models against rotation transformations, but also enhances overall performance with significantly improved parameter efficiency. Code is available at https://github.com/zhongchenzhao/EQ-VMamba.

