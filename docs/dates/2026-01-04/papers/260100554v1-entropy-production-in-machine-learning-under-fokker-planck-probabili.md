---
layout: default
title: Entropy Production in Machine Learning Under Fokker-Planck Probability Flow
---

# Entropy Production in Machine Learning Under Fokker-Planck Probability Flow
**arXiv**：[2601.00554v1](https://arxiv.org/abs/2601.00554) · [PDF](https://arxiv.org/pdf/2601.00554.pdf)  
**作者**：Lennon Shikhman  

**一句话要点**：提出基于熵的再训练框架以应对非平稳环境中的数据漂移问题

**关键词**：数据漂移, 熵触发再训练, Fokker-Planck方程, 非平稳环境, Kullback-Leibler散度

## 3 点简述
- 核心问题：机器学习模型在非平稳环境中因数据漂移导致性能下降，现有漂移检测方法缺乏动力学解释和再训练频率指导
- 方法要点：将数据漂移建模为Fokker-Planck方程控制的概率流，利用Kullback-Leibler散度量化模型-数据不匹配，并基于熵平衡分解设计无标签触发策略
- 实验或效果：在非平稳分类实验中，熵触发再训练在保持预测性能的同时，相比每日和基于标签的策略显著减少再训练次数

## 摘要（原文）

> Machine learning models deployed in nonstationary environments experience performance degradation due to data drift. While many drift detection heuristics exist, most lack a principled dynamical interpretation and provide limited guidance on how retraining frequency should be balanced against operational cost. In this work, we propose an entropy--based retraining framework grounded in nonequilibrium stochastic dynamics. Modeling deployment--time data drift as probability flow governed by a Fokker--Planck equation, we quantify model--data mismatch using a time--evolving Kullback--Leibler divergence. We show that the time derivative of this mismatch admits an entropy--balance decomposition featuring a nonnegative entropy production term driven by probability currents. This interpretation motivates entropy--triggered retraining as a label--free intervention strategy that responds to accumulated mismatch rather than delayed performance collapse. In a controlled nonstationary classification experiment, entropy--triggered retraining achieves predictive performance comparable to high--frequency retraining while reducing retraining events by an order of magnitude relative to daily and label--based policies.

