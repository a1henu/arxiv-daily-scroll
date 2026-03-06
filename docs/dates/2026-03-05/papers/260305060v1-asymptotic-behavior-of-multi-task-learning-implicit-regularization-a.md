---
layout: default
title: Asymptotic Behavior of Multi--Task Learning: Implicit Regularization and Double Descent Effects
---

# Asymptotic Behavior of Multi--Task Learning: Implicit Regularization and Double Descent Effects
**arXiv**：[2603.05060v1](https://arxiv.org/abs/2603.05060) · [PDF](https://arxiv.org/pdf/2603.05060.pdf)  
**作者**：Ayed M. Alrashdi, Oussama Dhifallah, Houssem Sifaou  

**一句话要点**：分析多任务学习的渐近行为，揭示其隐含正则化与双下降效应缓解机制

**关键词**：多任务学习, 渐近分析, 隐含正则化, 双下降效应, 泛化性能, 感知机模型

## 3 点简述
- 研究多任务学习中如何有效利用任务间共享信息以提升泛化性能
- 通过渐近分析证明多任务组合等价于传统方法添加正则化项
- 实证显示多任务组合能推迟并渐近缓解双下降现象

## 摘要（原文）

> Multi--task learning seeks to improve the generalization error by leveraging the common information shared by multiple related tasks. One challenge in multi--task learning is identifying formulations capable of uncovering the common information shared between different but related tasks. This paper provides a precise asymptotic analysis of a popular multi--task formulation associated with misspecified perceptron learning models. The main contribution of this paper is to precisely determine the reasons behind the benefits gained from combining multiple related tasks. Specifically, we show that combining multiple tasks is asymptotically equivalent to a traditional formulation with additional regularization terms that help improve the generalization performance. Another contribution is to empirically study the impact of combining tasks on the generalization error. In particular, we empirically show that the combination of multiple tasks postpones the double descent phenomenon and can mitigate it asymptotically.

