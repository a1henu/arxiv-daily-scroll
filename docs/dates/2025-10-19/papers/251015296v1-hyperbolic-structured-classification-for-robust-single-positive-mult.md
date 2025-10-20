---
layout: default
title: Hyperbolic Structured Classification for Robust Single Positive Multi-label Learning
---

# Hyperbolic Structured Classification for Robust Single Positive Multi-label Learning
**arXiv**：[2510.15296v1](https://arxiv.org/abs/2510.15296) · [PDF](https://arxiv.org/pdf/2510.15296.pdf)  
**作者**：Yiming Lin, Shang Wang, Junkai Zhou, Qiufeng Wang, Xiao-Bo Jin, Kaizhu Huang  

**一句话要点**：提出双曲结构化分类框架以解决单正多标签学习中的标签关系建模问题

**关键词**：单正多标签学习, 双曲几何, 结构化分类, 标签关系建模, 不完全监督学习

## 3 点简述
- 单正多标签学习中每个样本仅有一个正标签，难以捕捉复杂标签关系和层次结构
- 使用双曲球表示标签，通过几何交互建模包含、重叠和分离等多种关系类型
- 在多个基准数据集上验证了竞争性能，并显示学习嵌入与实际共现模式强相关

## 摘要（原文）

> Single Positive Multi-Label Learning (SPMLL) addresses the challenging
> scenario where each training sample is annotated with only one positive label
> despite potentially belonging to multiple categories, making it difficult to
> capture complex label relationships and hierarchical structures. While existing
> methods implicitly model label relationships through distance-based similarity,
> lacking explicit geometric definitions for different relationship types. To
> address these limitations, we propose the first hyperbolic classification
> framework for SPMLL that represents each label as a hyperbolic ball rather than
> a point or vector, enabling rich inter-label relationship modeling through
> geometric ball interactions. Our ball-based approach naturally captures
> multiple relationship types simultaneously: inclusion for hierarchical
> structures, overlap for co-occurrence patterns, and separation for semantic
> independence. Further, we introduce two key component innovations: a
> temperature-adaptive hyperbolic ball classifier and a physics-inspired
> double-well regularization that guides balls toward meaningful configurations.
> To validate our approach, extensive experiments on four benchmark datasets
> (MS-COCO, PASCAL VOC, NUS-WIDE, CUB-200-2011) demonstrate competitive
> performance with superior interpretability compared to existing methods.
> Furthermore, statistical analysis reveals strong correlation between learned
> embeddings and real-world co-occurrence patterns, establishing hyperbolic
> geometry as a more robust paradigm for structured classification under
> incomplete supervision.

