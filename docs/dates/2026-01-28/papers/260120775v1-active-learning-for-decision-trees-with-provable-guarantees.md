---
layout: default
title: Active Learning for Decision Trees with Provable Guarantees
---

# Active Learning for Decision Trees with Provable Guarantees
**arXiv**：[2601.20775v1](https://arxiv.org/abs/2601.20775) · [PDF](https://arxiv.org/pdf/2601.20775.pdf)  
**作者**：Arshia Soltani Moakhar, Tanapoom Laoaron, Faraz Ghahremani, Kiarash Banihashem, MohammadTaghi Hajiaghayi  

**一句话要点**：提出主动学习决策树算法，在特定假设下实现对数级标签复杂度与乘法误差保证。

**关键词**：主动学习, 决策树, 标签复杂度, 分歧系数, 乘法误差保证, 理论分析

## 3 点简述
- 核心问题：分析决策树主动学习的标签复杂度，首次研究分歧系数并建立理论保证。
- 方法要点：设计主动学习算法，在网格状数据结构和路径特征不重复假设下，实现(1+ε)-近似分类器。
- 实验或效果：证明算法标签复杂度接近最优，放松假设会导致多项式复杂度。

## 摘要（原文）

> This paper advances the theoretical understanding of active learning label complexity for decision trees as binary classifiers. We make two main contributions. First, we provide the first analysis of the disagreement coefficient for decision trees-a key parameter governing active learning label complexity. Our analysis holds under two natural assumptions required for achieving polylogarithmic label complexity, (i) each root-to-leaf path queries distinct feature dimensions, and (ii) the input data has a regular, grid-like structure. We show these assumptions are essential, as relaxing them leads to polynomial label complexity. Second, we present the first general active learning algorithm for binary classification that achieves a multiplicative error guarantee, producing a $(1+ε)$-approximate classifier. By combining these results, we design an active learning algorithm for decision trees that uses only a polylogarithmic number of label queries in the dataset size, under the stated assumptions. Finally, we establish a label complexity lower bound, showing our algorithm's dependence on the error tolerance $ε$ is close to optimal.

