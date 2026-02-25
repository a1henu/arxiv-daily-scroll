---
layout: default
title: Extending $μ$P: Spectral Conditions for Feature Learning Across Optimizers
---

# Extending $μ$P: Spectral Conditions for Feature Learning Across Optimizers
**arXiv**：[2602.20937v1](https://arxiv.org/abs/2602.20937) · [PDF](https://arxiv.org/pdf/2602.20937.pdf)  
**作者**：Akshita Gupta, Marieme Ngom, Sam Foreman, Venkatram Vishwanath  

**一句话要点**：提出基于谱条件的框架以扩展μP至多种优化器，实现超参数跨模型尺寸零样本迁移。

**关键词**：超参数缩放, 优化器理论, 模型训练加速, 谱条件分析, 零样本迁移

## 3 点简述
- 核心问题：自适应优化器超参数调优计算成本高，μP扩展困难。
- 方法要点：利用谱条件替代张量程序，推导μP规则覆盖AdamW等优化器。
- 实验或效果：在基准模型上验证零样本学习率迁移，提供深度缩放参数化经验见解。

## 摘要（原文）

> Several variations of adaptive first-order and second-order optimization methods have been proposed to accelerate and scale the training of large language models. The performance of these optimization routines is highly sensitive to the choice of hyperparameters (HPs), which are computationally expensive to tune for large-scale models. Maximal update parameterization $(μ$P$)$ is a set of scaling rules which aims to make the optimal HPs independent of the model size, thereby allowing the HPs tuned on a smaller (computationally cheaper) model to be transferred to train a larger, target model. Despite promising results for SGD and Adam, deriving $μ$P for other optimizers is challenging because the underlying tensor programming approach is difficult to grasp. Building on recent work that introduced spectral conditions as an alternative to tensor programs, we propose a novel framework to derive $μ$P for a broader class of optimizers, including AdamW, ADOPT, LAMB, Sophia, Shampoo and Muon. We implement our $μ$P derivations on multiple benchmark models and demonstrate zero-shot learning rate transfer across increasing model width for the above optimizers. Further, we provide empirical insights into depth-scaling parameterization for these optimizers.

