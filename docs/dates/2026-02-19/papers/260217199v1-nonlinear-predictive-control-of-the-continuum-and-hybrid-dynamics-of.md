---
layout: default
title: Nonlinear Predictive Control of the Continuum and Hybrid Dynamics of a Suspended Deformable Cable for Aerial Pick and Place
---

# Nonlinear Predictive Control of the Continuum and Hybrid Dynamics of a Suspended Deformable Cable for Aerial Pick and Place
**arXiv**：[2602.17199v1](https://arxiv.org/abs/2602.17199) · [PDF](https://arxiv.org/pdf/2602.17199.pdf)  
**作者**：Antonio Rapuano, Yaolei Shen, Federico Califano, Chiara Gabellieri, Antonio Franchi  

**一句话要点**：提出非线性预测控制框架，用于无人机悬挂可变形电缆的实时动态操控与混合过渡处理。

**关键词**：非线性预测控制, 连续体动力学, 降阶模型, 无人机操控, 电缆动态, 混合系统

## 3 点简述
- 核心问题：无人机操控悬挂可变形电缆时，需处理连续体动力学和混合过渡（如负载附着/脱离）的实时控制挑战。
- 方法要点：结合高保真PDE模型与降阶模型，通过非线性模型预测控制稳定振荡并处理混合动态。
- 实验或效果：仿真验证降阶模型的稳定性、效率和鲁棒性，控制器在多种工况下有效调节电缆动态。

## 摘要（原文）

> This paper presents a framework for aerial manipulation of an extensible cable that combines a high-fidelity model based on partial differential equations (PDEs) with a reduced-order representation suitable for real-time control. The PDEs are discretised using a finite-difference method, and proper orthogonal decomposition is employed to extract a reduced-order model (ROM) that retains the dominant deformation modes while significantly reducing computational complexity. Based on this ROM, a nonlinear model predictive control scheme is formulated, capable of stabilizing cable oscillations and handling hybrid transitions such as payload attachment and detachment. Simulation results confirm the stability, efficiency, and robustness of the ROM, as well as the effectiveness of the controller in regulating cable dynamics under a range of operating conditions. Additional simulations illustrate the application of the ROM for trajectory planning in constrained environments, demonstrating the versatility of the proposed approach. Overall, the framework enables real-time, dynamics-aware control of unmanned aerial vehicles (UAVs) carrying suspended flexible cables.

