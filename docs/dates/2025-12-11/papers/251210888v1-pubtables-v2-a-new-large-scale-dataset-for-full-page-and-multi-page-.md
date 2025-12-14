---
layout: default
title: PubTables-v2: A new large-scale dataset for full-page and multi-page table extraction
---

# PubTables-v2: A new large-scale dataset for full-page and multi-page table extraction
**arXiv**：[2512.10888v1](https://arxiv.org/abs/2512.10888) · [PDF](https://arxiv.org/pdf/2512.10888.pdf)  
**作者**：Brandon Smock, Valerie Faucon-Morin, Max Sokolov, Libin Liang, Tayyibah Khanam, Maury Courtland  

**一句话要点**：提出PubTables-v2数据集以解决视觉文档理解中表格提取的数据缺乏问题

**关键词**：表格提取, 视觉文档理解, 多页表格识别, 数据集构建, 视觉语言模型

## 3 点简述
- 核心问题：表格提取缺乏大规模标注数据，阻碍全页和多页表格提取方法的发展
- 方法要点：创建PubTables-v2数据集，支持全页和多页表格结构识别等挑战性任务
- 实验或效果：评估视觉语言模型，并基于数据集开发Page-Object Table Transformer扩展方法

## 摘要（原文）

> Table extraction (TE) is a key challenge in visual document understanding. Traditional approaches detect tables first, then recognize their structure. Recently, interest has surged in developing methods, such as vision-language models (VLMs), that can extract tables directly in their full page or document context. However, progress has been difficult to demonstrate due to a lack of annotated data. To address this, we create a new large-scale dataset, PubTables-v2. PubTables-v2 supports a number of current challenging table extraction tasks. Notably, it is the first large-scale benchmark for multi-page table structure recognition. We demonstrate its usefulness by evaluating domain-specialized VLMs on these tasks and highlighting current progress. Finally, we use PubTables-v2 to create the Page-Object Table Transformer (POTATR), an image-to-graph extension of the Table Transformer to comprehensive page-level TE. Data, code, and trained models will be released.

