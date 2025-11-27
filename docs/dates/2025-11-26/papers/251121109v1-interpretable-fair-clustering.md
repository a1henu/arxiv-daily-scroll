---
layout: default
title: Interpretable Fair Clustering
---

# Interpretable Fair Clustering
**arXiv**：[2511.21109v1](https://arxiv.org/abs/2511.21109) · [PDF](https://arxiv.org/pdf/2511.21109.pdf)  
**作者**：Mudi Jiang, Jiahui Zhou, Xinying Liu, Zengyou He, Zhikui Chen  

**一句话要点**：提出可解释公平聚类框架，通过决策树集成公平约束解决高风险场景应用问题。

**关键词**：公平聚类, 可解释性, 决策树, 多敏感属性, 高维数据

## 3 点简述
- 现有公平聚类方法缺乏可解释性，限制在高风险决策场景的应用。
- 方法将公平约束集成到决策树结构中，构建可解释的数据分区。
- 实验显示方法在聚类性能、公平性和多敏感属性处理上表现优异。

## 摘要（原文）

> Fair clustering has gained increasing attention in recent years, especially in applications involving socially sensitive attributes. However, existing fair clustering methods often lack interpretability, limiting their applicability in high-stakes scenarios where understanding the rationale behind clustering decisions is essential. In this work, we address this limitation by proposing an interpretable and fair clustering framework, which integrates fairness constraints into the structure of decision trees. Our approach constructs interpretable decision trees that partition the data while ensuring fair treatment across protected groups. To further enhance the practicality of our framework, we also introduce a variant that requires no fairness hyperparameter tuning, achieved through post-pruning a tree constructed without fairness constraints. Extensive experiments on both real-world and synthetic datasets demonstrate that our method not only delivers competitive clustering performance and improved fairness, but also offers additional advantages such as interpretability and the ability to handle multiple sensitive attributes. These strengths enable our method to perform robustly under complex fairness constraints, opening new possibilities for equitable and transparent clustering.

