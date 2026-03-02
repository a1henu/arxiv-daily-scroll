---
layout: default
title: Joint Geometric and Trajectory Consistency Learning for One-Step Real-World Super-Resolution
---

# Joint Geometric and Trajectory Consistency Learning for One-Step Real-World Super-Resolution
**arXiv**：[2602.24240v1](https://arxiv.org/abs/2602.24240) · [PDF](https://arxiv.org/pdf/2602.24240.pdf)  
**作者**：Chengyan Deng, Zhangquan Chen, Li Yu, Kai Zhang, Xue Zhou, Wang Zhang  

**一句话要点**：提出GTASR以解决一致性模型在真实图像超分辨率中的几何解耦和轨迹漂移问题

**关键词**：真实图像超分辨率, 一致性模型, 几何解耦, 轨迹对齐, 结构校正, 低延迟推理

## 3 点简述
- 核心问题：一致性模型在真实图像超分辨率中面临几何解耦和一致性漂移，导致结构失真和效率低下
- 方法要点：引入轨迹对齐策略和双参考结构校正机制，以优化生成轨迹并增强结构一致性
- 实验或效果：实验验证GTASR在保持低延迟的同时，性能优于代表性基线，代码将开源

## 摘要（原文）

> Diffusion-based Real-World Image Super-Resolution (Real-ISR) achieves impressive perceptual quality but suffers from high computational costs due to iterative sampling. While recent distillation approaches leveraging large-scale Text-to-Image (T2I) priors have enabled one-step generation, they are typically hindered by prohibitive parameter counts and the inherent capability bounds imposed by teacher models. As a lightweight alternative, Consistency Models offer efficient inference but struggle with two critical limitations: the accumulation of consistency drift inherent to transitive training, and a phenomenon we term "Geometric Decoupling" - where the generative trajectory achieves pixel-wise alignment yet fails to preserve structural coherence. To address these challenges, we propose GTASR (Geometric Trajectory Alignment Super-Resolution), a simple yet effective consistency training paradigm for Real-ISR. Specifically, we introduce a Trajectory Alignment (TA) strategy to rectify the tangent vector field via full-path projection, and a Dual-Reference Structural Rectification (DRSR) mechanism to enforce strict structural constraints. Extensive experiments verify that GTASR delivers superior performance over representative baselines while maintaining minimal latency. The code and model will be released at https://github.com/Blazedengcy/GTASR.

