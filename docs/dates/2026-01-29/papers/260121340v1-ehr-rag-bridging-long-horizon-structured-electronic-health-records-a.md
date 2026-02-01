---
layout: default
title: EHR-RAG: Bridging Long-Horizon Structured Electronic Health Records and Large Language Models via Enhanced Retrieval-Augmented Generation
---

# EHR-RAG: Bridging Long-Horizon Structured Electronic Health Records and Large Language Models via Enhanced Retrieval-Augmented Generation
**arXiv**：[2601.21340v1](https://arxiv.org/abs/2601.21340) · [PDF](https://arxiv.org/pdf/2601.21340.pdf)  
**作者**：Lang Cao, Qingyu Chen, Yue Guo  

**一句话要点**：提出EHR-RAG框架以解决长时程结构化电子健康记录中LLM预测的检索增强生成问题

**关键词**：电子健康记录, 检索增强生成, 长时程预测, 临床决策支持, 大型语言模型, 结构化数据

## 3 点简述
- 核心问题：长时程EHR超出LLM上下文限制，现有方法丢弃临床相关事件和时间依赖。
- 方法要点：引入事件和时间感知混合检索、自适应迭代检索和双路径证据检索与推理。
- 实验或效果：在四个长时程EHR预测任务中平均Macro-F1提升10.76%。

## 摘要（原文）

> Electronic Health Records (EHRs) provide rich longitudinal clinical evidence that is central to medical decision-making, motivating the use of retrieval-augmented generation (RAG) to ground large language model (LLM) predictions. However, long-horizon EHRs often exceed LLM context limits, and existing approaches commonly rely on truncation or vanilla retrieval strategies that discard clinically relevant events and temporal dependencies. To address these challenges, we propose EHR-RAG, a retrieval-augmented framework designed for accurate interpretation of long-horizon structured EHR data. EHR-RAG introduces three components tailored to longitudinal clinical prediction tasks: Event- and Time-Aware Hybrid EHR Retrieval to preserve clinical structure and temporal dynamics, Adaptive Iterative Retrieval to progressively refine queries in order to expand broad evidence coverage, and Dual-Path Evidence Retrieval and Reasoning to jointly retrieves and reasons over both factual and counterfactual evidence. Experiments across four long-horizon EHR prediction tasks show that EHR-RAG consistently outperforms the strongest LLM-based baselines, achieving an average Macro-F1 improvement of 10.76%. Overall, our work highlights the potential of retrieval-augmented LLMs to advance clinical prediction on structured EHR data in practice.

