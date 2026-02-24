---
layout: default
title: Recurrent Structural Policy Gradient for Partially Observable Mean Field Games
---

# Recurrent Structural Policy Gradient for Partially Observable Mean Field Games
**arXiv**：[2602.20141v1](https://arxiv.org/abs/2602.20141) · [PDF](https://arxiv.org/pdf/2602.20141.pdf)  
**作者**：Clarisse Wibault, Johannes Forkel, Sebastian Towers, Tiphaine Wibault, Juan Duque, George Whittle, Andreas Schaab, Yucheng Yang, Chiyuan Wang, Michael Osborne, Benjamin Moll, Jakob Foerster  

**一句话要点**：提出RSPG以解决部分可观测平均场博弈中历史感知策略的算法扩展问题

**关键词**：平均场博弈, 部分可观测性, 历史感知策略, 结构策略梯度, 蒙特卡洛采样, 宏观经济学模型

## 3 点简述
- 核心问题：部分可观测平均场博弈中，现有混合结构方法未扩展至历史感知策略场景
- 方法要点：结合已知转移动态，利用蒙特卡洛采样处理公共噪声，实现历史感知策略梯度
- 实验或效果：在异质智能体、公共噪声的宏观经济学平均场博弈中实现首次求解，收敛速度提升一个数量级

## 摘要（原文）

> Mean Field Games (MFGs) provide a principled framework for modeling interactions in large population models: at scale, population dynamics become deterministic, with uncertainty entering only through aggregate shocks, or common noise. However, algorithmic progress has been limited since model-free methods are too high variance and exact methods scale poorly. Recent Hybrid Structural Methods (HSMs) use Monte Carlo rollouts for the common noise in combination with exact estimation of the expected return, conditioned on those samples. However, HSMs have not been scaled to Partially Observable settings. We propose Recurrent Structural Policy Gradient (RSPG), the first history-aware HSM for settings involving public information. We also introduce MFAX, our JAX-based framework for MFGs. By leveraging known transition dynamics, RSPG achieves state-of-the-art performance as well as an order-of-magnitude faster convergence and solves, for the first time, a macroeconomics MFG with heterogeneous agents, common noise and history-aware policies. MFAX is publicly available at: https://github.com/CWibault/mfax.

