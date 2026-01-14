---
layout: default
title: On the use of graph models to achieve individual and group fairness
---

# On the use of graph models to achieve individual and group fairness
**arXiv**：[2601.08784v1](https://arxiv.org/abs/2601.08784) · [PDF](https://arxiv.org/pdf/2601.08784.pdf)  
**作者**：Arturo Pérez-Peralta, Sandra Benítez-Peña, Rosa E. Lillo  

**一句话要点**：提出基于层扩散的图模型框架，以统一处理个体与群体公平性约束

**关键词**：公平机器学习, 图模型, 层扩散, 个体公平, 群体公平, 可解释人工智能

## 3 点简述
- 核心问题：机器学习在关键决策中公平性理论不足，个体与群体公平关系不明确
- 方法要点：利用层扩散工具将数据投影到无偏空间，编码公平约束，支持多种网络拓扑
- 实验或效果：在模拟和标准基准测试中验证准确性、公平性及可解释性，分析帕累托前沿

## 摘要（原文）

> Machine Learning algorithms are ubiquitous in key decision-making contexts such as justice, healthcare and finance, which has spawned a great demand for fairness in these procedures. However, the theoretical properties of such models in relation with fairness are still poorly understood, and the intuition behind the relationship between group and individual fairness is still lacking. In this paper, we provide a theoretical framework based on Sheaf Diffusion to leverage tools based on dynamical systems and homology to model fairness. Concretely, the proposed method projects input data into a bias-free space that encodes fairness constrains, resulting in fair solutions. Furthermore, we present a collection of network topologies handling different fairness metrics, leading to a unified method capable of dealing with both individual and group bias. The resulting models have a layer of interpretability in the form of closed-form expressions for their SHAP values, consolidating their place in the responsible Artificial Intelligence landscape. Finally, these intuitions are tested on a simulation study and standard fairness benchmarks, where the proposed methods achieve satisfactory results. More concretely, the paper showcases the performance of the proposed models in terms of accuracy and fairness, studying available trade-offs on the Pareto frontier, checking the effects of changing the different hyper-parameters, and delving into the interpretation of its outputs.

