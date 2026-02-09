---
layout: default
title: SURE: Safe Uncertainty-Aware Robot-Environment Interaction using Trajectory Optimization
---

# SURE: Safe Uncertainty-Aware Robot-Environment Interaction using Trajectory Optimization
**arXiv**：[2602.06864v1](https://arxiv.org/abs/2602.06864) · [PDF](https://arxiv.org/pdf/2602.06864.pdf)  
**作者**：Zhuocheng Zhang, Haizhou Zhao, Xudong Sun, Aaron M. Johnson, Majid Khadiv  

**一句话要点**：提出SURE框架以解决机器人接触交互中的轨迹优化鲁棒性问题

**关键词**：轨迹优化, 接触交互, 不确定性处理, 机器人控制, 鲁棒性框架

## 3 点简述
- 核心问题：接触交互中的不连续动力学和接触时机不确定性限制轨迹优化的鲁棒性。
- 方法要点：通过允许轨迹从可能碰撞前状态分支并重新汇合，在统一优化中处理不确定性。
- 实验或效果：在推车-杆平衡和机械臂接蛋任务中，成功率分别提升21.6%和40%。

## 摘要（原文）

> Robotic tasks involving contact interactions pose significant challenges for trajectory optimization due to discontinuous dynamics. Conventional formulations typically assume deterministic contact events, which limit robustness and adaptability in real-world settings. In this work, we propose SURE, a robust trajectory optimization framework that explicitly accounts for contact timing uncertainty. By allowing multiple trajectories to branch from possible pre-impact states and later rejoin a shared trajectory, SURE achieves both robustness and computational efficiency within a unified optimization framework. We evaluate SURE on two representative tasks with unknown impact times. In a cart-pole balancing task involving uncertain wall location, SURE achieves an average improvement of 21.6% in success rate when branch switching is enabled during control. In an egg-catching experiment using a robotic manipulator, SURE improves the success rate by 40%. These results demonstrate that SURE substantially enhances robustness compared to conventional nominal formulations.

