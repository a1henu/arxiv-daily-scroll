---
layout: default
title: SpatialMem: Unified 3D Memory with Metric Anchoring and Fast Retrieval
---

# SpatialMem: Unified 3D Memory with Metric Anchoring and Fast Retrieval
**arXiv**：[2601.14895v1](https://arxiv.org/abs/2601.14895) · [PDF](https://arxiv.org/pdf/2601.14895.pdf)  
**作者**：Xinyi Zheng, Yunze Liu, Chi-Hao Wu, Fan Zhang, Hao Zheng, Wenqi Zhou, Walterio W. Mayol-Cuevas, Junxiao Shen  

**一句话要点**：提出SpatialMem系统，统一3D几何、语义和语言表示，支持室内场景的快速检索与推理

**关键词**：3D空间记忆, 室内场景理解, 语言引导导航, 层次化检索, 度量重建, 开放词汇物体检测

## 3 点简述
- 核心问题：如何从单目RGB视频构建可查询的3D空间记忆表示，支持语言引导的导航与物体检索
- 方法要点：基于度量重建的室内环境，使用结构锚点作为骨架，构建层次化记忆节点链接视觉与文本特征
- 实验效果：在真实室内场景测试中，系统在遮挡和杂乱环境下保持导航完成度和检索准确性

## 摘要（原文）

> We present SpatialMem, a memory-centric system that unifies 3D geometry, semantics, and language into a single, queryable representation. Starting from casually captured egocentric RGB video, SpatialMem reconstructs metrically scaled indoor environments, detects structural 3D anchors (walls, doors, windows) as the first-layer scaffold, and populates a hierarchical memory with open-vocabulary object nodes -- linking evidence patches, visual embeddings, and two-layer textual descriptions to 3D coordinates -- for compact storage and fast retrieval. This design enables interpretable reasoning over spatial relations (e.g., distance, direction, visibility) and supports downstream tasks such as language-guided navigation and object retrieval without specialized sensors. Experiments across three real-life indoor scenes demonstrate that SpatialMem maintains strong anchor-description-level navigation completion and hierarchical retrieval accuracy under increasing clutter and occlusion, offering an efficient and extensible framework for embodied spatial intelligence.

