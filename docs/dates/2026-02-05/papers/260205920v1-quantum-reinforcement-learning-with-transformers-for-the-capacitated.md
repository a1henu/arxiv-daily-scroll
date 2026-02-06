---
layout: default
title: Quantum Reinforcement Learning with Transformers for the Capacitated Vehicle Routing Problem
---

# Quantum Reinforcement Learning with Transformers for the Capacitated Vehicle Routing Problem
**arXiv**：[2602.05920v1](https://arxiv.org/abs/2602.05920) · [PDF](https://arxiv.org/pdf/2602.05920.pdf)  
**作者**：Eva Andrés  

**一句话要点**：提出量子增强强化学习与Transformer模型，以解决带容量约束的车辆路径问题。

**关键词**：量子强化学习, Transformer, 车辆路径问题, 混合量子经典模型, 自注意力机制

## 3 点简述
- 核心问题：带容量约束的车辆路径问题（CVRP），涉及多车辆和客户分配。
- 方法要点：比较经典、全量子和混合强化学习，集成Transformer通过自注意力和交叉注意力建模关系。
- 实验或效果：量子增强模型在距离、紧凑性和重叠度上优于经典基线，混合架构表现最佳。

## 摘要（原文）

> This paper addresses the Capacitated Vehicle Routing Problem (CVRP) by comparing classical and quantum Reinforcement Learning (RL) approaches. An Advantage Actor-Critic (A2C) agent is implemented in classical, full quantum, and hybrid variants, integrating transformer architectures to capture the relationships between vehicles, clients, and the depot through self- and cross-attention mechanisms. The experiments focus on multi-vehicle scenarios with capacity constraints, considering 20 clients and 4 vehicles, and are conducted over ten independent runs. Performance is assessed using routing distance, route compactness, and route overlap. The results show that all three approaches are capable of learning effective routing policies. However, quantum-enhanced models outperform the classical baseline and produce more robust route organization, with the hybrid architecture achieving the best overall performance across distance, compactness, and route overlap. In addition to quantitative improvements, qualitative visualizations reveal that quantum-based models generate more structured and coherent routing solutions. These findings highlight the potential of hybrid quantum-classical reinforcement learning models for addressing complex combinatorial optimization problems such as the CVRP.

