---
layout: default
title: Towards a unified framework for guided diffusion models
---

# Towards a unified framework for guided diffusion models
**arXiv**：[2512.04985v1](https://arxiv.org/abs/2512.04985) · [PDF](https://arxiv.org/pdf/2512.04985.pdf)  
**作者**：Yuchen Jiao, Yuxin Chen, Gen Li  

**一句话要点**：提出统一框架以理论分析引导扩散模型，量化奖励改进并解释分类器自由引导机制。

**关键词**：引导扩散模型, 理论分析, 奖励优化, 分类器自由引导, 统一框架, 采样算法

## 3 点简述
- 核心问题：引导扩散模型的理论理解不足，缺乏统一分析框架。
- 方法要点：构建统一框架，注入奖励引导项，量化奖励提升，推导分类器自由引导的理论特性。
- 实验或效果：数值实验验证理论，新采样器易于训练，无需完整扩散轨迹。

## 摘要（原文）

> Guided or controlled data generation with diffusion models\blfootnote{Partial preliminary results of this work appeared in International Conference on Machine Learning 2025 \citep{li2025provable}.} has become a cornerstone of modern generative modeling. Despite substantial advances in diffusion model theory, the theoretical understanding of guided diffusion samplers remains severely limited. We make progress by developing a unified algorithmic and theoretical framework that accommodates both diffusion guidance and reward-guided diffusion. Aimed at fine-tuning diffusion models to improve certain rewards, we propose injecting a reward guidance term -- constructed from the difference between the original and reward-reweighted scores -- into the backward diffusion process, and rigorously quantify the resulting reward improvement over the unguided counterpart. As a key application, our framework shows that classifier-free guidance (CFG) decreases the expected reciprocal of the classifier probability, providing the first theoretical characterization of the specific performance metric that CFG improves for general target distributions. When applied to reward-guided diffusion, our framework yields a new sampler that is easy-to-train and requires no full diffusion trajectories during training. Numerical experiments further corroborate our theoretical findings.

