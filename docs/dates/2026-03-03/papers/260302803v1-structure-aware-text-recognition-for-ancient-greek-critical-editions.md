---
layout: default
title: Structure-Aware Text Recognition for Ancient Greek Critical Editions
---

# Structure-Aware Text Recognition for Ancient Greek Critical Editions
**arXiv**：[2603.02803v1](https://arxiv.org/abs/2603.02803) · [PDF](https://arxiv.org/pdf/2603.02803.pdf)  
**作者**：Nicolas Angleraud, Antonia Karamolegkou, Benoît Sagot, Thibault Clérice  

**一句话要点**：提出结构感知文本识别方法，针对古希腊评注本，评估视觉语言模型性能。

**关键词**：结构感知文本识别, 视觉语言模型, 历史文档理解, 合成数据集, 字符错误率

## 3 点简述
- 核心问题：视觉语言模型对历史学术文本复杂布局语义理解有限。
- 方法要点：引入合成语料库和真实扫描基准数据集，评估三种先进模型。
- 实验或效果：Qwen3VL-8B模型在零样本设置下达到1.0%字符错误率。

## 摘要（原文）

> Recent advances in visual language models (VLMs) have transformed end-to-end document understanding. However, their ability to interpret the complex layout semantics of historical scholarly texts remains limited. This paper investigates structure-aware text recognition for Ancient Greek critical editions, which have dense reference hierarchies and extensive marginal annotations. We introduce two novel resources: (i) a large-scale synthetic corpus of 185,000 page images generated from TEI/XML sources with controlled typographic and layout variation, and (ii) a curated benchmark of real scanned editions spanning more than a century of editorial and typographic practices. Using these datasets, we evaluate three state-of-the-art VLMs under both zero-shot and fine-tuning regimes. Our experiments reveal substantial limitations in current VLM architectures when confronted with highly structured historical documents. In zero-shot settings, most models significantly underperform compared to established off-the-shelf software. Nevertheless, the Qwen3VL-8B model achieves state-of-the-art performance, reaching a median Character Error Rate of 1.0\% on real scans. These results highlight both the current shortcomings and the future potential of VLMs for structure-aware recognition of complex scholarly documents.

