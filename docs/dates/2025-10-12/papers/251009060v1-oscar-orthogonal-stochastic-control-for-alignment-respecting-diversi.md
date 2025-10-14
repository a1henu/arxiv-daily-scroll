---
layout: default
title: OSCAR: Orthogonal Stochastic Control for Alignment-Respecting Diversity in Flow Matching
---

# OSCAR: Orthogonal Stochastic Control for Alignment-Respecting Diversity in Flow Matching
**arXiv**：[2510.09060v1](https://arxiv.org/abs/2510.09060) · [PDF](https://arxiv.org/pdf/2510.09060.pdf)  
**作者**：Jingxuan Wu, Zhenglin Wan, Xingrui Yu, Yuzhe Yang, Bo An, Ivor Tsang  

**一句话要点**：提出OSCAR方法以提升基于流的文本到图像模型的多样性，同时保持图像质量。

**关键词**：文本到图像生成, 流匹配, 多样性增强, 推理时控制, 正交扰动, 图像质量保持

## 3 点简述
- 核心问题：基于流的文本到图像模型轨迹确定性，导致多样性探索成本高且低效。
- 方法要点：通过正交随机扰动和特征空间目标，在推理时增强轨迹多样性而不需重训练。
- 实验或效果：在固定采样预算下，提升Vendi Score等多样性指标，并保持图像质量和提示对齐。

## 摘要（原文）

> Flow-based text-to-image models follow deterministic trajectories, forcing
> users to repeatedly sample to discover diverse modes, which is a costly and
> inefficient process. We present a training-free, inference-time control
> mechanism that makes the flow itself diversity-aware. Our method simultaneously
> encourages lateral spread among trajectories via a feature-space objective and
> reintroduces uncertainty through a time-scheduled stochastic perturbation.
> Crucially, this perturbation is projected to be orthogonal to the generation
> flow, a geometric constraint that allows it to boost variation without
> degrading image details or prompt fidelity. Our procedure requires no
> retraining or modification to the base sampler and is compatible with common
> flow-matching solvers. Theoretically, our method is shown to monotonically
> increase a volume surrogate while, due to its geometric constraints,
> approximately preserving the marginal distribution. This provides a principled
> explanation for why generation quality is robustly maintained. Empirically,
> across multiple text-to-image settings under fixed sampling budgets, our method
> consistently improves diversity metrics such as the Vendi Score and Brisque
> over strong baselines, while upholding image quality and alignment.

