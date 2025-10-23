---
layout: default
title: olmOCR 2: Unit Test Rewards for Document OCR
---

# olmOCR 2: Unit Test Rewards for Document OCR
**arXiv**：[2510.19817v1](https://arxiv.org/abs/2510.19817) · [PDF](https://arxiv.org/pdf/2510.19817.pdf)  
**作者**：Jake Poznanski, Luca Soldaini, Kyle Lo  

**一句话要点**：提出olmOCR 2 OCR系统，使用单元测试奖励训练VLM以提升文档转换质量

**关键词**：文档OCR, 强化学习, 单元测试, 视觉语言模型, 合成数据生成, 布局解析

## 3 点简述
- 核心问题：文档OCR需将PDF等转换为有序纯文本，但复杂布局如数学公式和表格处理困难
- 方法要点：采用强化学习与可验证奖励，基于合成文档生成多样单元测试进行训练
- 实验或效果：在olmOCR-Bench基准上实现SOTA，数学公式、表格和多列布局转换改进显著

## 摘要（原文）

> We present olmOCR 2, the latest in our family of powerful OCR systems for
> converting digitized print documents, like PDFs, into clean, naturally ordered
> plain text. olmOCR 2 is powered by olmOCR-2-7B-1025, a specialized, 7B vision
> language model (VLM) trained using reinforcement learning with verifiable
> rewards (RLVR), where our rewards are a diverse set of binary unit tests. To
> scale unit test creation, we develop a pipeline for generating synthetic
> documents with diverse and challenging layouts, known ground-truth HTML source
> code, and extracted test cases. We show that RL training on these test cases
> results in state-of-the-art performance on olmOCR-Bench, our English-language
> OCR benchmark, with the largest improvements in math formula conversion, table
> parsing, and multi-column layouts compared to previous versions. We release our
> model, data and code under permissive open licenses.

