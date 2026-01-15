---
layout: default
title: MMR-GRPO: Accelerating GRPO-Style Training through Diversity-Aware Reward Reweighting
---

# MMR-GRPO: Accelerating GRPO-Style Training through Diversity-Aware Reward Reweighting
**arXiv**：[2601.09085v1](https://arxiv.org/abs/2601.09085) · [PDF](https://arxiv.org/pdf/2601.09085.pdf)  
**作者**：Kangda Wei, Ruihong Huang  

**一句话要点**：提出MMR-GRPO，通过多样性感知奖励重加权加速GRPO风格训练

**关键词**：数学推理模型, 策略优化, 奖励重加权, 训练加速, 多样性感知

## 3 点简述
- 核心问题：GRPO依赖多补全导致训练计算成本高，整体训练时间未显著减少
- 方法要点：集成最大边际相关性，基于补全多样性重加权奖励，优先多样化解决方案
- 实验或效果：在多个模型和基准上，平均减少47.9%训练步数和70.2%训练时间，性能相当

## 摘要（原文）

> Group Relative Policy Optimization (GRPO) has become a standard approach for training mathematical reasoning models; however, its reliance on multiple completions per prompt makes training computationally expensive. Although recent work has reduced the number of training steps required to reach peak performance, the overall wall-clock training time often remains unchanged or even increases due to higher per-step cost. We propose MMR-GRPO, which integrates Maximal Marginal Relevance to reweigh rewards based on completion diversity. Our key insight is that semantically redundant completions contribute limited marginal learning signal; prioritizing diverse solutions yields more informative updates and accelerates convergence. Extensive evaluations across three model sizes (1.5B, 7B, 8B), three GRPO variants, and five mathematical reasoning benchmarks show that MMR-GRPO achieves comparable peak performance while requiring on average 47.9% fewer training steps and 70.2% less wall-clock time. These gains are consistent across models, methods, and benchmarks. We will release our code, trained models, and experimental protocols.

