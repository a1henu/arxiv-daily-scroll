---
layout: default
title: FlowLPS: Langevin-Proximal Sampling for Flow-based Inverse Problem Solvers
---

# FlowLPS: Langevin-Proximal Sampling for Flow-based Inverse Problem Solvers
**arXiv**：[2512.07150v1](https://arxiv.org/abs/2512.07150) · [PDF](https://arxiv.org/pdf/2512.07150.pdf)  
**作者**：Jonghyun Park, Jong Chul Ye  

**一句话要点**：提出FlowLPS框架，通过Langevin-Proximal采样解决基于流模型的逆问题求解中的收敛与流形偏差问题。

**关键词**：逆问题求解, 流模型, Langevin采样, 近端优化, 训练免费方法

## 3 点简述
- 核心问题：现有训练免费方法在流模型逆问题求解中易收敛失败或产生流形偏差。
- 方法要点：结合Langevin动力学进行流形一致探索和近端优化实现精确模式寻找。
- 实验或效果：在FFHQ和DIV2K数据集上实现重建保真度与感知质量的平衡，优于现有方法。

## 摘要（原文）

> Deep generative models have become powerful priors for solving inverse problems, and various training-free methods have been developed. However, when applied to latent flow models, existing methods often fail to converge to the posterior mode or suffer from manifold deviation within latent spaces. To mitigate this, here we introduce a novel training-free framework, FlowLPS, that solves inverse problems with pretrained flow models via a Langevin Proximal Sampling (LPS) strategy. Our method integrates Langevin dynamics for manifold-consistent exploration with proximal optimization for precise mode seeking, achieving a superior balance between reconstruction fidelity and perceptual quality across multiple inverse tasks on FFHQ and DIV2K, outperforming state of the art inverse solvers.

