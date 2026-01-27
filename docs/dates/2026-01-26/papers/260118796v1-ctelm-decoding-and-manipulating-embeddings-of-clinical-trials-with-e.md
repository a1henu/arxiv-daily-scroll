---
layout: default
title: ctELM: Decoding and Manipulating Embeddings of Clinical Trials with Embedding Language Models
---

# ctELM: Decoding and Manipulating Embeddings of Clinical Trials with Embedding Language Models
**arXiv**：[2601.18796v1](https://arxiv.org/abs/2601.18796) · [PDF](https://arxiv.org/pdf/2601.18796.pdf)  
**作者**：Brian Ondov, Chia-Hsuan Chang, Yujia Zhou, Mauro Giuffrè, Hua Xu  

**一句话要点**：提出ctELM方法，通过嵌入语言模型解码和操纵临床试验嵌入，提升生物医学领域透明度与生成能力。

**关键词**：嵌入语言模型, 临床试验嵌入, 文本生成, 生物医学自然语言处理, 模型对齐

## 3 点简述
- 核心问题：文本嵌入空间解释性差，限制生成应用，尤其在临床试验领域。
- 方法要点：开发开源领域无关ELM架构，设计训练任务，使用专家验证合成数据集。
- 实验或效果：ctELM能准确描述和比较临床试验，生成响应年龄和性别概念向量的试验摘要。

## 摘要（原文）

> Text embeddings have become an essential part of a variety of language applications. However, methods for interpreting, exploring and reversing embedding spaces are limited, reducing transparency and precluding potentially valuable generative use cases. In this work, we align Large Language Models to embeddings of clinical trials using the recently reported Embedding Language Model (ELM) method. We develop an open-source, domain-agnostic ELM architecture and training framework, design training tasks for clinical trials, and introduce an expert-validated synthetic dataset. We then train a series of ELMs exploring the impact of tasks and training regimes. Our final model, ctELM, can accurately describe and compare unseen clinical trials from embeddings alone and produce plausible clinical trials from novel vectors. We further show that generated trial abstracts are responsive to moving embeddings along concept vectors for age and sex of study subjects. Our public ELM implementation and experimental results will aid the alignment of Large Language Models to embedding spaces in the biomedical domain and beyond.

