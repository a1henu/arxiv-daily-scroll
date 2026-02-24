---
layout: default
title: AgenticSum: An Agentic Inference-Time Framework for Faithful Clinical Text Summarization
---

# AgenticSum: An Agentic Inference-Time Framework for Faithful Clinical Text Summarization
**arXiv**：[2602.20040v1](https://arxiv.org/abs/2602.20040) · [PDF](https://arxiv.org/pdf/2602.20040.pdf)  
**作者**：Fahmida Liza Piya, Rahmatollah Beheshti  

**一句话要点**：提出AgenticSum框架，通过代理式推理阶段分解与针对性修正，提升临床文本摘要的事实一致性。

**关键词**：临床文本摘要, 事实一致性, 代理式推理, 针对性修正, LLM应用, 推理时间框架

## 3 点简述
- 核心问题：LLMs在临床文本摘要中面临事实一致性挑战，源于文档长度、噪声和异质性。
- 方法要点：框架将摘要分解为上下文选择、生成、验证和针对性修正的协调阶段，利用内部注意力信号识别弱支持内容。
- 实验或效果：在公开数据集上评估，相比基线模型，AgenticSum在多种指标上显示一致改进，包括基于参考、LLM作为评判和人工评估。

## 摘要（原文）

> Large language models (LLMs) offer substantial promise for automating clinical text summarization, yet maintaining factual consistency remains challenging due to the length, noise, and heterogeneity of clinical documentation. We present AgenticSum, an inference-time, agentic framework that separates context selection, generation, verification, and targeted correction to reduce hallucinated content. The framework decomposes summarization into coordinated stages that compress task-relevant context, generate an initial draft, identify weakly supported spans using internal attention grounding signals, and selectively revise flagged content under supervisory control. We evaluate AgenticSum on two public datasets, using reference-based metrics, LLM-as-a-judge assessment, and human evaluation. Across various measures, AgenticSum demonstrates consistent improvements compared to vanilla LLMs and other strong baselines. Our results indicate that structured, agentic design with targeted correction offers an effective inference time solution to improve clinical note summarization using LLMs.

