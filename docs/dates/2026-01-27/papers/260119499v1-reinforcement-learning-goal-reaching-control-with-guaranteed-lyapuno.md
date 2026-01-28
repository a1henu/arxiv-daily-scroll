---
layout: default
title: Reinforcement Learning Goal-Reaching Control with Guaranteed Lyapunov-Like Stabilizer for Mobile Robots
---

# Reinforcement Learning Goal-Reaching Control with Guaranteed Lyapunov-Like Stabilizer for Mobile Robots
**arXiv**：[2601.19499v1](https://arxiv.org/abs/2601.19499) · [PDF](https://arxiv.org/pdf/2601.19499.pdf)  
**作者**：Mehdi Heydari Shahna, Seyed Adel Alizadeh Kolagar, Jouni Mattila  

**一句话要点**：提出基于强化学习的移动机器人目标到达控制框架，集成李雅普诺夫类稳定器以提供形式化保证

**关键词**：强化学习控制, 移动机器人, 李雅普诺夫稳定器, 形式化保证, 实时部署

## 3 点简述
- 核心问题：强化学习缺乏形式化目标到达保证，需平衡学习与安全约束
- 方法要点：设计15项奖励项，并集成李雅普诺夫类稳定器作为策略监督层
- 实验或效果：目标到达率从84.6%提升至99.0%，减少失败并提高效率

## 摘要（原文）

> Reinforcement learning (RL) can be highly effective at learning goal-reaching policies, but it typically does not provide formal guarantees that the goal will always be reached. A common approach to provide formal goal-reaching guarantees is to introduce a shielding mechanism that restricts the agent to actions that satisfy predefined safety constraints. The main challenge here is integrating this mechanism with RL so that learning and exploration remain effective without becoming overly conservative. Hence, this paper proposes an RL-based control framework that provides formal goal-reaching guarantees for wheeled mobile robots operating in unstructured environments. We first design a real-time RL policy with a set of 15 carefully defined reward terms. These rewards encourage the robot to reach both static and dynamic goals while generating sufficiently smooth command signals that comply with predefined safety specifications, which is critical in practice. Second, a Lyapunov-like stabilizer layer is integrated into the benchmark RL framework as a policy supervisor to formally strengthen the goal-reaching control while preserving meaningful exploration of the state action space. The proposed framework is suitable for real-time deployment in challenging environments, as it provides a formal guarantee of convergence to the intended goal states and compensates for uncertainties by generating real-time control signals based on the current state, while respecting real-world motion constraints. The experimental results show that the proposed Lyapunov-like stabilizer consistently improves the benchmark RL policies, boosting the goal-reaching rate from 84.6% to 99.0%, sharply reducing failures, and improving efficiency.

