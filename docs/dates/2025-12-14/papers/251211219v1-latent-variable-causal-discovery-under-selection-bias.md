---
layout: default
title: Latent Variable Causal Discovery under Selection Bias
---

# Latent Variable Causal Discovery under Selection Bias
**arXiv**：[2512.11219v1](https://arxiv.org/abs/2512.11219) · [PDF](https://arxiv.org/pdf/2512.11219.pdf)  
**作者**：Haoyue Dai, Yiwen Qiu, Ignavier Ng, Xinshuai Dong, Peter Spirtes, Kun Zhang  

**一句话要点**：提出秩约束方法以解决选择偏差下的潜变量因果发现

**关键词**：因果发现, 选择偏差, 潜变量, 秩约束, 线性高斯模型

## 3 点简述
- 核心问题：选择偏差在潜变量因果发现中未被充分探索，缺乏统计工具。
- 方法要点：利用秩约束作为条件独立性的泛化，分析线性高斯模型中协方差子矩阵的秩。
- 实验或效果：通过模拟和真实实验验证秩约束的有效性，识别经典潜变量模型。

## 摘要（原文）

> Addressing selection bias in latent variable causal discovery is important yet underexplored, largely due to a lack of suitable statistical tools: While various tools beyond basic conditional independencies have been developed to handle latent variables, none have been adapted for selection bias. We make an attempt by studying rank constraints, which, as a generalization to conditional independence constraints, exploits the ranks of covariance submatrices in linear Gaussian models. We show that although selection can significantly complicate the joint distribution, interestingly, the ranks in the biased covariance matrices still preserve meaningful information about both causal structures and selection mechanisms. We provide a graph-theoretic characterization of such rank constraints. Using this tool, we demonstrate that the one-factor model, a classical latent variable model, can be identified under selection bias. Simulations and real-world experiments confirm the effectiveness of using our rank constraints.

