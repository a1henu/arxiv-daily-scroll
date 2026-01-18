---
layout: default
title: DeFlow: Decoupling Manifold Modeling and Value Maximization for Offline Policy Extraction
---

# DeFlow: Decoupling Manifold Modeling and Value Maximization for Offline Policy Extraction
**arXiv**：[2601.10471v1](https://arxiv.org/abs/2601.10471) · [PDF](https://arxiv.org/pdf/2601.10471.pdf)  
**作者**：Zhancun Mu  

**一句话要点**：提出DeFlow框架，通过解耦流匹配与价值最大化解决离线强化学习中的计算难题。

**关键词**：离线强化学习, 流匹配, 生成策略, 信任区域, ODE求解器, 离线到在线适应

## 3 点简述
- 核心问题：离线强化学习中，基于流匹配的生成策略优化计算成本高，需通过ODE求解器反向传播。
- 方法要点：在流形信任区域内学习轻量级精炼模块，避免求解器微分，保持迭代生成能力。
- 实验或效果：在OGBench基准上表现优异，并实现高效的离线到在线适应。

## 摘要（原文）

> We present DeFlow, a decoupled offline RL framework that leverages flow matching to faithfully capture complex behavior manifolds. Optimizing generative policies is computationally prohibitive, typically necessitating backpropagation through ODE solvers. We address this by learning a lightweight refinement module within an explicit, data-derived trust region of the flow manifold, rather than sacrificing the iterative generation capability via single-step distillation. This way, we bypass solver differentiation and eliminate the need for balancing loss terms, ensuring stable improvement while fully preserving the flow's iterative expressivity. Empirically, DeFlow achieves superior performance on the challenging OGBench benchmark and demonstrates efficient offline-to-online adaptation.

