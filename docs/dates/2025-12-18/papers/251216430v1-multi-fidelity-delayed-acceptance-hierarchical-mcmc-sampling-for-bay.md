---
layout: default
title: Multi-Fidelity Delayed Acceptance: hierarchical MCMC sampling for Bayesian inverse problems combining multiple solvers through deep neural networks
---

# Multi-Fidelity Delayed Acceptance: hierarchical MCMC sampling for Bayesian inverse problems combining multiple solvers through deep neural networks
**arXiv**：[2512.16430v1](https://arxiv.org/abs/2512.16430) · [PDF](https://arxiv.org/pdf/2512.16430.pdf)  
**作者**：Filippo Zacchei, Paolo Conti, Attilio Alberto Frangi, Andrea Manzoni  

**一句话要点**：提出多保真度延迟接受方法，结合深度神经网络解决贝叶斯反问题中的计算效率与精度平衡问题。

**关键词**：贝叶斯反问题, 多保真度采样, 延迟接受MCMC, 深度神经网络, 计算效率优化

## 3 点简述
- 核心问题：物理模型反问题中，高保真度求解器计算成本高，低保真度求解器精度不足。
- 方法要点：构建多保真度神经网络，离线训练结合高保真数据，在线阶段仅使用低保真求解器评估似然。
- 实验效果：在稳态地下水流动和非稳态反应扩散系统基准问题中，实现计算节省并加速后验推断。

## 摘要（原文）

> Inverse uncertainty quantification (UQ) tasks such as parameter estimation are computationally demanding whenever dealing with physics-based models, and typically require repeated evaluations of complex numerical solvers. When partial differential equations are involved, full-order models such as those based on the Finite Element Method can make traditional sampling approaches like Markov Chain Monte Carlo (MCMC) computationally infeasible. Although data-driven surrogate models may help reduce evaluation costs, their utility is often limited by the expense of generating high-fidelity data. In contrast, low-fidelity data can be produced more efficiently, although relying on them alone may degrade the accuracy of the inverse UQ solution.
>   To address these challenges, we propose a Multi-Fidelity Delayed Acceptance scheme for Bayesian inverse problems. Extending the Multi-Level Delayed Acceptance framework, the method introduces multi-fidelity neural networks that combine the predictions of solvers of varying fidelity, with high fidelity evaluations restricted to an offline training stage. During the online phase, likelihood evaluations are obtained by evaluating the coarse solvers and passing their outputs to the trained neural networks, thereby avoiding additional high-fidelity simulations.
>   This construction allows heterogeneous coarse solvers to be incorporated consistently within the hierarchy, providing greater flexibility than standard Multi-Level Delayed Acceptance. The proposed approach improves the approximation accuracy of the low fidelity solvers, leading to longer sub-chain lengths, better mixing, and accelerated posterior inference. The effectiveness of the strategy is demonstrated on two benchmark inverse problems involving (i) steady isotropic groundwater flow, (ii) an unsteady reaction-diffusion system, for which substantial computational savings are obtained.

