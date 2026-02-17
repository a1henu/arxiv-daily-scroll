---
layout: default
title: Bounding Probabilities of Causation with Partial Causal Diagrams
---

# Bounding Probabilities of Causation with Partial Causal Diagrams
**arXiv**：[2602.14503v1](https://arxiv.org/abs/2602.14503) · [PDF](https://arxiv.org/pdf/2602.14503.pdf)  
**作者**：Yuxuan Xie, Ang Li  

**一句话要点**：提出基于部分因果图的概率因果边界框架，以处理现实应用中因果信息不完整的问题。

**关键词**：概率因果, 因果边界, 部分因果图, 优化编程, 个体决策, 反事实推理

## 3 点简述
- 核心问题：概率因果在个体层面解释与决策中至关重要，但通常无法从数据中直接识别，现有方法受限于完全因果图或二元设置。
- 方法要点：通过优化编程系统整合可用结构或统计信息作为约束，推导更紧且形式有效的边界，无需完全可识别性。
- 实验或效果：扩展概率因果的适用性至因果知识不完整但信息丰富的现实场景，提升实用价值。

## 摘要（原文）

> Probabilities of causation are fundamental to individual-level explanation and decision making, yet they are inherently counterfactual and not point-identifiable from data in general. Existing bounds either disregard available covariates, require complete causal graphs, or rely on restrictive binary settings, limiting their practical use. In real-world applications, causal information is often partial but nontrivial. This paper proposes a general framework for bounding probabilities of causation using partial causal information. We show how the available structural or statistical information can be systematically incorporated as constraints in a optimization programming formulation, yielding tighter and formally valid bounds without full identifiability. This approach extends the applicability of probabilities of causation to realistic settings where causal knowledge is incomplete but informative.

