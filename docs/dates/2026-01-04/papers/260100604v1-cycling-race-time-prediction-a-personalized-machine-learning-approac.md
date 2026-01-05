---
layout: default
title: Cycling Race Time Prediction: A Personalized Machine Learning Approach Using Route Topology and Training Load
---

# Cycling Race Time Prediction: A Personalized Machine Learning Approach Using Route Topology and Training Load
**arXiv**：[2601.00604v1](https://arxiv.org/abs/2601.00604) · [PDF](https://arxiv.org/pdf/2601.00604.pdf)  
**作者**：Francisco Aguilera Moreno  

**一句话要点**：提出基于路线拓扑和训练负荷的个性化机器学习方法，以预测自行车骑行时间，解决业余骑手参数化难题。

**关键词**：自行车骑行时间预测, 个性化机器学习, 路线拓扑特征, 训练负荷指标, N-of-1研究设计, Lasso回归

## 3 点简述
- 核心问题：现有物理模型依赖复杂参数，如空气阻力系数和实时风速，对业余骑手不实用。
- 方法要点：使用机器学习结合路线拓扑特征和运动员当前体能状态（基于训练负荷指标），从历史数据学习个性化性能模式。
- 实验或效果：在单运动员数据集上，Lasso回归模型达到MAE=6.60分钟和R2=0.922，整合体能指标比仅用拓扑特征误差降低14%。

## 摘要（原文）

> Predicting cycling duration for a given route is essential for training planning and event preparation. Existing solutions rely on physics-based models that require extensive parameterization, including aerodynamic drag coefficients and real-time wind forecasts, parameters impractical for most amateur cyclists. This work presents a machine learning approach that predicts ride duration using route topology features combined with the athlete's current fitness state derived from training load metrics. The model learns athlete-specific performance patterns from historical data, substituting complex physical measurements with historical performance proxies. We evaluate the approach using a single-athlete dataset (N=96 rides) in an N-of-1 study design. After rigorous feature engineering to eliminate data leakage, we find that Lasso regression with Topology + Fitness features achieves MAE=6.60 minutes and R2=0.922. Notably, integrating fitness metrics (CTL, ATL) reduces error by 14% compared to topology alone (MAE=7.66 min), demonstrating that physiological state meaningfully constrains performance even in self-paced efforts. Progressive checkpoint predictions enable dynamic race planning as route difficulty becomes apparent.

