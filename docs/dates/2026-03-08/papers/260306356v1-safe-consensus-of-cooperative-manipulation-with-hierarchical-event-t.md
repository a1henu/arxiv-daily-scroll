---
layout: default
title: Safe Consensus of Cooperative Manipulation with Hierarchical Event-Triggered Control Barrier Functions
---

# Safe Consensus of Cooperative Manipulation with Hierarchical Event-Triggered Control Barrier Functions
**arXiv**：[2603.06356v1](https://arxiv.org/abs/2603.06356) · [PDF](https://arxiv.org/pdf/2603.06356.pdf)  
**作者**：Simiao Zhuang, Bingkun Huang, Zewen Yang  

**一句话要点**：提出分层事件触发控制屏障函数框架，实现多机械臂安全共识协调

**关键词**：协同操作, 控制屏障函数, 事件触发控制, 安全共识, 多机械臂系统

## 3 点简述
- 核心问题：多机械臂协同操作需在有限通信和计算下保证安全与协调
- 方法要点：基于共识协议和分层事件触发CBF，集成风险感知领导选择策略
- 实验或效果：硬件实验和仿真验证高精度安全协调，显著降低计算和通信成本

## 摘要（原文）

> Cooperative transport and manipulation of heavy or bulky payloads by multiple manipulators requires coordinated formation tracking, while simultaneously enforcing strict safety constraints in varying environments with limited communication and real-time computation budgets. This paper presents a distributed control framework that achieves consensus coordination with safety guarantees via hierarchical event-triggered control barrier functions (CBFs). We first develop a consensus-based protocol that relies solely on local neighbor information to enforce both translational and rotational consistency in task space. Building on this coordination layer, we propose a three-level hierarchical event-triggered safety architecture with CBFs, which is integrated with a risk-aware leader selection and smooth switching strategy to reduce online computation. The proposed approach is validated through real-world hardware experiments using two Franka manipulators operating with static obstacles, as well as comprehensive simulations demonstrating scalable multi-arm cooperation with dynamic obstacles. Results demonstrate higher precision cooperation under strict safety constraints, achieving substantially reduced computational cost and communication frequency compared to baseline methods.

