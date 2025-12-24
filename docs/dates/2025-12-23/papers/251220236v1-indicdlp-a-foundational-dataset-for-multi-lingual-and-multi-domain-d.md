---
layout: default
title: IndicDLP: A Foundational Dataset for Multi-Lingual and Multi-Domain Document Layout Parsing
---

# IndicDLP: A Foundational Dataset for Multi-Lingual and Multi-Domain Document Layout Parsing
**arXiv**：[2512.20236v1](https://arxiv.org/abs/2512.20236) · [PDF](https://arxiv.org/pdf/2512.20236.pdf)  
**作者**：Oikantik Nath, Sahithi Kukkala, Mitesh Khapra, Ravi Kiran Sarvadevabhatla  

**一句话要点**：提出IndicDLP数据集以解决多语言多领域文档布局分析中规模、多样性和标注粒度不足的问题。

**关键词**：文档布局分析, 多语言数据集, 印度语言文档, 细粒度标注, 领域多样性, 文档数字化

## 3 点简述
- 核心问题：现有数据集在细粒度标签、多语言覆盖和领域多样性方面存在不足，尤其缺乏对印度语言文档的支持。
- 方法要点：构建包含11种印度语言和英语、12个文档领域的大规模数据集IndicDLP，并整理UED-mini用于预训练。
- 实验或效果：在IndicDLP上微调现有模型显著提升性能，且模型能泛化到非印度文档布局，验证数据集有效性。

## 摘要（原文）

> Document layout analysis is essential for downstream tasks such as information retrieval, extraction, OCR, and digitization. However, existing large-scale datasets like PubLayNet and DocBank lack fine-grained region labels and multilingual diversity, making them insufficient for representing complex document layouts. In contrast, human-annotated datasets such as M6Doc and D4LA offer richer labels and greater domain diversity, but are too small to train robust models and lack adequate multilingual coverage. This gap is especially pronounced for Indic documents, which encompass diverse scripts yet remain underrepresented in current datasets, further limiting progress in this space. To address these shortcomings, we introduce IndicDLP, a large-scale foundational document layout dataset spanning 11 representative Indic languages alongside English and 12 common document domains. Additionally, we curate UED-mini, a dataset derived from DocLayNet and M6Doc, to enhance pretraining and provide a solid foundation for Indic layout models. Our experiments demonstrate that fine-tuning existing English models on IndicDLP significantly boosts performance, validating its effectiveness. Moreover, models trained on IndicDLP generalize well beyond Indic layouts, making it a valuable resource for document digitization. This work bridges gaps in scale, diversity, and annotation granularity, driving inclusive and efficient document understanding.

