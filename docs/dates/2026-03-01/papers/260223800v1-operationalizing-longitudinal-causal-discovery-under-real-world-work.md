---
layout: default
title: Operationalizing Longitudinal Causal Discovery Under Real-World Workflow Constraints
---

# Operationalizing Longitudinal Causal Discovery Under Real-World Workflow Constraints
**arXiv**：[2602.23800v1](https://arxiv.org/abs/2602.23800) · [PDF](https://arxiv.org/pdf/2602.23800.pdf)  
**作者**：Tadahisa Okuda, Shohei Shimizu, Thong Pham, Tatsuyoshi Ikenoue, Shingo Fukuma  

**一句话要点**：提出工作流约束纵向因果发现框架，以解决真实世界数据中因果结构模糊性问题

**关键词**：纵向因果发现, 工作流约束, 结构掩码, 时间索引, 不确定性量化, 健康数据分析

## 3 点简述
- 核心问题：真实世界工作流导致数据部分顺序未形式化，扩大因果图空间，增加结构模糊性
- 方法要点：通过工作流衍生结构掩码和时间索引约束因果图空间，结合引导法量化不确定性
- 实验或效果：在日本大规模健康筛查队列中应用，获得时间一致子结构和可解释滞后总效应

## 摘要（原文）

> Causal discovery has achieved substantial theoretical progress, yet its deployment in large-scale longitudinal systems remains limited. A key obstacle is that operational data are generated under institutional workflows whose induced partial orders are rarely formalized, enlarging the admissible graph space in ways inconsistent with the recording process. We characterize a workflow-induced constraint class for longitudinal causal discovery that restricts the admissible directed acyclic graph space through protocol-derived structural masks and timeline-aligned indexing. Rather than introducing a new optimization algorithm, we show that explicitly encoding workflow-consistent partial orders reduces structural ambiguity, especially in mixed discrete--continuous panels where within-time orientation is weakly identified. The framework combines workflow-derived admissible-edge constraints, measurement-aligned time indexing and block structure, bootstrap-based uncertainty quantification for lagged total effects, and a dynamic representation supporting intervention queries. In a nationwide annual health screening cohort in Japan with 107,261 individuals and 429,044 person-years, workflow-constrained longitudinal LiNGAM yields temporally consistent within-time substructures and interpretable lagged total effects with explicit uncertainty. Sensitivity analyses using alternative exposure and body-composition definitions preserve the main qualitative patterns. We argue that formalizing workflow-derived constraint classes improves structural interpretability without relying on domain-specific edge specification, providing a reproducible bridge between operational workflows and longitudinal causal discovery under standard identifiability assumptions.

