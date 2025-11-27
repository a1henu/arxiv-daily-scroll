---
layout: default
title: Gated KalmaNet: A Fading Memory Layer Through Test-Time Ridge Regression
---

# Gated KalmaNet: A Fading Memory Layer Through Test-Time Ridge Regression
**arXiv**：[2511.21016v1](https://arxiv.org/abs/2511.21016) · [PDF](https://arxiv.org/pdf/2511.21016.pdf)  
**作者**：Liangzu Peng, Aditya Chattopadhyay, Luca Zancato, Elvis Nunez, Wei Xia, Stefano Soatto  

**一句话要点**：提出Gated KalmaNet层，通过在线岭回归解决线性状态空间模型记忆损失问题，提升长上下文任务性能。

**关键词**：线性状态空间模型, 在线岭回归, 数值稳定性, 长上下文处理, 自适应门控, 硬件优化

## 3 点简述
- 线性状态空间模型在召回任务中因记忆损失导致性能不佳。
- 采用在线岭回归和自适应门控，确保数值稳定性和高效计算。
- 在长上下文任务中，相对基线模型提升超过10%。

## 摘要（原文）

> As efficient alternatives to softmax Attention, linear state-space models (SSMs) achieve constant memory and linear compute, but maintain only a lossy, fading summary of the past, often leading to inferior performance in recall oriented tasks. We propose Gated KalmaNet (GKA), a layer that reduces this gap by accounting for the full past when predicting the next token, while maintaining SSM-style efficiency. GKA achieves this by solving an online ridge regression problem at test time, with constant memory and linear compute cost in the sequence length. Drawing inspiration from the Kalman Filter, we iteratively solve the online ridge regression problem. However, a critical insight is that standard Kalman filter equations are numerically unstable in low-precision environments (like bfloat16) and difficult to parallelize in modern hardware. We address both challenges through two key innovations: (1) an adaptive regularization strategy with input-dependent gating that controls the condition number of the ridge regression, ensuring numerical stability while balancing memory retention. And (2) the use of Chebyshev Iteration instead of other conventional iterative solvers, which we demonstrate to be more stable in low-precision settings. To further improve scalability, we develop a hardware-aware chunk-wise implementation of Chebyshev Iteration along with custom kernels for backpropagating through our adaptive regularization and gating mechanisms. Empirically, GKA shows strong language understanding capabilites on short-context tasks outperforming existing SSM layers (like Mamba2, GLA and Gated DeltaNet). On long-context, GKA excels at real-world RAG and LongQA tasks up to 128k tokens, achieving more than $10$% relative improvement over other fading memory baselines.

