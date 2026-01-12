---
layout: default
title: Visualising Information Flow in Word Embeddings with Diffusion Tensor Imaging
---

# Visualising Information Flow in Word Embeddings with Diffusion Tensor Imaging
**arXiv**：[2601.05713v1](https://arxiv.org/abs/2601.05713) · [PDF](https://arxiv.org/pdf/2601.05713.pdf)  
**作者**：Thomas Fabian  

**一句话要点**：提出基于扩散张量成像的模型分析工具，以可视化自然语言表达中的信息流

**关键词**：信息流可视化, 扩散张量成像, 词嵌入分析, 模型可解释性, 自然语言处理

## 3 点简述
- 核心问题：现有方法仅分析孤立词嵌入，忽略上下文和自然语言表达的整体信息流
- 方法要点：应用扩散张量成像到词嵌入中，追踪信息在模型层间的流动
- 实验或效果：揭示模型结构差异，支持剪枝优化，并展示在代词解析和隐喻检测等任务中的信息流差异

## 摘要（原文）

> Understanding how large language models (LLMs) represent natural language is a central challenge in natural language processing (NLP) research. Many existing methods extract word embeddings from an LLM, visualise the embedding space via point-plots, and compare the relative positions of certain words. However, this approach only considers single words and not whole natural language expressions, thus disregards the context in which a word is used. Here we present a novel tool for analysing and visualising information flow in natural language expressions by applying diffusion tensor imaging (DTI) to word embeddings. We find that DTI reveals how information flows between word embeddings. Tracking information flows within the layers of an LLM allows for comparing different model structures and revealing opportunities for pruning an LLM's under-utilised layers. Furthermore, our model reveals differences in information flows for tasks like pronoun resolution and metaphor detection. Our results show that our model permits novel insights into how LLMs represent actual natural language expressions, extending the comparison of isolated word embeddings and improving the interpretability of NLP models.

