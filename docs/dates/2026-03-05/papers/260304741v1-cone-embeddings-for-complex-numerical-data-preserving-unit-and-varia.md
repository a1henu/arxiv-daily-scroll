---
layout: default
title: CONE: Embeddings for Complex Numerical Data Preserving Unit and Variable Semantics
---

# CONE: Embeddings for Complex Numerical Data Preserving Unit and Variable Semantics
**arXiv**：[2603.04741v1](https://arxiv.org/abs/2603.04741) · [PDF](https://arxiv.org/pdf/2603.04741.pdf)  
**作者**：Gyanendra Shrestha, Anna Pyayt, Michael Gubanov  

**一句话要点**：提出CONE模型以解决大模型在数值数据上语义编码不足的问题

**关键词**：数值嵌入, 复合嵌入算法, Transformer编码器, 数值推理, 语义保持

## 3 点简述
- 核心问题：大模型处理数值数据时难以保持语义和距离关系
- 方法要点：使用混合Transformer编码器，结合数值、单位和属性名构建复合嵌入
- 实验或效果：在DROP数据集上F1达87.28%，比SOTA提升9.37%

## 摘要（原文）

> Large pre-trained models (LMs) and Large Language Models (LLMs) are typically effective at capturing language semantics and contextual relationships. However, these models encounter challenges in maintaining optimal performance on tasks involving numbers. Blindly treating numerical or structured data as terms is inadequate -- their semantics must be well understood and encoded by the models. In this paper, we propose CONE, a hybrid transformer encoder pre-trained model that encodes numbers, ranges, and gaussians into an embedding vector space preserving distance. We introduce a novel composite embedding construction algorithm that integrates numerical values, ranges or gaussians together with their associated units and attribute names to precisely capture their intricate semantics. We conduct extensive experimental evaluation on large-scale datasets across diverse domains (web, medical, finance, and government) that justifies CONE's strong numerical reasoning capabilities, achieving an F1 score of 87.28% on DROP, a remarkable improvement of up to 9.37% in F1 over state-of-the-art (SOTA) baselines, and outperforming major SOTA models with a significant Recall@10 gain of up to 25%.

