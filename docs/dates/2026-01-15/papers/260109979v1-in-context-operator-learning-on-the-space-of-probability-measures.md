---
layout: default
title: In-Context Operator Learning on the Space of Probability Measures
---

# In-Context Operator Learning on the Space of Probability Measures
**arXiv**：[2601.09979v1](https://arxiv.org/abs/2601.09979) · [PDF](https://arxiv.org/pdf/2601.09979.pdf)  
**作者**：Frank Cole, Dixi Wang, Yineng Chen, Yulong Lu, Rongjie Lai  

**一句话要点**：提出概率测度空间上的上下文算子学习框架，用于最优传输任务，实现少样本无梯度推理。

**关键词**：最优传输, 上下文学习, 概率测度空间, 算子学习, 少样本学习, 泛化理论

## 3 点简述
- 核心问题：在概率测度空间上学习最优传输映射的算子，仅用少样本提示且推理时无需梯度更新。
- 方法要点：参数化解算子，建立非参数和参数设置下的缩放理论，包括泛化界和精确恢复架构。
- 实验或效果：在合成传输和生成建模基准上验证框架，展示上下文准确性随提示大小和任务维度的扩展。

## 摘要（原文）

> We introduce \emph{in-context operator learning on probability measure spaces} for optimal transport (OT). The goal is to learn a single solution operator that maps a pair of distributions to the OT map, using only few-shot samples from each distribution as a prompt and \emph{without} gradient updates at inference. We parameterize the solution operator and develop scaling-law theory in two regimes. In the \emph{nonparametric} setting, when tasks concentrate on a low-intrinsic-dimension manifold of source--target pairs, we establish generalization bounds that quantify how in-context accuracy scales with prompt size, intrinsic task dimension, and model capacity. In the \emph{parametric} setting (e.g., Gaussian families), we give an explicit architecture that recovers the exact OT map in context and provide finite-sample excess-risk bounds. Our numerical experiments on synthetic transports and generative-modeling benchmarks validate the framework.

