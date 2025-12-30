---
layout: default
title: RxnBench: A Multimodal Benchmark for Evaluating Large Language Models on Chemical Reaction Understanding from Scientific Literature
---

# RxnBench: A Multimodal Benchmark for Evaluating Large Language Models on Chemical Reaction Understanding from Scientific Literature
**arXiv**：[2512.23565v1](https://arxiv.org/abs/2512.23565) · [PDF](https://arxiv.org/pdf/2512.23565.pdf)  
**作者**：Hanzheng Li, Xi Fang, Yixuan Li, Chaozheng Huang, Junjie Wang, Xi Wang, Hongzhe Bai, Bojun Hao, Shenyu Lin, Huiqi Liang, Linfeng Zhang, Guolin Ke  

**一句话要点**：提出RxnBench基准以评估多模态大语言模型在科学文献中化学反应理解的能力

**关键词**：多模态大语言模型, 化学反应理解, 科学文献基准, 视觉感知, 跨模态整合, 推理引擎

## 3 点简述
- 核心问题：多模态大语言模型在理解科学文献中密集图形化化学反应方面存在能力不足
- 方法要点：构建包含单图问答和全文档问答的多层次基准，测试视觉感知和跨模态整合
- 实验或效果：模型在文本提取上表现良好，但在深层化学逻辑和结构识别上表现不佳，推理时模型优于标准架构

## 摘要（原文）

> The integration of Multimodal Large Language Models (MLLMs) into chemistry promises to revolutionize scientific discovery, yet their ability to comprehend the dense, graphical language of reactions within authentic literature remains underexplored. Here, we introduce RxnBench, a multi-tiered benchmark designed to rigorously evaluate MLLMs on chemical reaction understanding from scientific PDFs. RxnBench comprises two tasks: Single-Figure QA (SF-QA), which tests fine-grained visual perception and mechanistic reasoning using 1,525 questions derived from 305 curated reaction schemes, and Full-Document QA (FD-QA), which challenges models to synthesize information from 108 articles, requiring cross-modal integration of text, schemes, and tables. Our evaluation of MLLMs reveals a critical capability gap: while models excel at extracting explicit text, they struggle with deep chemical logic and precise structural recognition. Notably, models with inference-time reasoning significantly outperform standard architectures, yet none achieve 50\% accuracy on FD-QA. These findings underscore the urgent need for domain-specific visual encoders and stronger reasoning engines to advance autonomous AI chemists.

