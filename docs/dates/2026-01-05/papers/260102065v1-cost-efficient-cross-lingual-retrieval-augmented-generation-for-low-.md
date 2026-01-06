---
layout: default
title: Cost-Efficient Cross-Lingual Retrieval-Augmented Generation for Low-Resource Languages: A Case Study in Bengali Agricultural Advisory
---

# Cost-Efficient Cross-Lingual Retrieval-Augmented Generation for Low-Resource Languages: A Case Study in Bengali Agricultural Advisory
**arXiv**：[2601.02065v1](https://arxiv.org/abs/2601.02065) · [PDF](https://arxiv.org/pdf/2601.02065.pdf)  
**作者**：Md. Asif Hossain, Nabil Subhan, Mantasha Rahman Mahi, Jannatul Ferdous Nabila  

**一句话要点**：提出跨语言检索增强生成框架，以低成本解决孟加拉语农业咨询中的语言障碍问题

**关键词**：跨语言检索增强生成, 低资源语言处理, 农业咨询系统, 翻译中心架构, 密集向量检索, 开源模型部署

## 3 点简述
- 核心问题：英语权威农业手册与孟加拉语农民交流间的语言鸿沟，导致低资源语言生成质量差且云方案成本高
- 方法要点：采用翻译中心架构，通过关键词注入增强查询，基于英语语料库进行密集向量检索，并回译确保可访问性
- 实验或效果：系统在消费级硬件上运行，实现可靠源接地响应、拒绝对域外查询，平均端到端延迟低于20秒

## 摘要（原文）

> Access to reliable agricultural advisory remains limited in many developing regions due to a persistent language barrier: authoritative agricultural manuals are predominantly written in English, while farmers primarily communicate in low-resource local languages such as Bengali. Although recent advances in Large Language Models (LLMs) enable natural language interaction, direct generation in low-resource languages often exhibits poor fluency and factual inconsistency, while cloud-based solutions remain cost-prohibitive. This paper presents a cost-efficient, cross-lingual Retrieval-Augmented Generation (RAG) framework for Bengali agricultural advisory that emphasizes factual grounding and practical deployability. The proposed system adopts a translation-centric architecture in which Bengali user queries are translated into English, enriched through domain-specific keyword injection to align colloquial farmer terminology with scientific nomenclature, and answered via dense vector retrieval over a curated corpus of English agricultural manuals (FAO, IRRI). The generated English response is subsequently translated back into Bengali to ensure accessibility. The system is implemented entirely using open-source models and operates on consumer-grade hardware without reliance on paid APIs. Experimental evaluation demonstrates reliable source-grounded responses, robust rejection of out-of-domain queries, and an average end-to-end latency below 20 seconds. The results indicate that cross-lingual retrieval combined with controlled translation offers a practical and scalable solution for agricultural knowledge access in low-resource language settings

