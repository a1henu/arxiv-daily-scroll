---
layout: default
title: Lyapunov Constrained Soft Actor-Critic (LC-SAC) using Koopman Operator Theory for Quadrotor Trajectory Tracking
---

# Lyapunov Constrained Soft Actor-Critic (LC-SAC) using Koopman Operator Theory for Quadrotor Trajectory Tracking
**arXiv**：[2602.04132v1](https://arxiv.org/abs/2602.04132) · [PDF](https://arxiv.org/pdf/2602.04132.pdf)  
**作者**：Dhruv S. Kushwaha, Zoleikha A. Biron  

**一句话要点**：提出基于Koopman算子的Lyapunov约束软演员-评论家算法，用于四旋翼轨迹跟踪的稳定性保证

**关键词**：强化学习, Lyapunov稳定性, Koopman算子, 四旋翼控制, 轨迹跟踪, 软演员-评论家

## 3 点简述
- 强化学习在安全关键物理系统中缺乏稳定性保证，标准算法可能导致振荡或状态发散。
- 利用扩展动态模式分解线性化系统，推导候选Lyapunov函数，并整合到软演员-评论家算法中。
- 在2D四旋翼环境中评估，相比基线算法，训练收敛且Lyapunov稳定性准则违反减少。

## 摘要（原文）

> Reinforcement Learning (RL) has achieved remarkable success in solving complex sequential decision-making problems. However, its application to safety-critical physical systems remains constrained by the lack of stability guarantees. Standard RL algorithms prioritize reward maximization, often yielding policies that may induce oscillations or unbounded state divergence. There has significant work in incorporating Lyapunov-based stability guarantees in RL algorithms with key challenges being selecting a candidate Lyapunov function, computational complexity by using excessive function approximators and conservative policies by incorporating stability criterion in the learning process. In this work we propose a novel Lyapunov-constrained Soft Actor-Critic (LC-SAC) algorithm using Koopman operator theory. We propose use of extended dynamic mode decomposition (EDMD) to produce a linear approximation of the system and use this approximation to derive a closed form solution for candidate Lyapunov function. This derived Lyapunov function is incorporated in the SAC algorithm to further provide guarantees for a policy that stabilizes the nonlinear system. The results are evaluated trajectory tracking of a 2D Quadrotor environment based on safe-control-gym. The proposed algorithm shows training convergence and decaying violations for Lyapunov stability criterion compared to baseline vanilla SAC algorithm. GitHub Repository: https://github.com/DhruvKushwaha/LC-SAC-Quadrotor-Trajectory-Tracking

