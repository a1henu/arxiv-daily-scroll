---
layout: default
title: CzechTopic: A Benchmark for Zero-Shot Topic Localization in Historical Czech Documents
---

# CzechTopic: A Benchmark for Zero-Shot Topic Localization in Historical Czech Documents
**arXiv**：[2603.03884v1](https://arxiv.org/abs/2603.03884) · [PDF](https://arxiv.org/pdf/2603.03884.pdf)  
**作者**：Martin Kostelník, Michal Hradiš, Martin Dočekal  

**一句话要点**：提出捷克历史文档零样本主题定位基准，评估大语言模型与BERT模型性能。

**关键词**：主题定位, 零样本学习, 历史文档处理, 大语言模型评估, 捷克语自然语言处理

## 3 点简述
- 核心问题：主题定位任务，识别文本中表达给定主题的跨度，基于捷克历史文档。
- 方法要点：引入人工标注基准，支持文档和词级别评估，以人类一致性为参考。
- 实验或效果：评估多种大语言模型和蒸馏微调BERT模型，性能差异大，最强模型接近人类水平。

## 摘要（原文）

> Topic localization aims to identify spans of text that express a given topic defined by a name and description. To study this task, we introduce a human-annotated benchmark based on Czech historical documents, containing human-defined topics together with manually annotated spans and supporting evaluation at both document and word levels. Evaluation is performed relative to human agreement rather than a single reference annotation. We evaluate a diverse range of large language models alongside BERT-based models fine-tuned on a distilled development dataset. Results reveal substantial variability among LLMs, with performance ranging from near-human topic detection to pronounced failures in span localization. While the strongest models approach human agreement, the distilled token embedding models remain competitive despite their smaller scale. The dataset and evaluation framework are publicly available at: https://github.com/dcgm/czechtopic.

