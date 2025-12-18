---
layout: default
title: O-EENC-SD: Efficient Online End-to-End Neural Clustering for Speaker Diarization
---

# O-EENC-SD: Efficient Online End-to-End Neural Clustering for Speaker Diarization
**arXiv**：[2512.15229v1](https://arxiv.org/abs/2512.15229) · [PDF](https://arxiv.org/pdf/2512.15229.pdf)  
**作者**：Elio Gruttadauria, Mathieu Fontaine, Jonathan Le Roux, Slim Essid  

**一句话要点**：提出O-EENC-SD在线端到端说话人日志系统，基于EEND-EDA，引入RNN拼接机制和质心精炼解码器以提高效率。

**关键词**：说话人日志, 端到端学习, 在线处理, RNN拼接, 质心精炼, 计算效率

## 3 点简述
- 核心问题：在线说话人日志需平衡准确性与计算效率，现有方法或依赖超参数或计算成本高。
- 方法要点：采用端到端架构，结合RNN在线拼接和质心精炼解码器，实现无超参数的高效处理。
- 实验或效果：在CallHome数据集上验证，在双人电话对话场景中，DER与复杂度达到良好权衡，优于现有在线方法。

## 摘要（原文）

> We introduce O-EENC-SD: an end-to-end online speaker diarization system based on EEND-EDA, featuring a novel RNN-based stitching mechanism for online prediction. In particular, we develop a novel centroid refinement decoder whose usefulness is assessed through a rigorous ablation study. Our system provides key advantages over existing methods: a hyperparameter-free solution compared to unsupervised clustering approaches, and a more efficient alternative to current online end-to-end methods, which are computationally costly. We demonstrate that O-EENC-SD is competitive with the state of the art in the two-speaker conversational telephone speech domain, as tested on the CallHome dataset. Our results show that O-EENC-SD provides a great trade-off between DER and complexity, even when working on independent chunks with no overlap, making the system extremely efficient.

