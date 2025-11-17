---
layout: default
title: Hyperbolic Hierarchical Alignment Reasoning Network for Text-3D Retrieval
---

# Hyperbolic Hierarchical Alignment Reasoning Network for Text-3D Retrieval
**arXiv**：[2511.11045v1](https://arxiv.org/abs/2511.11045) · [PDF](https://arxiv.org/pdf/2511.11045.pdf)  
**作者**：Wenrui Li, Yidan Lu, Yeyu Chai, Rui Zhao, Hengyu Man, Xiaopeng Fan  

**一句话要点**：提出双曲层次对齐推理网络以解决文本-3D检索中的层次表示崩溃和冗余诱导显著性稀释问题

**关键词**：文本-3D检索, 双曲嵌入, 层次对齐, 贡献感知聚合, 洛伦兹模型, 对比学习

## 3 点简述
- 核心问题：层次表示崩溃压缩抽象-具体和整体-部分层次，冗余诱导显著性稀释平均噪声片段，削弱模型区分能力
- 方法要点：在洛伦兹双曲空间嵌入文本和3D数据，使用层次排序损失和实例级对比损失，结合贡献感知双曲聚合模块
- 实验或效果：发布扩展T3DR-HIT v2基准，包含8935对文本-3D数据，代码开源，未知具体性能指标

## 摘要（原文）

> With the daily influx of 3D data on the internet, text-3D retrieval has gained increasing attention. However, current methods face two major challenges: Hierarchy Representation Collapse (HRC) and Redundancy-Induced Saliency Dilution (RISD). HRC compresses abstract-to-specific and whole-to-part hierarchies in Euclidean embeddings, while RISD averages noisy fragments, obscuring critical semantic cues and diminishing the model's ability to distinguish hard negatives. To address these challenges, we introduce the Hyperbolic Hierarchical Alignment Reasoning Network (H$^{2}$ARN) for text-3D retrieval. H$^{2}$ARN embeds both text and 3D data in a Lorentz-model hyperbolic space, where exponential volume growth inherently preserves hierarchical distances. A hierarchical ordering loss constructs a shrinking entailment cone around each text vector, ensuring that the matched 3D instance falls within the cone, while an instance-level contrastive loss jointly enforces separation from non-matching samples. To tackle RISD, we propose a contribution-aware hyperbolic aggregation module that leverages Lorentzian distance to assess the relevance of each local feature and applies contribution-weighted aggregation guided by hyperbolic geometry, enhancing discriminative regions while suppressing redundancy without additional supervision. We also release the expanded T3DR-HIT v2 benchmark, which contains 8,935 text-to-3D pairs, 2.6 times the original size, covering both fine-grained cultural artefacts and complex indoor scenes. Our codes are available at https://github.com/liwrui/H2ARN.

