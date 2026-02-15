---
layout: default
title: Adaptive-Horizon Conflict-Based Search for Closed-Loop Multi-Agent Path Finding
---

# Adaptive-Horizon Conflict-Based Search for Closed-Loop Multi-Agent Path Finding
**arXiv**：[2602.12024v1](https://arxiv.org/abs/2602.12024) · [PDF](https://arxiv.org/pdf/2602.12024.pdf)  
**作者**：Jiarui Li, Federico Pecora, Runyu Zhang, Gioele Zardini  

**一句话要点**：提出ACCBS算法以解决闭环多智能体路径规划中的扰动处理与性能保证问题

**关键词**：多智能体路径规划, 闭环规划, 自适应时域, 冲突搜索, 机器人协调, 性能保证

## 3 点简述
- 核心问题：现有开环规划器难以处理扰动，闭环启发式方法缺乏可靠性能保证，限制安全关键部署
- 方法要点：基于有限时域CBS，引入时域调整机制，重用约束树实现时域间无缝切换
- 实验或效果：在案例研究中展示对扰动的灵活性和强性能保证，实现渐进最优和随时行为

## 摘要（原文）

> MAPF is a core coordination problem for large robot fleets in automated warehouses and logistics. Existing approaches are typically either open-loop planners, which generate fixed trajectories and struggle to handle disturbances, or closed-loop heuristics without reliable performance guarantees, limiting their use in safety-critical deployments. This paper presents ACCBS, a closed-loop algorithm built on a finite-horizon variant of CBS with a horizon-changing mechanism inspired by iterative deepening in MPC. ACCBS dynamically adjusts the planning horizon based on the available computational budget, and reuses a single constraint tree to enable seamless transitions between horizons. As a result, it produces high-quality feasible solutions quickly while being asymptotically optimal as the budget increases, exhibiting anytime behavior. Extensive case studies demonstrate that ACCBS combines flexibility to disturbances with strong performance guarantees, effectively bridging the gap between theoretical optimality and practical robustness for large-scale robot deployment.

