---
layout: default
title: Structured Prototype-Guided Adaptation for EEG Foundation Models
---

# Structured Prototype-Guided Adaptation for EEG Foundation Models
**arXiv**：[2602.17251v1](https://arxiv.org/abs/2602.17251) · [PDF](https://arxiv.org/pdf/2602.17251.pdf)  
**作者**：Jingying Ma, Feng Wu, Yucheng Xing, Qika Lin, Tianyu Liu, Chenyu Liu, Ziyu Jia, Mengling Feng  

**一句话要点**：提出SCOPE框架以解决脑电图基础模型在标签有限跨被试场景下的泛化问题

**关键词**：脑电图基础模型, 结构化适应, 原型引导, 标签有限学习, 跨被试泛化, 轻量适配器

## 3 点简述
- 核心问题：脑电图基础模型在监督有限时泛化差，源于噪声监督与模型参数空间的结构不匹配
- 方法要点：SCOPE通过几何正则化任务先验构建原型，并利用轻量适配器ProAdapter进行结构化适应
- 实验或效果：在三个脑电图任务和五个基础模型上验证，SCOPE在标签有限跨被试设置下表现优异且高效

## 摘要（原文）

> Electroencephalography (EEG) foundation models (EFMs) have achieved strong performance under full fine-tuning but exhibit poor generalization when subject-level supervision is limited, a common constraint in real-world clinical settings. We show that this failure stems not merely from limited supervision, but from a structural mismatch between noisy, limited supervision and the highly plastic parameter space of EFMs. To address this challenge, we propose SCOPE, a Structured COnfidence-aware Prototype-guided adaptation framework for EFM fine-tuning. SCOPE follows a two-stage pipeline. In the first stage, we construct reliable external supervision by learning geometry-regularized task priors, constructing balanced class-level prototypes over the resulting embeddings, and producing confidence-aware pseudo-labels from their agreement to filter unreliable signals on unlabeled data. In the second stage, we introduce ProAdapter, which adapts frozen EEG foundation models via a lightweight adapter conditioned on the structured prototypes. Experiments across three EEG tasks and five foundation model backbones demonstrate that SCOPE consistently achieves strong performance and efficiency under label-limited cross-subject settings.

