---
layout: default
title: WebFAQ 2.0: A Multilingual QA Dataset with Mined Hard Negatives for Dense Retrieval
---

# WebFAQ 2.0: A Multilingual QA Dataset with Mined Hard Negatives for Dense Retrieval
**arXiv**：[2602.17327v1](https://arxiv.org/abs/2602.17327) · [PDF](https://arxiv.org/pdf/2602.17327.pdf)  
**作者**：Michael Dinzinger, Laura Caspari, Ali Salman, Irvin Topi, Jelena Mitrović, Michael Granitzer  

**一句话要点**：提出WebFAQ 2.0多语言问答数据集，包含挖掘的困难负例以支持稠密检索训练

**关键词**：多语言问答数据集, 稠密检索, 困难负例挖掘, 对比学习, 知识蒸馏, 跨语言信息检索

## 3 点简述
- 核心问题：构建大规模多语言FAQ数据集，支持稠密检索模型训练，解决资源稀缺问题
- 方法要点：采用新数据收集策略直接爬取网页内容，扩展至108种语言，并挖掘困难负例
- 实验或效果：发布包含1.25M查询的困难负例数据集，支持对比学习和知识蒸馏两种微调策略

## 摘要（原文）

> We introduce WebFAQ 2.0, a new version of the WebFAQ dataset, containing 198 million FAQ-based natural question-answer pairs across 108 languages. Compared to the previous version, it significantly expands multilingual coverage and the number of bilingual aligned QA pairs to over 14.3M, making it the largest FAQ-based resource. Unlike the original release, WebFAQ 2.0 uses a novel data collection strategy that directly crawls and extracts relevant web content, resulting in a substantially more diverse and multilingual dataset with richer context through page titles and descriptions. In response to community feedback, we also release a hard negatives dataset for training dense retrievers, with 1.25M queries across 20 languages. These hard negatives were mined using a two-stage retrieval pipeline and include cross-encoder scores for 200 negatives per query. We further show how this resource enables two primary fine-tuning strategies for dense retrievers: Contrastive Learning with MultipleNegativesRanking loss, and Knowledge Distillation with MarginMSE loss. WebFAQ 2.0 is not a static resource but part of a long-term effort. Since late 2025, structured FAQs are being regularly released through the Open Web Index, enabling continuous expansion and refinement. We publish the datasets and training scripts to facilitate further research in multilingual and cross-lingual IR. The dataset itself and all related resources are publicly available on GitHub and HuggingFace.

