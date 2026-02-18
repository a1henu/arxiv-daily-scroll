---
layout: default
title: Enhancing Building Semantics Preservation in AI Model Training with Large Language Model Encodings
---

# Enhancing Building Semantics Preservation in AI Model Training with Large Language Model Encodings
**arXiv**：[2602.15791v1](https://arxiv.org/abs/2602.15791) · [PDF](https://arxiv.org/pdf/2602.15791.pdf)  
**作者**：Suhyung Jang, Ghang Lee, Jaekun Lee, Hyunjun Lee  

**一句话要点**：提出基于大语言模型嵌入的编码方法，以增强建筑语义在AI模型训练中的保留能力。

**关键词**：建筑语义编码, 大语言模型嵌入, GraphSAGE分类, 建筑信息模型, 语义保留

## 3 点简述
- 核心问题：传统编码方法难以捕捉建筑子类型间的细微语义关系，限制AI语义理解。
- 方法要点：使用大语言模型嵌入（如GPT和LLaMA）作为编码，保留建筑语义的精细区分。
- 实验或效果：在GraphSAGE模型分类任务中，LLM编码优于one-hot基线，最高F1分数达0.8766。

## 摘要（原文）

> Accurate representation of building semantics, encompassing both generic object types and specific subtypes, is essential for effective AI model training in the architecture, engineering, construction, and operation (AECO) industry. Conventional encoding methods (e.g., one-hot) often fail to convey the nuanced relationships among closely related subtypes, limiting AI's semantic comprehension. To address this limitation, this study proposes a novel training approach that employs large language model (LLM) embeddings (e.g., OpenAI GPT and Meta LLaMA) as encodings to preserve finer distinctions in building semantics. We evaluated the proposed method by training GraphSAGE models to classify 42 building object subtypes across five high-rise residential building information models (BIMs). Various embedding dimensions were tested, including original high-dimensional LLM embeddings (1,536, 3,072, or 4,096) and 1,024-dimensional compacted embeddings generated via the Matryoshka representation model. Experimental results demonstrated that LLM encodings outperformed the conventional one-hot baseline, with the llama-3 (compacted) embedding achieving a weighted average F1-score of 0.8766, compared to 0.8475 for one-hot encoding. The results underscore the promise of leveraging LLM-based encodings to enhance AI's ability to interpret complex, domain-specific building semantics. As the capabilities of LLMs and dimensionality reduction techniques continue to evolve, this approach holds considerable potential for broad application in semantic elaboration tasks throughout the AECO industry.

