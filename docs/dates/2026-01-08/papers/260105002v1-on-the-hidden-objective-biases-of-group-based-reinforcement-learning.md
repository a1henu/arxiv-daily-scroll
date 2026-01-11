---
layout: default
title: On the Hidden Objective Biases of Group-based Reinforcement Learning
---

# On the Hidden Objective Biases of Group-based Reinforcement Learning
**arXiv**：[2601.05002v1](https://arxiv.org/abs/2601.05002) · [PDF](https://arxiv.org/pdf/2601.05002.pdf)  
**作者**：Aleksandar Fontana, Marco Simoni, Giulio Rossolini, Andrea Saracino, Paolo Mori  

**一句话要点**：分析GRPO类方法揭示梯度偏差与优化器交互问题

**关键词**：强化学习, 梯度偏差, 优化器交互, 理论分析, 大语言模型

## 3 点简述
- 核心问题：组强化学习方法存在奖励优化与训练目标的结构性不匹配
- 方法要点：通过统一代理公式理论分析，揭示非均匀组权重导致梯度偏差
- 实验或效果：发现AdamW优化器使训练对奖励缩放不敏感，动量可能超出裁剪区域

## 摘要（原文）

> Group-based reinforcement learning methods, like Group Relative Policy Optimization (GRPO), are widely used nowadays to post-train large language models. Despite their empirical success, they exhibit structural mismatches between reward optimization and the underlying training objective. In this paper, we present a theoretical analysis of GRPO style methods by studying them within a unified surrogate formulation. This perspective reveals recurring properties that affect all the methods under analysis: (i) non-uniform group weighting induces systematic gradient biases on shared prefix tokens; (ii) interactions with the AdamW optimizer make training dynamics largely insensitive to reward scaling; and (iii) optimizer momentum can push policy updates beyond the intended clipping region under repeated optimization steps. We believe that these findings highlight fundamental limitations of current approaches and provide principled guidance for the design of future formulations.

