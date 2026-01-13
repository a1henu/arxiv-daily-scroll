---
layout: default
title: Kinship Data Benchmark for Multi-hop Reasoning
---

# Kinship Data Benchmark for Multi-hop Reasoning
**arXiv**：[2601.07794v1](https://arxiv.org/abs/2601.07794) · [PDF](https://arxiv.org/pdf/2601.07794.pdf)  
**作者**：Tianda Sun, Dimitar Kazakov  

**一句话要点**：提出KinshipQA基准以评估大语言模型在亲属关系多跳推理中的能力

**关键词**：多跳推理, 亲属关系基准, 家谱数据生成, 文化特异性, 大语言模型评估

## 3 点简述
- 核心问题：评估大语言模型的多跳推理能力，即整合多信息进行连贯推断
- 方法要点：开发生成管道，大规模生成文化特异性家谱数据，支持系统控制任务难度
- 实验或效果：在零样本协议下评估六种先进模型，揭示模型和文化设置间的系统性差异

## 摘要（原文）

> Large language models (LLMs) are increasingly evaluated on their ability to perform multi-hop reasoning, i.e., to combine multiple pieces of information into a coherent inference. We introduce KinshipQA, a benchmark designed to probe this capability through reasoning over kinship relations. The central contribution of our work is a generative pipeline that produces, on demand, large-scale, realistic, and culture-specific genealogical data: collections of interconnected family trees that satisfy explicit marriage constraints associated with different kinship systems. This allows task difficulty, cultural assumptions, and relational depth to be systematically controlled and varied. From these genealogies, we derive textual inference tasks that require reasoning over implicit relational chains. We evaluate the resulting benchmark using six state-of-the-art LLMs, spanning both open-source and closed-source models, under a uniform zero-shot protocol with deterministic decoding. Performance is measured using exact-match and set-based metrics. Our results demonstrate that KinshipQA yields a wide spread of outcomes and exposes systematic differences in multi-hop reasoning across models and cultural settings.

