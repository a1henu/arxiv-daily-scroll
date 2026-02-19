---
layout: default
title: Graph neural network for colliding particles with an application to sea ice floe modeling
---

# Graph neural network for colliding particles with an application to sea ice floe modeling
**arXiv**：[2602.16213v1](https://arxiv.org/abs/2602.16213) · [PDF](https://arxiv.org/pdf/2602.16213.pdf)  
**作者**：Ruibiao Zhu  

**一句话要点**：提出基于图神经网络的碰撞捕获网络，用于高效模拟海冰浮冰动力学

**关键词**：图神经网络, 海冰建模, 碰撞模拟, 数据同化, 计算效率

## 3 点简述
- 核心问题：传统海冰建模方法计算密集且扩展性差，难以高效处理浮冰间的物理交互。
- 方法要点：利用海冰的天然图结构，以节点表示冰片、边建模碰撞，结合数据同化技术学习动力学。
- 实验或效果：在合成数据上验证，模型加速轨迹模拟而不损失精度，适用于边缘冰区预测。

## 摘要（原文）

> This paper introduces a novel approach to sea ice modeling using Graph Neural Networks (GNNs), utilizing the natural graph structure of sea ice, where nodes represent individual ice pieces, and edges model the physical interactions, including collisions. This concept is developed within a one-dimensional framework as a foundational step. Traditional numerical methods, while effective, are computationally intensive and less scalable. By utilizing GNNs, the proposed model, termed the Collision-captured Network (CN), integrates data assimilation (DA) techniques to effectively learn and predict sea ice dynamics under various conditions. The approach was validated using synthetic data, both with and without observed data points, and it was found that the model accelerates the simulation of trajectories without compromising accuracy. This advancement offers a more efficient tool for forecasting in marginal ice zones (MIZ) and highlights the potential of combining machine learning with data assimilation for more effective and efficient modeling.

