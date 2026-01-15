---
layout: default
title: Geometric Stability: The Missing Axis of Representations
---

# Geometric Stability: The Missing Axis of Representations
**arXiv**：[2601.09173v1](https://arxiv.org/abs/2601.09173) · [PDF](https://arxiv.org/pdf/2601.09173.pdf)  
**作者**：Prashant C. Raju  

**一句话要点**：提出几何稳定性以补充表示分析，量化扰动下表示几何的可靠性，应用于安全监控和可控性等场景。

**关键词**：表示学习, 几何稳定性, 鲁棒性分析, 安全监控, 可控性预测, 模型评估

## 3 点简述
- 核心问题：表示分析忽视几何稳定性，仅关注相似性，无法评估结构鲁棒性。
- 方法要点：引入几何稳定性概念，并开发Shesha框架进行测量。
- 实验或效果：在七个领域验证稳定性与相似性无关，并展示在安全监控和可控性中的实用价值。

## 摘要（原文）

> Analysis of learned representations has a blind spot: it focuses on $similarity$, measuring how closely embeddings align with external references, but similarity reveals only what is represented, not whether that structure is robust. We introduce $geometric$ $stability$, a distinct dimension that quantifies how reliably representational geometry holds under perturbation, and present $Shesha$, a framework for measuring it. Across 2,463 configurations in seven domains, we show that stability and similarity are empirically uncorrelated ($ρ\approx 0.01$) and mechanistically distinct: similarity metrics collapse after removing the top principal components, while stability retains sensitivity to fine-grained manifold structure. This distinction yields actionable insights: for safety monitoring, stability acts as a functional geometric canary, detecting structural drift nearly 2$\times$ more sensitively than CKA while filtering out the non-functional noise that triggers false alarms in rigid distance metrics; for controllability, supervised stability predicts linear steerability ($ρ= 0.89$-$0.96$); for model selection, stability dissociates from transferability, revealing a geometric tax that transfer optimization incurs. Beyond machine learning, stability predicts CRISPR perturbation coherence and neural-behavioral coupling. By quantifying $how$ $reliably$ systems maintain structure, geometric stability provides a necessary complement to similarity for auditing representations across biological and computational systems.

