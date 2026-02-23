---
layout: default
title: DohaScript: A Large-Scale Multi-Writer Dataset for Continuous Handwritten Hindi Text
---

# DohaScript: A Large-Scale Multi-Writer Dataset for Continuous Handwritten Hindi Text
**arXiv**：[2602.18089v1](https://arxiv.org/abs/2602.18089) · [PDF](https://arxiv.org/pdf/2602.18089.pdf)  
**作者**：Kunwar Arpit Singh, Ankush Prakash, Haroon R Lone  

**一句话要点**：提出DohaScript数据集以解决连续手写印地语文本基准数据稀缺问题

**关键词**：手写印地语文本, 多作者数据集, 连续手写识别, 作者识别, 风格分析, 低资源脚本

## 3 点简述
- 核心问题：现有手写天城体数据集规模小，缺乏连续文本和多样作者，限制数据驱动分析。
- 方法要点：收集531位作者手写相同六首传统对句，构建平行风格语料库，支持系统分析。
- 实验或效果：基线实验显示质量分离和强泛化能力，验证数据集可靠性和实用价值。

## 摘要（原文）

> Despite having hundreds of millions of speakers, handwritten Devanagari text remains severely underrepresented in publicly available benchmark datasets. Existing resources are limited in scale, focus primarily on isolated characters or short words, and lack controlled lexical content and writer level diversity, which restricts their utility for modern data driven handwriting analysis. As a result, they fail to capture the continuous, fused, and structurally complex nature of Devanagari handwriting, where characters are connected through a shared shirorekha (horizontal headline) and exhibit rich ligature formations. We introduce DohaScript, a large scale, multi writer dataset of handwritten Hindi text collected from 531 unique contributors. The dataset is designed as a parallel stylistic corpus, in which all writers transcribe the same fixed set of six traditional Hindi dohas (couplets). This controlled design enables systematic analysis of writer specific variation independent of linguistic content, and supports tasks such as handwriting recognition, writer identification, style analysis, and generative modeling. The dataset is accompanied by non identifiable demographic metadata, rigorous quality curation based on objective sharpness and resolution criteria, and page level layout difficulty annotations that facilitate stratified benchmarking. Baseline experiments demonstrate clear quality separation and strong generalization to unseen writers, highlighting the dataset's reliability and practical value. DohaScript is intended to serve as a standardized and reproducible benchmark for advancing research on continuous handwritten Devanagari text in low resource script settings.

