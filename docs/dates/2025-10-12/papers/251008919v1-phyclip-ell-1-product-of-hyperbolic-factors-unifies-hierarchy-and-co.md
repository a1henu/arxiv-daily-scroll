---
layout: default
title: PHyCLIP: $\ell_1$-Product of Hyperbolic Factors Unifies Hierarchy and Compositionality in Vision-Language Representation Learning
---

# PHyCLIP: $\ell_1$-Product of Hyperbolic Factors Unifies Hierarchy and Compositionality in Vision-Language Representation Learning
**arXiv**：[2510.08919v1](https://arxiv.org/abs/2510.08919) · [PDF](https://arxiv.org/pdf/2510.08919.pdf)  
**作者**：Daiki Yoshikawa, Takashi Matsubara  

**一句话要点**：提出PHyCLIP以统一视觉语言表示中的层次性和组合性

**关键词**：视觉语言表示学习, 双曲空间, ℓ₁-积度量, 层次性建模, 组合性建模, 零样本学习

## 3 点简述
- 视觉语言模型难以同时表达概念族内层次和跨族组合性
- 使用双曲空间ℓ₁-积度量，分别捕获层次和组合结构
- 在零样本分类等任务中优于单空间方法，嵌入更可解释

## 摘要（原文）

> Vision-language models have achieved remarkable success in multi-modal
> representation learning from large-scale pairs of visual scenes and linguistic
> descriptions. However, they still struggle to simultaneously express two
> distinct types of semantic structures: the hierarchy within a concept family
> (e.g., dog $\preceq$ mammal $\preceq$ animal) and the compositionality across
> different concept families (e.g., "a dog in a car" $\preceq$ dog, car). Recent
> works have addressed this challenge by employing hyperbolic space, which
> efficiently captures tree-like hierarchy, yet its suitability for representing
> compositionality remains unclear. To resolve this dilemma, we propose PHyCLIP,
> which employs an $\ell_1$-Product metric on a Cartesian product of Hyperbolic
> factors. With our design, intra-family hierarchies emerge within individual
> hyperbolic factors, and cross-family composition is captured by the
> $\ell_1$-product metric, analogous to a Boolean algebra. Experiments on
> zero-shot classification, retrieval, hierarchical classification, and
> compositional understanding tasks demonstrate that PHyCLIP outperforms existing
> single-space approaches and offers more interpretable structures in the
> embedding space.

