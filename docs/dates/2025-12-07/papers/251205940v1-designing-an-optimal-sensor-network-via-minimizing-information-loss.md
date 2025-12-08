---
layout: default
title: Designing an Optimal Sensor Network via Minimizing Information Loss
---

# Designing an Optimal Sensor Network via Minimizing Information Loss
**arXiv**：[2512.05940v1](https://arxiv.org/abs/2512.05940) · [PDF](https://arxiv.org/pdf/2512.05940.pdf)  
**作者**：Daniel Waxman, Fernando Llorente, Katia Lamer, Petar M. Djurić  

**一句话要点**：提出基于物理模拟和贝叶斯实验设计的传感器网络优化方法，以最小化时空过程监测中的信息损失。

**关键词**：传感器网络优化, 贝叶斯实验设计, 时空过程监测, 物理模拟集成, 稀疏变分推断

## 3 点简述
- 核心问题：在时空过程监测中，如何优化传感器放置以最小化信息损失，传统方法常忽略时间维度。
- 方法要点：结合物理模拟和贝叶斯实验设计，使用稀疏变分推断和高斯-马尔可夫先验，提出高效优化算法。
- 实验或效果：在亚利桑那州凤凰城气温监测案例中，验证方法优于随机或准随机采样，尤其在传感器数量有限时。

## 摘要（原文）

> Optimal experimental design is a classic topic in statistics, with many well-studied problems, applications, and solutions. The design problem we study is the placement of sensors to monitor spatiotemporal processes, explicitly accounting for the temporal dimension in our modeling and optimization. We observe that recent advancements in computational sciences often yield large datasets based on physics-based simulations, which are rarely leveraged in experimental design. We introduce a novel model-based sensor placement criterion, along with a highly-efficient optimization algorithm, which integrates physics-based simulations and Bayesian experimental design principles to identify sensor networks that "minimize information loss" from simulated data. Our technique relies on sparse variational inference and (separable) Gauss-Markov priors, and thus may adapt many techniques from Bayesian experimental design. We validate our method through a case study monitoring air temperature in Phoenix, Arizona, using state-of-the-art physics-based simulations. Our results show our framework to be superior to random or quasi-random sampling, particularly with a limited number of sensors. We conclude by discussing practical considerations and implications of our framework, including more complex modeling tools and real-world deployments.

