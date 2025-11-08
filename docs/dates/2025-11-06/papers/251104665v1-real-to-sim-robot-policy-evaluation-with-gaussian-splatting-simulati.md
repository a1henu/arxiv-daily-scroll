---
layout: default
title: Real-to-Sim Robot Policy Evaluation with Gaussian Splatting Simulation of Soft-Body Interactions
---

# Real-to-Sim Robot Policy Evaluation with Gaussian Splatting Simulation of Soft-Body Interactions
**arXiv**：[2511.04665v1](https://arxiv.org/abs/2511.04665) · [PDF](https://arxiv.org/pdf/2511.04665.pdf)  
**作者**：Kaifeng Zhang, Shuo Sha, Hanxiao Jiang, Matthew Loper, Hyunjong Song, Guangyan Cai, Zhuo Xu, Xiaochen Hu, Changxi Zheng, Yunzhu Li  

**一句话要点**：提出基于3D高斯泼溅的真实到仿真框架，用于软体交互机器人策略评估

**关键词**：机器人策略评估, 软体交互仿真, 3D高斯泼溅, 数字孪生, 真实到仿真

## 3 点简述
- 核心问题：真实世界机器人策略评估成本高、难复现，尤其涉及软体对象交互。
- 方法要点：从真实视频构建软体数字孪生，结合物理重建与高质量渲染。
- 实验或效果：在玩具包装等任务中，仿真与真实性能强相关，揭示策略行为模式。

## 摘要（原文）

> Robotic manipulation policies are advancing rapidly, but their direct
> evaluation in the real world remains costly, time-consuming, and difficult to
> reproduce, particularly for tasks involving deformable objects. Simulation
> provides a scalable and systematic alternative, yet existing simulators often
> fail to capture the coupled visual and physical complexity of soft-body
> interactions. We present a real-to-sim policy evaluation framework that
> constructs soft-body digital twins from real-world videos and renders robots,
> objects, and environments with photorealistic fidelity using 3D Gaussian
> Splatting. We validate our approach on representative deformable manipulation
> tasks, including plush toy packing, rope routing, and T-block pushing,
> demonstrating that simulated rollouts correlate strongly with real-world
> execution performance and reveal key behavioral patterns of learned policies.
> Our results suggest that combining physics-informed reconstruction with
> high-quality rendering enables reproducible, scalable, and accurate evaluation
> of robotic manipulation policies. Website: https://real2sim-eval.github.io/

