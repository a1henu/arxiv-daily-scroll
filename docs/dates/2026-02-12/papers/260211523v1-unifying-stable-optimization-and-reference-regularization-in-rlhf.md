---
layout: default
title: Unifying Stable Optimization and Reference Regularization in RLHF
---

# Unifying Stable Optimization and Reference Regularization in RLHF
**arXiv**：[2602.11523v1](https://arxiv.org/abs/2602.11523) · [PDF](https://arxiv.org/pdf/2602.11523.pdf)  
**作者**：Li He, Qiang Qu, He Zhao, Stephen Wan, Dadong Wang, Lina Yao, Tongliang Liu  

**一句话要点**：提出统一正则化方法以平衡RLHF中的奖励黑客和稳定优化问题。

**关键词**：强化学习人类反馈, 奖励黑客, 稳定优化, 正则化方法, 对齐性能

## 3 点简述
- 核心问题：RLHF面临奖励黑客和稳定优化的双重挑战，现有方法独立处理导致隐式权衡。
- 方法要点：引入统一正则化，显式平衡防止奖励黑客和保持策略更新稳定的目标。
- 实验或效果：在多个基准测试中优于RLHF和在线偏好学习方法，提升对齐性能和稳定性。

## 摘要（原文）

> Reinforcement Learning from Human Feedback (RLHF) has advanced alignment capabilities significantly but remains hindered by two core challenges: \textbf{reward hacking} and \textbf{stable optimization}. Current solutions independently address these issues through separate regularization strategies, specifically a KL-divergence penalty against a supervised fine-tuned model ($π_0$) to mitigate reward hacking, and policy ratio clipping towards the current policy ($π_t$) to promote stable alignment. However, the implicit trade-off arising from simultaneously regularizing towards both $π_0$ and $π_t$ remains under-explored. In this paper, we introduce a unified regularization approach that explicitly balances the objectives of preventing reward hacking and maintaining stable policy updates. Our simple yet principled alignment objective yields a weighted supervised fine-tuning loss with a superior trade-off, which demonstrably improves both alignment results and implementation complexity. Extensive experiments across diverse benchmarks validate that our method consistently outperforms RLHF and online preference learning methods, achieving enhanced alignment performance and stability.

