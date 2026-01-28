---
layout: default
title: Self-Supervised Path Planning in Unstructured Environments via Global-Guided Differentiable Hard Constraint Projection
---

# Self-Supervised Path Planning in Unstructured Environments via Global-Guided Differentiable Hard Constraint Projection
**arXiv**：[2601.19354v1](https://arxiv.org/abs/2601.19354) · [PDF](https://arxiv.org/pdf/2601.19354.pdf)  
**作者**：Ziqian Wang, Chenxi Fang, Zhen Zhang  

**一句话要点**：提出自监督路径规划框架，通过全局引导可微分硬约束投影解决非结构化环境中的安全与实时性问题。

**关键词**：自监督学习, 路径规划, 硬约束投影, 非结构化环境, 嵌入式智能, 实时系统

## 3 点简述
- 核心问题：非结构化环境中自主导航面临安全、数据稀缺和计算资源限制的挑战，传统方法延迟高，学习型方法难以保证确定性可行性。
- 方法要点：结合全局引导人工势场提供密集监督信号，并采用自适应神经投影层迭代修正网络输出以满足执行器和几何约束。
- 实验或效果：在20,000个场景测试中达到88.75%成功率，CARLA闭环实验验证动态约束下的物理可实现性，NVIDIA Jetson Orin NX上推理延迟94毫秒。

## 摘要（原文）

> Deploying deep learning agents for autonomous navigation in unstructured environments faces critical challenges regarding safety, data scarcity, and limited computational resources. Traditional solvers often suffer from high latency, while emerging learning-based approaches struggle to ensure deterministic feasibility. To bridge the gap from embodied to embedded intelligence, we propose a self-supervised framework incorporating a differentiable hard constraint projection layer for runtime assurance. To mitigate data scarcity, we construct a Global-Guided Artificial Potential Field (G-APF), which provides dense supervision signals without manual labeling. To enforce actuator limitations and geometric constraints efficiently, we employ an adaptive neural projection layer, which iteratively rectifies the coarse network output onto the feasible manifold. Extensive benchmarks on a test set of 20,000 scenarios demonstrate an 88.75\% success rate, substantiating the enhanced operational safety. Closed-loop experiments in CARLA further validate the physical realizability of the planned paths under dynamic constraints. Furthermore, deployment verification on an NVIDIA Jetson Orin NX confirms an inference latency of 94 ms, showing real-time feasibility on resource-constrained embedded hardware. This framework offers a generalized paradigm for embedding physical laws into neural architectures, providing a viable direction for solving constrained optimization in mechatronics. Source code is available at: https://github.com/wzq-13/SSHC.git.

