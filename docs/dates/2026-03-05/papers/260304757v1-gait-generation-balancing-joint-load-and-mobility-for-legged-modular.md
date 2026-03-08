---
layout: default
title: Gait Generation Balancing Joint Load and Mobility for Legged Modular Robots with Easily Detachable Joints
---

# Gait Generation Balancing Joint Load and Mobility for Legged Modular Robots with Easily Detachable Joints
**arXiv**：[2603.04757v1](https://arxiv.org/abs/2603.04757) · [PDF](https://arxiv.org/pdf/2603.04757.pdf)  
**作者**：Kennosuke Chihara, Takuya Kiyokawa, Kensuke Harada  

**一句话要点**：提出基于NSGA-III的步态生成优化框架，以平衡关节负载与移动性，适用于易拆卸关节的模块化腿式机器人。

**关键词**：模块化腿式机器人, 关节负载优化, NSGA-III算法, 步态生成, 帕累托最优解, 结构完整性

## 3 点简述
- 核心问题：模块化腿式机器人在运动时关节扭矩过大，易导致机械故障，特别是易拆卸关节。
- 方法要点：使用NSGA-III算法优化步态，生成帕累托最优解，最小化关节负载同时保持必要速度和稳定性。
- 实验或效果：通过仿真和物理实验验证，在斜坡和台阶等多样环境中成功生成步态，确保结构完整性而不牺牲移动性。

## 摘要（原文）

> While modular robots offer versatility, excessive joint torque during locomotion poses a significant risk of mechanical failure, especially for detachable joints. To address this, we propose an optimization framework using the NSGA-III algorithm. Unlike conventional approaches that prioritize mobility alone, our method derives Pareto optimal solutions to minimize joint load while maintaining necessary locomotion speed and stability. Simulations and physical experiments demonstrate that our approach successfully generates gait motions for diverse environments, such as slopes and steps, ensuring structural integrity without compromising overall mobility.

