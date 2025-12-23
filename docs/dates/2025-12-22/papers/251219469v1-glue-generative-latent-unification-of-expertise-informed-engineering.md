---
layout: default
title: GLUE: Generative Latent Unification of Expertise-Informed Engineering Models
---

# GLUE: Generative Latent Unification of Expertise-Informed Engineering Models
**arXiv**：[2512.19469v1](https://arxiv.org/abs/2512.19469) · [PDF](https://arxiv.org/pdf/2512.19469.pdf)  
**作者**：Tim Aebersold, Soheyl Massoudi, Mark D. Fuge  

**一句话要点**：提出GLUE方法以协调预训练子系统生成器，实现复杂工程系统的生成设计。

**关键词**：生成设计, 系统工程, 预训练模型协调, 数据无依赖训练, 可微分几何

## 3 点简述
- 核心问题：如何协调冻结的预训练子模型，生成可行、多样且高性能的全系统设计。
- 方法要点：通过数据驱动和数据无依赖两种GLUE模型，在可微分几何层上强制执行系统级约束。
- 实验或效果：在无人机设计问题中，数据无依赖方法在性能与可行性上媲美优化方法，训练效率显著提升。

## 摘要（原文）

> Engineering complex systems (aircraft, buildings, vehicles) requires accounting for geometric and performance couplings across subsystems. As generative models proliferate for specialized domains (wings, structures, engines), a key research gap is how to coordinate frozen, pre-trained submodels to generate full-system designs that are feasible, diverse, and high-performing. We introduce Generative Latent Unification of Expertise-Informed Engineering Models (GLUE), which orchestrates pre-trained, frozen subsystem generators while enforcing system-level feasibility, optimality, and diversity. We propose and benchmark (i) data-driven GLUE models trained on pre-generated system-level designs and (ii) a data-free GLUE model trained online on a differentiable geometry layer. On a UAV design problem with five coupling constraints, we find that data-driven approaches yield diverse, high-performing designs but require large datasets to satisfy constraints reliably. The data-free approach is competitive with Bayesian optimization and gradient-based optimization in performance and feasibility while training a full generative model in only 10 min on a RTX 4090 GPU, requiring more than two orders of magnitude fewer geometry evaluations and FLOPs than the data-driven method. Ablations focused on data-free training show that subsystem output continuity affects coordination, and equality constraints can trigger mode collapse unless mitigated. By integrating unmodified, domain-informed submodels into a modular generative workflow, this work provides a viable path for scaling generative design to complex, real-world engineering systems.

