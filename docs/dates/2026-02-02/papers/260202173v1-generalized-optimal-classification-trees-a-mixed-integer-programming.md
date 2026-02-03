---
layout: default
title: Generalized Optimal Classification Trees: A Mixed-Integer Programming Approach
---

# Generalized Optimal Classification Trees: A Mixed-Integer Programming Approach
**arXiv**：[2602.02173v1](https://arxiv.org/abs/2602.02173) · [PDF](https://arxiv.org/pdf/2602.02173.pdf)  
**作者**：Jiancheng Tu, Wenqi Fan, Zhibin Wu  

**一句话要点**：提出基于混合整数规划的广义最优分类树框架，以优化非线性指标并处理类别不平衡。

**关键词**：决策树优化, 混合整数规划, 非线性性能指标, 类别不平衡, 可解释机器学习, 分支切割算法

## 3 点简述
- 核心问题：决策树全局优化是组合优化中的长期挑战，对可解释机器学习至关重要。
- 方法要点：采用混合整数规划建模，支持F1分数等非线性指标，并开发加速技术如分支切割算法。
- 实验或效果：在50个基准数据集上评估，显示能高效优化非线性指标，提升预测性能并减少求解时间。

## 摘要（原文）

> Global optimization of decision trees is a long-standing challenge in combinatorial optimization, yet such models play an important role in interpretable machine learning. Although the problem has been investigated for several decades, only recent advances in discrete optimization have enabled practical algorithms for solving optimal classification tree problems on real-world datasets. Mixed-integer programming (MIP) offers a high degree of modeling flexibility, and we therefore propose a MIP-based framework for learning optimal classification trees under nonlinear performance metrics, such as the F1-score, that explicitly addresses class imbalance. To improve scalability, we develop problem-specific acceleration techniques, including a tailored branch-and-cut algorithm, an instance-reduction scheme, and warm-start strategies. We evaluate the proposed approach on 50 benchmark datasets. The computational results show that the framework can efficiently optimize nonlinear metrics while achieving strong predictive performance and reduced solution times compared with existing methods.

