---
layout: default
title: Benchmarking LLM Summaries of Multimodal Clinical Time Series for Remote Monitoring
---

# Benchmarking LLM Summaries of Multimodal Clinical Time Series for Remote Monitoring
**arXiv**：[2603.01557v1](https://arxiv.org/abs/2603.01557) · [PDF](https://arxiv.org/pdf/2603.01557.pdf)  
**作者**：Aditya Shukla, Yining Yuan, Ben Tamo, Yifei Wang, Micky Nnamdi, Shaun Tan, Jieru Li, Benoit Marteau, Brad Willingham, May Wang  

**一句话要点**：提出基于事件的评估框架，以解决多模态临床时间序列摘要中临床事件保真度不足的问题。

**关键词**：多模态时间序列摘要, 临床事件评估, 远程监控, 大语言模型, 异常检测, 事件对齐

## 3 点简述
- 核心问题：现有评估指标主要关注语义相似性和语言质量，缺乏对临床事件级正确性的测量。
- 方法要点：引入基于事件的评估框架，使用规则化异常阈值和时间持续性标准从TIHM-1.5数据集提取临床事件。
- 实验或效果：基准测试显示，基于视觉的方法在事件对齐上表现最佳，异常召回率达45.7%，而传统指标与事件保真度脱钩。

## 摘要（原文）

> Large language models (LLMs) can generate fluent clinical summaries of remote therapeutic monitoring time series. However, it remains unclear whether these narratives faithfully capture clinically significant events, such as sustained abnormalities. Existing evaluation metrics primarily focus on semantic similarity and linguistic quality, leaving event-level correctness largely unmeasured.
>   To address this gap, we introduce an event-based evaluation framework for multimodal time-series summarization using the Technology-Integrated Health Management (TIHM)-1.5 dementia monitoring dataset. Clinically grounded daily events are derived through rule-based abnormal thresholds and temporal persistence criteria. Model-generated summaries are then aligned with these structured facts.
>   Our evaluation protocol measures abnormality recall, duration recall, measurement coverage, and hallucinated event mentions. We benchmark three approaches: zero-shot prompting, statistical prompting, and a vision-based pipeline that uses rendered time-series visualizations. The results reveal a striking decoupling between conventional metrics and clinical event fidelity. Models that achieve high semantic similarity scores often exhibit near-zero abnormality recall. In contrast, the vision-based approach demonstrates the strongest event alignment, achieving 45.7% abnormality recall and 100% duration recall.
>   These findings underscore the importance of event-aware evaluation to ensure reliable clinical time-series summarization.

