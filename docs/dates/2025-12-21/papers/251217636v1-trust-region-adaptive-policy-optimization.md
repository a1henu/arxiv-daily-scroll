---
layout: default
title: Trust-Region Adaptive Policy Optimization
---

# Trust-Region Adaptive Policy Optimization
**arXiv**：[2512.17636v1](https://arxiv.org/abs/2512.17636) · [PDF](https://arxiv.org/pdf/2512.17636.pdf)  
**作者**：Mingyu Su, Jian Guan, Yuxian Gu, Minlie Huang, Hongning Wang  

**一句话要点**：提出TRAPO框架以解决大语言模型训练中SFT与RL不一致的问题，提升推理能力。

**关键词**：大语言模型训练, 信任域优化, 自适应策略优化, 数学推理, 混合学习框架

## 3 点简述
- 核心问题：传统SFT后RL的两阶段训练导致模仿抑制探索和遗忘，限制RL改进潜力。
- 方法要点：TRAPO混合SFT与RL，在信任域内优化SFT损失，自适应选择专家前缀，统一监督与探索。
- 实验或效果：在五个数学推理基准上超越标准方法和最新方法，建立推理增强新范式。

## 摘要（原文）

> Post-training methods, especially Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL), play an important role in improving large language models' (LLMs) complex reasoning abilities. However, the dominant two-stage pipeline (SFT then RL) suffers from a key inconsistency: SFT enforces rigid imitation that suppresses exploration and induces forgetting, limiting RL's potential for improvements. We address this inefficiency with TRAPO (\textbf{T}rust-\textbf{R}egion \textbf{A}daptive \textbf{P}olicy \textbf{O}ptimization), a hybrid framework that interleaves SFT and RL within each training instance by optimizing SFT loss on expert prefixes and RL loss on the model's own completions, unifying external supervision and self-exploration. To stabilize training, we introduce Trust-Region SFT (TrSFT), which minimizes forward KL divergence inside a trust region but attenuates optimization outside, effectively shifting toward reverse KL and yielding stable, mode-seeking updates favorable for RL. An adaptive prefix-selection mechanism further allocates expert guidance based on measured utility. Experiments on five mathematical reasoning benchmarks show that TRAPO consistently surpasses standard SFT, RL, and SFT-then-RL pipelines, as well as recent state-of-the-art approaches, establishing a strong new paradigm for reasoning-enhanced LLMs.

