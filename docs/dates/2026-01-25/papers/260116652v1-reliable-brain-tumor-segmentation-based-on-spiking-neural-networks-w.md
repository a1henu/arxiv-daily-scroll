---
layout: default
title: Reliable Brain Tumor Segmentation Based on Spiking Neural Networks with Efficient Training
---

# Reliable Brain Tumor Segmentation Based on Spiking Neural Networks with Efficient Training
**arXiv**：[2601.16652v1](https://arxiv.org/abs/2601.16652) · [PDF](https://arxiv.org/pdf/2601.16652.pdf)  
**作者**：Aurora Pia Ghiardelli, Guangzhi Tang, Tao Sun  

**一句话要点**：提出基于脉冲神经网络的可靠脑肿瘤分割框架，通过多视图集成和高效训练降低计算成本。

**关键词**：脑肿瘤分割, 脉冲神经网络, 不确定性估计, 多视图集成, 高效训练, 医学图像分析

## 3 点简述
- 核心问题：脑肿瘤分割需高精度与低功耗，但传统方法计算成本高，且缺乏不确定性估计。
- 方法要点：使用多视图脉冲神经网络集成进行体素级不确定性估计，并采用前向传播时间训练以提升效率。
- 实验或效果：在BraTS数据集上实现竞争性精度，不确定性校准良好，计算量减少87%。

## 摘要（原文）

> We propose a reliable and energy-efficient framework for 3D brain tumor segmentation using spiking neural networks (SNNs). A multi-view ensemble of sagittal, coronal, and axial SNN models provides voxel-wise uncertainty estimation and enhances segmentation robustness. To address the high computational cost in training SNN models for semantic image segmentation, we employ Forward Propagation Through Time (FPTT), which maintains temporal learning efficiency with significantly reduced computational cost. Experiments on the Multimodal Brain Tumor Segmentation Challenges (BraTS 2017 and BraTS 2023) demonstrate competitive accuracy, well-calibrated uncertainty, and an 87% reduction in FLOPs, underscoring the potential of SNNs for reliable, low-power medical IoT and Point-of-Care systems.

