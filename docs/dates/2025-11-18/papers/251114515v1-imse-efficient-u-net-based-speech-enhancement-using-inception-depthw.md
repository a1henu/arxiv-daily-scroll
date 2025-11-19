---
layout: default
title: IMSE: Efficient U-Net-based Speech Enhancement using Inception Depthwise Convolution and Amplitude-Aware Linear Attention
---

# IMSE: Efficient U-Net-based Speech Enhancement using Inception Depthwise Convolution and Amplitude-Aware Linear Attention
**arXiv**：[2511.14515v1](https://arxiv.org/abs/2511.14515) · [PDF](https://arxiv.org/pdf/2511.14515.pdf)  
**作者**：Xinxin Tang, Bin Qin, Yufang Li  

**一句话要点**：提出IMSE网络，使用MALA和IDConv优化语音增强，实现超轻量高性能。

**关键词**：语音增强, 超轻量网络, 线性注意力, 深度卷积, U-Net架构, 参数优化

## 3 点简述
- 核心问题：现有方法如MUSE在资源受限设备上存在效率瓶颈，参数冗余和计算负担高。
- 方法要点：引入振幅感知线性注意力MALA和Inception深度卷积IDConv，提升全局建模和特征提取效率。
- 实验或效果：在VoiceBank+DEMAND数据集上，参数减少16.8%，PESQ达3.373，性能媲美SOTA。

## 摘要（原文）

> Achieving a balance between lightweight design and high performance remains a significant challenge for speech enhancement (SE) tasks on resource-constrained devices. Existing state-of-the-art methods, such as MUSE, have established a strong baseline with only 0.51M parameters by introducing a Multi-path Enhanced Taylor (MET) transformer and Deformable Embedding (DE). However, an in-depth analysis reveals that MUSE still suffers from efficiency bottlenecks: the MET module relies on a complex "approximate-compensate" mechanism to mitigate the limitations of Taylor-expansion-based attention, while the offset calculation for deformable embedding introduces additional computational burden. This paper proposes IMSE, a systematically optimized and ultra-lightweight network. We introduce two core innovations: 1) Replacing the MET module with Amplitude-Aware Linear Attention (MALA). MALA fundamentally rectifies the "amplitude-ignoring" problem in linear attention by explicitly preserving the norm information of query vectors in the attention calculation, achieving efficient global modeling without an auxiliary compensation branch. 2) Replacing the DE module with Inception Depthwise Convolution (IDConv). IDConv borrows the Inception concept, decomposing large-kernel operations into efficient parallel branches (square, horizontal, and vertical strips), thereby capturing spectrogram features with extremely low parameter redundancy. Extensive experiments on the VoiceBank+DEMAND dataset demonstrate that, compared to the MUSE baseline, IMSE significantly reduces the parameter count by 16.8\% (from 0.513M to 0.427M) while achieving competitive performance comparable to the state-of-the-art on the PESQ metric (3.373). This study sets a new benchmark for the trade-off between model size and speech quality in ultra-lightweight speech enhancement.

