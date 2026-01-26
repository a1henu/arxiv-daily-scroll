---
layout: default
title: Adaptive Reinforcement and Model Predictive Control Switching for Safe Human-Robot Cooperative Navigation
---

# Adaptive Reinforcement and Model Predictive Control Switching for Safe Human-Robot Cooperative Navigation
**arXiv**：[2601.16686v1](https://arxiv.org/abs/2601.16686) · [PDF](https://arxiv.org/pdf/2601.16686.pdf)  
**作者**：Ning Liu, Sen Shen, Zheng Li, Matthew D'Souza, Jen Jen Chung, Thomas Braunl  

**一句话要点**：提出自适应强化学习与模型预测控制切换框架，以解决人机协作导航中的安全与机动性平衡问题。

**关键词**：人机协作导航, 自适应控制切换, 强化学习, 模型预测控制, 安全约束, 部分可观测性

## 3 点简述
- 核心问题：在部分可观测和非平稳人运动下，实现移动协作机器人的安全人引导导航。
- 方法要点：结合PPO强化学习跟随者和QP安全滤波MPC，通过自适应神经切换器进行软动作融合。
- 实验或效果：在高度杂乱环境中成功率82.5%，优于DWA和RL基线，计算延迟降低33%。

## 摘要（原文）

> This paper addresses the challenge of human-guided navigation for mobile collaborative robots under simultaneous proximity regulation and safety constraints. We introduce Adaptive Reinforcement and Model Predictive Control Switching (ARMS), a hybrid learning-control framework that integrates a reinforcement learning follower trained with Proximal Policy Optimization (PPO) and an analytical one-step Model Predictive Control (MPC) formulated as a quadratic program safety filter. To enable robust perception under partial observability and non-stationary human motion, ARMS employs a decoupled sensing architecture with a Long Short-Term Memory (LSTM) temporal encoder for the human-robot relative state and a spatial encoder for 360-degree LiDAR scans. The core contribution is a learned adaptive neural switcher that performs context-aware soft action fusion between the two controllers, favoring conservative, constraint-aware QP-based control in low-risk regions while progressively shifting control authority to the learned follower in highly cluttered or constrained scenarios where maneuverability is critical, and reverting to the follower action when the QP becomes infeasible. Extensive evaluations against Pure Pursuit, Dynamic Window Approach (DWA), and an RL-only baseline demonstrate that ARMS achieves an 82.5 percent success rate in highly cluttered environments, outperforming DWA and RL-only approaches by 7.1 percent and 3.1 percent, respectively, while reducing average computational latency by 33 percent to 5.2 milliseconds compared to a multi-step MPC baseline. Additional simulation transfer in Gazebo and initial real-world deployment results further indicate the practicality and robustness of ARMS for safe and efficient human-robot collaboration. Source code and a demonstration video are available at https://github.com/21ning/ARMS.git.

