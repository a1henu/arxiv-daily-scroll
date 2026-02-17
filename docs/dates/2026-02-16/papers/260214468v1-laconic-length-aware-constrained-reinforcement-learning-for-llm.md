---
layout: default
title: LACONIC: Length-Aware Constrained Reinforcement Learning for LLM
---

# LACONIC: Length-Aware Constrained Reinforcement Learning for LLM
**arXiv**：[2602.14468v1](https://arxiv.org/abs/2602.14468) · [PDF](https://arxiv.org/pdf/2602.14468.pdf)  
**作者**：Chang Liu, Yiran Zhao, Lawrence Liu, Yaoqi Ye, Csaba Szepesvári, Lin F. Yang  

**一句话要点**：提出LACONIC方法，通过强化学习约束大语言模型响应长度，以降低推理延迟和计算开销。

**关键词**：大语言模型, 强化学习, 长度控制, 推理优化, 自适应训练

## 3 点简述
- 核心问题：强化学习训练大语言模型易产生过长响应，增加推理延迟和计算成本。
- 方法要点：在训练中结合任务奖励和基于长度的成本，自适应调整成本尺度以平衡简洁性和任务性能。
- 实验或效果：在数学推理任务中保持或提升性能，输出长度减少超50%，并在通用知识基准上减少44%令牌。

## 摘要（原文）

> Reinforcement learning (RL) has enhanced the capabilities of large language models (LLMs) through reward-driven training. Nevertheless, this process can introduce excessively long responses, inflating inference latency and computational overhead. Prior length-control approaches typically rely on fixed heuristic reward shaping, which can misalign with the task objective and require brittle tuning. In this work, we propose LACONIC, a reinforcement learning method that enforces a target token budget during training. Specifically, we update policy models using an augmented objective that combines the task reward with a length-based cost. To balance brevity and task performance, the cost scale is adaptively adjusted throughout training. This yields robust length control while preserving task reward. We provide a theoretical guarantee that support the method. Across mathematical reasoning models and datasets, LACONIC preserves or improves pass@1 while reducing output length by over 50%. It maintains out-of-domain performance on general knowledge and multilingual benchmarks with 44% fewer tokens. Moreover, LACONIC integrates into standard RL-tuning with no inference changes and minimal deployment overhead.

