---
layout: default
title: Unregularized Linear Convergence in Zero-Sum Game from Preference Feedback
---

# Unregularized Linear Convergence in Zero-Sum Game from Preference Feedback
**arXiv**：[2512.24818v1](https://arxiv.org/abs/2512.24818) · [PDF](https://arxiv.org/pdf/2512.24818.pdf)  
**作者**：Shulun Chen, Runlong Zhou, Zihan Zhang, Maryam Fazel, Simon S. Du  

**一句话要点**：提出乐观乘性权重更新在非传递偏好反馈中实现无正则化线性收敛

**关键词**：零和博弈, 偏好反馈, 纳什均衡, 线性收敛, 大语言模型对齐, 非传递偏好

## 3 点简述
- 核心问题：标准偏好建模假设传递性，忽略人类偏好的非传递复杂性，导致对齐偏差
- 方法要点：使用乐观乘性权重更新算法，在纳什均衡存在时实现无正则化线性收敛，无需唯一性假设
- 实验或效果：在表格和神经策略类中验证理论优势，展示在大语言模型应用中的潜力

## 摘要（原文）

> Aligning large language models (LLMs) with human preferences has proven effective for enhancing model capabilities, yet standard preference modeling using the Bradley-Terry model assumes transitivity, overlooking the inherent complexity of human population preferences. Nash learning from human feedback (NLHF) addresses this by framing non-transitive preferences as a two-player zero-sum game, where alignment reduces to finding the Nash equilibrium (NE). However, existing algorithms typically rely on regularization, incurring unavoidable bias when computing the duality gap in the original game. In this work, we provide the first convergence guarantee for Optimistic Multiplicative Weights Update ($\mathtt{OMWU}$) in NLHF, showing that it achieves last-iterate linear convergence after a burn-in phase whenever an NE with full support exists, with an instance-dependent linear convergence rate to the original NE, measured by duality gaps. Compared to prior results in Wei et al. (2020), we do not require the assumption of NE uniqueness. Our analysis identifies a novel marginal convergence behavior, where the probability of rarely played actions grows exponentially from exponentially small values, enabling exponentially better dependence on instance-dependent constants than prior results. Experiments corroborate the theoretical strengths of $\mathtt{OMWU}$ in both tabular and neural policy classes, demonstrating its potential for LLM applications.

