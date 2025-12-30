---
layout: default
title: TV-RAG: A Temporal-aware and Semantic Entropy-Weighted Framework for Long Video Retrieval and Understanding
---

# TV-RAG: A Temporal-aware and Semantic Entropy-Weighted Framework for Long Video Retrieval and Understanding
**arXiv**：[2512.23483v1](https://arxiv.org/abs/2512.23483) · [PDF](https://arxiv.org/pdf/2512.23483.pdf)  
**作者**：Zongsheng Cao, Yangfan He, Anran Liu, Feng Chen, Zepeng Wang, Jun Xie  

**一句话要点**：提出TV-RAG框架，通过时间对齐与熵加权语义提升长视频检索与理解能力

**关键词**：长视频检索, 时间对齐, 语义熵加权, 大视频语言模型, 关键帧采样, 无需训练框架

## 3 点简述
- 核心问题：现有大视频语言模型在长视频中面临时间窗口窄、语义变化忽略及检索依赖表面词汇重叠的局限
- 方法要点：引入时间衰减检索模块和熵加权关键帧采样器，结合时间与语义信号实现无需训练的双层推理
- 实验或效果：在Video-MME等基准测试中超越主流基线，提供轻量级升级路径

## 摘要（原文）

> Large Video Language Models (LVLMs) have rapidly emerged as the focus of multimedia AI research. Nonetheless, when confronted with lengthy videos, these models struggle: their temporal windows are narrow, and they fail to notice fine-grained semantic shifts that unfold over extended durations. Moreover, mainstream text-based retrieval pipelines, which rely chiefly on surface-level lexical overlap, ignore the rich temporal interdependence among visual, audio, and subtitle channels. To mitigate these limitations, we propose TV-RAG, a training-free architecture that couples temporal alignment with entropy-guided semantics to improve long-video reasoning. The framework contributes two main mechanisms: \emph{(i)} a time-decay retrieval module that injects explicit temporal offsets into the similarity computation, thereby ranking text queries according to their true multimedia context; and \emph{(ii)} an entropy-weighted key-frame sampler that selects evenly spaced, information-dense frames, reducing redundancy while preserving representativeness. By weaving these temporal and semantic signals together, TV-RAG realises a dual-level reasoning routine that can be grafted onto any LVLM without re-training or fine-tuning. The resulting system offers a lightweight, budget-friendly upgrade path and consistently surpasses most leading baselines across established long-video benchmarks such as Video-MME, MLVU, and LongVideoBench, confirming the effectiveness of our model. The code can be found at https://github.com/AI-Researcher-Team/TV-RAG.

