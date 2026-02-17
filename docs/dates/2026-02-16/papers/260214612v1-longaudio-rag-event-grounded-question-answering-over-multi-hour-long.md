---
layout: default
title: LongAudio-RAG: Event-Grounded Question Answering over Multi-Hour Long Audio
---

# LongAudio-RAG: Event-Grounded Question Answering over Multi-Hour Long Audio
**arXiv**：[2602.14612v1](https://arxiv.org/abs/2602.14612) · [PDF](https://arxiv.org/pdf/2602.14612.pdf)  
**作者**：Naveen Vakada, Kartik Hegde, Arvind Krishna Sridhar, Yinyi Guo, Erik Visser  

**一句话要点**：提出LongAudio-RAG框架，通过事件检索增强LLM，解决多小时长音频问答问题。

**关键词**：长音频问答, 检索增强生成, 事件检测, SQL数据库, 边缘计算

## 3 点简述
- 核心问题：长音频问答受限于上下文长度，导致幻觉和精度不足。
- 方法要点：将音频转换为结构化事件记录，基于SQL检索增强LLM生成答案。
- 实验或效果：事件级检索相比传统RAG或文本到SQL方法显著提升准确性。

## 摘要（原文）

> Long-duration audio is increasingly common in industrial and consumer settings, yet reviewing multi-hour recordings is impractical, motivating systems that answer natural-language queries with precise temporal grounding and minimal hallucination. Existing audio-language models show promise, but long-audio question answering remains difficult due to context-length limits. We introduce LongAudio-RAG (LA-RAG), a hybrid framework that grounds Large Language Model (LLM) outputs in retrieved, timestamped acoustic event detections rather than raw audio. Multi-hour streams are converted into structured event records stored in an SQL database, and at inference time the system resolves natural-language time references, classifies intent, retrieves only the relevant events, and generates answers using this constrained evidence. To evaluate performance, we construct a synthetic long-audio benchmark by concatenating recordings with preserved timestamps and generating template-based question-answer pairs for detection, counting, and summarization tasks. Finally, we demonstrate the practicality of our approach by deploying it in a hybrid edge-cloud environment, where the audio grounding model runs on-device on IoT-class hardware while the LLM is hosted on a GPU-backed server. This architecture enables low-latency event extraction at the edge and high-quality language reasoning in the cloud. Experiments show that structured, event-level retrieval significantly improves accuracy compared to vanilla Retrieval-Augmented Generation (RAG) or text-to-SQL approaches.

