---
layout: default
title: Talos: Optimizing Top-$K$ Accuracy in Recommender Systems
---

# Talos: Optimizing Top-$K$ Accuracy in Recommender Systems
**arXiv**：[2601.19276v1](https://arxiv.org/abs/2601.19276) · [PDF](https://arxiv.org/pdf/2601.19276.pdf)  
**作者**：Shengjia Zhang, Weiqin Yang, Jiawei Chen, Peng Wu, Yuegang Sun, Gang Wang, Qihao Shi, Can Wang  

**一句话要点**：提出Talos损失函数以优化推荐系统Top-K准确率

**关键词**：推荐系统, Top-K优化, 损失函数设计, 分位数技术, 分布鲁棒性

## 3 点简述
- 核心问题：Top-K准确率优化计算复杂且受分布偏移影响
- 方法要点：使用分位数技术将排序依赖操作简化为分数阈值比较
- 实验效果：理论分析和实证实验验证了有效性、效率和鲁棒性

## 摘要（原文）

> Recommender systems (RS) aim to retrieve a small set of items that best match individual user preferences. Naturally, RS place primary emphasis on the quality of the Top-$K$ results rather than performance across the entire item set. However, estimating Top-$K$ accuracy (e.g., Precision@$K$, Recall@$K$) requires determining the ranking positions of items, which imposes substantial computational overhead and poses significant challenges for optimization. In addition, RS often suffer from distribution shifts due to evolving user preferences or data biases, further complicating the task.
>   To address these issues, we propose Talos, a loss function that is specifically designed to optimize the Talos recommendation accuracy. Talos leverages a quantile technique that replaces the complex ranking-dependent operations into simpler comparisons between predicted scores and learned score thresholds. We further develop a sampling-based regression algorithm for efficient and accurate threshold estimation, and introduce a constraint term to maintain optimization stability by preventing score inflation. Additionally, we incorporate a tailored surrogate function to address discontinuity and enhance robustness against distribution shifts. Comprehensive theoretical analyzes and empirical experiments are conducted to demonstrate the effectiveness, efficiency, convergence, and distributional robustness of Talos. The code is available at https://github.com/cynthia-shengjia/WWW-2026-Talos.

