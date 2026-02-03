---
layout: default
title: From Perception to Action: Spatial AI Agents and World Models
---

# From Perception to Action: Spatial AI Agents and World Models
**arXiv**：[2602.01644v1](https://arxiv.org/abs/2602.01644) · [PDF](https://arxiv.org/pdf/2602.01644.pdf)  
**作者**：Gloria Felicia, Nolan Bryant, Handi Putra, Ayaan Gazali, Eliel Lobo, Esteban Rojas  

**一句话要点**：提出统一三维空间智能与代理能力的分类法，以促进具身智能系统发展

**关键词**：空间智能, 具身代理, 世界模型, 分类法, GNN-LLM集成, 分层记忆

## 3 点简述
- 核心问题：现有研究孤立处理代理架构与空间智能，缺乏统一框架连接两者
- 方法要点：通过综述2000多篇论文，建立连接代理能力、空间任务和尺度的三维分类法
- 实验或效果：分析揭示分层记忆系统、GNN-LLM集成和世界模型在空间任务中的关键作用

## 摘要（原文）

> While large language models have become the prevailing approach for agentic reasoning and planning, their success in symbolic domains does not readily translate to the physical world. Spatial intelligence, the ability to perceive 3D structure, reason about object relationships, and act under physical constraints, is an orthogonal capability that proves important for embodied agents. Existing surveys address either agentic architectures or spatial domains in isolation. None provide a unified framework connecting these complementary capabilities. This paper bridges that gap. Through a thorough review of over 2,000 papers, citing 742 works from top-tier venues, we introduce a unified three-axis taxonomy connecting agentic capabilities with spatial tasks across scales. Crucially, we distinguish spatial grounding (metric understanding of geometry and physics) from symbolic grounding (associating images with text), arguing that perception alone does not confer agency. Our analysis reveals three key findings mapped to these axes: (1) hierarchical memory systems (Capability axis) are important for long-horizon spatial tasks. (2) GNN-LLM integration (Task axis) is a promising approach for structured spatial reasoning. (3) World models (Scale axis) are essential for safe deployment across micro-to-macro spatial scales. We conclude by identifying six grand challenges and outlining directions for future research, including the need for unified evaluation frameworks to standardize cross-domain assessment. This taxonomy provides a foundation for unifying fragmented research efforts and enabling the next generation of spatially-aware autonomous systems in robotics, autonomous vehicles, and geospatial intelligence.

