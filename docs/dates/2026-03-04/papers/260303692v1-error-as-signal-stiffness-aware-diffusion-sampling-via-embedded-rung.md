---
layout: default
title: Error as Signal: Stiffness-Aware Diffusion Sampling via Embedded Runge-Kutta Guidance
---

# Error as Signal: Stiffness-Aware Diffusion Sampling via Embedded Runge-Kutta Guidance
**arXiv**：[2603.03692v1](https://arxiv.org/abs/2603.03692) · [PDF](https://arxiv.org/pdf/2603.03692.pdf)  
**作者**：Inho Kong, Sojin Lee, Youngjoon Hong, Hyunwoo J. Kim  

**一句话要点**：提出嵌入式龙格-库塔引导以解决扩散模型采样中因刚性区域导致的局部截断误差问题。

**关键词**：扩散模型, 采样稳定性, 刚性检测, 局部截断误差, 引导机制

## 3 点简述
- 核心问题：刚性区域中ODE轨迹突变，局部截断误差降低样本质量。
- 方法要点：利用求解器误差作为引导信号，设计嵌入式龙格-库塔引导减少误差并稳定采样。
- 实验或效果：在合成数据集和ImageNet上优于现有方法，代码已开源。

## 摘要（原文）

> Classifier-Free Guidance (CFG) has established the foundation for guidance mechanisms in diffusion models, showing that well-designed guidance proxies significantly improve conditional generation and sample quality. Autoguidance (AG) has extended this idea, but it relies on an auxiliary network and leaves solver-induced errors unaddressed. In stiff regions, the ODE trajectory changes sharply, where local truncation error (LTE) becomes a critical factor that deteriorates sample quality. Our key observation is that these errors align with the dominant eigenvector, motivating us to leverage the solver-induced error as a guidance signal. We propose Embedded Runge-Kutta Guidance (ERK-Guid), which exploits detected stiffness to reduce LTE and stabilize sampling. We theoretically and empirically analyze stiffness and eigenvector estimators with solver errors to motivate the design of ERK-Guid. Our experiments on both synthetic datasets and the popular benchmark dataset, ImageNet, demonstrate that ERK-Guid consistently outperforms state-of-the-art methods. Code is available at https://github.com/mlvlab/ERK-Guid.

