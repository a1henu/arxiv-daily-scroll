---
layout: default
title: Logical Guidance for the Exact Composition of Diffusion Models
---

# Logical Guidance for the Exact Composition of Diffusion Models
**arXiv**：[2602.05549v1](https://arxiv.org/abs/2602.05549) · [PDF](https://arxiv.org/pdf/2602.05549.pdf)  
**作者**：Francesco Alesiani, Jonathan Warrell, Tanja Bien, Henrik Christiansen, Matheus Ferraz, Mathias Niepert  

**一句话要点**：提出LOGDIFF框架，实现扩散模型在推理时基于复杂逻辑表达式的精确约束生成。

**关键词**：扩散模型, 逻辑引导, 约束生成, 布尔演算, 混合引导, 推理优化

## 3 点简述
- 核心问题：扩散模型如何基于复杂逻辑表达式进行精确约束生成，避免近似误差。
- 方法要点：推导布尔演算条件，确保逻辑公式可精确分解为原子属性，并设计高效递归算法计算引导信号。
- 实验或效果：在图像和蛋白质结构生成任务中验证框架有效性，支持混合引导方法。

## 摘要（原文）

> We propose LOGDIFF (Logical Guidance for the Exact Composition of Diffusion Models), a guidance framework for diffusion models that enables principled constrained generation with complex logical expressions at inference time.
>   We study when exact score-based guidance for complex logical formulas can be obtained from guidance signals associated with atomic properties.
>   First, we derive an exact Boolean calculus that provides a sufficient condition for exact logical guidance.
>   Specifically, if a formula admits a circuit representation in which conjunctions combine conditionally independent subformulas and disjunctions combine subformulas that are either conditionally independent or mutually exclusive, exact logical guidance is achievable.
>   In this case, the guidance signal can be computed exactly from atomic scores and posterior probabilities using an efficient recursive algorithm.
>   Moreover, we show that, for commonly encountered classes of distributions, any desired Boolean formula is compilable into such a circuit representation.
>   Second, by combining atomic guidance scores with posterior probability estimates, we introduce a hybrid guidance approach that bridges classifierguidance and classifier-free guidance, applicable to both compositional logical guidance and standard conditional generation.
>   We demonstrate the effectiveness of our framework on multiple image and protein structure generation tasks.

