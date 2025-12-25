---
layout: default
title: C2LLM Technical Report: A New Frontier in Code Retrieval via Adaptive Cross-Attention Pooling
---

# C2LLM Technical Report: A New Frontier in Code Retrieval via Adaptive Cross-Attention Pooling
**arXiv**：[2512.21332v1](https://arxiv.org/abs/2512.21332) · [PDF](https://arxiv.org/pdf/2512.21332.pdf)  
**作者**：Jin Qin, Zihan Liao, Ziyin Zhang, Hang Yu, Peng Di, Rui Wang  

**一句话要点**：提出C2LLM代码嵌入模型，通过自适应交叉注意力池化提升代码检索性能

**关键词**：代码嵌入模型, 多头注意力池化, 代码检索, 对比学习, 大语言模型

## 3 点简述
- 核心问题：传统基于EOS的序列嵌入存在信息瓶颈，限制代码检索效果
- 方法要点：基于Qwen-2.5-Coder骨干，采用多头注意力池化模块生成序列嵌入，支持灵活维度调整
- 实验或效果：在MTEB-Code基准上，C2LLM-7B在相似规模模型中排名第一，刷新记录

## 摘要（原文）

> We present C2LLM - Contrastive Code Large Language Models, a family of code embedding models in both 0.5B and 7B sizes. Building upon Qwen-2.5-Coder backbones, C2LLM adopts a Pooling by Multihead Attention (PMA) module for generating sequence embedding from token embeddings, effectively 1) utilizing the LLM's causal representations acquired during pretraining, while also 2) being able to aggregate information from all tokens in the sequence, breaking the information bottleneck in EOS-based sequence embeddings, and 3) supporting flexible adaptation of embedding dimension, serving as an alternative to MRL. Trained on three million publicly available data, C2LLM models set new records on MTEB-Code among models of similar sizes, with C2LLM-7B ranking 1st on the overall leaderboard.

