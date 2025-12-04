---
layout: default
title: Divide, then Ground: Adapting Frame Selection to Query Types for Long-Form Video Understanding
---

# Divide, then Ground: Adapting Frame Selection to Query Types for Long-Form Video Understanding
**arXiv**：[2512.04000v1](https://arxiv.org/abs/2512.04000) · [PDF](https://arxiv.org/pdf/2512.04000.pdf)  
**作者**：Jialuo Li, Bin Li, Jiahao Li, Yan Lu  

**一句话要点**：提出DIG框架，根据查询类型自适应选择帧策略以提升长视频理解效率与性能

**关键词**：长视频理解, 帧选择, 查询类型, 大型多模态模型, 自适应策略

## 3 点简述
- 核心问题：长视频理解中，现有查询感知帧选择方法计算开销大，且未区分查询类型。
- 方法要点：基于查询类型（全局与局部），DIG采用均匀采样或专用管道自适应选择帧，无需训练。
- 实验或效果：在三个基准测试中，DIG优于基线，输入帧数达256时仍能提升LMM性能。

## 摘要（原文）

> The application of Large Multimodal Models (LMMs) to long-form video understanding is constrained by limited context lengths and the computationally prohibitive cost of processing dense video tokens. Consequently, recent research has focused on query-aware frame selection, methods that often incur significant computational overhead. This paper challenges the assumption that such complex search mechanisms are universally necessary. We first identify and validate a query typology distinguishing between global query and localized query. We demonstrate that while uniform sampling is both effective and efficient for global queries, localized queries indeed necessitate query-aware selection for optimal performance. Building on this insight, we propose DIG, a training-free frame selection framework that adapts its strategy based on the query type. Specifically,DIG employs efficient uniform sampling for global queries while activating a specialized pipeline to extract query-relevant frames for localized queries. Experiments on three long-form video understanding benchmarks demonstrate that DIG consistently outperforms existing baselines and robustly improves LMM performance, even when scaling the input frame count to 256.

