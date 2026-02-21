---
layout: default
title: Nonlinear Predictive Control of the Continuum and Hybrid Dynamics of a Suspended Deformable Cable for Aerial Pick and Place
---

# Nonlinear Predictive Control of the Continuum and Hybrid Dynamics of a Suspended Deformable Cable for Aerial Pick and Place
**arXiv**：[2602.17199v1](https://arxiv.org/abs/2602.17199) · [PDF](https://arxiv.org/pdf/2602.17199.pdf)  
**作者**：Antonio Rapuano, Yaolei Shen, Federico Califano, Chiara Gabellieri, Antonio Franchi  

**一句话要点**：提出基于降阶模型的非线性预测控制框架，用于无人机悬挂可变形电缆的实时操控与稳定

**关键词**：无人机操控, 可变形电缆控制, 降阶模型, 非线性预测控制, 混合动力学, 实时控制

## 3 点简述
- 核心问题：无人机操控悬挂可变形电缆时，需处理连续体动力学与混合过渡（如负载附着/分离）的实时控制挑战。
- 方法要点：结合PDE高保真模型与降阶模型，采用有限差分法和本征正交分解提取主导变形模式，设计非线性模型预测控制器。
- 实验或效果：仿真验证降阶模型的稳定性、效率和鲁棒性，控制器能有效调节电缆振荡，并应用于受限环境轨迹规划。

## 摘要（原文）

> This paper presents a framework for aerial manipulation of an extensible cable that combines a high-fidelity model based on partial differential equations (PDEs) with a reduced-order representation suitable for real-time control. The PDEs are discretised using a finite-difference method, and proper orthogonal decomposition is employed to extract a reduced-order model (ROM) that retains the dominant deformation modes while significantly reducing computational complexity. Based on this ROM, a nonlinear model predictive control scheme is formulated, capable of stabilizing cable oscillations and handling hybrid transitions such as payload attachment and detachment. Simulation results confirm the stability, efficiency, and robustness of the ROM, as well as the effectiveness of the controller in regulating cable dynamics under a range of operating conditions. Additional simulations illustrate the application of the ROM for trajectory planning in constrained environments, demonstrating the versatility of the proposed approach. Overall, the framework enables real-time, dynamics-aware control of unmanned aerial vehicles (UAVs) carrying suspended flexible cables.

