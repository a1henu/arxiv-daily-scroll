---
layout: default
title: On the Identifiability of Steering Vectors in Large Language Models
---

# On the Identifiability of Steering Vectors in Large Language Models
**arXiv**：[2602.06801v1](https://arxiv.org/abs/2602.06801) · [PDF](https://arxiv.org/pdf/2602.06801.pdf)  
**作者**：Sohan Venkatesh, Ashish Mahendran Kurapath  

**一句话要点**：证明大语言模型中激活导向向量在现实条件下不可识别，但可通过结构假设恢复

**关键词**：激活导向, 可识别性, 大语言模型, 内部表示, 行为控制, 结构假设

## 3 点简述
- 核心问题：激活导向向量（如人格向量）的识别性假设可能不成立，影响模型行为控制与解释
- 方法要点：形式化导向为内部表示干预，理论证明行为等效干预类导致非识别性，实验验证正交扰动效果相似
- 实验或效果：多模型与语义特征验证非识别性，但统计独立性、稀疏约束等结构假设可恢复识别性

## 摘要（原文）

> Activation steering methods, such as persona vectors, are widely used to control large language model behavior and increasingly interpreted as revealing meaningful internal representations. This interpretation implicitly assumes steering directions are identifiable and uniquely recoverable from input-output behavior. We formalize steering as an intervention on internal representations and prove that, under realistic modeling and data conditions, steering vectors are fundamentally non-identifiable due to large equivalence classes of behaviorally indistinguishable interventions. Empirically, we validate this across multiple models and semantic traits, showing orthogonal perturbations achieve near-equivalent efficacy with negligible effect sizes. However, identifiability is recoverable under structural assumptions including statistical independence, sparsity constraints, multi-environment validation or cross-layer consistency. These findings reveal fundamental interpretability limits and clarify structural assumptions required for reliable safety-critical control.

