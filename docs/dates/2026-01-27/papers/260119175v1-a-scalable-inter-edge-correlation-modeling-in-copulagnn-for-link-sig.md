---
layout: default
title: A Scalable Inter-edge Correlation Modeling in CopulaGNN for Link Sign Prediction
---

# A Scalable Inter-edge Correlation Modeling in CopulaGNN for Link Sign Prediction
**arXiv**：[2601.19175v1](https://arxiv.org/abs/2601.19175) · [PDF](https://arxiv.org/pdf/2601.19175.pdf)  
**作者**：Jinkyu Sung, Myunggeum Jee, Joonseok Lee  

**一句话要点**：提出基于高斯Copula的边间相关性建模方法，以解决符号图链接预测中的可扩展性问题。

**关键词**：符号图链接预测, 高斯Copula, 边间相关性建模, 可扩展性优化, 图神经网络

## 3 点简述
- 核心问题：符号图中负边违反同质性假设，传统图方法需辅助结构处理，直接建模边间相关性计算成本高。
- 方法要点：使用高斯Copula建模边间统计依赖，通过边嵌入的Gramian表示相关矩阵以减少参数，并重构条件概率分布降低推理成本。
- 实验或效果：理论证明线性收敛，实验显示比基线更快收敛，预测性能与最先进模型竞争。

## 摘要（原文）

> Link sign prediction on a signed graph is a task to determine whether the relationship represented by an edge is positive or negative. Since the presence of negative edges violates the graph homophily assumption that adjacent nodes are similar, regular graph methods have not been applicable without auxiliary structures to handle them. We aim to directly model the latent statistical dependency among edges with the Gaussian copula and its corresponding correlation matrix, extending CopulaGNN. However, a naive modeling of edge-edge relations is computationally intractable even for a graph with moderate scale. To address this, we propose to 1) represent the correlation matrix as a Gramian of edge embeddings, significantly reducing the number of parameters, and 2) reformulate the conditional probability distribution to dramatically reduce the inference cost. We theoretically verify scalability of our method by proving its linear convergence. Also, our extensive experiments demonstrate that it achieves significantly faster convergence than baselines, maintaining competitive prediction performance to the state-of-the-art models.

