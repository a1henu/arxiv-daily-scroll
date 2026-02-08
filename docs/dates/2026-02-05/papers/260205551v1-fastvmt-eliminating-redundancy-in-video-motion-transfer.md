---
layout: default
title: FastVMT: Eliminating Redundancy in Video Motion Transfer
---

# FastVMT: Eliminating Redundancy in Video Motion Transfer
**arXiv**：[2602.05551v1](https://arxiv.org/abs/2602.05551) · [PDF](https://arxiv.org/pdf/2602.05551.pdf)  
**作者**：Yue Ma, Zhikai Wang, Tianhao Ren, Mingzhe Zheng, Hongyu Liu, Jiayi Guo, Mark Fong, Yuxuan Xue, Zixiang Zhao, Konrad Schindler, Qifeng Chen, Linfeng Zhang  

**一句话要点**：提出FastVMT以消除视频运动传递中的计算冗余，实现加速而不损失质量

**关键词**：视频运动传递, 扩散变换器, 计算冗余, 注意力机制, 梯度优化, 加速方法

## 3 点简述
- 核心问题：现有视频运动传递方法存在运动冗余和梯度冗余，导致计算效率低下
- 方法要点：通过局部注意力掩码减少运动冗余，重用梯度优化减少梯度冗余
- 实验或效果：平均实现3.43倍加速，保持视觉保真度和时间一致性

## 摘要（原文）

> Video motion transfer aims to synthesize videos by generating visual content according to a text prompt while transferring the motion pattern observed in a reference video. Recent methods predominantly use the Diffusion Transformer (DiT) architecture. To achieve satisfactory runtime, several methods attempt to accelerate the computations in the DiT, but fail to address structural sources of inefficiency. In this work, we identify and remove two types of computational redundancy in earlier work: motion redundancy arises because the generic DiT architecture does not reflect the fact that frame-to-frame motion is small and smooth; gradient redundancy occurs if one ignores that gradients change slowly along the diffusion trajectory. To mitigate motion redundancy, we mask the corresponding attention layers to a local neighborhood such that interaction weights are not computed unnecessarily distant image regions. To exploit gradient redundancy, we design an optimization scheme that reuses gradients from previous diffusion steps and skips unwarranted gradient computations. On average, FastVMT achieves a 3.43x speedup without degrading the visual fidelity or the temporal consistency of the generated videos.

