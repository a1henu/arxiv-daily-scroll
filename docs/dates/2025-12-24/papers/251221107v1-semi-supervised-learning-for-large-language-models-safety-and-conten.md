---
layout: default
title: Semi-Supervised Learning for Large Language Models Safety and Content Moderation
---

# Semi-Supervised Learning for Large Language Models Safety and Content Moderation
**arXiv**：[2512.21107v1](https://arxiv.org/abs/2512.21107) · [PDF](https://arxiv.org/pdf/2512.21107.pdf)  
**作者**：Eduard Stefan Dinuta, Iustin Sirbu, Traian Rebedea  

**一句话要点**：提出半监督学习方法以提升大语言模型安全分类器性能

**关键词**：半监督学习, 大语言模型安全, 内容审核, 数据增强, 安全分类器

## 3 点简述
- 核心问题：安全分类器训练依赖大量标注数据，获取困难且易出错。
- 方法要点：利用半监督学习结合标注与未标注数据，并采用任务特定数据增强。
- 实验或效果：任务特定增强显著优于通用增强，提升提示与响应的安全分类性能。

## 摘要（原文）

> Safety for Large Language Models (LLMs) has been an ongoing research focus since their emergence and is even more relevant nowadays with the increasing capacity of those models. Currently, there are several guardrails in place for all public LLMs and multiple proposed datasets for training safety classifiers. However, training these safety classifiers relies on large quantities of labeled data, which can be problematic to acquire, prone to labeling errors, or often include synthetic data. To address these issues, we suggest a different approach: utilizing semi-supervised learning techniques, which leverage both labeled and unlabeled data, to improve the performance on the safety task. We analyze the improvements that these techniques can offer for both prompts given to Large Language Models and the responses to those requests. Moreover, since augmentation is the central part of semi-supervised algorithms, we demonstrate the importance of using task-specific augmentations, which significantly increase the performance when compared to general-purpose augmentation techniques.

