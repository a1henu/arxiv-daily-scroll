---
layout: default
title: Beyond Learning on Molecules by Weakly Supervising on Molecules
---

# Beyond Learning on Molecules by Weakly Supervising on Molecules
**arXiv**：[2602.04696v1](https://arxiv.org/abs/2602.04696) · [PDF](https://arxiv.org/pdf/2602.04696.pdf)  
**作者**：Gordan Prastalo, Kevin Maik Jablonka  

**一句话要点**：提出ACE-Mol模型，通过弱监督分子基序实现任务自适应分子表示学习

**关键词**：分子表示学习, 弱监督学习, 任务自适应, 分子基序, 化学信息学

## 3 点简述
- 核心问题：预训练分子编码器缺乏任务依赖性，现有任务条件方法依赖昂贵标注数据
- 方法要点：利用程序化生成的分子基序与自然语言描述进行弱监督，实现廉价可扩展的任务对齐
- 实验或效果：在分子性质预测基准上达到最先进性能，提供可解释的化学意义表示

## 摘要（原文）

> Molecular representations are inherently task-dependent, yet most pre-trained molecular encoders are not. Task conditioning promises representations that reorganize based on task descriptions, but existing approaches rely on expensive labeled data. We show that weak supervision on programmatically derived molecular motifs is sufficient. Our Adaptive Chemical Embedding Model (ACE-Mol) learns from hundreds of motifs paired with natural language descriptors that are cheap to compute, trivial to scale. Conventional encoders slowly search the embedding space for task-relevant structure, whereas ACE-Mol immediately aligns its representations with the task. ACE-Mol achieves state-of-the-art performance across molecular property prediction benchmarks with interpretable, chemically meaningful representations.

