---
layout: default
title: A Probabilistic U-Net Approach to Downscaling Climate Simulations
---

# A Probabilistic U-Net Approach to Downscaling Climate Simulations
**arXiv**：[2511.03197v1](https://arxiv.org/abs/2511.03197) · [PDF](https://arxiv.org/pdf/2511.03197.pdf)  
**作者**：Maryam Alipourhajiagha, Pierre-Louis Lemaire, Youssef Diouane, Julie Carreau  

**一句话要点**：提出概率U-Net方法以解决气候模拟降尺度问题

**关键词**：气候模拟降尺度, 概率U-Net, 不确定性建模, 训练目标评估, 空间分辨率提升

## 3 点简述
- 气候模型计算成本高，输出空间分辨率粗，影响研究精度
- 结合确定性U-Net与变分潜空间，捕捉随机不确定性
- 评估四种训练目标，WMSE-MS-SSIM在极端事件表现好，afCRPS捕捉空间变异性

## 摘要（原文）

> Climate models are limited by heavy computational costs, often producing
> outputs at coarse spatial resolutions, while many climate change impact studies
> require finer scales. Statistical downscaling bridges this gap, and we adapt
> the probabilistic U-Net for this task, combining a deterministic U-Net backbone
> with a variational latent space to capture aleatoric uncertainty. We evaluate
> four training objectives, afCRPS and WMSE-MS-SSIM with three settings for
> downscaling precipitation and temperature from $16\times$ coarser resolution.
> Our main finding is that WMSE-MS-SSIM performs well for extremes under certain
> settings, whereas afCRPS better captures spatial variability across scales.

