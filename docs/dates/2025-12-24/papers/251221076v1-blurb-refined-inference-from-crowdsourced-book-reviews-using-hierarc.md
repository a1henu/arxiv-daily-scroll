---
layout: default
title: Blurb-Refined Inference from Crowdsourced Book Reviews using Hierarchical Genre Mining with Dual-Path Graph Convolutions
---

# Blurb-Refined Inference from Crowdsourced Book Reviews using Hierarchical Genre Mining with Dual-Path Graph Convolutions
**arXiv**：[2512.21076v1](https://arxiv.org/abs/2512.21076) · [PDF](https://arxiv.org/pdf/2512.21076.pdf)  
**作者**：Suraj Kumar, Utsav Kumar Nareti, Soumi Chattopadhyay, Chandranath Adak, Prolay Mallick  

**一句话要点**：提出HiGeMine框架，利用双路径图卷积和层次化挖掘，结合书评与简介提升书籍分类准确性。

**关键词**：层次化书籍分类, 双路径图卷积, 零样本语义对齐, 标签共现图, 用户评论过滤, 多标签预测

## 3 点简述
- 核心问题：现有书籍分类方法忽略层次结构，依赖嘈杂用户评论，导致可靠性下降。
- 方法要点：采用零样本语义对齐过滤评论，构建双路径图卷积模型，显式建模标签共现依赖。
- 实验或效果：在新数据集上，HiGeMine在层次分类任务中优于基线，提供结构化与非结构化数据融合方案。

## 摘要（原文）

> Accurate book genre classification is fundamental to digital library organization, content discovery, and personalized recommendation. Existing approaches typically model genre prediction as a flat, single-label task, ignoring hierarchical genre structure and relying heavily on noisy, subjective user reviews, which often degrade classification reliability. We propose HiGeMine, a two-phase hierarchical genre mining framework that robustly integrates user reviews with authoritative book blurbs. In the first phase, HiGeMine employs a zero-shot semantic alignment strategy to filter reviews, retaining only those semantically consistent with the corresponding blurb, thereby mitigating noise, bias, and irrelevance. In the second phase, we introduce a dual-path, two-level graph-based classification architecture: a coarse-grained Level-1 binary classifier distinguishes fiction from non-fiction, followed by Level-2 multi-label classifiers for fine-grained genre prediction. Inter-genre dependencies are explicitly modeled using a label co-occurrence graph, while contextual representations are derived from pretrained language models applied to the filtered textual content. To facilitate systematic evaluation, we curate a new hierarchical book genre dataset. Extensive experiments demonstrate that HiGeMine consistently outperformed strong baselines across hierarchical genre classification tasks. The proposed framework offers a principled and effective solution for leveraging both structured and unstructured textual data in hierarchical book genre analysis.

