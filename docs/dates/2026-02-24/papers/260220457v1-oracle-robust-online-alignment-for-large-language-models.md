---
layout: default
title: Oracle-Robust Online Alignment for Large Language Models
---

# Oracle-Robust Online Alignment for Large Language Models
**arXiv**：[2602.20457v1](https://arxiv.org/abs/2602.20457) · [PDF](https://arxiv.org/pdf/2602.20457.pdf)  
**作者**：Zimeng Li, Mudit Gaur, Vaneet Aggarwal  

**一句话要点**：提出Oracle-Robust在线对齐方法，以处理大语言模型在偏好反馈误设下的鲁棒性问题。

**关键词**：大语言模型对齐, 在线学习, 鲁棒优化, 偏好反馈, 不确定性建模, 强化学习

## 3 点简述
- 研究大语言模型在线对齐中偏好反馈误设问题，即观测偏好与未知真实偏好存在偏差。
- 引入点式Oracle不确定性集，将鲁棒对齐目标建模为最坏情况优化问题，并推导出闭式分解。
- 开发投影随机复合更新算法，证明达到近似平稳点的Oracle复杂度为O(ε^{-2})。

## 摘要（原文）

> We study online alignment of large language models under misspecified preference feedback, where the observed preference oracle deviates from an ideal but unknown ground-truth oracle. The online LLM alignment problem is a bi-level reinforcement problem due to the coupling between data collection and policy updates. Recently, the problem has been reduced to tractable single-level objective in the SAIL (Self-Improving Efficient Online Alignment) framework. In this paper, we introduce a pointwise oracle uncertainty set in this problem and formulate an oracle-robust online alignment objective as a worst-case optimization problem. For log-linear policies, we show that this robust objective admits an exact closed-form decomposition into the original loss function plus an explicit sensitivity penalty. We develop projected stochastic composite updates for the resulting weakly convex objective and prove $\widetilde{O}(\varepsilon^{-2})$ oracle complexity for reaching approximate stationarity.

