---
layout: default
title: Autoregressive Direct Preference Optimization
---

# Autoregressive Direct Preference Optimization
**arXiv**：[2602.09533v1](https://arxiv.org/abs/2602.09533) · [PDF](https://arxiv.org/pdf/2602.09533.pdf)  
**作者**：Masanari Oi, Mahiro Ukai, Masahiro Kaneko, Naoaki Okazaki, Nakamasa Inoue  

**一句话要点**：提出自回归直接偏好优化以改进大语言模型对齐方法

**关键词**：直接偏好优化, 自回归建模, 大语言模型对齐, Bradley-Terry模型, 偏好优化框架

## 3 点简述
- 核心问题：直接偏好优化依赖响应级Bradley-Terry模型，可能限制潜力，因自回归假设仅在推导目标函数后引入。
- 方法要点：重新审视理论基础，在应用Bradley-Terry模型前显式引入自回归假设，推导出自回归直接偏好优化变体。
- 实验或效果：理论分析揭示需考虑令牌长度和反馈长度两种度量，为基于直接偏好优化的算法设计提供新见解。

## 摘要（原文）

> Direct preference optimization (DPO) has emerged as a promising approach for aligning large language models (LLMs) with human preferences. However, the widespread reliance on the response-level Bradley-Terry (BT) model may limit its full potential, as the reference and learnable models are assumed to be autoregressive only after deriving the objective function. Motivated by this limitation, we revisit the theoretical foundations of DPO and propose a novel formulation that explicitly introduces the autoregressive assumption prior to applying the BT model. By reformulating and extending DPO, we derive a novel variant, termed Autoregressive DPO (ADPO), that explicitly integrates autoregressive modeling into the preference optimization framework. Without violating the theoretical foundations, the derived loss takes an elegant form: it shifts the summation operation in the DPO objective outside the log-sigmoid function. Furthermore, through theoretical analysis of ADPO, we show that there exist two length measures to be considered when designing DPO-based algorithms: the token length $μ$ and the feedback length $μ$'. To the best of our knowledge, we are the first to explicitly distinguish these two measures and analyze their implications for preference optimization in LLMs.

