---
layout: default
title: OSCAR: Orthogonal Stochastic Control for Alignment-Respecting Diversity in Flow Matching
---

# OSCAR: Orthogonal Stochastic Control for Alignment-Respecting Diversity in Flow Matching
**arXiv**：[2510.09060v1](https://arxiv.org/abs/2510.09060) · [PDF](https://arxiv.org/pdf/2510.09060.pdf)  
**作者**：Jingxuan Wu, Zhenglin Wan, Xingrui Yu, Yuzhe Yang, Bo An, Ivor Tsang  

**一句话要点**：提出正交随机控制方法以提升流匹配模型在文本到图像生成中的多样性

**关键词**：文本到图像生成, 流匹配模型, 多样性增强, 正交扰动, 训练免费控制

## 3 点简述
- 流匹配模型轨迹确定性导致多样性不足，需重复采样
- 通过特征空间目标和正交随机扰动增强轨迹多样性
- 实验显示在固定采样预算下提升多样性指标并保持质量

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

