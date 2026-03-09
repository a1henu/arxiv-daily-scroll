---
layout: default
title: Energy-Driven Adaptive Visual Token Pruning for Efficient Vision-Language Models
---

# Energy-Driven Adaptive Visual Token Pruning for Efficient Vision-Language Models
**arXiv**：[2603.05950v1](https://arxiv.org/abs/2603.05950) · [PDF](https://arxiv.org/pdf/2603.05950.pdf)  
**作者**：Jialuo He, Huangxun Chen  

**一句话要点**：提出能量驱动的自适应视觉令牌剪枝框架E-AdaPrune，以提升视觉-语言模型效率

**关键词**：视觉-语言模型, 令牌剪枝, 自适应剪枝, 奇异值分解, 模型加速, 能量驱动

## 3 点简述
- 核心问题：现有视觉令牌剪枝方法采用固定预算，忽略图像信息密度差异，影响模型效率与性能。
- 方法要点：基于视觉特征空间的奇异值谱，通过保留特定比例谱能量自适应确定令牌预算，无额外可学习参数。
- 实验或效果：在九个基准和三个VLM骨干上评估，匹配平均令牌预算时平均提升达0.6%，MMVet推理任务相对提升+5.1%，额外延迟仅8ms每图像。

## 摘要（原文）

> Visual token reduction is critical for accelerating Vision-Language Models (VLMs), yet most existing approaches rely on a fixed budget shared across all inputs, overlooking the substantial variation in image information density. We propose E-AdaPrune, an energy-driven adaptive pruning framework that determines the token budget from the singular value spectrum of the visual features space. By preserving a certain proportion of spectral energy, our method allocates more tokens to information-dense scenes while aggressively compressing redundant ones, without introducing additional learnable parameters. We evaluate E-AdaPrune on nine benchmarks and three VLM backbones, LLaVA-1.5-7B, LLaVA-1.5-13B, and LLaVA-NeXT-8B. Under matched average token budgets, E-AdaPrune consistently yields an average improvement of up to 0.6\%, including a significant +5.1\% relative boost on the MMVet reasoning task. Using randomized singular value decomposition, the additional latency is limited to 8ms per image.

