---
layout: default
title: Introducing TrGLUE and SentiTurca: A Comprehensive Benchmark for Turkish General Language Understanding and Sentiment Analysis
---

# Introducing TrGLUE and SentiTurca: A Comprehensive Benchmark for Turkish General Language Understanding and Sentiment Analysis
**arXiv**：[2512.22100v1](https://arxiv.org/abs/2512.22100) · [PDF](https://arxiv.org/pdf/2512.22100.pdf)  
**作者**：Duygu Altinok  

**一句话要点**：提出TrGLUE和SentiTurca基准，以解决土耳其语自然语言理解与情感分析缺乏全面评估框架的问题。

**关键词**：土耳其语自然语言理解, 基准数据集, 半自动化标注, 情感分析, Transformer模型, 多任务评估

## 3 点简述
- 核心问题：土耳其语缺乏类似GLUE的全面自然语言理解基准，阻碍模型评估与比较。
- 方法要点：构建TrGLUE涵盖多任务NLU，采用半自动化标注流程结合LLM与人工验证，确保数据质量。
- 实验或效果：提供微调与评估代码，支持基于Transformer的模型，旨在建立可扩展、可复现的评估框架。

## 摘要（原文）

> Evaluating the performance of various model architectures, such as transformers, large language models (LLMs), and other NLP systems, requires comprehensive benchmarks that measure performance across multiple dimensions. Among these, the evaluation of natural language understanding (NLU) is particularly critical as it serves as a fundamental criterion for assessing model capabilities. Thus, it is essential to establish benchmarks that enable thorough evaluation and analysis of NLU abilities from diverse perspectives. While the GLUE benchmark has set a standard for evaluating English NLU, similar benchmarks have been developed for other languages, such as CLUE for Chinese, FLUE for French, and JGLUE for Japanese. However, no comparable benchmark currently exists for the Turkish language. To address this gap, we introduce TrGLUE, a comprehensive benchmark encompassing a variety of NLU tasks for Turkish. In addition, we present SentiTurca, a specialized benchmark for sentiment analysis. To support researchers, we also provide fine-tuning and evaluation code for transformer-based models, facilitating the effective use of these benchmarks. TrGLUE comprises Turkish-native corpora curated to mirror the domains and task formulations of GLUE-style evaluations, with labels obtained through a semi-automated pipeline that combines strong LLM-based annotation, cross-model agreement checks, and subsequent human validation. This design prioritizes linguistic naturalness, minimizes direct translation artifacts, and yields a scalable, reproducible workflow. With TrGLUE, our goal is to establish a robust evaluation framework for Turkish NLU, empower researchers with valuable resources, and provide insights into generating high-quality semi-automated datasets.

