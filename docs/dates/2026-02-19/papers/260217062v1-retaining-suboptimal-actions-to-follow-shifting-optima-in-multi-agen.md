---
layout: default
title: Retaining Suboptimal Actions to Follow Shifting Optima in Multi-Agent Reinforcement Learning
---

# Retaining Suboptimal Actions to Follow Shifting Optima in Multi-Agent Reinforcement Learning
**arXiv**：[2602.17062v1](https://arxiv.org/abs/2602.17062) · [PDF](https://arxiv.org/pdf/2602.17062.pdf)  
**作者**：Yonghyeon Jo, Sunwoo Lee, Seungyul Han  

**一句话要点**：提出S2Q方法以解决多智能体强化学习中价值函数漂移导致的策略适应性问题。

**关键词**：多智能体强化学习, 值分解, 策略适应, 子价值函数, Softmax策略, 持续探索

## 3 点简述
- 核心问题：现有值分解方法依赖单一最优动作，难以适应训练中价值函数漂移，易收敛至次优策略。
- 方法要点：学习多个子价值函数保留高价值替代动作，结合Softmax策略促进持续探索和快速适应。
- 实验或效果：在挑战性MARL基准测试中，S2Q一致优于多种算法，展现出改进的适应性和整体性能。

## 摘要（原文）

> Value decomposition is a core approach for cooperative multi-agent reinforcement learning (MARL). However, existing methods still rely on a single optimal action and struggle to adapt when the underlying value function shifts during training, often converging to suboptimal policies. To address this limitation, we propose Successive Sub-value Q-learning (S2Q), which learns multiple sub-value functions to retain alternative high-value actions. Incorporating these sub-value functions into a Softmax-based behavior policy, S2Q encourages persistent exploration and enables $Q^{\text{tot}}$ to adjust quickly to the changing optima. Experiments on challenging MARL benchmarks confirm that S2Q consistently outperforms various MARL algorithms, demonstrating improved adaptability and overall performance. Our code is available at https://github.com/hyeon1996/S2Q.

