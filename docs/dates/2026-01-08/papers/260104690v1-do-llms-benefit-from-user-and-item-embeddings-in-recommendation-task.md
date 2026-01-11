---
layout: default
title: Do LLMs Benefit from User and Item Embeddings in Recommendation Tasks?
---

# Do LLMs Benefit from User and Item Embeddings in Recommendation Tasks?
**arXiv**：[2601.04690v1](https://arxiv.org/abs/2601.04690) · [PDF](https://arxiv.org/pdf/2601.04690.pdf)  
**作者**：Mir Rayat Imtiaz Hossain, Leo Feng, Leonid Sigal, Mohamed Osama Ahmed  

**一句话要点**：提出投影用户与物品嵌入到LLM令牌空间的方法，以增强推荐任务性能。

**关键词**：推荐系统, 大语言模型, 协同过滤, 嵌入投影, 多模态融合

## 3 点简述
- 核心问题：现有LLM推荐方法依赖文本语义或有限协同信号，难以处理多物品嵌入。
- 方法要点：通过轻量级投影模块将协同过滤学到的用户和物品嵌入映射到LLM令牌空间。
- 实验或效果：初步结果显示，该方法有效利用结构化交互数据，提升基于文本的LLM基线性能。

## 摘要（原文）

> Large Language Models (LLMs) have emerged as promising recommendation systems, offering novel ways to model user preferences through generative approaches. However, many existing methods often rely solely on text semantics or incorporate collaborative signals in a limited manner, typically using only user or item embeddings. These methods struggle to handle multiple item embeddings representing user history, reverting to textual semantics and neglecting richer collaborative information. In this work, we propose a simple yet effective solution that projects user and item embeddings, learned from collaborative filtering, into the LLM token space via separate lightweight projector modules. A finetuned LLM then conditions on these projected embeddings alongside textual tokens to generate recommendations. Preliminary results show that this design effectively leverages structured user-item interaction data, improves recommendation performance over text-only LLM baselines, and offers a practical path for bridging traditional recommendation systems with modern LLMs.

