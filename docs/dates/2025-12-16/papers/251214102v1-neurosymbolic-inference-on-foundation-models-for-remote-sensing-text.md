---
layout: default
title: Neurosymbolic Inference On Foundation Models For Remote Sensing Text-to-image Retrieval With Complex Queries
---

# Neurosymbolic Inference On Foundation Models For Remote Sensing Text-to-image Retrieval With Complex Queries
**arXiv**：[2512.14102v1](https://arxiv.org/abs/2512.14102) · [PDF](https://arxiv.org/pdf/2512.14102.pdf)  
**作者**：Emanuele Mezzi, Gertjan Burghouts, Maarten Kruithof  

**一句话要点**：提出RUNE方法，结合LLM与神经符号AI，通过显式推理解决遥感文本到图像检索中复杂查询的挑战。

**关键词**：遥感图像检索, 神经符号AI, 一阶逻辑推理, 大型语言模型, 复杂查询处理, 可解释性增强

## 3 点简述
- 核心问题：遥感文本到图像检索中，现有模型解释性差且难以处理复杂空间关系。
- 方法要点：利用LLM将文本查询转换为一阶逻辑表达式，通过神经符号推理模块进行显式推理。
- 实验或效果：在DOTA数据集上评估，RUNE在复杂检索任务中优于现有RS-LVLMs，并引入新指标评估鲁棒性。

## 摘要（原文）

> Text-to-image retrieval in remote sensing (RS) has advanced rapidly with the rise of large vision-language models (LVLMs) tailored for aerial and satellite imagery, culminating in remote sensing large vision-language models (RS-LVLMS). However, limited explainability and poor handling of complex spatial relations remain key challenges for real-world use. To address these issues, we introduce RUNE (Reasoning Using Neurosymbolic Entities), an approach that combines Large Language Models (LLMs) with neurosymbolic AI to retrieve images by reasoning over the compatibility between detected entities and First-Order Logic (FOL) expressions derived from text queries. Unlike RS-LVLMs that rely on implicit joint embeddings, RUNE performs explicit reasoning, enhancing performance and interpretability. For scalability, we propose a logic decomposition strategy that operates on conditioned subsets of detected entities, guaranteeing shorter execution time compared to neural approaches. Rather than using foundation models for end-to-end retrieval, we leverage them only to generate FOL expressions, delegating reasoning to a neurosymbolic inference module. For evaluation we repurpose the DOTA dataset, originally designed for object detection, by augmenting it with more complex queries than in existing benchmarks. We show the LLM's effectiveness in text-to-logic translation and compare RUNE with state-of-the-art RS-LVLMs, demonstrating superior performance. We introduce two metrics, Retrieval Robustness to Query Complexity (RRQC) and Retrieval Robustness to Image Uncertainty (RRIU), which evaluate performance relative to query complexity and image uncertainty. RUNE outperforms joint-embedding models in complex RS retrieval tasks, offering gains in performance, robustness, and explainability. We show RUNE's potential for real-world RS applications through a use case on post-flood satellite image retrieval.

