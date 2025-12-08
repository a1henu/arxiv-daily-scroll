---
layout: default
title: A Systematic Framework for Enterprise Knowledge Retrieval: Leveraging LLM-Generated Metadata to Enhance RAG Systems
---

# A Systematic Framework for Enterprise Knowledge Retrieval: Leveraging LLM-Generated Metadata to Enhance RAG Systems
**arXiv**：[2512.05411v1](https://arxiv.org/abs/2512.05411) · [PDF](https://arxiv.org/pdf/2512.05411.pdf)  
**作者**：Pranav Pushkar Mishra, Kranti Prakash Yeole, Ramyashree Keshavamurthy, Mokshit Bharat Surana, Fatemeh Sarayloo  

**一句话要点**：提出基于LLM生成元数据的系统框架，以增强企业RAG系统的文档检索效果

**关键词**：元数据增强, 检索增强生成, 文档检索, 企业知识库, 大语言模型, 向量聚类

## 3 点简述
- 核心问题：企业知识库中高效检索复杂信息，提升操作效率和决策支持。
- 方法要点：采用结构化流水线，动态生成文档片段的元数据，优化语义表示和检索精度。
- 实验或效果：元数据增强方法优于仅内容基线，递归分块结合TF-IDF加权嵌入实现82.5%精确率。

## 摘要（原文）

> In enterprise settings, efficiently retrieving relevant information from large and complex knowledge bases is essential for operational productivity and informed decision-making. This research presents a systematic framework for metadata enrichment using large language models (LLMs) to enhance document retrieval in Retrieval-Augmented Generation (RAG) systems. Our approach employs a comprehensive, structured pipeline that dynamically generates meaningful metadata for document segments, substantially improving their semantic representations and retrieval accuracy. Through extensive experiments, we compare three chunking strategies-semantic, recursive, and naive-and evaluate their effectiveness when combined with advanced embedding techniques. The results demonstrate that metadata-enriched approaches consistently outperform content-only baselines, with recursive chunking paired with TF-IDF weighted embeddings yielding an 82.5% precision rate compared to 73.3% for semantic content-only approaches. The naive chunking strategy with prefix-fusion achieved the highest Hit Rate@10 of 0.925. Our evaluation employs cross-encoder reranking for ground truth generation, enabling rigorous assessment via Hit Rate and Metadata Consistency metrics. These findings confirm that metadata enrichment enhances vector clustering quality while reducing retrieval latency, making it a key optimization for RAG systems across knowledge domains. This work offers practical insights for deploying high-performance, scalable document retrieval solutions in enterprise settings, demonstrating that metadata enrichment is a powerful approach for enhancing RAG effectiveness.

