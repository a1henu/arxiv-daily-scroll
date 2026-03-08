---
layout: default
title: LAW & ORDER: Adaptive Spatial Weighting for Medical Diffusion and Segmentation
---

# LAW & ORDER: Adaptive Spatial Weighting for Medical Diffusion and Segmentation
**arXiv**：[2603.04795v1](https://arxiv.org/abs/2603.04795) · [PDF](https://arxiv.org/pdf/2603.04795.pdf)  
**作者**：Anugunj Naman, Ayushman Singh, Gaibo Zhang, Yaguang Zhang  

**一句话要点**：提出LAW与ORDER自适应空间加权方法，以解决医学图像扩散生成与分割中的空间不平衡问题。

**关键词**：医学图像分割, 扩散模型, 自适应空间加权, 计算效率优化, 病灶检测, 合成数据增强

## 3 点简述
- 核心问题：医学图像分析中，病灶区域小、背景大导致空间不平衡，影响扩散模型生成准确性和分割效率。
- 方法要点：LAW通过可学习权重调制扩散训练损失，ORDER在解码器阶段应用选择性双向跳跃注意力以优化分割。
- 实验效果：LAW提升生成质量20% FID，合成数据改善分割4.9% Dice；ORDER在低计算成本下实现6.0% Dice提升。

## 摘要（原文）

> Medical image analysis relies on accurate segmentation, and benefits from controllable synthesis (of new training images). Yet both tasks of the cyclical pipeline face spatial imbalance: lesions occupy small regions against vast backgrounds. In particular, diffusion models have been shown to drift from prescribed lesion layouts, while efficient segmenters struggle on spatially uncertain regions. Adaptive spatial weighting addresses this by learning where to allocate computational resources. This paper introduces a pair of network adapters: 1) Learnable Adaptive Weighter (LAW) which predicts per-pixel loss modulation from features and masks for diffusion training, stabilized via a mix of normalization, clamping, and regularization to prevent degenerate solutions; and 2) Optimal Region Detection with Efficient Resolution (ORDER) which applies selective bidirectional skip attention at late decoder stages for efficient segmentation. Experiments on polyp and kidney tumor datasets demonstrate that LAW achieves 20% FID generative improvement over a uniform baseline (52.28 vs. 65.60), with synthetic data then improving downstream segmentation by 4.9% Dice coefficient (83.2% vs. 78.3%). ORDER reaches 6.0% Dice improvement on MK-UNet (81.3% vs. 75.3%) with 0.56 GFLOPs and just 42K parameters, remaining 730x smaller than the standard nnUNet.

