---
layout: default
title: SMART SLM: Structured Memory and Reasoning Transformer, A Small Language Model for Accurate Document Assistance
---

# SMART SLM: Structured Memory and Reasoning Transformer, A Small Language Model for Accurate Document Assistance
**arXiv**：[2512.21280v1](https://arxiv.org/abs/2512.21280) · [PDF](https://arxiv.org/pdf/2512.21280.pdf)  
**作者**：Divij Dudeja, Mayukha Pal  

**一句话要点**：提出结构化记忆与推理Transformer，以解决工程手册文档辅助中的准确性问题

**关键词**：结构化记忆, 文档辅助, 小型语言模型, 事实提取, 索引记忆网络, 推理Transformer

## 3 点简述
- 核心问题：工程手册文档冗长密集，传统小型Transformer处理为扁平令牌流，导致数字答案错误且记忆低效
- 方法要点：采用分层处理，包括语法感知事实提取器、紧凑索引记忆网络和6层Transformer融合事实
- 实验或效果：模型参数45.51M，比GPT-2和BERT少64-69%，准确率提高21.3%，支持快速和动态推理路径

## 摘要（原文）

> The user of Engineering Manuals (EM) finds it difficult to read EM s because they are long, have a dense format which includes written documents, step by step procedures, and standard parameter lists for engineering equipment. Off the shelf transformers, especially compact ones, treat this material as a flat stream of tokens. This approach leads to confident but incorrect numeric answers and forces the models to memorize separate facts inefficiently. SMART (Structured Memory and Reasoning Transformer) offers a different and practical solution to the above problem. SMART structures its processing by using a hierarchical approach, and is based upon three main job categories (1) A syntax-aware Fact Extractor (Grammarian) Tree LSTM which extracts facts as subject relation object relations from EM sentences (2) A compact indexed memory MANN (Memory Augmented Neural Network) that indexes these Rational Subject Relation Objects as 384 dimensional vectors that are associated with the source of the information, and (3) A 6 layer Transformer that learns to fuse the previously retrieved facts into its generated response. The entire SMART model utilizes 45.51M parameters, which is 64% less than GPT-2 (124M) and 69% less than BERT (133M), and it achieves a 21.3% higher accuracy than GPT-2, indicating that SMART fits the data better with the least amount of processing requirements. SMART employs dual modes of inference an indexed fast path for known documents (sub-second answer times) and an indexed dynamic path assisted by RAGs for new uploads (FAISS Top 20 results with memory severed at 64 slots). In real world deployment, this framework leads to more well supported results with reduced hallucinations than comparable small transformer models.

