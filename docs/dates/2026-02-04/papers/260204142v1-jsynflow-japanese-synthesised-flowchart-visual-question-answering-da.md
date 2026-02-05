---
layout: default
title: JSynFlow: Japanese Synthesised Flowchart Visual Question Answering Dataset built with Large Language Models
---

# JSynFlow: Japanese Synthesised Flowchart Visual Question Answering Dataset built with Large Language Models
**arXiv**：[2602.04142v1](https://arxiv.org/abs/2602.04142) · [PDF](https://arxiv.org/pdf/2602.04142.pdf)  
**作者**：Hiroshi Sasaki  

**一句话要点**：提出JSynFlow数据集，利用大语言模型合成日本流程图视觉问答数据以解决数据集构建耗时问题。

**关键词**：流程图视觉问答, 数据集合成, 大语言模型, 视觉语言模型, 日本文档分析

## 3 点简述
- 核心问题：视觉语言模型需大规模流程图图像与文本数据，但人工构建耗时。
- 方法要点：使用大语言模型合成日本流程图视觉问答数据集，包括任务描述、流程图图像和问答对。
- 实验或效果：微调后显著提升视觉语言模型在流程图问答任务上的性能。

## 摘要（原文）

> Vision and language models (VLMs) are expected to analyse complex documents, such as those containing flowcharts, through a question-answering (QA) interface. The ability to recognise and interpret these flowcharts is in high demand, as they provide valuable insights unavailable in text-only explanations. However, developing VLMs with precise flowchart understanding requires large-scale datasets of flowchart images and corresponding text, the creation of which is highly time-consuming. To address this challenge, we introduce JSynFlow, a synthesised visual QA dataset for Japanese flowcharts, generated using large language models (LLMs). Our dataset comprises task descriptions for various business occupations, the corresponding flowchart images rendered from domain-specific language (DSL) code, and related QA pairs. This paper details the dataset's synthesis procedure and demonstrates that fine-tuning with JSynFlow significantly improves VLM performance on flowchart-based QA tasks. Our dataset is publicly available at https://huggingface.co/datasets/jri-advtechlab/jsynflow.

