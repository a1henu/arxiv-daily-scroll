---
layout: default
title: From Facts to Conclusions : Integrating Deductive Reasoning in Retrieval-Augmented LLMs
---

# From Facts to Conclusions : Integrating Deductive Reasoning in Retrieval-Augmented LLMs
**arXiv**：[2512.16795v1](https://arxiv.org/abs/2512.16795) · [PDF](https://arxiv.org/pdf/2512.16795.pdf)  
**作者**：Shubham Mishra, Samyek Jain, Gorang Mehrishi, Shiv Tiwari, Harsh Sharma, Pratik Narang, Dhruv Kumar  

**一句话要点**：提出推理轨迹增强的RAG框架，以解决检索信息冲突和不可靠问题，提升答案正确性和可解释性。

**关键词**：检索增强生成, 推理轨迹, 冲突分析, 可解释性, LLM评估, 监督微调

## 3 点简述
- 核心问题：RAG在检索源冲突、过时或主观信息时失效，缺乏统一推理监督。
- 方法要点：引入三阶段结构化推理（文档裁决、冲突分析、基础合成）和CATS评估管道。
- 实验或效果：在Qwen模型上，端到端答案正确率从0.069提升至0.883，行为一致性从0.074提升至0.722。

## 摘要（原文）

> Retrieval-Augmented Generation (RAG) grounds large language models (LLMs) in external evidence, but fails when retrieved sources conflict or contain outdated or subjective information. Prior work address these issues independently but lack unified reasoning supervision. We propose a reasoning-trace-augmented RAG framework that adds structured, interpretable reasoning across three stages : (1) document-level adjudication, (2) conflict analysis, and (3) grounded synthesis, producing citation-linked answers or justified refusals. A Conflict-Aware Trust-Score (CATS) pipeline is introduced which evaluates groundedness, factual correctness, refusal accuracy, and conflict-behavior alignment using an LLM-as-a-Judge. Our 539-query reasoning dataset and evaluation pipeline establish a foundation for conflict-aware, interpretable RAG systems. Experimental results demonstrate substantial gains over baselines, most notably with Qwen, where Supervised Fine-Tuning improved End-to-End answer correctness from 0.069 to 0.883 and behavioral adherence from 0.074 to 0.722.

