---
layout: default
title: Multi UAVs Preflight Planning in a Shared and Dynamic Airspace
---

# Multi UAVs Preflight Planning in a Shared and Dynamic Airspace
**arXiv**：[2602.12055v1](https://arxiv.org/abs/2602.12055) · [PDF](https://arxiv.org/pdf/2602.12055.pdf)  
**作者**：Amath Sow, Mauricio Rodriguez Cesen, Fabiola Martins Campos de Oliveira, Mariusz Wzorek, Daniel de Leng, Mattias Tiger, Fredrik Heintz, Christian Esteve Rothenberg  

**一句话要点**：提出DTAPP-IICR方法，以解决动态共享空域中大规模无人机机队预飞行规划的挑战。

**关键词**：无人机预飞行规划, 多智能体路径规划, 动态空域管理, 冲突解决, 优先级规划, 时间性禁飞区

## 3 点简述
- 核心问题：大规模无人机在动态共享空域预飞行规划面临时间性禁飞区、异构车辆和严格交付期限等挑战。
- 方法要点：采用基于紧急度的优先级规划，结合SFIPP-ST单智能体规划器和迭代大邻域搜索解决冲突。
- 实验或效果：在含时间性禁飞区的基准测试中，支持1000架无人机，成功率近100%，运行时间减少达50%。

## 摘要（原文）

> Preflight planning for large-scale Unmanned Aerial Vehicle (UAV) fleets in dynamic, shared airspace presents significant challenges, including temporal No-Fly Zones (NFZs), heterogeneous vehicle profiles, and strict delivery deadlines. While Multi-Agent Path Finding (MAPF) provides a formal framework, existing methods often lack the scalability and flexibility required for real-world Unmanned Traffic Management (UTM). We propose DTAPP-IICR: a Delivery-Time Aware Prioritized Planning method with Incremental and Iterative Conflict Resolution. Our framework first generates an initial solution by prioritizing missions based on urgency. Secondly, it computes roundtrip trajectories using SFIPP-ST, a novel 4D single-agent planner (Safe Flight Interval Path Planning with Soft and Temporal Constraints). SFIPP-ST handles heterogeneous UAVs, strictly enforces temporal NFZs, and models inter-agent conflicts as soft constraints. Subsequently, an iterative Large Neighborhood Search, guided by a geometric conflict graph, efficiently resolves any residual conflicts. A completeness-preserving directional pruning technique further accelerates the 3D search. On benchmarks with temporal NFZs, DTAPP-IICR achieves near-100% success with fleets of up to 1,000 UAVs and gains up to 50% runtime reduction from pruning, outperforming batch Enhanced Conflict-Based Search in the UTM context. Scaling successfully in realistic city-scale operations where other priority-based methods fail even at moderate deployments, DTAPP-IICR is positioned as a practical and scalable solution for preflight planning in dense, dynamic urban airspace.

