---
layout: default
title: Textile IR: A Bidirectional Intermediate Representation for Physics-Aware Fashion CAD
---

# Textile IR: A Bidirectional Intermediate Representation for Physics-Aware Fashion CAD
**arXiv**：[2601.02792v1](https://arxiv.org/abs/2601.02792) · [PDF](https://arxiv.org/pdf/2601.02792.pdf)  
**作者**：Petteri Teikari, Neliana Fuenmayor  

**一句话要点**：提出Textile IR双向中间表示，以连接时尚CAD、物理模拟和生命周期评估，解决工程约束集成问题。

**关键词**：时尚CAD, 物理模拟, 生命周期评估, 中间表示, 约束满足, 不确定性传播

## 3 点简述
- 核心问题：时尚设计工具孤立，导致可制造性、物理行为和可持续性评估脱节，缺乏统一表示。
- 方法要点：引入七层验证阶梯，从语法检查到物理验证，支持双向反馈和不确定性传播。
- 实验或效果：框架使AI系统能操纵结构化服装程序，减少物理原型成本，促进可持续性权衡。

## 摘要（原文）

> We introduce Textile IR, a bidirectional intermediate representation that connects manufacturing-valid CAD, physics-based simulation, and lifecycle assessment for fashion design. Unlike existing siloed tools where pattern software guarantees sewable outputs but understands nothing about drape, and physics simulation predicts behaviour but cannot automatically fix patterns, Textile IR provides the semantic glue for integration through a seven-layer Verification Ladder -- from cheap syntactic checks (pattern closure, seam compatibility) to expensive physics validation (drape simulation, stress analysis). The architecture enables bidirectional feedback: simulation failures suggest pattern modifications; material substitutions update sustainability estimates in real time; uncertainty propagates across the pipeline with explicit confidence bounds. We formalise fashion engineering as constraint satisfaction over three domains and demonstrate how Textile IR's scene-graph representation enables AI systems to manipulate garments as structured programs rather than pixel arrays. The framework addresses the compound uncertainty problem: when measurement errors in material testing, simulation approximations, and LCA database gaps combine, sustainability claims become unreliable without explicit uncertainty tracking. We propose six research priorities and discuss deployment considerations for fashion SMEs where integrated workflows reduce specialised engineering requirements. Key contribution: a formal representation that makes engineering constraints perceptible, manipulable, and immediately consequential -- enabling designers to navigate sustainability, manufacturability, and aesthetic tradeoffs simultaneously rather than discovering conflicts after costly physical prototyping.

