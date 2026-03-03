---
layout: default
title: LexChronos: An Agentic Framework for Structured Event Timeline Extraction in Indian Jurisprudence
---

# LexChronos: An Agentic Framework for Structured Event Timeline Extraction in Indian Jurisprudence
**arXiv**：[2603.01651v1](https://arxiv.org/abs/2603.01651) · [PDF](https://arxiv.org/pdf/2603.01651.pdf)  
**作者**：Anka Chandrahas Tummepalli, Preethu Rose Anish  

**一句话要点**：提出LexChronos框架以从印度最高法院判决中提取结构化事件时间线

**关键词**：法律事件提取, 智能体框架, 印度法理学, 结构化时间线, 合成数据集

## 3 点简述
- 传统方法将法律文档视为非结构化文本，限制LLM在摘要和预测等任务中的效果
- 采用双智能体架构：提取智能体识别候选事件，反馈智能体通过置信度驱动循环评分和优化
- 构建合成数据集评估，BERT F1分数达0.8751，下游任务中GPT-4在75%案例中偏好结构化时间线

## 摘要（原文）

> Understanding and predicting judicial outcomes demands nuanced analysis of legal documents. Traditional approaches treat judgments and proceedings as unstructured text, limiting the effectiveness of large language models (LLMs) in tasks such as summarization, argument generation, and judgment prediction. We propose LexChronos, an agentic framework that iteratively extracts structured event timelines from Supreme Court of India judgments. LexChronos employs a dual-agent architecture: a LoRA-instruct-tuned extraction agent identifies candidate events, while a pre-trained feedback agent scores and refines them through a confidence-driven loop. To address the scarcity of Indian legal event datasets, we construct a synthetic corpus of 2000 samples using reverse-engineering techniques with DeepSeek-R1 and GPT-4, generating gold-standard event annotations. Our pipeline achieves a BERT-based F1 score of 0.8751 against this synthetic ground truth. In downstream evaluations on legal text summarization, GPT-4 preferred structured timelines over unstructured baselines in 75% of cases, demonstrating improved comprehension and reasoning in Indian jurisprudence. This work lays a foundation for future legal AI applications in the Indian context, such as precedent mapping, argument synthesis, and predictive judgment modelling, by harnessing structured representations of legal events.

