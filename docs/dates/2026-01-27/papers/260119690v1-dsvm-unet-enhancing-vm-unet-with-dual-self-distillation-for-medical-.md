---
layout: default
title: DSVM-UNet : Enhancing VM-UNet with Dual Self-distillation for Medical Image Segmentation
---

# DSVM-UNet : Enhancing VM-UNet with Dual Self-distillation for Medical Image Segmentation
**arXiv**：[2601.19690v1](https://arxiv.org/abs/2601.19690) · [PDF](https://arxiv.org/pdf/2601.19690.pdf)  
**作者**：Renrong Shao, Dongyang Li, Dong Xia, Lin Shao, Jiangdong Lu, Fen Zheng, Lulu Zhang  

**一句话要点**：提出DSVM-UNet，通过双自蒸馏增强VM-UNet，用于医学图像分割。

**关键词**：医学图像分割, Vision Mamba, 自蒸馏, VM-UNet, 特征对齐

## 3 点简述
- 核心问题：现有VM-UNet方法依赖复杂结构优化，可能增加计算负担。
- 方法要点：引入双自蒸馏，在全局和局部层面对齐特征，无需复杂架构设计。
- 实验或效果：在ISIC2017、ISIC2018和Synapse基准上实现先进性能，保持计算效率。

## 摘要（原文）

> Vision Mamba models have been extensively researched in various fields, which address the limitations of previous models by effectively managing long-range dependencies with a linear-time overhead. Several prospective studies have further designed Vision Mamba based on UNet(VM-UNet) for medical image segmentation. These approaches primarily focus on optimizing architectural designs by creating more complex structures to enhance the model's ability to perceive semantic features. In this paper, we propose a simple yet effective approach to improve the model by Dual Self-distillation for VM-UNet (DSVM-UNet) without any complex architectural designs. To achieve this goal, we develop double self-distillation methods to align the features at both the global and local levels. Extensive experiments conducted on the ISIC2017, ISIC2018, and Synapse benchmarks demonstrate that our approach achieves state-of-the-art performance while maintaining computational efficiency. Code is available at https://github.com/RoryShao/DSVM-UNet.git.

