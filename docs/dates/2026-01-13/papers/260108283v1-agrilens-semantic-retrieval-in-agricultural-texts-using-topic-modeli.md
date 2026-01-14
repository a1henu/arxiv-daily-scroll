---
layout: default
title: AgriLens: Semantic Retrieval in Agricultural Texts Using Topic Modeling and Language Models
---

# AgriLens: Semantic Retrieval in Agricultural Texts Using Topic Modeling and Language Models
**arXiv**：[2601.08283v1](https://arxiv.org/abs/2601.08283) · [PDF](https://arxiv.org/pdf/2601.08283.pdf)  
**作者**：Heba Shakeel, Tanvir Ahmad, Tanya Liyaqat, Chandni Saxena  

**一句话要点**：提出统一框架，结合主题建模与语言模型，实现农业文本的语义检索与解释性组织。

**关键词**：主题建模, 语义检索, 零样本学习, 农业文本分析, BERTopic, 向量搜索

## 3 点简述
- 核心问题：农业领域无标签文本量大，需可扩展方法进行信息组织与检索。
- 方法要点：使用BERTopic提取主题，通过提示工程实现零样本标签生成与摘要。
- 实验或效果：评估模块检查主题连贯性与偏见，支持向量搜索进行查询与文档探索。

## 摘要（原文）

> As the volume of unstructured text continues to grow across domains, there is an urgent need for scalable methods that enable interpretable organization, summarization, and retrieval of information. This work presents a unified framework for interpretable topic modeling, zero-shot topic labeling, and topic-guided semantic retrieval over large agricultural text corpora. Leveraging BERTopic, we extract semantically coherent topics. Each topic is converted into a structured prompt, enabling a language model to generate meaningful topic labels and summaries in a zero-shot manner. Querying and document exploration are supported via dense embeddings and vector search, while a dedicated evaluation module assesses topical coherence and bias. This framework supports scalable and interpretable information access in specialized domains where labeled data is limited.

