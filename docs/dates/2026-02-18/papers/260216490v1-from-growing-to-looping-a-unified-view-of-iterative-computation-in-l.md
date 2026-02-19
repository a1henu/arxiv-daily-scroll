---
layout: default
title: From Growing to Looping: A Unified View of Iterative Computation in LLMs
---

# From Growing to Looping: A Unified View of Iterative Computation in LLMs
**arXiv**：[2602.16490v1](https://arxiv.org/abs/2602.16490) · [PDF](https://arxiv.org/pdf/2602.16490.pdf)  
**作者**：Ferdinand Kapl, Emmanouil Angelis, Kaitlin Maile, Johannes von Oswald, Stefan Bauer  

**一句话要点**：统一循环与深度增长为迭代计算，提升大语言模型推理能力

**关键词**：迭代计算, 深度增长, 循环推理, 大语言模型, 推理能力提升

## 3 点简述
- 核心问题：循环与深度增长在提升推理能力上的关系不明
- 方法要点：揭示两者共享深度特征，支持迭代计算统一视图
- 实验或效果：组合应用可提升推理精度，适应更多数据增强性能

## 摘要（原文）

> Looping, reusing a block of layers across depth, and depth growing, training shallow-to-deep models by duplicating middle layers, have both been linked to stronger reasoning, but their relationship remains unclear. We provide a mechanistic unification: looped and depth-grown models exhibit convergent depth-wise signatures, including increased reliance on late layers and recurring patterns aligned with the looped or grown block. These shared signatures support the view that their gains stem from a common form of iterative computation. Building on this connection, we show that the two techniques are adaptable and composable: applying inference-time looping to the middle blocks of a depth-grown model improves accuracy on some reasoning primitives by up to $2\times$, despite the model never being trained to loop. Both approaches also adapt better than the baseline when given more in-context examples or additional supervised fine-tuning data. Additionally, depth-grown models achieve the largest reasoning gains when using higher-quality, math-heavy cooldown mixtures, which can be further boosted by adapting a middle block to loop. Overall, our results position depth growth and looping as complementary, practical methods for inducing and scaling iterative computation to improve reasoning.

