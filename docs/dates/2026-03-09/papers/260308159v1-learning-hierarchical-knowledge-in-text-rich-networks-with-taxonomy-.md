---
layout: default
title: Learning Hierarchical Knowledge in Text-Rich Networks with Taxonomy-Informed Representation Learning
---

# Learning Hierarchical Knowledge in Text-Rich Networks with Taxonomy-Informed Representation Learning
**arXiv**：[2603.08159v1](https://arxiv.org/abs/2603.08159) · [PDF](https://arxiv.org/pdf/2603.08159.pdf)  
**作者**：Yunhui Liu, Yongchao Liu, Yinfeng Chen, Chuntao Hong, Tao Zheng, Tieke He  

**一句话要点**：提出TIER方法，通过构建隐式层次分类法并融入节点表示，以解决文本丰富网络中层次知识学习不足的问题。

**关键词**：文本丰富网络, 层次分类法, 表示学习, 对比学习, 聚类细化, 正则化损失

## 3 点简述
- 核心问题：现有文本丰富网络方法忽略文本中的层次语义，导致扁平化建模。
- 方法要点：TIER使用相似性引导对比学习构建嵌入空间，结合层次K-Means和LLM聚类细化构建分类法，并引入正则化损失对齐层次结构。
- 实验或效果：在多个领域数据集上显著优于现有方法，验证了层次知识学习的重要性。

## 摘要（原文）

> Hierarchical knowledge structures are ubiquitous across real-world domains and play a vital role in organizing information from coarse to fine semantic levels. While such structures have been widely used in taxonomy systems, biomedical ontologies, and retrieval-augmented generation, their potential remains underexplored in the context of Text-Rich Networks (TRNs), where each node contains rich textual content and edges encode semantic relationships. Existing methods for learning on TRNs often focus on flat semantic modeling, overlooking the inherent hierarchical semantics embedded in textual documents. To this end, we propose TIER (Hierarchical \textbf{T}axonomy-\textbf{I}nformed R\textbf{E}presentation Learning on Text-\textbf{R}ich Networks), which first constructs an implicit hierarchical taxonomy and then integrates it into the learned node representations. Specifically, TIER employs similarity-guided contrastive learning to build a clustering-friendly embedding space, upon which it performs hierarchical K-Means followed by LLM-powered clustering refinement to enable semantically coherent taxonomy construction. Leveraging the resulting taxonomy, TIER introduces a cophenetic correlation coefficient-based regularization loss to align the learned embeddings with the hierarchical structure. By learning representations that respect both fine-grained and coarse-grained semantics, TIER enables more interpretable and structured modeling of real-world TRNs. We demonstrate that our approach significantly outperforms existing methods on multiple datasets across diverse domains, highlighting the importance of hierarchical knowledge learning for TRNs.

