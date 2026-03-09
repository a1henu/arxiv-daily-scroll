---
layout: default
title: Few-Shot Neural Differentiable Simulator: Real-to-Sim Rigid-Contact Modeling
---

# Few-Shot Neural Differentiable Simulator: Real-to-Sim Rigid-Contact Modeling
**arXiv**：[2603.06218v1](https://arxiv.org/abs/2603.06218) · [PDF](https://arxiv.org/pdf/2603.06218.pdf)  
**作者**：Zhenhao Huang, Siyuan Luo, Bingyang Zhou, Ziqiu Zeng, Jason Pho, Fan Shi  

**一句话要点**：提出少样本神经可微模拟器，结合解析模拟与图神经网络，以提升机器人学习中的物理仿真精度与效率。

**关键词**：可微模拟, 少样本学习, 图神经网络, 刚体接触建模, 机器人控制, 物理仿真

## 3 点简述
- 核心问题：解析模拟器难以捕捉复杂接触动力学，而基于学习的模拟器通常需要大量真实数据。
- 方法要点：使用少量真实数据校准解析模拟器生成合成数据集，并基于网格图神经网络实现全可微的刚体前向动力学建模。
- 实验或效果：在复制真实轨迹上优于基线，支持基于梯度的优化，提高仿真保真度和策略学习效率。

## 摘要（原文）

> Accurate physics simulation is essential for robotic learning and control, yet analytical simulators often fail to capture complex contact dynamics, while learning-based simulators typically require large amounts of costly real-world data. To bridge this gap, we propose a few-shot real-to-sim approach that combines the physical consistency of analytical formulations with the representational capacity of graph neural network (GNN)-based models. Using only a small amount of real-world data, our method calibrates analytical simulators to generate large-scale synthetic datasets that capture diverse contact interactions. On this foundation, we introduce a mesh-based GNN that implicitly models rigid-body forward dynamics and derive surrogate gradients for collision detection, achieving full differentiability. Experimental results demonstrate that our approach enables learning-based simulators to outperform differentiable baselines in replicating real-world trajectories. In addition, the differentiable design supports gradient-based optimization, which we validate through simulation-based policy learning in multi-object interaction scenarios. Extensive experiments show that our framework not only improves simulation fidelity with minimal supervision but also increases the efficiency of policy learning. Taken together, these findings suggest that differentiable simulation with few-shot real-world grounding provides a powerful direction for advancing future robotic manipulation and control.

