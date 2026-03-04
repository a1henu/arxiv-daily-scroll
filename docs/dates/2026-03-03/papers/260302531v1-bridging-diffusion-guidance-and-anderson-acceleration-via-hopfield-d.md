---
layout: default
title: Bridging Diffusion Guidance and Anderson Acceleration via Hopfield Dynamics
---

# Bridging Diffusion Guidance and Anderson Acceleration via Hopfield Dynamics
**arXiv**：[2603.02531v1](https://arxiv.org/abs/2603.02531) · [PDF](https://arxiv.org/pdf/2603.02531.pdf)  
**作者**：Kwanyoung Kim  

**一句话要点**：提出几何感知注意力引导以稳定扩散模型中的注意力空间外推

**关键词**：扩散模型, 注意力机制, Hopfield网络, Anderson加速, 生成质量, 即插即用

## 3 点简述
- 核心问题：注意力空间外推方法缺乏理论基础，且现有方法可能不稳定。
- 方法要点：将注意力动态建模为现代Hopfield网络中的定点迭代，并基于弱收缩性质提出几何感知注意力引导。
- 实验或效果：该方法作为即插即用模块，显著提升生成质量，适用于现有框架。

## 摘要（原文）

> Classifier-Free Guidance (CFG) has significantly enhanced the generative quality of diffusion models by extrapolating between conditional and unconditional outputs. However, its high inference cost and limited applicability to distilled or single-step models have shifted research focus toward attention-space extrapolation. While these methods offer computational efficiency, their theoretical underpinnings remain elusive. In this work, we establish a foundational framework for attention-space extrapolation by modeling attention dynamics as fixed-point iterations within Modern Hopfield Networks. We demonstrate that the extrapolation effect in attention space constitutes a special case of Anderson Acceleration applied to these dynamics. Building on this insight and the weak contraction property, we propose Geometry Aware Attention Guidance (GAG). By decomposing attention updates into parallel and orthogonal components relative to the guidance direction, GAG stabilizes the acceleration process and maximizes guidance efficiency. Our plug-and-play method seamlessly integrates with existing frameworks while significantly improving generation quality.

