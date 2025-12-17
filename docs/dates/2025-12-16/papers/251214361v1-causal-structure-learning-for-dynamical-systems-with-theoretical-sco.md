---
layout: default
title: Causal Structure Learning for Dynamical Systems with Theoretical Score Analysis
---

# Causal Structure Learning for Dynamical Systems with Theoretical Score Analysis
**arXiv**：[2512.14361v1](https://arxiv.org/abs/2512.14361) · [PDF](https://arxiv.org/pdf/2512.14361.pdf)  
**作者**：Nicholas Tagliapietra, Katharina Ensinger, Christoph Zimmer, Osman Mian  

**一句话要点**：提出CaDyT方法以解决动态系统中因果结构学习在连续时间和不规则采样数据上的挑战。

**关键词**：因果发现, 动态系统, 连续时间建模, 高斯过程, 不规则采样数据, 算法马尔可夫条件

## 3 点简述
- 核心问题：现有方法在连续时间动态系统因果发现中，常因时间离散化或忽略因果性导致性能不佳。
- 方法要点：基于Difference-based因果模型，利用高斯过程推理建模连续时间动态，结合贪婪搜索和算法马尔可夫条件进行结构识别。
- 实验或效果：在规则和不规则采样数据上优于现有方法，能更接近真实动态发现因果网络。

## 摘要（原文）

> Real world systems evolve in continuous-time according to their underlying causal relationships, yet their dynamics are often unknown. Existing approaches to learning such dynamics typically either discretize time -- leading to poor performance on irregularly sampled data -- or ignore the underlying causality. We propose CaDyT, a novel method for causal discovery on dynamical systems addressing both these challenges. In contrast to state-of-the-art causal discovery methods that model the problem using discrete-time Dynamic Bayesian networks, our formulation is grounded in Difference-based causal models, which allow milder assumptions for modeling the continuous nature of the system. CaDyT leverages exact Gaussian Process inference for modeling the continuous-time dynamics which is more aligned with the underlying dynamical process. We propose a practical instantiation that identifies the causal structure via a greedy search guided by the Algorithmic Markov Condition and Minimum Description Length principle. Our experiments show that CaDyT outperforms state-of-the-art methods on both regularly and irregularly-sampled data, discovering causal networks closer to the true underlying dynamics.

