---
layout: default
title: MMViR: A Multi-Modal and Multi-Granularity Representation for Long-range Video Understanding
---

# MMViR: A Multi-Modal and Multi-Granularity Representation for Long-range Video Understanding
**arXiv**：[2601.05495v1](https://arxiv.org/abs/2601.05495) · [PDF](https://arxiv.org/pdf/2601.05495.pdf)  
**作者**：Zizhong Li, Haopeng Zhang, Jiawei Zhang  

**一句话要点**：提出MMViR多模态多粒度表示以解决长视频理解中的计算冗余与内容碎片化问题

**关键词**：长视频理解, 多模态表示, 多粒度结构, 视频分割, 检索效率, 性能提升

## 3 点简述
- 长视频因复杂事件和长程依赖，直接编码计算昂贵，简单转换易冗余或碎片化
- MMViR通过关键转折点分割视频，构建三级描述耦合全局叙事与细粒度视觉细节
- 在QA、摘要和检索任务中，MMViR超越先前方法，提升19.67%理解效果并降低处理延迟至45.4%

## 摘要（原文）

> Long videos, ranging from minutes to hours, present significant challenges for current Multi-modal Large Language Models (MLLMs) due to their complex events, diverse scenes, and long-range dependencies. Direct encoding of such videos is computationally too expensive, while simple video-to-text conversion often results in redundant or fragmented content. To address these limitations, we introduce MMViR, a novel multi-modal, multi-grained structured representation for long video understanding. MMViR identifies key turning points to segment the video and constructs a three-level description that couples global narratives with fine-grained visual details. This design supports efficient query-based retrieval and generalizes well across various scenarios. Extensive evaluations across three tasks, including QA, summarization, and retrieval, show that MMViR outperforms the prior strongest method, achieving a 19.67% improvement in hour-long video understanding while reducing processing latency to 45.4% of the original.

