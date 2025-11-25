---
layout: default
title: UISearch: Graph-Based Embeddings for Multimodal Enterprise UI Screenshots Retrieval
---

# UISearch: Graph-Based Embeddings for Multimodal Enterprise UI Screenshots Retrieval
**arXiv**：[2511.19380v1](https://arxiv.org/abs/2511.19380) · [PDF](https://arxiv.org/pdf/2511.19380.pdf)  
**作者**：Maroun Ayli, Youssef Bakouny, Tushar Sharma, Nader Jalloul, Hani Seifeddine, Rima Kilany  

**一句话要点**：提出基于图的嵌入方法UISearch，以解决企业UI截图多模态检索中的结构建模不足问题。

**关键词**：UI检索, 图嵌入, 多模态学习, 企业软件, 对比学习, 结构建模

## 3 点简述
- 企业UI截图数量庞大，现有方法缺乏对UI结构属性的显式建模。
- 将UI截图转换为属性图，使用对比图自编码器学习多模态嵌入。
- 在金融软件UI数据集上，Top-5准确率达0.92，延迟低至47.5ms。

## 摘要（原文）

> Enterprise software companies maintain thousands of user interface screens across products and versions, creating critical challenges for design consistency, pattern discovery, and compliance check. Existing approaches rely on visual similarity or text semantics, lacking explicit modeling of structural properties fundamental to user interface (UI) composition. We present a novel graph-based representation that converts UI screenshots into attributed graphs encoding hierarchical relationships and spatial arrangements, potentially generalizable to document layouts, architectural diagrams, and other structured visual domains. A contrastive graph autoencoder learns embeddings preserving multi-level similarity across visual, structural, and semantic properties. The comprehensive analysis demonstrates that our structural embeddings achieve better discriminative power than state-of-the-art Vision Encoders, representing a fundamental advance in the expressiveness of the UI representation. We implement this representation in UISearch, a multi-modal search framework that combines structural embeddings with semantic search through a composable query language. On 20,396 financial software UIs, UISearch achieves 0.92 Top-5 accuracy with 47.5ms median latency (P95: 124ms), scaling to 20,000+ screens. The hybrid indexing architecture enables complex queries and supports fine-grained UI distinction impossible with vision-only approaches.

