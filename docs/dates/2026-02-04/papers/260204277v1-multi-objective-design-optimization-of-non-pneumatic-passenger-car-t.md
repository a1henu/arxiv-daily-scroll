---
layout: default
title: Multi Objective Design Optimization of Non Pneumatic Passenger Car Tires Using Finite Element Modeling, Machine Learning, and Particle swarm Optimization and Bayesian Optimization Algorithms
---

# Multi Objective Design Optimization of Non Pneumatic Passenger Car Tires Using Finite Element Modeling, Machine Learning, and Particle swarm Optimization and Bayesian Optimization Algorithms
**arXiv**：[2602.04277v1](https://arxiv.org/abs/2602.04277) · [PDF](https://arxiv.org/pdf/2602.04277.pdf)  
**作者**：Priyankkumar Dhrangdhariya, Soumyadipta Maiti, Venkataramana Runkana  

**一句话要点**：提出集成生成式设计与机器学习的框架，以优化非充气轮胎的辐条几何结构。

**关键词**：非充气轮胎优化, 生成式设计, 机器学习预测, 多目标优化, 有限元建模

## 3 点简述
- 核心问题：非充气轮胎辐条结构在刚度调节、耐久性和高速振动方面存在挑战。
- 方法要点：使用高阶多项式参数化辐条轮廓，结合KRR和XGBoost机器学习模型预测性能，并应用PSO和贝叶斯优化进行多目标优化。
- 实验或效果：优化设计实现53%刚度可调性、50%耐久性提升和43%振动减少，PSO快速收敛，贝叶斯优化有效探索权衡。

## 摘要（原文）

> Non Pneumatic tires offer a promising alternative to pneumatic tires. However, their discontinuous spoke structures present challenges in stiffness tuning, durability, and high speed vibration. This study introduces an integrated generative design and machine learning driven framework to optimize UPTIS type spoke geometries for passenger vehicles. Upper and lower spoke profiles were parameterized using high order polynomial representations, enabling the creation of approximately 250 generative designs through PCHIP based geometric variation. Machine learning models like KRR for stiffness and XGBoost for durability and vibration achieved strong predictive accuracy, reducing the reliance on computationally intensive FEM simulations. Optimization using Particle Swarm Optimization and Bayesian Optimization further enabled extensive performance refinement. The resulting designs demonstrate 53% stiffness tunability, up to 50% durability improvement, and 43% reduction in vibration compared to the baseline. PSO provided fast, targeted convergence, while Bayesian Optimization effectively explored multi objective tradeoffs. Overall, the proposed framework enables systematic development of high performance, next generation UPTIS spoke structures.

