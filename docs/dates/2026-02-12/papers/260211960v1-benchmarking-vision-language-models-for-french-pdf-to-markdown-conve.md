---
layout: default
title: Benchmarking Vision-Language Models for French PDF-to-Markdown Conversion
---

# Benchmarking Vision-Language Models for French PDF-to-Markdown Conversion
**arXiv**：[2602.11960v1](https://arxiv.org/abs/2602.11960) · [PDF](https://arxiv.org/pdf/2602.11960.pdf)  
**作者**：Bruno Rigal, Victor Dupriez, Alexis Mignon, Ronan Le Hy, Nicolas Mery  

**一句话要点**：提出法语PDF转Markdown基准，评估视觉语言模型在复杂文档上的性能。

**关键词**：PDF转Markdown, 视觉语言模型, 法语文档解析, 基准评估, 复杂布局处理, 检索增强生成

## 3 点简述
- 核心问题：现有基准多关注英语或中文，对法语文档转换的评估不足，易因格式差异误判模型性能。
- 方法要点：基于模型分歧采样构建法语困难页面基准，包含手写表单和复杂布局，采用单元测试和类别归一化评估。
- 实验或效果：评估15个模型，专有模型在手写和表单上更稳健，开源模型在标准印刷布局上保持竞争力。

## 摘要（原文）

> This report evaluates PDF-to-Markdown conversion using recent Vision-Language Models (VLMs) on challenging French documents. Document parsing is a critical step for Retrieval-Augmented Generation (RAG) pipelines, where transcription and layout errors propagate to downstream retrieval and grounding. Existing benchmarks often emphasize English or Chinese and can over-penalize benign formatting and linearization choices (e.g., line breaks, list segmentation, alternative table renderings) that are largely irrelevant for downstream use.
>   We introduce a French-focused benchmark of difficult pages selected via model-disagreement sampling from a corpus of 60{,}000 documents, covering handwritten forms, complex layouts, dense tables, and graphics-rich pages. Evaluation is performed with unit-test-style checks that target concrete failure modes (text presence, reading order, and local table constraints) combined with category-specific normalization designed to discount presentation-only variance. Across 15 models, we observe substantially higher robustness for the strongest proprietary models on handwriting and forms, while several open-weights systems remain competitive on standard printed layouts.

