---
layout: default
title: Tackling the Inherent Difficulty of Noise Filtering in RAG
---

# Tackling the Inherent Difficulty of Noise Filtering in RAG
**arXiv**：[2601.01896v1](https://arxiv.org/abs/2601.01896) · [PDF](https://arxiv.org/pdf/2601.01896.pdf)  
**作者**：Jingyu Liu, Jiaen Lin, Yong Liu  

**一句话要点**：提出一种新微调方法以增强LLMs在RAG中区分相关与无关信息的能力。

**关键词**：检索增强生成, 噪声过滤, 微调方法, 注意力机制, 鲁棒性提升

## 3 点简述
- 核心问题：RAG中检索到的噪声文档难以过滤，标准微调因注意力结构限制而效果不佳。
- 方法要点：设计新微调方法，提升模型在检索文档中区分相关与无关信息的能力。
- 实验或效果：在多个基准测试中显著提高LLMs的鲁棒性和性能。

## 摘要（原文）

> Retrieval-Augmented Generation (RAG) has become a widely adopted approach to enhance Large Language Models (LLMs) by incorporating external knowledge and reducing hallucinations. However, noisy or irrelevant documents are often introduced during RAG, potentially degrading performance and even causing hallucinated outputs. While various methods have been proposed to filter out such noise, we argue that identifying irrelevant information from retrieved content is inherently difficult and limited number of transformer layers can hardly solve this. Consequently, retrievers fail to filter out irrelevant documents entirely. Therefore, LLMs must be robust against such noise, but we demonstrate that standard fine-tuning approaches are often ineffective in enabling the model to selectively utilize relevant information while ignoring irrelevant content due to the structural constraints of attention patterns. To address this, we propose a novel fine-tuning method designed to enhance the model's ability to distinguish between relevant and irrelevant information within retrieved documents. Extensive experiments across multiple benchmarks show that our approach significantly improves the robustness and performance of LLMs.

