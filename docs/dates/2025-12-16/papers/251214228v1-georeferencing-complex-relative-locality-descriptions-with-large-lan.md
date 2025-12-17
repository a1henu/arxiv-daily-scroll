---
layout: default
title: Georeferencing complex relative locality descriptions with large language models
---

# Georeferencing complex relative locality descriptions with large language models
**arXiv**：[2512.14228v1](https://arxiv.org/abs/2512.14228) · [PDF](https://arxiv.org/pdf/2512.14228.pdf)  
**作者**：Aneesha Fernando, Surangika Ranathunga, Kristin Stock, Raj Prasanna, Christopher B. Jones  

**一句话要点**：提出基于大语言模型的复杂相对位置描述地理编码方法，用于生物多样性记录自动化处理。

**关键词**：地理编码, 大语言模型, 生物多样性记录, 相对位置描述, QLoRA微调, 自动化处理

## 3 点简述
- 核心问题：生物标本记录中复杂相对位置描述难以通过传统地名或地理指示词方法准确地理编码。
- 方法要点：通过提示模式识别和QLoRA微调大语言模型，处理多区域多语言生物多样性数据集。
- 实验或效果：在固定训练数据下，平均65%记录在10公里半径内，最佳结果在纽约州达到85%在10公里内和67%在1公里内。

## 摘要（原文）

> Georeferencing text documents has typically relied on either gazetteer-based methods to assign geographic coordinates to place names, or on language modelling approaches that associate textual terms with geographic locations. However, many location descriptions specify positions relatively with spatial relationships, making geocoding based solely on place names or geo-indicative words inaccurate. This issue frequently arises in biological specimen collection records, where locations are often described through narratives rather than coordinates if they pre-date GPS. Accurate georeferencing is vital for biodiversity studies, yet the process remains labour-intensive, leading to a demand for automated georeferencing solutions. This paper explores the potential of Large Language Models (LLMs) to georeference complex locality descriptions automatically, focusing on the biodiversity collections domain. We first identified effective prompting patterns, then fine-tuned an LLM using Quantized Low-Rank Adaptation (QLoRA) on biodiversity datasets from multiple regions and languages. Our approach outperforms existing baselines with an average, across datasets, of 65% of records within a 10 km radius, for a fixed amount of training data. The best results (New York state) were 85% within 10km and 67% within 1km. The selected LLM performs well for lengthy, complex descriptions, highlighting its potential for georeferencing intricate locality descriptions.

