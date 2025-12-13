---
layout: default
title: Error-Propagation-Free Learned Video Compression With Dual-Domain Progressive Temporal Alignment
---

# Error-Propagation-Free Learned Video Compression With Dual-Domain Progressive Temporal Alignment
**arXiv**：[2512.10450v1](https://arxiv.org/abs/2512.10450) · [PDF](https://arxiv.org/pdf/2512.10450.pdf)  
**作者**：Han Li, Shaohui Li, Wenrui Dai, Chenglin Li, Xinlong Pan, Haipeng Wang, Junni Zou, Hongkai Xiong  

**一句话要点**：提出双域渐进时间对齐与质量条件专家混合的统一变换框架，以消除学习视频压缩中的误差传播。

**关键词**：学习视频压缩, 误差传播消除, 双域时间对齐, 质量条件专家混合, 运动估计与补偿

## 3 点简述
- 现有学习视频压缩框架在运动估计与补偿中存在时间对齐不准确与误差传播的困境。
- 采用双域渐进时间对齐，结合粗像素域对齐和精炼潜在域对齐，增强时间上下文建模。
- 实验表明，该方法在消除误差传播的同时，实现了竞争性的率失真性能。

## 摘要（原文）

> Existing frameworks for learned video compression suffer from a dilemma between inaccurate temporal alignment and error propagation for motion estimation and compensation (ME/MC). The separate-transform framework employs distinct transforms for intra-frame and inter-frame compression to yield impressive rate-distortion (R-D) performance but causes evident error propagation, while the unified-transform framework eliminates error propagation via shared transforms but is inferior in ME/MC in shared latent domains. To address this limitation, in this paper, we propose a novel unifiedtransform framework with dual-domain progressive temporal alignment and quality-conditioned mixture-of-expert (QCMoE) to enable quality-consistent and error-propagation-free streaming for learned video compression. Specifically, we propose dualdomain progressive temporal alignment for ME/MC that leverages coarse pixel-domain alignment and refined latent-domain alignment to significantly enhance temporal context modeling in a coarse-to-fine fashion. The coarse pixel-domain alignment efficiently handles simple motion patterns with optical flow estimated from a single reference frame, while the refined latent-domain alignment develops a Flow-Guided Deformable Transformer (FGDT) over latents from multiple reference frames to achieve long-term motion refinement (LTMR) for complex motion patterns. Furthermore, we design a QCMoE module for continuous bit-rate adaptation that dynamically assigns different experts to adjust quantization steps per pixel based on target quality and content rather than relies on a single quantization step. QCMoE allows continuous and consistent rate control with appealing R-D performance. Experimental results show that the proposed method achieves competitive R-D performance compared with the state-of-the-arts, while successfully eliminating error propagation.

