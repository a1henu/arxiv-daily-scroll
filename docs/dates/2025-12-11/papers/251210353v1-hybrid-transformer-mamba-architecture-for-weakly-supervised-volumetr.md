---
layout: default
title: Hybrid Transformer-Mamba Architecture for Weakly Supervised Volumetric Medical Segmentation
---

# Hybrid Transformer-Mamba Architecture for Weakly Supervised Volumetric Medical Segmentation
**arXiv**：[2512.10353v1](https://arxiv.org/abs/2512.10353) · [PDF](https://arxiv.org/pdf/2512.10353.pdf)  
**作者**：Yiheng Lyu, Lian Xu, Mohammed Bennamoun, Farid Boussaid, Coen Arrow, Girish Dwivedi  

**一句话要点**：提出TranSamba混合Transformer-Mamba架构，用于弱监督体积医学分割以捕获3D上下文。

**关键词**：弱监督分割, 体积医学图像, Transformer-Mamba架构, 3D上下文建模, 线性复杂度

## 3 点简述
- 核心问题：现有弱监督体积医学分割方法依赖2D编码器，忽略数据体积特性。
- 方法要点：结合Transformer和Mamba块，通过线性复杂度状态空间模型跨切片交换信息，增强自注意力。
- 实验或效果：在三个数据集上实现新SOTA，性能优于现有方法，复杂度线性且内存恒定。

## 摘要（原文）

> Weakly supervised semantic segmentation offers a label-efficient solution to train segmentation models for volumetric medical imaging. However, existing approaches often rely on 2D encoders that neglect the inherent volumetric nature of the data. We propose TranSamba, a hybrid Transformer-Mamba architecture designed to capture 3D context for weakly supervised volumetric medical segmentation. TranSamba augments a standard Vision Transformer backbone with Cross-Plane Mamba blocks, which leverage the linear complexity of state space models for efficient information exchange across neighboring slices. The information exchange enhances the pairwise self-attention within slices computed by the Transformer blocks, directly contributing to the attention maps for object localization. TranSamba achieves effective volumetric modeling with time complexity that scales linearly with the input volume depth and maintains constant memory usage for batch processing. Extensive experiments on three datasets demonstrate that TranSamba establishes new state-of-the-art performance, consistently outperforming existing methods across diverse modalities and pathologies. Our source code and trained models are openly accessible at: https://github.com/YihengLyu/TranSamba.

