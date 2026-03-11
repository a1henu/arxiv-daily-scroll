---
layout: default
title: Latent World Models for Automated Driving: A Unified Taxonomy, Evaluation Framework, and Open Challenges
---

# Latent World Models for Automated Driving: A Unified Taxonomy, Evaluation Framework, and Open Challenges
**arXiv**：[2603.09086v1](https://arxiv.org/abs/2603.09086) · [PDF](https://arxiv.org/pdf/2603.09086.pdf)  
**作者**：Rongxiang Zeng, Yongqi Dong  

**一句话要点**：提出统一潜在空间框架以整合自动驾驶世界模型进展，并建立评估体系与研究方向。

**关键词**：自动驾驶世界模型, 潜在表示, 统一分类法, 评估框架, 闭环指标, 资源效率

## 3 点简述
- 核心问题：自动驾驶中生成世界模型与视觉-语言-动作系统的潜在表示设计缺乏统一框架，影响鲁棒性与部署。
- 方法要点：基于潜在表示目标与形式（如潜在世界、动作、生成器）及结构先验（几何、拓扑、语义）构建分类法，并阐述五项内部机制。
- 实验或效果：提出闭环评估指标与资源感知计算成本，以减少开环/闭环不匹配，并识别可行动研究方向。

## 摘要（原文）

> Emerging generative world models and vision-language-action (VLA) systems are rapidly reshaping automated driving by enabling scalable simulation, long-horizon forecasting, and capability-rich decision making. Across these directions, latent representations serve as the central computational substrate: they compress high-dimensional multi-sensor observations, enable temporally coherent rollouts, and provide interfaces for planning, reasoning, and controllable generation. This paper proposes a unifying latent-space framework that synthesizes recent progress in world models for automated driving. The framework organizes the design space by the target and form of latent representations (latent worlds, latent actions, latent generators; continuous states, discrete tokens, and hybrids) and by structural priors for geometry, topology, and semantics. Building on this taxonomy, the paper articulates five cross-cutting internal mechanics (i.e, structural isomorphism, long-horizon temporal stability, semantic and reasoning alignment, value-aligned objectives and post-training, as well as adaptive computation and deliberation) and connects these design choices to robustness, generalization, and deployability. The work also proposes concrete evaluation prescriptions, including a closed-loop metric suite and a resource-aware deliberation cost, designed to reduce the open-loop / closed-loop mismatch. Finally, the paper identifies actionable research directions toward advancing latent world model for decision-ready, verifiable, and resource-efficient automated driving.

