---
layout: default
title: SUSD: Structured Unsupervised Skill Discovery through State Factorization
---

# SUSD: Structured Unsupervised Skill Discovery through State Factorization
**arXiv**：[2602.01619v1](https://arxiv.org/abs/2602.01619) · [PDF](https://arxiv.org/pdf/2602.01619.pdf)  
**作者**：Seyed Mohammad Hadi Hosseini, Mahdieh Soleymani Baghshah  

**一句话要点**：提出SUSD框架，通过状态因子化解决无监督技能发现中技能简单和动态性不足的问题。

**关键词**：无监督技能发现, 状态因子化, 技能多样性, 分层强化学习, 动态模型

## 3 点简述
- 核心问题：现有无监督技能发现方法易产生简单静态技能，难以覆盖环境所有可控因素。
- 方法要点：将状态空间因子化为独立组件，分配不同技能变量，并动态调整学习焦点。
- 实验或效果：在因子化环境中显著优于现有方法，发现更多样复杂技能，支持分层强化学习。

## 摘要（原文）

> Unsupervised Skill Discovery (USD) aims to autonomously learn a diverse set of skills without relying on extrinsic rewards. One of the most common USD approaches is to maximize the Mutual Information (MI) between skill latent variables and states. However, MI-based methods tend to favor simple, static skills due to their invariance properties, limiting the discovery of dynamic, task-relevant behaviors. Distance-Maximizing Skill Discovery (DSD) promotes more dynamic skills by leveraging state-space distances, yet still fall short in encouraging comprehensive skill sets that engage all controllable factors or entities in the environment. In this work, we introduce SUSD, a novel framework that harnesses the compositional structure of environments by factorizing the state space into independent components (e.g., objects or controllable entities). SUSD allocates distinct skill variables to different factors, enabling more fine-grained control on the skill discovery process. A dynamic model also tracks learning across factors, adaptively steering the agent's focus toward underexplored factors. This structured approach not only promotes the discovery of richer and more diverse skills, but also yields a factorized skill representation that enables fine-grained and disentangled control over individual entities which facilitates efficient training of compositional downstream tasks via Hierarchical Reinforcement Learning (HRL). Our experimental results across three environments, with factors ranging from 1 to 10, demonstrate that our method can discover diverse and complex skills without supervision, significantly outperforming existing unsupervised skill discovery methods in factorized and complex environments. Code is publicly available at: https://github.com/hadi-hosseini/SUSD.

