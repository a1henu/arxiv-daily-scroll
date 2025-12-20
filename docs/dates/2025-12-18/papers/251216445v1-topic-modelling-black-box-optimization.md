---
layout: default
title: Topic Modelling Black Box Optimization
---

# Topic Modelling Black Box Optimization
**arXiv**：[2512.16445v1](https://arxiv.org/abs/2512.16445) · [PDF](https://arxiv.org/pdf/2512.16445.pdf)  
**作者**：Roman Akramov, Artem Khamatullin, Svetlana Glazyrina, Maksim Kryzhanovskiy, Roman Ischenko  

**一句话要点**：提出基于黑盒优化的主题数选择方法，提升LDA模型效率与性能

**关键词**：主题建模, 黑盒优化, LDA模型, 摊销优化, 进化算法, 验证困惑度

## 3 点简述
- 核心问题：LDA主题数选择影响模型统计拟合与可解释性，需高效优化
- 方法要点：将主题数选择建模为离散黑盒优化，比较进化算法与摊销优化器
- 实验或效果：摊销优化器SABBO和PABBO在样本和时间效率上显著优于GA和ES

## 摘要（原文）

> Choosing the number of topics $T$ in Latent Dirichlet Allocation (LDA) is a key design decision that strongly affects both the statistical fit and interpretability of topic models. In this work, we formulate the selection of $T$ as a discrete black-box optimization problem, where each function evaluation corresponds to training an LDA model and measuring its validation perplexity. Under a fixed evaluation budget, we compare four families of optimizers: two hand-designed evolutionary methods - Genetic Algorithm (GA) and Evolution Strategy (ES) - and two learned, amortized approaches, Preferential Amortized Black-Box Optimization (PABBO) and Sharpness-Aware Black-Box Optimization (SABBO). Our experiments show that, while GA, ES, PABBO, and SABBO eventually reach a similar band of final perplexity, the amortized optimizers are substantially more sample- and time-efficient. SABBO typically identifies a near-optimal topic number after essentially a single evaluation, and PABBO finds competitive configurations within a few evaluations, whereas GA and ES require almost the full budget to approach the same region.

