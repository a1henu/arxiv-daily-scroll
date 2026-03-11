---
layout: default
title: Robust Spatiotemporal Motion Planning for Multi-Agent Autonomous Racing via Topological Gap Identification and Accelerated MPC
---

# Robust Spatiotemporal Motion Planning for Multi-Agent Autonomous Racing via Topological Gap Identification and Accelerated MPC
**arXiv**：[2603.09188v1](https://arxiv.org/abs/2603.09188) · [PDF](https://arxiv.org/pdf/2603.09188.pdf)  
**作者**：Mingyi Zhang, Cheng Hu, Yiqin Wang, Haotong Qin, Hongye Su, Lei Xie  

**一句话要点**：提出基于拓扑间隙识别与加速MPC的框架，以解决高速多智能体自主赛车中的鲁棒时空规划问题。

**关键词**：多智能体自主赛车, 时空运动规划, 拓扑间隙识别, 模型预测控制, 鲁棒控制, 计算加速

## 3 点简述
- 核心问题：高速多智能体自主赛车需在严格计算限制下实现鲁棒时空规划与精确控制，现有方法常简化交互或忽略运动学约束。
- 方法要点：通过SGP预测对手行为，构建动态占用走廊以鲁棒选择超车间隙，并采用基于PTC求解器的线性时变MPC确保运动学可行性。
- 实验效果：在F1TENTH平台上，总机动时间减少51.6%，密集瓶颈中超车成功率超81%，平均计算延迟降低20.3%。

## 摘要（原文）

> High-speed multi-agent autonomous racing demands robust spatiotemporal planning and precise control under strict computational limits. Current methods often oversimplify interactions or abandon strict kinematic constraints. We resolve this by proposing a Topological Gap Identification and Accelerated MPC framework. By predicting opponent behaviors via SGPs, our method constructs dynamic occupancy corridors to robustly select optimal overtaking gaps. We ensure strict kinematic feasibility using a Linear Time-Varying MPC powered by a customized Pseudo-Transient Continuation (PTC) solver for high-frequency execution. Experimental results on the F1TENTH platform show that our method significantly outperforms state-of-the-art baselines: it reduces total maneuver time by 51.6% in sequential scenarios, consistently maintains an overtaking success rate exceeding 81% in dense bottlenecks, and lowers average computational latency by 20.3%, pushing the boundaries of safe and high-speed autonomous racing.

