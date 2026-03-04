---
layout: default
title: On the Expressive Power of Transformers for Maxout Networks and Continuous Piecewise Linear Functions
---

# On the Expressive Power of Transformers for Maxout Networks and Continuous Piecewise Linear Functions
**arXiv**：[2603.03084v1](https://arxiv.org/abs/2603.03084) · [PDF](https://arxiv.org/pdf/2603.03084.pdf)  
**作者**：Linyan Gu, Lihua Yang, Feng Zhou  

**一句话要点**：建立Transformer与maxout网络的理论联系，分析其对连续分段线性函数的表达能力。

**关键词**：Transformer理论, 表达能力分析, maxout网络, 连续分段线性函数, 近似理论, 神经网络结构

## 3 点简述
- 研究Transformer的理论表达能力，核心问题在于其与标准前馈网络的近似关系。
- 方法上，通过Transformer显式近似maxout网络，并基于此分析连续分段线性函数的逼近。
- 效果上，量化表达性，线性区域数随深度指数增长，为Transformer结构提供理论洞察。

## 摘要（原文）

> Transformer networks have achieved remarkable empirical success across a wide range of applications, yet their theoretical expressive power remains insufficiently understood. In this paper, we study the expressive capabilities of Transformer architectures. We first establish an explicit approximation of maxout networks by Transformer networks while preserving comparable model complexity. As a consequence, Transformers inherit the universal approximation capability of ReLU networks under similar complexity constraints. Building on this connection, we develop a framework to analyze the approximation of continuous piecewise linear functions by Transformers and quantitatively characterize their expressivity via the number of linear regions, which grows exponentially with depth. Our analysis establishes a theoretical bridge between approximation theory for standard feedforward neural networks and Transformer architectures. It also yields structural insights into Transformers: self-attention layers implement max-type operations, while feedforward layers realize token-wise affine transformations.

