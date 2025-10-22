---
layout: default
title: MADR: MPC-guided Adversarial DeepReach
---

# MADR: MPC-guided Adversarial DeepReach
**arXiv**：[2510.18845v1](https://arxiv.org/abs/2510.18845) · [PDF](https://arxiv.org/pdf/2510.18845.pdf)  
**作者**：Ryan Teoh, Sander Tonkens, William Sharpless, Aijia Yang, Zeyuan Feng, Somil Bansal, Sylvia Herbert  

**一句话要点**：提出MADR框架以解决高维对抗性零和微分博弈中的安全策略计算问题

**关键词**：Hamilton-Jacobi可达性, 对抗性控制, 零和博弈, 物理信息深度学习, 模型预测控制, 机器人安全策略

## 3 点简述
- 核心问题：Hamilton-Jacobi可达性分析受维度诅咒限制，物理信息深度学习收敛慢且不准确
- 方法要点：结合MPC指导与自监督学习，近似双玩家零和博弈值函数，生成最优策略
- 实验或效果：在高维模拟和真实机器人测试中，显著优于现有基线，硬件表现优异

## 摘要（原文）

> Hamilton-Jacobi (HJ) Reachability offers a framework for generating safe
> value functions and policies in the face of adversarial disturbance, but is
> limited by the curse of dimensionality. Physics-informed deep learning is able
> to overcome this infeasibility, but itself suffers from slow and inaccurate
> convergence, primarily due to weak PDE gradients and the complexity of
> self-supervised learning. A few works, recently, have demonstrated that
> enriching the self-supervision process with regular supervision (based on the
> nature of the optimal control problem), greatly accelerates convergence and
> solution quality, however, these have been limited to single player problems
> and simple games. In this work, we introduce MADR: MPC-guided Adversarial
> DeepReach, a general framework to robustly approximate the two-player, zero-sum
> differential game value function. In doing so, MADR yields the corresponding
> optimal strategies for both players in zero-sum games as well as safe policies
> for worst-case robustness. We test MADR on a multitude of high-dimensional
> simulated and real robotic agents with varying dynamics and games, finding that
> our approach significantly out-performs state-of-the-art baselines in
> simulation and produces impressive results in hardware.

