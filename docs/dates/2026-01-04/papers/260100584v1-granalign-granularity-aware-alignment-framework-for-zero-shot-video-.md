---
layout: default
title: GranAlign: Granularity-Aware Alignment Framework for Zero-Shot Video Moment Retrieval
---

# GranAlign: Granularity-Aware Alignment Framework for Zero-Shot Video Moment Retrieval
**arXiv**：[2601.00584v1](https://arxiv.org/abs/2601.00584) · [PDF](https://arxiv.org/pdf/2601.00584.pdf)  
**作者**：Mingyu Jeon, Sunjae Yoon, Jonghee Kim, Junyeoung Kim  

**一句话要点**：提出GranAlign框架以解决零样本视频时刻检索中的语义粒度不匹配问题

**关键词**：零样本视频时刻检索, 语义粒度对齐, 查询重写, 查询感知字幕生成, 训练免费框架

## 3 点简述
- 核心问题：零样本视频时刻检索中文本查询与视觉内容的语义粒度不匹配导致检索不准确
- 方法要点：通过粒度感知对齐，结合查询重写和查询感知字幕生成，平衡多级语义表示
- 实验或效果：在三个主要基准测试中达到新最优，在QVHighlights上mAP@avg提升3.23%

## 摘要（原文）

> Zero-shot video moment retrieval (ZVMR) is the task of localizing a temporal moment within an untrimmed video using a natural language query without relying on task-specific training data. The primary challenge in this setting lies in the mismatch in semantic granularity between textual queries and visual content. Previous studies in ZVMR have attempted to achieve alignment by leveraging high-quality pre-trained knowledge that represents video and language in a joint space. However, these approaches failed to balance the semantic granularity between the pre-trained knowledge provided by each modality for a given scene. As a result, despite the high quality of each modality's representations, the mismatch in granularity led to inaccurate retrieval. In this paper, we propose a training-free framework, called Granularity-Aware Alignment (GranAlign), that bridges this gap between coarse and fine semantic representations. Our approach introduces two complementary techniques: granularity-based query rewriting to generate varied semantic granularities, and query-aware caption generation to embed query intent into video content. By pairing multi-level queries with both query-agnostic and query-aware captions, we effectively resolve semantic mismatches. As a result, our method sets a new state-of-the-art across all three major benchmarks (QVHighlights, Charades-STA, ActivityNet-Captions), with a notable 3.23% mAP@avg improvement on the challenging QVHighlights dataset.

