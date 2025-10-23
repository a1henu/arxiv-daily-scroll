---
layout: default
title: Augmenting Moment Retrieval: Zero-Dependency Two-Stage Learning
---

# Augmenting Moment Retrieval: Zero-Dependency Two-Stage Learning
**arXiv**：[2510.19622v1](https://arxiv.org/abs/2510.19622) · [PDF](https://arxiv.org/pdf/2510.19622.pdf)  
**作者**：Zhengxuan Wei, Jiajin Tang, Sibei Yang  

**一句话要点**：提出零依赖两阶段学习框架AMR，以解决时刻检索中的数据稀缺、边界模糊和语义区分不足问题。

**关键词**：时刻检索, 两阶段学习, 数据增强, 蒸馏训练, 边界检测, 语义区分

## 3 点简述
- 核心问题：现有方法面临数据稀缺、边界模糊和细粒度语义区分不足的瓶颈。
- 方法要点：采用两阶段训练，冷启动阶段增强边界和语义感知，蒸馏阶段通过双查询集实现泛化。
- 实验或效果：在多个基准测试中，AMR性能优于先前最先进方法。

## 摘要（原文）

> Existing Moment Retrieval methods face three critical bottlenecks: (1) data
> scarcity forces models into shallow keyword-feature associations; (2) boundary
> ambiguity in transition regions between adjacent events; (3) insufficient
> discrimination of fine-grained semantics (e.g., distinguishing ``kicking" vs.
> ``throwing" a ball). In this paper, we propose a zero-external-dependency
> Augmented Moment Retrieval framework, AMR, designed to overcome local optima
> caused by insufficient data annotations and the lack of robust boundary and
> semantic discrimination capabilities. AMR is built upon two key insights: (1)
> it resolves ambiguous boundary information and semantic confusion in existing
> annotations without additional data (avoiding costly manual labeling), and (2)
> it preserves boundary and semantic discriminative capabilities enhanced by
> training while generalizing to real-world scenarios, significantly improving
> performance. Furthermore, we propose a two-stage training framework with
> cold-start and distillation adaptation. The cold-start stage employs curriculum
> learning on augmented data to build foundational boundary/semantic awareness.
> The distillation stage introduces dual query sets: Original Queries maintain
> DETR-based localization using frozen Base Queries from the cold-start model,
> while Active Queries dynamically adapt to real-data distributions. A
> cross-stage distillation loss enforces consistency between Original and Base
> Queries, preventing knowledge forgetting while enabling real-world
> generalization. Experiments on multiple benchmarks show that AMR achieves
> improved performance over prior state-of-the-art approaches.

