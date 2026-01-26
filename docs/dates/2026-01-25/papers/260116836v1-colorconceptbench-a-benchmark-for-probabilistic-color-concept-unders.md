---
layout: default
title: ColorConceptBench: A Benchmark for Probabilistic Color-Concept Understanding in Text-to-Image Models
---

# ColorConceptBench: A Benchmark for Probabilistic Color-Concept Understanding in Text-to-Image Models
**arXiv**：[2601.16836v1](https://arxiv.org/abs/2601.16836) · [PDF](https://arxiv.org/pdf/2601.16836.pdf)  
**作者**：Chenxi Ruan, Yu Xiao, Yihan Hou, Guosheng Hu, Wei Zeng  

**一句话要点**：提出ColorConceptBench基准以评估文本到图像模型在概率颜色-概念理解上的能力

**关键词**：文本到图像模型, 颜色概念理解, 概率分布评估, 人类标注基准, 隐式语义分析

## 3 点简述
- 核心问题：文本到图像模型在关联颜色与隐式概念方面能力不足，缺乏系统评估
- 方法要点：基于人类标注构建基准，通过概率颜色分布评估1281个隐式颜色概念
- 实验或效果：评估七个领先模型，发现其对抽象语义不敏感，且标准干预无效

## 摘要（原文）

> While text-to-image (T2I) models have advanced considerably, their capability to associate colors with implicit concepts remains underexplored. To address the gap, we introduce ColorConceptBench, a new human-annotated benchmark to systematically evaluate color-concept associations through the lens of probabilistic color distributions. ColorConceptBench moves beyond explicit color names or codes by probing how models translate 1,281 implicit color concepts using a foundation of 6,369 human annotations. Our evaluation of seven leading T2I models reveals that current models lack sensitivity to abstract semantics, and crucially, this limitation appears resistant to standard interventions (e.g., scaling and guidance). This demonstrates that achieving human-like color semantics requires more than larger models, but demands a fundamental shift in how models learn and represent implicit meaning.

