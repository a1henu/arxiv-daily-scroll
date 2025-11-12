---
layout: default
title: VideoChain: A Transformer-Based Framework for Multi-hop Video Question Generation
---

# VideoChain: A Transformer-Based Framework for Multi-hop Video Question Generation
**arXiv**：[2511.08348v1](https://arxiv.org/abs/2511.08348) · [PDF](https://arxiv.org/pdf/2511.08348.pdf)  
**作者**：Arpan Phukan, Anupam Pandey, Deepjyoti Bodo, Asif Ekbal  

**一句话要点**：提出VideoChain框架以解决多跳视频问题生成任务

**关键词**：多跳视频问题生成, Transformer框架, 视频嵌入, BART模型, 多模态推理, TVQA+数据集

## 3 点简述
- 核心问题：多跳问题生成局限于文本，视频问题生成仅支持零跳单片段
- 方法要点：基于改进BART的模块化架构，融合视频嵌入捕获多模态依赖
- 实验或效果：在MVQ-60数据集上评估，ROUGE-L达0.6454，生成问题连贯且推理密集

## 摘要（原文）

> Multi-hop Question Generation (QG) effectively evaluates reasoning but remains confined to text; Video Question Generation (VideoQG) is limited to zero-hop questions over single segments. To address this, we introduce VideoChain, a novel Multi-hop Video Question Generation (MVQG) framework designed to generate questions that require reasoning across multiple, temporally separated video segments. VideoChain features a modular architecture built on a modified BART backbone enhanced with video embeddings, capturing textual and visual dependencies. Using the TVQA+ dataset, we automatically construct the large-scale MVQ-60 dataset by merging zero-hop QA pairs, ensuring scalability and diversity. Evaluations show VideoChain's strong performance across standard generation metrics: ROUGE-L (0.6454), ROUGE-1 (0.6854), BLEU-1 (0.6711), BERTScore-F1 (0.7967), and semantic similarity (0.8110). These results highlight the model's ability to generate coherent, contextually grounded, and reasoning-intensive questions.

