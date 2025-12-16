---
layout: default
title: MADTempo: An Interactive System for Multi-Event Temporal Video Retrieval with Query Augmentation
---

# MADTempo: An Interactive System for Multi-Event Temporal Video Retrieval with Query Augmentation
**arXiv**：[2512.12929v1](https://arxiv.org/abs/2512.12929) · [PDF](https://arxiv.org/pdf/2512.12929.pdf)  
**作者**：Huu-An Vu, Van-Khanh Mai, Trong-Tam Nguyen, Quang-Duc Dam, Tien-Huy Nguyen, Thanh-Huong Le  

**一句话要点**：提出MADTempo框架，通过时序搜索与查询增强解决多事件视频检索中的时序依赖和OOD查询问题。

**关键词**：多事件视频检索, 时序搜索, 查询增强, 视觉基础, 泛化能力, 大规模视频库

## 3 点简述
- 核心问题：现有方法难以建模多事件间的时序依赖，且对未见或罕见视觉概念的查询处理不足。
- 方法要点：结合时序搜索机制捕获事件连续性，并利用Google图像搜索模块增强查询表示以提升泛化能力。
- 实验或效果：系统提升了视频检索的时序推理和泛化能力，适用于大规模视频库的语义感知检索。

## 摘要（原文）

> The rapid expansion of video content across online platforms has accelerated the need for retrieval systems capable of understanding not only isolated visual moments but also the temporal structure of complex events. Existing approaches often fall short in modeling temporal dependencies across multiple events and in handling queries that reference unseen or rare visual concepts. To address these challenges, we introduce MADTempo, a video retrieval framework developed by our team, AIO_Trinh, that unifies temporal search with web-scale visual grounding. Our temporal search mechanism captures event-level continuity by aggregating similarity scores across sequential video segments, enabling coherent retrieval of multi-event queries. Complementarily, a Google Image Search-based fallback module expands query representations with external web imagery, effectively bridging gaps in pretrained visual embeddings and improving robustness against out-of-distribution (OOD) queries. Together, these components advance the temporal rea- soning and generalization capabilities of modern video retrieval systems, paving the way for more semantically aware and adaptive retrieval across large-scale video corpora.

