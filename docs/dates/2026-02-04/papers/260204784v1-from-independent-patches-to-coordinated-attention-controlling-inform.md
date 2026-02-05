---
layout: default
title: From independent patches to coordinated attention: Controlling information flow in vision transformers
---

# From independent patches to coordinated attention: Controlling information flow in vision transformers
**arXiv**：[2602.04784v1](https://arxiv.org/abs/2602.04784) · [PDF](https://arxiv.org/pdf/2602.04784.pdf)  
**作者**：Kieran A. Murphy  

**一句话要点**：提出在视觉Transformer中插入变分信息瓶颈以控制注意力信息流，实现从独立补丁处理到全局注意力的可控谱系。

**关键词**：视觉Transformer, 注意力机制, 信息瓶颈, 可控学习, 模型可解释性, 图像分类

## 3 点简述
- 核心问题：视觉Transformer中注意力机制的信息传输难以量化和控制，影响模型可解释性和可控性。
- 方法要点：在所有注意力写入残差流时插入变分信息瓶颈，通过信息成本训练模型，无需其他架构改动。
- 实验或效果：在ImageNet-100上分析分类行为和信息路由演化，初步揭示全局视觉表示如何从局部补丁处理中涌现。

## 摘要（原文）

> We make the information transmitted by attention an explicit, measurable quantity in vision transformers. By inserting variational information bottlenecks on all attention-mediated writes to the residual stream -- without other architectural changes -- we train models with an explicit information cost and obtain a controllable spectrum from independent patch processing to fully expressive global attention. On ImageNet-100, we characterize how classification behavior and information routing evolve across this spectrum, and provide initial insights into how global visual representations emerge from local patch processing by analyzing the first attention heads that transmit information. By biasing learning toward solutions with constrained internal communication, our approach yields models that are more tractable for mechanistic analysis and more amenable to control.

