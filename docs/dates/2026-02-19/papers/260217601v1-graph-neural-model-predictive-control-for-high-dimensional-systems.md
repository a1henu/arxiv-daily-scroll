---
layout: default
title: Graph Neural Model Predictive Control for High-Dimensional Systems
---

# Graph Neural Model Predictive Control for High-Dimensional Systems
**arXiv**：[2602.17601v1](https://arxiv.org/abs/2602.17601) · [PDF](https://arxiv.org/pdf/2602.17601.pdf)  
**作者**：Patrick Benito Eberhard, Luis Pabon, Daniele Gammelli, Hugo Buurmeijer, Amon Lahr, Mark Leone, Andrea Carron, Marco Pavone  

**一句话要点**：提出图神经网络模型预测控制框架，用于高维系统实时控制

**关键词**：图神经网络, 模型预测控制, 高维系统控制, 软机器人, 实时计算, GPU并行化

## 3 点简述
- 核心问题：高维系统（如软机器人）控制需兼顾模型精度与计算效率。
- 方法要点：结合图神经网络动态模型与结构利用模型预测控制，通过图表示和定制压缩算法实现高效计算。
- 实验或效果：在仿真和物理软机器人实验中，实现1000节点系统100Hz闭环控制，硬件跟踪精度亚厘米级，优于基线63.6%。

## 摘要（原文）

> The control of high-dimensional systems, such as soft robots, requires models that faithfully capture complex dynamics while remaining computationally tractable. This work presents a framework that integrates Graph Neural Network (GNN)-based dynamics models with structure-exploiting Model Predictive Control to enable real-time control of high-dimensional systems. By representing the system as a graph with localized interactions, the GNN preserves sparsity, while a tailored condensing algorithm eliminates state variables from the control problem, ensuring efficient computation. The complexity of our condensing algorithm scales linearly with the number of system nodes, and leverages Graphics Processing Unit (GPU) parallelization to achieve real-time performance. The proposed approach is validated in simulation and experimentally on a physical soft robotic trunk. Results show that our method scales to systems with up to 1,000 nodes at 100 Hz in closed-loop, and demonstrates real-time reference tracking on hardware with sub-centimeter accuracy, outperforming baselines by 63.6%. Finally, we show the capability of our method to achieve effective full-body obstacle avoidance.

