---
layout: default
title: Hierarchical Long Video Understanding with Audiovisual Entity Cohesion and Agentic Search
---

# Hierarchical Long Video Understanding with Audiovisual Entity Cohesion and Agentic Search
**arXiv**：[2601.13719v1](https://arxiv.org/abs/2601.13719) · [PDF](https://arxiv.org/pdf/2601.13719.pdf)  
**作者**：Xinlei Yin, Xiulian Peng, Xiao Li, Zhiwei Xiong, Yan Lu  

**一句话要点**：提出HAVEN框架，通过视听实体凝聚和分层索引结合智能搜索，解决长视频理解中的信息碎片化和全局连贯性问题。

**关键词**：长视频理解, 视听实体凝聚, 分层视频索引, 智能搜索, 多模态推理, 全局连贯性

## 3 点简述
- 核心问题：长视频理解因上下文窗口极长，现有方法基于简单分块和检索增强生成，常导致信息碎片化和全局连贯性丢失。
- 方法要点：整合视听流中的实体级表示以保持语义一致性，并构建从全局摘要到实体的分层结构，结合智能搜索机制进行动态检索和推理。
- 实验或效果：在LVBench上达到84.1%的整体准确率，在推理类别中表现突出，达80.1%，验证了结构化多模态推理的有效性。

## 摘要（原文）

> Long video understanding presents significant challenges for vision-language models due to extremely long context windows. Existing solutions relying on naive chunking strategies with retrieval-augmented generation, typically suffer from information fragmentation and a loss of global coherence. We present HAVEN, a unified framework for long-video understanding that enables coherent and comprehensive reasoning by integrating audiovisual entity cohesion and hierarchical video indexing with agentic search. First, we preserve semantic consistency by integrating entity-level representations across visual and auditory streams, while organizing content into a structured hierarchy spanning global summary, scene, segment, and entity levels. Then we employ an agentic search mechanism to enable dynamic retrieval and reasoning across these layers, facilitating coherent narrative reconstruction and fine-grained entity tracking. Extensive experiments demonstrate that our method achieves good temporal coherence, entity consistency, and retrieval efficiency, establishing a new state-of-the-art with an overall accuracy of 84.1% on LVBench. Notably, it achieves outstanding performance in the challenging reasoning category, reaching 80.1%. These results highlight the effectiveness of structured, multimodal reasoning for comprehensive and context-consistent understanding of long-form videos.

