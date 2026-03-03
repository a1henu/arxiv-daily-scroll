---
layout: default
title: NICO-RAG: Multimodal Hypergraph Retrieval-Augmented Generation for Understanding the Nicotine Public Health Crisis
---

# NICO-RAG: Multimodal Hypergraph Retrieval-Augmented Generation for Understanding the Nicotine Public Health Crisis
**arXiv**：[2603.02047v1](https://arxiv.org/abs/2603.02047) · [PDF](https://arxiv.org/pdf/2603.02047.pdf)  
**作者**：Manuel Serna-Aguilera, Raegan Anderes, Page Dobbs, Khoa Luu  

**一句话要点**：提出NICO-RAG多模态超图检索增强生成框架，以应对尼古丁公共卫生危机中的大规模数据分析挑战。

**关键词**：多模态检索增强生成, 超图知识表示, 公共卫生数据分析, 图像检索, 尼古丁产品数据集

## 3 点简述
- 核心问题：尼古丁成瘾危机中，烟草行业创新产品削弱反烟草努力，现有研究难以连接大规模多模态数据点。
- 方法要点：构建NICO数据集，包含20万+图像和文本样本；提出NICO-RAG框架，利用超图组织实体关系，实现低成本图像检索和语义相似性查询。
- 实验或效果：在100+问题测试中，NICO-RAG无需处理图像令牌，性能媲美最先进的图像适配RAG方法。

## 摘要（原文）

> The nicotine addiction public health crisis continues to be pervasive. In this century alone, the tobacco industry has released and marketed new products in an aggressive effort to lure new and young customers for life. Such innovations and product development, namely flavored nicotine or tobacco such as nicotine pouches, have undone years of anti-tobacco campaign work. Past work is limited both in scope and in its ability to connect large-scale data points. Thus, we introduce the Nicotine Innovation Counter-Offensive (NICO) Dataset to provide public health researchers with over 200,000 multimodal samples, including images and text descriptions, on 55 tobacco and nicotine product brands. In addition, to provide public health researchers with factual connections across a large-scale dataset, we propose NICO-RAG, a retrieval-augmented generation (RAG) framework that can retrieve image features without incurring the high-cost of language models, as well as the added cost of processing image tokens with large-scale datasets such as NICO. At construction time, NICO-RAG organizes image- and text-extracted entities and relations into hypergraphs to produce as factual responses as possible. This joint multimodal knowledge representation enables NICO-RAG to retrieve images for query answering not only by visual similarity but also by the semantic similarity of image descriptions. Experimentals show that without needing to process additional tokens from images for over 100 questions, NICO-RAG performs comparably to the state-of-the-art RAG method adapted for images.

