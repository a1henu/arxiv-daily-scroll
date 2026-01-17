---
layout: default
title: In-Context Operator Learning on the Space of Probability Measures
---

# In-Context Operator Learning on the Space of Probability Measures
**arXiv**：[2601.09979v1](https://arxiv.org/abs/2601.09979) · [PDF](https://arxiv.org/pdf/2601.09979.pdf)  
**作者**：Frank Cole, Dixi Wang, Yineng Chen, Yulong Lu, Rongjie Lai  

**一句话要点**：提出概率测度空间上的上下文算子学习，用于最优传输的少样本推断。

**关键词**：最优传输, 上下文学习, 概率测度空间, 算子学习, 少样本推断, 泛化理论

## 3 点简述
- 核心问题：学习一个算子，从分布对映射到最优传输映射，无需推理时梯度更新。
- 方法要点：参数化解算子，在非参数和参数设置下建立泛化界和精确架构理论。
- 实验或效果：在合成传输和生成模型基准上验证框架的有效性。

## 摘要（原文）

> We introduce \emph{in-context operator learning on probability measure spaces} for optimal transport (OT). The goal is to learn a single solution operator that maps a pair of distributions to the OT map, using only few-shot samples from each distribution as a prompt and \emph{without} gradient updates at inference. We parameterize the solution operator and develop scaling-law theory in two regimes. In the \emph{nonparametric} setting, when tasks concentrate on a low-intrinsic-dimension manifold of source--target pairs, we establish generalization bounds that quantify how in-context accuracy scales with prompt size, intrinsic task dimension, and model capacity. In the \emph{parametric} setting (e.g., Gaussian families), we give an explicit architecture that recovers the exact OT map in context and provide finite-sample excess-risk bounds. Our numerical experiments on synthetic transports and generative-modeling benchmarks validate the framework.

