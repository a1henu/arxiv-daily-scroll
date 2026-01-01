---
layout: default
title: MSACL: Multi-Step Actor-Critic Learning with Lyapunov Certificates for Exponentially Stabilizing Control
---

# MSACL: Multi-Step Actor-Critic Learning with Lyapunov Certificates for Exponentially Stabilizing Control
**arXiv**：[2512.24955v1](https://arxiv.org/abs/2512.24955) · [PDF](https://arxiv.org/pdf/2512.24955.pdf)  
**作者**：Yongwei Zhang, Yuanzhe Xing, Quan Quan, Zhikun She  

**一句话要点**：提出MSACL框架，通过多步Lyapunov证书学习实现模型无关强化学习的指数稳定控制

**关键词**：指数稳定性, Lyapunov证书, 多步学习, 模型无关强化学习, 安全控制

## 3 点简述
- 核心问题：模型无关强化学习中实现可证明稳定性，平衡探索与安全
- 方法要点：集成指数稳定性理论与最大熵强化学习，利用多步数据学习Lyapunov证书
- 实验或效果：在六个基准测试中优于现有Lyapunov方法，实现指数稳定性和快速收敛

## 摘要（原文）

> Achieving provable stability in model-free reinforcement learning (RL) remains a challenge, particularly in balancing exploration with rigorous safety. This article introduces MSACL, a framework that integrates exponential stability theory with maximum entropy RL through multi-step Lyapunov certificate learning. Unlike methods relying on complex reward engineering, MSACL utilizes off-policy multi-step data to learn Lyapunov certificates satisfying theoretical stability conditions. By introducing Exponential Stability Labels (ESL) and a $λ$-weighted aggregation mechanism, the framework effectively balances the bias-variance trade-off in multi-step learning. Policy optimization is guided by a stability-aware advantage function, ensuring the learned policy promotes rapid Lyapunov descent. We evaluate MSACL across six benchmarks, including stabilization and nonlinear tracking tasks, demonstrating its superiority over state-of-the-art Lyapunov-based RL algorithms. MSACL achieves exponential stability and rapid convergence under simple rewards, while exhibiting significant robustness to uncertainties and generalization to unseen trajectories. Sensitivity analysis establishes the multi-step horizon $n=20$ as a robust default across diverse systems. By linking Lyapunov theory with off-policy actor-critic frameworks, MSACL provides a foundation for verifiably safe learning-based control. Source code and benchmark environments will be made publicly available.

