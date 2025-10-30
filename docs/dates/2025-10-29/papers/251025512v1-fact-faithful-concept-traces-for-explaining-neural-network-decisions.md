---
layout: default
title: FaCT: Faithful Concept Traces for Explaining Neural Network Decisions
---

# FaCT: Faithful Concept Traces for Explaining Neural Network Decisions
**arXiv**：[2510.25512v1](https://arxiv.org/abs/2510.25512) · [PDF](https://arxiv.org/pdf/2510.25512.pdf)  
**作者**：Amin Parchami-Araghi, Sukrut Rao, Jonas Fischer, Bernt Schiele  

**一句话要点**：提出FaCT模型以提供忠实的概念追踪解释神经网络决策

**关键词**：神经网络解释, 概念追踪, 忠实性评估, 跨类概念, C2-Score, 模型可视化

## 3 点简述
- 核心问题：现有概念解释方法不忠实于模型，且对概念学习有严格假设。
- 方法要点：设计模型固有机制概念，跨类共享，可忠实追踪其对logit的贡献。
- 实验或效果：概念更一致、用户更易解释，同时保持ImageNet性能竞争力。

## 摘要（原文）

> Deep networks have shown remarkable performance across a wide range of tasks,
> yet getting a global concept-level understanding of how they function remains a
> key challenge. Many post-hoc concept-based approaches have been introduced to
> understand their workings, yet they are not always faithful to the model.
> Further, they make restrictive assumptions on the concepts a model learns, such
> as class-specificity, small spatial extent, or alignment to human expectations.
> In this work, we put emphasis on the faithfulness of such concept-based
> explanations and propose a new model with model-inherent mechanistic
> concept-explanations. Our concepts are shared across classes and, from any
> layer, their contribution to the logit and their input-visualization can be
> faithfully traced. We also leverage foundation models to propose a new
> concept-consistency metric, C$^2$-Score, that can be used to evaluate
> concept-based methods. We show that, compared to prior work, our concepts are
> quantitatively more consistent and users find our concepts to be more
> interpretable, all while retaining competitive ImageNet performance.

