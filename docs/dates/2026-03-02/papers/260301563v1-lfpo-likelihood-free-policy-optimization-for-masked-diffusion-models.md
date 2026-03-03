---
layout: default
title: LFPO: Likelihood-Free Policy Optimization for Masked Diffusion Models
---

# LFPO: Likelihood-Free Policy Optimization for Masked Diffusion Models
**arXiv**：[2603.01563v1](https://arxiv.org/abs/2603.01563) · [PDF](https://arxiv.org/pdf/2603.01563.pdf)  
**作者**：Chenxing Wei, Jiazhen Kang, Hong Wang, Jianqing Zhang, Hao Jiang, Xiaolong Xu, Ningyuan Sun, Ying He, F. Richard Yu, Yao Shu, Bo Jiang  

**一句话要点**：提出LFPO以解决扩散大语言模型在强化学习中对齐时似然计算不可行的问题

**关键词**：扩散大语言模型, 强化学习对齐, 似然自由优化, 几何速度校正, 推理加速

## 3 点简述
- 核心问题：扩散大语言模型因精确似然计算不可行，难以直接应用强化学习对齐方法
- 方法要点：LFPO将向量场流匹配映射到离散令牌空间，通过几何速度校正优化去噪对数
- 实验或效果：在代码和推理基准上超越现有方法，并通过减少扩散步骤加速推理约20%

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) has achieved remarkable success in improving autoregressive models, especially in domains requiring correctness like mathematical reasoning and code generation. However, directly applying such paradigms to Diffusion Large Language Models (dLLMs) is fundamentally hindered by the intractability of exact likelihood computation, which forces existing methods to rely on high-variance approximations. To bridge this gap, we propose Likelihood-Free Policy Optimization (LFPO), a native framework that maps the concept of vector field flow matching to the discrete token space. Specifically, LFPO formulates alignment as geometric velocity rectification, which directly optimizes denoising logits via contrastive updates. This design effectively bypasses the errors inherent in likelihood approximation, yielding the precise gradient estimation. Furthermore, LFPO enforce consistency by predicting final solutions from intermediate steps, effectively straightening the probability flow to enable high-quality generation with significantly fewer iterations. Extensive experiments demonstrate that LFPO not only outperforms state-of-the-art baselines on code and reasoning benchmarks but also accelerates inference by approximately 20% through reduced diffusion steps.

