---
layout: default
title: EgoGraph: Temporal Knowledge Graph for Egocentric Video Understanding
---

# EgoGraph: Temporal Knowledge Graph for Egocentric Video Understanding
**arXiv**：[2602.23709v1](https://arxiv.org/abs/2602.23709) · [PDF](https://arxiv.org/pdf/2602.23709.pdf)  
**作者**：Shitong Sun, Ke Han, Yukai Huang, Weitong Cai, Jifei Song  

**一句话要点**：提出EgoGraph框架以解决超长第一人称视频理解中的长期依赖建模问题

**关键词**：第一人称视频理解, 知识图谱构建, 时序依赖建模, 长期视频问答, 无训练框架

## 3 点简述
- 核心问题：超长第一人称视频（多天跨度）的长期依赖建模困难，现有方法依赖局部处理和有限时序建模
- 方法要点：基于无训练动态知识图谱构建，统一提取核心实体（人、物、地点、事件）并建模其跨实体时序依赖
- 实验或效果：在EgoLifeQA和EgoR1-bench基准上实现最先进的长期视频问答性能，验证了框架有效性

## 摘要（原文）

> Ultra-long egocentric videos spanning multiple days present significant challenges for video understanding. Existing approaches still rely on fragmented local processing and limited temporal modeling, restricting their ability to reason over such extended sequences. To address these limitations, we introduce EgoGraph, a training-free and dynamic knowledge-graph construction framework that explicitly encodes long-term, cross-entity dependencies in egocentric video streams. EgoGraph employs a novel egocentric schema that unifies the extraction and abstraction of core entities, such as people, objects, locations, and events, and structurally reasons about their attributes and interactions, yielding a significantly richer and more coherent semantic representation than traditional clip-based video models. Crucially, we develop a temporal relational modeling strategy that captures temporal dependencies across entities and accumulates stable long-term memory over multiple days, enabling complex temporal reasoning. Extensive experiments on the EgoLifeQA and EgoR1-bench benchmarks demonstrate that EgoGraph achieves state-of-the-art performance on long-term video question answering, validating its effectiveness as a new paradigm for ultra-long egocentric video understanding.

