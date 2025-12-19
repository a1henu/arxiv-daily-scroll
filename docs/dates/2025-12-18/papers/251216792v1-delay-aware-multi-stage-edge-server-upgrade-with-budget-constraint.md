---
layout: default
title: Delay-Aware Multi-Stage Edge Server Upgrade with Budget Constraint
---

# Delay-Aware Multi-Stage Edge Server Upgrade with Budget Constraint
**arXiv**：[2512.16792v1](https://arxiv.org/abs/2512.16792) · [PDF](https://arxiv.org/pdf/2512.16792.pdf)  
**作者**：Endar Suprih Wihidayat, Sieteng Soh, Kwan-Wu Chin, Duc-son Pham  

**一句话要点**：提出多阶段边缘服务器升级框架以优化预算约束下的任务延迟满足率

**关键词**：边缘计算, 服务器升级, 任务卸载, 预算约束, 多阶段规划, 延迟优化

## 3 点简述
- 核心问题：在预算约束下，多阶段升级边缘服务器以最大化满足延迟要求的任务平均数量
- 方法要点：结合混合整数线性规划模型和高效启发式算法，决策服务器部署、升级和任务卸载
- 实验或效果：启发式算法在小网络中接近最优解，在大网络中相比基线提升任务满足率高达21.57%

## 摘要（原文）

> In this paper, the Multi-stage Edge Server Upgrade (M-ESU) is proposed as a new network planning problem, involving the upgrading of an existing multi-access edge computing (MEC) system through multiple stages (e.g., over several years). More precisely, the problem considers two key decisions: (i) whether to deploy additional edge servers or upgrade those already installed, and (ii) how tasks should be offloaded so that the average number of tasks that meet their delay requirement is maximized. The framework specifically involves: (i) deployment of new servers combined with capacity upgrades for existing servers, and (ii) the optimal task offloading to maximize the average number of tasks with a delay requirement. It also considers the following constraints: (i) budget per stage, (ii) server deployment and upgrade cost (in $) and cost depreciation rate, (iii) computation resource of servers, (iv) number of tasks and their growth rate (in %), and (v) the increase in task sizes and stricter delay requirements over time. We present two solutions: a Mixed Integer Linear Programming (MILP) model and an efficient heuristic algorithm (M-ESU/H). MILP yields the optimal solution for small networks, whereas M-ESU/H is used in large-scale networks. For small networks, the simulation results show that the solution computed by M-ESU/H is within 1.25% of the optimal solution while running several orders of magnitude faster. For large networks, M-ESU/H is compared against three alternative heuristic solutions that consider only server deployment, or giving priority to server deployment or upgrade. Our experiments show that M-ESU/H yields up to 21.57% improvement in task satisfaction under identical budget and demand growth conditions, confirming its scalability and practical value for long-term MEC systems.

