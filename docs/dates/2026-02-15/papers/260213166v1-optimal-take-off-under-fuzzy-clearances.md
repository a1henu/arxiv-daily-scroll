---
layout: default
title: Optimal Take-off under Fuzzy Clearances
---

# Optimal Take-off under Fuzzy Clearances
**arXiv**：[2602.13166v1](https://arxiv.org/abs/2602.13166) · [PDF](https://arxiv.org/pdf/2602.13166.pdf)  
**作者**：Hugo Henry, Arthur Tsai, Kelly Cohen  

**一句话要点**：提出混合模糊最优控制架构，用于无人机在模糊许可下的自适应避障。

**关键词**：无人机避障, 模糊最优控制, 自适应约束处理, 航空安全系统, 实时轨迹规划

## 3 点简述
- 核心问题：经典最优控制在不确定性下受限，需可解释决策以符合航空安全规范。
- 方法要点：集成模糊规则系统与最优控制，通过三层模糊层调制约束参数，作为软约束求解。
- 实验或效果：简化模型验证可行，迭代计算时间2-3秒，但发现软件不兼容导致约束执行失效。

## 摘要（原文）

> This paper presents a hybrid obstacle avoidance architecture that integrates Optimal Control under clearance with a Fuzzy Rule Based System (FRBS) to enable adaptive constraint handling for unmanned aircraft. Motivated by the limitations of classical optimal control under uncertainty and the need for interpretable decision making in safety critical aviation systems, we design a three stage Takagi Sugeno Kang fuzzy layer that modulates constraint radii, urgency levels, and activation decisions based on regulatory separation minima and airworthiness guidelines from FAA and EASA. These fuzzy-derived clearances are then incorporated as soft constraints into an optimal control problem solved using the FALCON toolbox and IPOPT. The framework aims to reduce unnecessary recomputations by selectively activating obstacle avoidance updates while maintaining compliance with aviation procedures. A proof of concept implementation using a simplified aircraft model demonstrates that the approach can generate optimal trajectories with computation times of 2,3 seconds per iteration in a single threaded MATLAB environment, suggesting feasibility for near real time applications. However, our experiments revealed a critical software incompatibility in the latest versions of FALCON and IPOPT, in which the Lagrangian penalty term remained identically zero, preventing proper constraint enforcement. This behavior was consistent across scenarios and indicates a solver toolbox regression rather than a modeling flaw. Future work includes validating this effect by reverting to earlier software versions, optimizing the fuzzy membership functions using evolutionary methods, and extending the system to higher fidelity aircraft models and stochastic obstacle environments.

