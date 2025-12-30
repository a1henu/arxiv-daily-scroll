---
layout: default
title: Lie to Me: Knowledge Graphs for Robust Hallucination Self-Detection in LLMs
---

# Lie to Me: Knowledge Graphs for Robust Hallucination Self-Detection in LLMs
**arXiv**：[2512.23547v1](https://arxiv.org/abs/2512.23547) · [PDF](https://arxiv.org/pdf/2512.23547.pdf)  
**作者**：Sahil Kale, Antonio Luca Alfeo  

**一句话要点**：提出基于知识图谱的幻觉自检测方法，以提升大语言模型输出的可靠性。

**关键词**：幻觉检测, 知识图谱, 大语言模型, 自检测方法, 模型可靠性

## 3 点简述
- 核心问题：大语言模型生成虚假陈述（幻觉）阻碍其安全部署。
- 方法要点：将模型响应转换为实体关系知识图谱，用于估计幻觉可能性。
- 实验或效果：在GPT-4o和Gemini-2.5-Flash上测试，相比现有方法准确率提升最高16%。

## 摘要（原文）

> Hallucinations, the generation of apparently convincing yet false statements, remain a major barrier to the safe deployment of LLMs. Building on the strong performance of self-detection methods, we examine the use of structured knowledge representations, namely knowledge graphs, to improve hallucination self-detection. Specifically, we propose a simple yet powerful approach that enriches hallucination self-detection by (i) converting LLM responses into knowledge graphs of entities and relations, and (ii) using these graphs to estimate the likelihood that a response contains hallucinations. We evaluate the proposed approach using two widely used LLMs, GPT-4o and Gemini-2.5-Flash, across two hallucination detection datasets. To support more reliable future benchmarking, one of these datasets has been manually curated and enhanced and is released as a secondary outcome of this work. Compared to standard self-detection methods and SelfCheckGPT, a state-of-the-art approach, our method achieves up to 16% relative improvement in accuracy and 20% in F1-score. Our results show that LLMs can better analyse atomic facts when they are structured as knowledge graphs, even when initial outputs contain inaccuracies. This low-cost, model-agnostic approach paves the way toward safer and more trustworthy language models.

