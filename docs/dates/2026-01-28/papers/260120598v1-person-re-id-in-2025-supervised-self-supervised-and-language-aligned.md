---
layout: default
title: Person Re-ID in 2025: Supervised, Self-Supervised, and Language-Aligned. What Works?
---

# Person Re-ID in 2025: Supervised, Self-Supervised, and Language-Aligned. What Works?
**arXiv**：[2601.20598v1](https://arxiv.org/abs/2601.20598) · [PDF](https://arxiv.org/pdf/2601.20598.pdf)  
**作者**：Lakshman Balasubramanian  

**一句话要点**：比较监督、自监督和语言对齐模型在行人重识别中的跨域性能

**关键词**：行人重识别, 跨域泛化, 监督学习, 自监督学习, 语言对齐模型, 基础模型

## 3 点简述
- 核心问题：评估行人重识别模型在跨域场景下的泛化能力
- 方法要点：分析11个模型在9个数据集上的表现，比较三种训练范式
- 实验或效果：语言对齐模型在跨域任务中表现出意外鲁棒性

## 摘要（原文）

> Person Re-Identification (ReID) remains a challenging problem in computer vision. This work reviews various training paradigm and evaluates the robustness of state-of-the-art ReID models in cross-domain applications and examines the role of foundation models in improving generalization through richer, more transferable visual representations. We compare three training paradigms, supervised, self-supervised, and language-aligned models. Through the study the aim is to answer the following questions: Can supervised models generalize in cross-domain scenarios? How does foundation models like SigLIP2 perform for the ReID tasks? What are the weaknesses of current supervised and foundational models for ReID? We have conducted the analysis across 11 models and 9 datasets. Our results show a clear split: supervised models dominate their training domain but crumble on cross-domain data. Language-aligned models, however, show surprising robustness cross-domain for ReID tasks, even though they are not explicitly trained to do so. Code and data available at: https://github.com/moiiai-tech/object-reid-benchmark.

