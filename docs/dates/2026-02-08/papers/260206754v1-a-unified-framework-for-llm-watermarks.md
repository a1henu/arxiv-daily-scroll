---
layout: default
title: A Unified Framework for LLM Watermarks
---

# A Unified Framework for LLM Watermarks
**arXiv**：[2602.06754v1](https://arxiv.org/abs/2602.06754) · [PDF](https://arxiv.org/pdf/2602.06754.pdf)  
**作者**：Thibaud Gloaguen, Robin Staab, Nikola Jovanović, Martin Vechev  

**一句话要点**：提出统一框架以形式化LLM水印设计，揭示质量-多样性-检测力权衡。

**关键词**：LLM水印, 约束优化, 质量-多样性权衡, 检测力, 统一框架, 形式化方法

## 3 点简述
- 核心问题：现有LLM水印方法缺乏通用原则性形式化，设计分散。
- 方法要点：将多数水印方案统一为约束优化问题，明确约束与优化目标。
- 实验或效果：验证框架有效性，新方案在给定约束下最大化检测力。

## 摘要（原文）

> LLM watermarks allow tracing AI-generated texts by inserting a detectable signal into their generated content. Recent works have proposed a wide range of watermarking algorithms, each with distinct designs, usually built using a bottom-up approach. Crucially, there is no general and principled formulation for LLM watermarking.
>   In this work, we show that most existing and widely used watermarking schemes can in fact be derived from a principled constrained optimization problem. Our formulation unifies existing watermarking methods and explicitly reveals the constraints that each method optimizes. In particular, it highlights an understudied quality-diversity-power trade-off. At the same time, our framework also provides a principled approach for designing novel watermarking schemes tailored to specific requirements. For instance, it allows us to directly use perplexity as a proxy for quality, and derive new schemes that are optimal with respect to this constraint. Our experimental evaluation validates our framework: watermarking schemes derived from a given constraint consistently maximize detection power with respect to that constraint.

