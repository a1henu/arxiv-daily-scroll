---
layout: default
title: Co-Design of Rover Wheels and Control using Bayesian Optimization and Rover-Terrain Simulations
---

# Co-Design of Rover Wheels and Control using Bayesian Optimization and Rover-Terrain Simulations
**arXiv**：[2602.01535v1](https://arxiv.org/abs/2602.01535) · [PDF](https://arxiv.org/pdf/2602.01535.pdf)  
**作者**：Huzaifa Mustafa Unjhawala, Khizar Shaikh, Luning Bakke, Radu Serban, Dan Negrut  

**一句话要点**：提出贝叶斯优化框架，联合优化越野车车轮几何与转向控制器参数，基于高保真全车闭环仿真。

**关键词**：贝叶斯优化, 车轮设计, 转向控制, 地形力学仿真, 越野车优化, 联合优化

## 3 点简述
- 核心问题：传统离散元方法仿真成本高，限制全车研究，难以联合优化机械设计与控制。
- 方法要点：使用连续体表示模型进行高效地形力学仿真，结合贝叶斯优化平衡速度、跟踪误差和能耗。
- 实验或效果：在3000次仿真中，优化周期缩短至5-9天，初步硬件验证显示仿真优化设计保持相对性能趋势。

## 摘要（原文）

> While simulation is vital for optimizing robotic systems, the cost of modeling deformable terrain has long limited its use in full-vehicle studies of off-road autonomous mobility. For example, Discrete Element Method (DEM) simulations are often confined to single-wheel tests, which obscures coupled wheel-vehicle-controller interactions and prevents joint optimization of mechanical design and control. This paper presents a Bayesian optimization framework that co-designs rover wheel geometry and steering controller parameters using high-fidelity, full-vehicle closed-loop simulations on deformable terrain. Using the efficiency and scalability of a continuum-representation model (CRM) for terramechanics, we evaluate candidate designs on trajectories of varying complexity while towing a fixed load. The optimizer tunes wheel parameters (radius, width, and grouser features) and steering PID gains under a multi-objective formulation that balances traversal speed, tracking error, and energy consumption. We compare two strategies: simultaneous co-optimization of wheel and controller parameters versus a sequential approach that decouples mechanical and control design. We analyze trade-offs in performance and computational cost. Across 3,000 full-vehicle simulations, campaigns finish in five to nine days, versus months with the group's earlier DEM-based workflow. Finally, a preliminary hardware study suggests the simulation-optimized wheel designs preserve relative performance trends on the physical rover. Together, these results show that scalable, high-fidelity simulation can enable practical co-optimization of wheel design and control for off-road vehicles on deformable terrain without relying on prohibitively expensive DEM studies. The simulation infrastructure (scripts and models) is released as open source in a public repository to support reproducibility and further research.

