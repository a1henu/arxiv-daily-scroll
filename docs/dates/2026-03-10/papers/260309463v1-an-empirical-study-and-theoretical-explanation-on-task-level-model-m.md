---
layout: default
title: An Empirical Study and Theoretical Explanation on Task-Level Model-Merging Collapse
---

# An Empirical Study and Theoretical Explanation on Task-Level Model-Merging Collapse
**arXiv**：[2603.09463v1](https://arxiv.org/abs/2603.09463) · [PDF](https://arxiv.org/pdf/2603.09463.pdf)  
**作者**：Yuan Cao, Dezhi Ran, Yuzhe Guo, Mengzhou Wu, Simin Chen, Linyi Li, Wei Yang, Tao Xie  

**一句话要点**：提出任务级模型合并崩溃的实证与理论解释，揭示任务表示不兼容性导致性能下降。

**关键词**：模型合并, 任务表示不兼容, 合并崩溃, 率失真理论, 大语言模型

## 3 点简述
- 核心问题：模型合并时，某些任务组合会导致灾难性性能下降，称为合并崩溃。
- 方法要点：通过实验和统计分析，发现表示不兼容性是崩溃主因，挑战参数冲突的传统观点。
- 实验或效果：基于率失真理论提供维度依赖界限，建立任务可合并性的基本限制。

## 摘要（原文）

> Model merging unifies independently fine-tuned LLMs from the same base, enabling reuse and integration of parallel development efforts without retraining. However, in practice we observe that merging does not always succeed: certain combinations of task-specialist models suffer from catastrophic performance degradation after merging. We refer to this failure mode as merging collapse. Intuitively, collapse arises when the learned representations or parameter adjustments for different tasks are fundamentally incompatible, so that merging forces destructive interference rather than synergy. In this paper, we identify and characterize the phenomenon of task-level merging collapse, where certain task combinations consistently trigger huge performance degradation across all merging methods. Through extensive experiments and statistical analysis, we demonstrate that representational incompatibility between tasks is strongly correlated with merging collapse, while parameter-space conflict metrics show minimal correlation, challenging conventional wisdom in model merging literature. We provide a theoretical explanation on this phenomenon through rate-distortion theory with a dimension-dependent bound, establishing fundamental limits on task mergeability regardless of methodology.

