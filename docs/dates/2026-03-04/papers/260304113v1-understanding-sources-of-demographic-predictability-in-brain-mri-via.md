---
layout: default
title: Understanding Sources of Demographic Predictability in Brain MRI via Disentangling Anatomy and Contrast
---

# Understanding Sources of Demographic Predictability in Brain MRI via Disentangling Anatomy and Contrast
**arXiv**：[2603.04113v1](https://arxiv.org/abs/2603.04113) · [PDF](https://arxiv.org/pdf/2603.04113.pdf)  
**作者**：Mehmet Yigit Avci, Akshit Achara, Andrew King, Jorge Cardoso  

**一句话要点**：提出基于解耦表示学习的框架，以量化脑MRI中人口统计学信号的结构与采集来源

**关键词**：脑MRI分析, 解耦表示学习, 人口统计学预测, 偏见缓解, 解剖变异, 采集差异

## 3 点简述
- 核心问题：脑MRI中人口统计学信号（如年龄、性别、种族）的来源不明，可能源于解剖变异或采集差异，导致临床AI系统偏见难以缓解。
- 方法要点：通过解耦表示学习，将脑MRI分解为抑制采集影响的解剖表示和捕获采集特征的对比嵌入，以分离解剖与采集信号。
- 实验或效果：在三个数据集和多种MRI序列上，解剖表示保留原始图像性能，对比嵌入信号较弱且数据集特定，表明人口统计学可预测性主要源于解剖变异。

## 摘要（原文）

> Demographic attributes such as age, sex, and race can be predicted from medical images, raising concerns about bias in clinical AI systems. In brain MRI, this signal may arise from anatomical variation, acquisition-dependent contrast differences, or both, yet these sources remain entangled in conventional analyses. Without disentangling them, mitigation strategies risk failing to address the underlying causes. We propose a controlled framework based on disentangled representation learning, decomposing brain MRI into anatomy-focused representations that suppress acquisition influence and contrast embeddings that capture acquisition-dependent characteristics. Training predictive models for age, sex, and race on full images, anatomical representations, and contrast-only embeddings allows us to quantify the relative contributions of structure and acquisition to the demographic signal. Across three datasets and multiple MRI sequences, we find that demographic predictability is primarily rooted in anatomical variation: anatomy-focused representations largely preserve the performance of models trained on raw images. Contrast-only embeddings retain a weaker but systematic signal that is dataset-specific and does not generalise across sites. These findings suggest that effective mitigation must explicitly account for the distinct anatomical and acquisition-dependent origins of the demographic signal, ensuring that any bias reduction generalizes robustly across domains.

