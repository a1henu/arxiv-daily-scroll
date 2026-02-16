---
layout: default
title: GRAIL: Geometry-Aware Retrieval-Augmented Inference with LLMs over Hyperbolic Representations of Patient Trajectories
---

# GRAIL: Geometry-Aware Retrieval-Augmented Inference with LLMs over Hyperbolic Representations of Patient Trajectories
**arXiv**：[2602.12828v1](https://arxiv.org/abs/2602.12828) · [PDF](https://arxiv.org/pdf/2602.12828.pdf)  
**作者**：Zhan Qu, Michael Färber  

**一句话要点**：提出GRAIL框架，通过双曲空间嵌入和结构感知检索，改进基于电子健康记录的下次就诊事件预测。

**关键词**：电子健康记录预测, 双曲空间嵌入, 结构感知检索, 大语言模型重排序, 下次就诊事件预测

## 3 点简述
- 核心问题：电子健康记录稀疏、多类型且具层次性，大语言模型在长结构化历史推理中易产生幻觉。
- 方法要点：构建统一临床图，嵌入双曲空间，利用结构感知检索获取临床合理未来事件。
- 实验或效果：在MIMIC-IV上验证，提升多类型预测准确性和层次一致性。

## 摘要（原文）

> Predicting future clinical events from longitudinal electronic health records (EHRs) is challenging due to sparse multi-type clinical events, hierarchical medical vocabularies, and the tendency of large language models (LLMs) to hallucinate when reasoning over long structured histories. We study next-visit event prediction, which aims to forecast a patient's upcoming clinical events based on prior visits. We propose GRAIL, a framework that models longitudinal EHRs using structured geometric representations and structure-aware retrieval. GRAIL constructs a unified clinical graph by combining deterministic coding-system hierarchies with data-driven temporal associations across event types, embeds this graph in hyperbolic space, and summarizes each visit as a probabilistic Central Event that denoises sparse observations. At inference time, GRAIL retrieves a structured set of clinically plausible future events aligned with hierarchical and temporal progression, and optionally refines their ranking using an LLM as a constrained inference-time reranker. Experiments on MIMIC-IV show that GRAIL consistently improves multi-type next-visit prediction and yields more hierarchy-consistent forecasts.

