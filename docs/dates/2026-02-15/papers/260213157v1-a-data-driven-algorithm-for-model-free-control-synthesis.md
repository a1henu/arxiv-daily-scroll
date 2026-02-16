---
layout: default
title: A Data-Driven Algorithm for Model-Free Control Synthesis
---

# A Data-Driven Algorithm for Model-Free Control Synthesis
**arXiv**：[2602.13157v1](https://arxiv.org/abs/2602.13157) · [PDF](https://arxiv.org/pdf/2602.13157.pdf)  
**作者**：Sean Bowerfind, Matthew R. Kirchner, Gary Hewer  

**一句话要点**：提出数据驱动算法以合成连续时间系统的最优无限时域LQR反馈控制器

**关键词**：数据驱动控制, LQR控制器, 模型无关合成, 连续时间系统, 参考跟踪

## 3 点简述
- 核心问题：在未知系统动力学下，仅基于有限输入输出数据合成最优LQR控制器
- 方法要点：通过约束优化强制最优值函数沿轨迹的必要条件，无需模型知识
- 实验或效果：包括理论验证和真实飞机上的测试示例

## 摘要（原文）

> Presented is an algorithm to synthesize the optimal infinite-horizon LQR feedback controller for continuous-time systems. The algorithm does not require knowledge of the system dynamics but instead uses only a finite-length sampling of arbitrary input-output data. The algorithm is based on a constrained optimization problem that enforces a necessary condition on the dynamics of the optimal value function along any trajectory. In addition to calculating the standard LQR gain matrix, a feedforward gain can be found to implement a reference tracking controller. This paper presents a theoretical justification for the method and shows several examples, including a validation test on a real scale aircraft.

