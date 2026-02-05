---
layout: default
title: Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention
---

# Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention
**arXiv**：[2602.04711v1](https://arxiv.org/abs/2602.04711) · [PDF](https://arxiv.org/pdf/2602.04711.pdf)  
**作者**：Sagie Dekel, Moshe Tennenholtz, Oren Kurland  

**一句话要点**：提出稀疏文档注意力RAG以防御检索增强生成中的语料知识中毒攻击

**关键词**：检索增强生成, 语料知识中毒, 稀疏注意力, 防御机制, 问答系统

## 3 点简述
- 核心问题：RAG易受语料知识中毒攻击，攻击者注入误导文档操控LLM输出。
- 方法要点：引入SDAG，采用块稀疏注意力机制，禁止检索文档间的交叉注意力。
- 实验或效果：SDAG显著降低攻击成功率，与现有防御方法集成效果更优。

## 摘要（原文）

> Retrieval Augmented Generation (RAG) is a highly effective paradigm for keeping LLM-based responses up-to-date and reducing the likelihood of hallucinations. Yet, RAG was recently shown to be quite vulnerable to corpus knowledge poisoning: an attacker injects misleading documents to the corpus to steer an LLMs' output to an undesired response. We argue that the standard causal attention mechanism in LLMs enables harmful cross-document interactions, specifically in cases of attacks. Accordingly, we introduce a novel defense approach for RAG: Sparse Document Attention RAG (SDAG). This is a block-sparse attention mechanism that disallows cross-attention between retrieved documents. SDAG requires a minimal inference-time change to the attention mask; furthermore, no fine-tuning or additional architectural changes are needed. We present an empirical evaluation of LLM-based question answering (QA) with a variety of attack strategies on RAG. We show that our SDAG method substantially outperforms the standard causal attention mechanism in terms of attack success rate. We further demonstrate the clear merits of integrating SDAG with state-of-the-art RAG defense methods. Specifically, the integration results in performance that is statistically significantly better than the state-of-the-art.

