---
layout: default
title: Diagnosing Causal Reasoning in Vision-Language Models via Structured Relevance Graphs
---

# Diagnosing Causal Reasoning in Vision-Language Models via Structured Relevance Graphs
**arXiv**：[2602.20878v1](https://arxiv.org/abs/2602.20878) · [PDF](https://arxiv.org/pdf/2602.20878.pdf)  
**作者**：Dhita Putri Pratama, Soyeon Caren Han, Yihao Ding  

**一句话要点**：提出视觉语言因果图以诊断大视觉语言模型的因果推理能力

**关键词**：视觉语言模型, 因果推理, 诊断基准, 结构化表示, 相关性评估

## 3 点简述
- 核心问题：大视觉语言模型在视觉问答中常依赖虚假关联而非真实因果推理，现有评估难以区分失败原因。
- 方法要点：引入视觉语言因果图作为结构化表示，编码因果相关对象、属性、关系和场景假设，并基于此构建ViLCaR诊断基准。
- 实验或效果：实验显示注入结构化相关性信息显著提升归因和推理一致性，表明当前限制主要源于结构指导不足而非推理能力缺乏。

## 摘要（原文）

> Large Vision-Language Models (LVLMs) achieve strong performance on visual question answering benchmarks, yet often rely on spurious correlations rather than genuine causal reasoning. Existing evaluations primarily assess the correctness of the answers, making it unclear whether failures arise from limited reasoning capability or from misidentifying causally relevant information. We introduce Vision-Language Causal Graphs (VLCGs), a structured, query-conditioned representation that explicitly encodes causally relevant objects, attributes, relations, and scene-grounded assumptions. Building on this representation, we present ViLCaR, a diagnostic benchmark comprising tasks for Causal Attribution, Causal Inference, and Question Answering, along with graph-aligned evaluation metrics that assess relevance identification beyond final answer accuracy. Experiments in state-of-the-art LVLMs show that injecting structured relevance information significantly improves attribution and inference consistency compared to zero-shot and standard in-context learning. These findings suggest that current limitations in LVLM causal reasoning stem primarily from insufficient structural guidance rather than a lack of reasoning capacity.

