---
layout: default
title: Constrained PSO Six-Parameter Fuzzy PID Tuning Method for Balanced Optimization of Depth Tracking Performance in Underwater Vehicles
---

# Constrained PSO Six-Parameter Fuzzy PID Tuning Method for Balanced Optimization of Depth Tracking Performance in Underwater Vehicles
**arXiv**：[2602.12700v1](https://arxiv.org/abs/2602.12700) · [PDF](https://arxiv.org/pdf/2602.12700.pdf)  
**作者**：Yanxi Ding, Tingyue Jia  

**一句话要点**：提出约束粒子群优化六参数模糊PID整定方法，以优化水下航行器深度跟踪性能的平衡问题。

**关键词**：水下航行器控制, 模糊PID整定, 粒子群优化, 约束优化, 深度跟踪, 控制能量约束

## 3 点简述
- 核心问题：传统模糊PID整定依赖经验，难以在性能提升与控制成本间实现稳定平衡。
- 方法要点：采用约束PSO调整PID基准参数及模糊控制器输入量化因子与输出比例增益，实现协同优化。
- 实验或效果：仿真显示，在控制能量和饱和水平一致下，跟踪误差、调整时间和超调均显著降低。

## 摘要（原文）

> Depth control of underwater vehicles in engineering applications must simultaneously satisfy requirements for rapid tracking, low overshoot, and actuator constraints. Traditional fuzzy PID tuning often relies on empirical methods, making it difficult to achieve a stable and reproducible equilibrium solution between performance enhancement and control cost. This paper proposes a constrained particle swarm optimization (PSO) method for tuning six-parameter fuzzy PID controllers. By adjusting the benchmark PID parameters alongside the fuzzy controller's input quantization factor and output proportional gain, it achieves synergistic optimization of the overall tuning strength and dynamic response characteristics of the fuzzy PID system. To ensure engineering feasibility of the optimization results, a time-weighted absolute error integral, adjustment time, relative overshoot control energy, and saturation occupancy rate are introduced. Control energy constraints are applied to construct a constraint-driven comprehensive evaluation system, suppressing pseudo-improvements achieved solely by increasing control inputs. Simulation results demonstrate that, while maintaining consistent control energy and saturation levels, the proposed method significantly enhances deep tracking performance: the time-weighted absolute error integral decreases from 0.2631 to 0.1473, the settling time shortens from 2.301 s to 1.613 s, and the relative overshoot reduces from 0.1494 to 0.01839. Control energy varied from 7980 to 7935, satisfying the energy constraint, while saturation occupancy decreased from 0.004 to 0.003. These results validate the effectiveness and engineering significance of the proposed constrained six-parameter joint tuning strategy for depth control in underwater vehicle navigation scenarios.

