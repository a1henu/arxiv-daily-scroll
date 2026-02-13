---
layout: default
title: ULTRA:Urdu Language Transformer-based Recommendation Architecture
---

# ULTRA:Urdu Language Transformer-based Recommendation Architecture
**arXiv**：[2602.11836v1](https://arxiv.org/abs/2602.11836) · [PDF](https://arxiv.org/pdf/2602.11836.pdf)  
**作者**：Alishbah Bashir, Fatima Qaiser, Ijaz Hussain  

**一句话要点**：提出ULTRA框架，通过查询长度感知路由机制解决乌尔都语低资源语义推荐问题。

**关键词**：乌尔都语推荐, 查询长度感知, 双嵌入架构, 语义路由, 低资源语言, 变压器嵌入

## 3 点简述
- 核心问题：乌尔都语作为低资源语言，现有推荐系统依赖词汇匹配，语义捕捉能力差，导致推荐相关性低。
- 方法要点：采用双嵌入架构，基于阈值路由区分短查询和长查询，优化标题级或全文级语义管道。
- 实验或效果：在大规模乌尔都语新闻语料上实验，相比单管道基线，精度提升超过90%。

## 摘要（原文）

> Urdu, as a low-resource language, lacks effective semantic content recommendation systems, particularly in the domain of personalized news retrieval. Existing approaches largely rely on lexical matching or language-agnostic techniques, which struggle to capture semantic intent and perform poorly under varying query lengths and information needs. This limitation results in reduced relevance and adaptability in Urdu content recommendation. We propose ULTRA (Urdu Language Transformer-based Recommendation Architecture),an adaptive semantic recommendation framework designed to address these challenges. ULTRA introduces a dual-embedding architecture with a query-length aware routing mechanism that dynamically distinguishes between short, intent-focused queries and longer, context-rich queries. Based on a threshold-driven decision process, user queries are routed to specialized semantic pipelines optimized for either title/headline-level or full-content/document level representations, ensuring appropriate semantic granularity during retrieval. The proposed system leverages transformer-based embeddings and optimized pooling strategies to move beyond surface-level keyword matching and enable context-aware similarity search. Extensive experiments conducted on a large-scale Urdu news corpus demonstrate that the proposed architecture consistently improves recommendation relevance across diverse query types. Results show gains in precision above 90% compared to single-pipeline baselines, highlighting the effectiveness of query-adaptive semantic alignment for low-resource languages. The findings establish ULTRA as a robust and generalizable content recommendation architecture, offering practical design insights for semantic retrieval systems in low-resource language settings.

