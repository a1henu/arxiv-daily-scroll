---
layout: default
title: A Rubric-Supervised Critic from Sparse Real-World Outcomes
---

# A Rubric-Supervised Critic from Sparse Real-World Outcomes
**arXiv**：[2603.03800v1](https://arxiv.org/abs/2603.03800) · [PDF](https://arxiv.org/pdf/2603.03800.pdf)  
**作者**：Xingyao Wang, Valerie Chen, Heng Ji, Graham Neubig  

**一句话要点**：提出基于行为特征和稀疏反馈的批评者模型，以弥合编码代理在学术基准与现实应用间的差距。

**关键词**：编码代理, 批评者模型, 稀疏反馈, 人机交互, 半监督学习, 行为特征

## 3 点简述
- 核心问题：现实世界编码代理的成功信号稀疏、延迟且嘈杂，与学术基准的自主任务完成奖励不匹配。
- 方法要点：引入批评者准则，通过24个行为特征从人机交互轨迹中学习，结合半监督目标预测准则和稀疏反馈。
- 实验或效果：在SWE-bench上提升最佳N重排性能，支持早期停止和训练时数据筛选，提高效率。

## 摘要（原文）

> Academic benchmarks for coding agents tend to reward autonomous task completion, measured by verifiable rewards such as unit-test success. In contrast, real-world coding agents operate with humans in the loop, where success signals are typically noisy, delayed, and sparse. How can we bridge this gap? In this paper, we propose a process to learn a "critic" model from sparse and noisy interaction data, which can then be used both as a reward model for either RL-based training or inference-time scaling. Specifically, we introduce Critic Rubrics, a rubric-based supervision framework with 24 behavioral features that can be derived from human-agent interaction traces alone. Using a semi-supervised objective, we can then jointly predict these rubrics and sparse human feedback (when present). In experiments, we demonstrate that, despite being trained primarily from trace-observable rubrics and sparse real-world outcome proxies, these critics improve best-of-N reranking on SWE-bench (Best@8 +15.9 over Random@8 over the rerankable subset of trajectories), enable early stopping (+17.7 with 83% fewer attempts), and support training-time data curation via critic-selected trajectories.

