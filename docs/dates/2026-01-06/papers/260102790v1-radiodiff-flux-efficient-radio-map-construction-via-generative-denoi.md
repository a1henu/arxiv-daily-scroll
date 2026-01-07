---
layout: default
title: RadioDiff-Flux: Efficient Radio Map Construction via Generative Denoise Diffusion Model Trajectory Midpoint Reuse
---

# RadioDiff-Flux: Efficient Radio Map Construction via Generative Denoise Diffusion Model Trajectory Midpoint Reuse
**arXiv**：[2601.02790v1](https://arxiv.org/abs/2601.02790) · [PDF](https://arxiv.org/pdf/2601.02790.pdf)  
**作者**：Xiucheng Wang, Peilin Zheng, Honggang Jia, Nan Cheng, Ruijin Sun, Conghao Zhou, Xuemin Shen  

**一句话要点**：提出RadioDiff-Flux，通过重用生成去噪扩散模型轨迹中点，实现6G场景下高效无线电地图构建。

**关键词**：无线电地图构建, 生成扩散模型, 潜在扩散框架, 6G网络, 推理加速, 动态场景适应

## 3 点简述
- 核心问题：6G高速动态场景中，生成扩散模型因迭代推理延迟高，难以满足实时无线电地图构建需求。
- 方法要点：基于扩散过程潜在中点一致性，设计两阶段潜在扩散框架，分离静态环境建模与动态细化，重用预计算中点减少去噪冗余。
- 实验或效果：实验显示，RadioDiff-Flux在精度损失小于0.15%下，推理速度提升高达50倍，适用于6G网络快速可扩展生成。

## 摘要（原文）

> Accurate radio map (RM) construction is essential to enabling environment-aware and adaptive wireless communication. However, in future 6G scenarios characterized by high-speed network entities and fast-changing environments, it is very challenging to meet real-time requirements. Although generative diffusion models (DMs) can achieve state-of-the-art accuracy with second-level delay, their iterative nature leads to prohibitive inference latency in delay-sensitive scenarios. In this paper, by uncovering a key structural property of diffusion processes: the latent midpoints remain highly consistent across semantically similar scenes, we propose RadioDiff-Flux, a novel two-stage latent diffusion framework that decouples static environmental modeling from dynamic refinement, enabling the reuse of precomputed midpoints to bypass redundant denoising. In particular, the first stage generates a coarse latent representation using only static scene features, which can be cached and shared across similar scenarios. The second stage adapts this representation to dynamic conditions and transmitter locations using a pre-trained model, thereby avoiding repeated early-stage computation. The proposed RadioDiff-Flux significantly reduces inference time while preserving fidelity. Experiment results show that RadioDiff-Flux can achieve up to 50 acceleration with less than 0.15% accuracy loss, demonstrating its practical utility for fast, scalable RM generation in future 6G networks.

