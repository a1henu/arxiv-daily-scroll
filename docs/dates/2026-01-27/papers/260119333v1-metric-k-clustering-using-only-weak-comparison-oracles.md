---
layout: default
title: Metric $k$-clustering using only Weak Comparison Oracles
---

# Metric $k$-clustering using only Weak Comparison Oracles
**arXiv**：[2601.19333v1](https://arxiv.org/abs/2601.19333) · [PDF](https://arxiv.org/pdf/2601.19333.pdf)  
**作者**：Rahul Raychaudhury, Aryan Esmailpour, Sainyam Galhotra, Stavros Sintos  

**一句话要点**：提出基于弱比较预言机的度量k聚类算法，以解决无精确距离时的聚类问题。

**关键词**：聚类算法, 弱比较预言机, 度量空间, 查询复杂度, 噪声模型, 可扩展聚类

## 3 点简述
- 研究在仅提供相对距离比较的Rank模型中进行k聚类，替代传统精确距离需求。
- 设计随机算法，使用噪声四元组预言机，实现常数倍最优成本的聚类，查询复杂度为O(n·k·polylog(n))。
- 在度量空间有界加倍维度时，改进查询复杂度至O((n+k²)·polylog(n))，并可达到1+ε近似。

## 摘要（原文）

> Clustering is a fundamental primitive in unsupervised learning. However, classical algorithms for $k$-clustering (such as $k$-median and $k$-means) assume access to exact pairwise distances -- an unrealistic requirement in many modern applications. We study clustering in the \emph{Rank-model (R-model)}, where access to distances is entirely replaced by a \emph{quadruplet oracle} that provides only relative distance comparisons. In practice, such an oracle can represent learned models or human feedback, and is expected to be noisy and entail an access cost.
>   Given a metric space with $n$ input items, we design randomized algorithms that, using only a noisy quadruplet oracle, compute a set of $O(k \cdot \mathsf{polylog}(n))$ centers along with a mapping from the input items to the centers such that the clustering cost of the mapping is at most constant times the optimum $k$-clustering cost. Our method achieves a query complexity of $O(n\cdot k \cdot \mathsf{polylog}(n))$ for arbitrary metric spaces and improves to $O((n+k^2) \cdot \mathsf{polylog}(n))$ when the underlying metric has bounded doubling dimension. When the metric has bounded doubling dimension we can further improve the approximation from constant to $1+\varepsilon$, for any arbitrarily small constant $\varepsilon\in(0,1)$, while preserving the same asymptotic query complexity. Our framework demonstrates how noisy, low-cost oracles, such as those derived from large language models, can be systematically integrated into scalable clustering algorithms.

