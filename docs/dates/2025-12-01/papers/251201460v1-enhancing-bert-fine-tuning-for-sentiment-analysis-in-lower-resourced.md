---
layout: default
title: Enhancing BERT Fine-Tuning for Sentiment Analysis in Lower-Resourced Languages
---

# Enhancing BERT Fine-Tuning for Sentiment Analysis in Lower-Resourced Languages
**arXiv**：[2512.01460v1](https://arxiv.org/abs/2512.01460) · [PDF](https://arxiv.org/pdf/2512.01460.pdf)  
**作者**：Jozef Kubík, Marek Šuppa, Martin Takáč  

**一句话要点**：提出结合主动学习与聚类的微调管道，以提升低资源语言情感分析性能并减少标注成本。

**关键词**：低资源语言处理, 主动学习, 数据聚类, 微调优化, 情感分析, 标注效率

## 3 点简述
- 核心问题：低资源语言数据有限导致语言模型微调效果不佳，需在有限数据下优化性能。
- 方法要点：集成主动学习、数据聚类和动态选择调度器，构建系统化微调流程以高效利用标注数据。
- 实验或效果：在斯洛伐克语等语言上测试，实现高达30%的标注节省和最多4个F1分数的性能提升，同时增强微调稳定性。

## 摘要（原文）

> Limited data for low-resource languages typically yield weaker language models (LMs). Since pre-training is compute-intensive, it is more pragmatic to target improvements during fine-tuning. In this work, we examine the use of Active Learning (AL) methods augmented by structured data selection strategies which we term 'Active Learning schedulers', to boost the fine-tuning process with a limited amount of training data. We connect the AL to data clustering and propose an integrated fine-tuning pipeline that systematically combines AL, clustering, and dynamic data selection schedulers to enhance model's performance. Experiments in the Slovak, Maltese, Icelandic and Turkish languages show that the use of clustering during the fine-tuning phase together with AL scheduling can simultaneously produce annotation savings up to 30% and performance improvements up to four F1 score points, while also providing better fine-tuning stability.

