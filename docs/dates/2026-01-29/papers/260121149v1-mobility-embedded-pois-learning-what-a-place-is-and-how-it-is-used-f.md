---
layout: default
title: Mobility-Embedded POIs: Learning What A Place Is and How It Is Used from Human Movement
---

# Mobility-Embedded POIs: Learning What A Place Is and How It Is Used from Human Movement
**arXiv**：[2601.21149v1](https://arxiv.org/abs/2601.21149) · [PDF](https://arxiv.org/pdf/2601.21149.pdf)  
**作者**：Maria Despoina Siampou, Shushman Choudhury, Shang-Ling Hsu, Neha Arora, Cyrus Shahabi  

**一句话要点**：提出ME-POIs框架，通过人类移动数据增强POI嵌入以学习基于实际使用的表示

**关键词**：POI表示学习, 人类移动数据, 对比学习, 地图丰富任务, 时空嵌入

## 3 点简述
- 现有方法依赖静态元数据或轨迹上下文，缺乏POI功能信号
- ME-POIs利用对比学习对齐访问嵌入与POI表示，并通过空间尺度传播解决稀疏性
- 在五个地图丰富任务中，ME-POIs优于纯文本和纯移动基线，突显POI功能的重要性

## 摘要（原文）

> Recent progress in geospatial foundation models highlights the importance of learning general-purpose representations for real-world locations, particularly points-of-interest (POIs) where human activity concentrates. Existing approaches, however, focus primarily on place identity derived from static textual metadata, or learn representations tied to trajectory context, which capture movement regularities rather than how places are actually used (i.e., POI's function). We argue that POI function is a missing but essential signal for general POI representations. We introduce Mobility-Embedded POIs (ME-POIs), a framework that augments POI embeddings derived, from language models with large-scale human mobility data to learn POI-centric, context-independent representations grounded in real-world usage. ME-POIs encodes individual visits as temporally contextualized embeddings and aligns them with learnable POI representations via contrastive learning to capture usage patterns across users and time. To address long-tail sparsity, we propose a novel mechanism that propagates temporal visit patterns from nearby, frequently visited POIs across multiple spatial scales. We evaluate ME-POIs on five newly proposed map enrichment tasks, testing its ability to capture both the identity and function of POIs. Across all tasks, augmenting text-based embeddings with ME-POIs consistently outperforms both text-only and mobility-only baselines. Notably, ME-POIs trained on mobility data alone can surpass text-only models on certain tasks, highlighting that POI function is a critical component of accurate and generalizable POI representations.

