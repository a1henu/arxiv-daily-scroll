---
layout: default
title: Real-to-Sim for Highly Cluttered Environments via Physics-Consistent Inter-Object Reasoning
---

# Real-to-Sim for Highly Cluttered Environments via Physics-Consistent Inter-Object Reasoning
**arXiv**：[2602.12633v1](https://arxiv.org/abs/2602.12633) · [PDF](https://arxiv.org/pdf/2602.12633.pdf)  
**作者**：Tianyi Xiang, Jiahang Cao, Sikai Guo, Guoyang Zhao, Andrew F. Luo, Jun Ma  

**一句话要点**：提出物理约束的Real-to-Sim管道，通过接触图推理解决高杂乱环境下的单视角3D场景重建问题。

**关键词**：单视角3D重建, 物理一致性优化, 接触图推理, 可微分模拟, 机器人操控, 高杂乱环境

## 3 点简述
- 核心问题：单视角RGB-D数据重建3D场景时，几何保真度不足，忽略物理约束导致无效状态如漂浮或穿透，影响机器人操控。
- 方法要点：采用可微分优化管道，通过接触图建模空间依赖，联合优化物体姿态和物理属性，实现物理一致性重建。
- 实验或效果：在仿真和真实环境中评估，重建场景具有高物理保真度，能准确复制接触动态，支持稳定接触丰富的操控。

## 摘要（原文）

> Reconstructing physically valid 3D scenes from single-view observations is a prerequisite for bridging the gap between visual perception and robotic control. However, in scenarios requiring precise contact reasoning, such as robotic manipulation in highly cluttered environments, geometric fidelity alone is insufficient. Standard perception pipelines often neglect physical constraints, resulting in invalid states, e.g., floating objects or severe inter-penetration, rendering downstream simulation unreliable. To address these limitations, we propose a novel physics-constrained Real-to-Sim pipeline that reconstructs physically consistent 3D scenes from single-view RGB-D data. Central to our approach is a differentiable optimization pipeline that explicitly models spatial dependencies via a contact graph, jointly refining object poses and physical properties through differentiable rigid-body simulation. Extensive evaluations in both simulation and real-world settings demonstrate that our reconstructed scenes achieve high physical fidelity and faithfully replicate real-world contact dynamics, enabling stable and reliable contact-rich manipulation.

