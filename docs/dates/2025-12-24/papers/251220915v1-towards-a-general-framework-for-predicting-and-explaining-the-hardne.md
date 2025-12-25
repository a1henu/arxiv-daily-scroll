---
layout: default
title: Towards a General Framework for Predicting and Explaining the Hardness of Graph-based Combinatorial Optimization Problems using Machine Learning and Association Rule Mining
---

# Towards a General Framework for Predicting and Explaining the Hardness of Graph-based Combinatorial Optimization Problems using Machine Learning and Association Rule Mining
**arXiv**：[2512.20915v1](https://arxiv.org/abs/2512.20915) · [PDF](https://arxiv.org/pdf/2512.20915.pdf)  
**作者**：Bharat Sharman, Elkafi Hassini  

**一句话要点**：提出GCO-HPIF框架，基于机器学习和关联规则挖掘预测并解释图组合优化问题的计算难度

**关键词**：图组合优化, 计算难度预测, 机器学习分类, 关联规则挖掘, 最大团问题, 图特征分析

## 3 点简述
- 核心问题：预测和解释图组合优化问题的计算难度，以指导算法选择或优化。
- 方法要点：两阶段框架，先训练分类模型预测难度，再用关联规则挖掘解释预测结果。
- 实验效果：在最大团问题上，仅用三个图特征实现高精度预测，关联规则解释准确率达87.64%。

## 摘要（原文）

> This study introduces GCO-HPIF, a general machine-learning-based framework to predict and explain the computational hardness of combinatorial optimization problems that can be represented on graphs. The framework consists of two stages. In the first stage, a dataset is created comprising problem-agnostic graph features and hardness classifications of problem instances. Machine-learning-based classification algorithms are trained to map graph features to hardness categories. In the second stage, the framework explains the predictions using an association rule mining algorithm. Additionally, machine-learning-based regression models are trained to predict algorithmic computation times. The GCO-HPIF framework was applied to a dataset of 3287 maximum clique problem instances compiled from the COLLAB, IMDB, and TWITTER graph datasets using five state-of-the-art algorithms, namely three exact branch-and-bound-based algorithms (Gurobi, CliSAT, and MOMC) and two graph-neural-network-based algorithms (EGN and HGS). The framework demonstrated excellent performance in predicting instance hardness, achieving a weighted F1 score of 0.9921, a minority-class F1 score of 0.878, and an ROC-AUC score of 0.9083 using only three graph features. The best association rule found by the FP-Growth algorithm for explaining the hardness predictions had a support of 0.8829 for hard instances and an overall accuracy of 87.64 percent, underscoring the framework's usefulness for both prediction and explanation. Furthermore, the best-performing regression model for predicting computation times achieved a percentage RMSE of 5.12 and an R2 value of 0.991.

