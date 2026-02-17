---
layout: default
title: Scalable Multi-Robot Path Planning via Quadratic Unconstrained Binary Optimization
---

# Scalable Multi-Robot Path Planning via Quadratic Unconstrained Binary Optimization
**arXiv**：[2602.14799v1](https://arxiv.org/abs/2602.14799) · [PDF](https://arxiv.org/pdf/2602.14799.pdf)  
**作者**：Javier González Villasmil  

**一句话要点**：提出基于QUBO的多机器人路径规划方法，以解决集中式方法在规模扩展时的计算复杂度问题。

**关键词**：多机器人路径规划, 二次无约束二进制优化, 可扩展性, 碰撞避免, 时间窗口分解, 量子启发计算

## 3 点简述
- 核心问题：多智能体路径规划中，集中式方法随智能体数量增加面临指数级状态空间增长。
- 方法要点：采用QUBO公式，结合BFS预处理、自适应惩罚设计和时间窗口分解，实现结构可扩展性。
- 实验或效果：在网格环境中最多四机器人测试，展示密集场景下接近最优解和优于顺序规划的扩展性能。

## 摘要（原文）

> Multi-Agent Path Finding (MAPF) remains a fundamental challenge in robotics, where classical centralized approaches exhibit exponential growth in joint-state complexity as the number of agents increases. This paper investigates Quadratic Unconstrained Binary Optimization (QUBO) as a structurally scalable alternative for simultaneous multi-robot path planning. This approach is a robotics-oriented QUBO formulation incorporating BFS-based logical pre-processing (achieving over 95% variable reduction), adaptive penalty design for collision and constraint enforcement, and a time-windowed decomposition strategy that enables execution within current hardware limitations. An experimental evaluation in grid environments with up to four robots demonstrated near-optimal solutions in dense scenarios and favorable scaling behavior compared to sequential classical planning. These results establish a practical and reproducible baseline for future quantum and quantum-inspired multi-robot coordinations.

