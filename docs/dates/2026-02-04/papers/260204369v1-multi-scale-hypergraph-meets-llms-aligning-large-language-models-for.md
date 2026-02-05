---
layout: default
title: Multi-scale hypergraph meets LLMs: Aligning large language models for time series analysis
---

# Multi-scale hypergraph meets LLMs: Aligning large language models for time series analysis
**arXiv**：[2602.04369v1](https://arxiv.org/abs/2602.04369) · [PDF](https://arxiv.org/pdf/2602.04369.pdf)  
**作者**：Zongjiang Shang, Dongliang Cui, Binqing Wu, Ling Chen  

**一句话要点**：提出MSH-LLM方法，通过多尺度超图对齐大语言模型以提升时间序列分析性能

**关键词**：时间序列分析, 大语言模型对齐, 多尺度超图, 跨模态对齐, 混合提示机制

## 3 点简述
- 核心问题：现有方法未充分考虑自然语言与时间序列的多尺度结构，导致大语言模型能力利用不足。
- 方法要点：设计超边机制增强时间序列语义空间，引入跨模态对齐模块和混合提示机制以对齐多尺度模态。
- 实验或效果：在27个真实世界数据集上验证，MSH-LLM在5个应用中达到最先进结果。

## 摘要（原文）

> Recently, there has been great success in leveraging pre-trained large language models (LLMs) for time series analysis. The core idea lies in effectively aligning the modality between natural language and time series. However, the multi-scale structures of natural language and time series have not been fully considered, resulting in insufficient utilization of LLMs capabilities. To this end, we propose MSH-LLM, a Multi-Scale Hypergraph method that aligns Large Language Models for time series analysis. Specifically, a hyperedging mechanism is designed to enhance the multi-scale semantic information of time series semantic space. Then, a cross-modality alignment (CMA) module is introduced to align the modality between natural language and time series at different scales. In addition, a mixture of prompts (MoP) mechanism is introduced to provide contextual information and enhance the ability of LLMs to understand the multi-scale temporal patterns of time series. Experimental results on 27 real-world datasets across 5 different applications demonstrate that MSH-LLM achieves the state-of-the-art results.

