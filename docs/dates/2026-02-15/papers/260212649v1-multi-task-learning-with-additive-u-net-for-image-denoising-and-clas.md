---
layout: default
title: Multi-Task Learning with Additive U-Net for Image Denoising and Classification
---

# Multi-Task Learning with Additive U-Net for Image Denoising and Classification
**arXiv**：[2602.12649v1](https://arxiv.org/abs/2602.12649) · [PDF](https://arxiv.org/pdf/2602.12649.pdf)  
**作者**：Vikram Lakkavalli, Neelam Sinha  

**一句话要点**：提出Additive U-Net，通过门控加法融合改进U-Net跳跃连接，用于图像去噪和多任务学习。

**关键词**：图像去噪, 多任务学习, U-Net架构, 跳跃连接, 门控融合, 训练稳定性

## 3 点简述
- 研究U-Net中跳跃连接的加法融合，替代拼接以控制信息流和稳定训练。
- 在单任务去噪和联合去噪-分类任务中，AddUNet实现竞争性性能并提升训练稳定性。
- 多任务学习中，跳跃权重呈现任务感知分布：浅层支持重建，深层支持分类，实现隐式任务解耦。

## 摘要（原文）

> We investigate additive skip fusion in U-Net architectures for image denoising and denoising-centric multi-task learning (MTL). By replacing concatenative skips with gated additive fusion, the proposed Additive U-Net (AddUNet) constrains shortcut capacity while preserving fixed feature dimensionality across depth. This structural regularization induces controlled encoder-decoder information flow and stabilizes joint optimization. Across single-task denoising and joint denoising-classification settings, AddUNet achieves competitive reconstruction performance with improved training stability. In MTL, learned skip weights exhibit systematic task-aware redistribution: shallow skips favor reconstruction, while deeper features support discrimination. Notably, reconstruction remains robust even under limited classification capacity, indicating implicit task decoupling through additive fusion. These findings show that simple constraints on skip connections act as an effective architectural regularizer for stable and scalable multi-task learning without increasing model complexity.

