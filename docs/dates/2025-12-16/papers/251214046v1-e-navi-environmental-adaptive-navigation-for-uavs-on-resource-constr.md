---
layout: default
title: E-Navi: Environmental Adaptive Navigation for UAVs on Resource Constrained Platforms
---

# E-Navi: Environmental Adaptive Navigation for UAVs on Resource Constrained Platforms
**arXiv**：[2512.14046v1](https://arxiv.org/abs/2512.14046) · [PDF](https://arxiv.org/pdf/2512.14046.pdf)  
**作者**：Boyang Li, Zhongpeng Jin, Shuai Zhao, Jiahui Liao, Tian Liu, Han Liu, Yuanhai Zhang, Kai Huang  

**一句话要点**：提出E-Navi系统，通过动态调整任务执行以适应无人机在资源受限平台上的环境变化。

**关键词**：无人机导航, 环境自适应, 资源约束平台, 动态任务调整, 硬件部署灵活性

## 3 点简述
- 核心问题：现有无人机导航系统采用固定配置，忽略环境动态和计算资源，导致飞行策略僵化和计算过载。
- 方法要点：基于环境复杂度评估，动态调整映射分辨率和执行频率，优化感知-规划流程。
- 实验或效果：硬件在环和真实实验显示，系统显著优于基线，减少任务负载达53.9%，节省飞行时间达63.8%。

## 摘要（原文）

> The ability to adapt to changing environments is crucial for the autonomous navigation systems of Unmanned Aerial Vehicles (UAVs). However, existing navigation systems adopt fixed execution configurations without considering environmental dynamics based on available computing resources, e.g., with a high execution frequency and task workload. This static approach causes rigid flight strategies and excessive computations, ultimately degrading flight performance or even leading to failures in UAVs. Despite the necessity for an adaptive system, dynamically adjusting workloads remains challenging, due to difficulties in quantifying environmental complexity and modeling the relationship between environment and system configuration. Aiming at adapting to dynamic environments, this paper proposes E-Navi, an environmental-adaptive navigation system for UAVs that dynamically adjusts task executions on the CPUs in response to environmental changes based on available computational resources. Specifically, the perception-planning pipeline of UAVs navigation system is redesigned through dynamic adaptation of mapping resolution and execution frequency, driven by the quantitative environmental complexity evaluations. In addition, E-Navi supports flexible deployment across hardware platforms with varying levels of computing capability. Extensive Hardware-In-the-Loop and real-world experiments demonstrate that the proposed system significantly outperforms the baseline method across various hardware platforms, achieving up to 53.9% navigation task workload reduction, up to 63.8% flight time savings, and delivering more stable velocity control.

