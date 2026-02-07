---
layout: default
title: AgentXRay: White-Boxing Agentic Systems via Workflow Reconstruction
---

# AgentXRay: White-Boxing Agentic Systems via Workflow Reconstruction
**arXiv**：[2602.05353v1](https://arxiv.org/abs/2602.05353) · [PDF](https://arxiv.org/pdf/2602.05353.pdf)  
**作者**：Ruijie Shi, Houbin Zhang, Yuecheng Han, Yuheng Wang, Jingru Fan, Runde Yang, Yufan Dang, Huatao Li, Dewen Liu, Yuan Cheng, Chen Qian  

**一句话要点**：提出AgentXRay框架，通过工作流重构实现黑盒智能体系统的白盒化解释。

**关键词**：智能体系统, 工作流重构, 白盒化, 蒙特卡洛树搜索, 组合优化, 代理相似度

## 3 点简述
- 核心问题：智能体系统内部工作流不透明，难以解释和控制。
- 方法要点：基于搜索的组合优化，在链式工作流空间中重构可编辑的白盒工作流。
- 实验或效果：在多样领域实现更高代理相似度，减少令牌消耗，支持深度探索。

## 摘要（原文）

> Large Language Models have shown strong capabilities in complex problem solving, yet many agentic systems remain difficult to interpret and control due to opaque internal workflows. While some frameworks offer explicit architectures for collaboration, many deployed agentic systems operate as black boxes to users. We address this by introducing Agentic Workflow Reconstruction (AWR), a new task aiming to synthesize an explicit, interpretable stand-in workflow that approximates a black-box system using only input--output access. We propose AgentXRay, a search-based framework that formulates AWR as a combinatorial optimization problem over discrete agent roles and tool invocations in a chain-structured workflow space. Unlike model distillation, AgentXRay produces editable white-box workflows that match target outputs under an observable, output-based proxy metric, without accessing model parameters. To navigate the vast search space, AgentXRay employs Monte Carlo Tree Search enhanced by a scoring-based Red-Black Pruning mechanism, which dynamically integrates proxy quality with search depth. Experiments across diverse domains demonstrate that AgentXRay achieves higher proxy similarity and reduces token consumption compared to unpruned search, enabling deeper workflow exploration under fixed iteration budgets.

