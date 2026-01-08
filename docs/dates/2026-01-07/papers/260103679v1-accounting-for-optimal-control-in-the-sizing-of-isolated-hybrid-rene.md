---
layout: default
title: Accounting for Optimal Control in the Sizing of Isolated Hybrid Renewable Energy Systems Using Imitation Learning
---

# Accounting for Optimal Control in the Sizing of Isolated Hybrid Renewable Energy Systems Using Imitation Learning
**arXiv**：[2601.03679v1](https://arxiv.org/abs/2601.03679) · [PDF](https://arxiv.org/pdf/2601.03679.pdf)  
**作者**：Simon Halvdansson, Lucas Ferreira Bernardino, Brage Rugstad Knudsen  

**一句话要点**：提出基于模仿学习的孤立混合可再生能源系统容量优化框架，以解决有限视界最优控制问题。

**关键词**：孤立能源系统, 容量优化, 模仿学习, 模型预测控制, 可再生能源不确定性, 最优控制

## 3 点简述
- 核心问题：孤立能源系统容量优化中，有限视界最优控制影响难以量化，导致减排效果评估不准确。
- 方法要点：采用模仿学习结合随机神经模型预测控制，高效处理可再生能源不确定性和最优反馈控制。
- 实验或效果：在离岸能源系统案例中，发现投资成本与燃气使用减少呈非线性关系，验证了框架的有效性。

## 摘要（原文）

> Decarbonization of isolated or off-grid energy systems through phase-in of large shares of intermittent solar or wind generation requires co-installation of energy storage or continued use of existing fossil dispatchable power sources to balance supply and demand. The effective CO2 emission reduction depends on the relative capacity of the energy storage and renewable sources, the stochasticity of the renewable generation, and the optimal control or dispatch of the isolated energy system. While the operations of the energy storage and dispatchable sources may impact the optimal sizing of the system, it is challenging to account for the effect of finite horizon, optimal control at the stage of system sizing. Here, we present a flexible and computationally efficient sizing framework for energy storage and renewable capacity in isolated energy systems, accounting for uncertainty in the renewable generation and the optimal feedback control. To this end, we implement an imitation learning approach to stochastic neural model predictive control (MPC) which allows us to relate the battery storage and wind peak capacities to the emissions reduction and investment costs while accounting for finite horizon, optimal control. Through this approach, decision makers can evaluate the effective emission reduction and costs of different storage and wind capacities at any price point while accounting for uncertainty in the renewable generation with limited foresight. We evaluate the proposed sizing framework on a case study of an offshore energy system with a gas turbine, a wind farm and a battery energy storage system (BESS). In this case, we find a nonlinear, nontrivial relationship between the investment costs and reduction in gas usage relative to the wind and BESS capacities, emphasizing the complexity and importance of accounting for optimal control in the design of isolated energy systems.

