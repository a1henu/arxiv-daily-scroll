---
layout: default
title: When are radiology reports useful for training medical image classifiers?
---

# When are radiology reports useful for training medical image classifiers?
**arXiv**：[2510.24385v1](https://arxiv.org/abs/2510.24385) · [PDF](https://arxiv.org/pdf/2510.24385.pdf)  
**作者**：Herman Bergström, Zhongqi Yue, Fredrik D. Johansson  

**一句话要点**：系统研究放射学报告在医学图像分类训练中的适用条件与方法

**关键词**：医学图像分类, 放射学报告, 预训练方法, 微调策略, 诊断任务, 预后任务

## 3 点简述
- 核心问题：放射学报告何时能提升图像分类性能，避免依赖手动标注。
- 方法要点：在预训练和微调阶段利用报告，评估诊断与预后任务。
- 实验效果：预训练对文本相关任务有益，微调在某些场景下影响更大。

## 摘要（原文）

> Medical images used to train machine learning models are often accompanied by
> radiology reports containing rich expert annotations. However, relying on these
> reports as inputs for clinical prediction requires the timely manual work of a
> trained radiologist. This raises a natural question: when can radiology reports
> be leveraged during training to improve image-only classification? Prior works
> are limited to evaluating pre-trained image representations by fine-tuning them
> to predict diagnostic labels, often extracted from reports, ignoring tasks with
> labels that are weakly associated with the text. To address this gap, we
> conduct a systematic study of how radiology reports can be used during both
> pre-training and fine-tuning, across diagnostic and prognostic tasks (e.g.,
> 12-month readmission), and under varying training set sizes. Our findings
> reveal that: (1) Leveraging reports during pre-training is beneficial for
> downstream classification tasks where the label is well-represented in the
> text; however, pre-training through explicit image-text alignment can be
> detrimental in settings where it's not; (2) Fine-tuning with reports can lead
> to significant improvements and even have a larger impact than the pre-training
> method in certain settings. These results provide actionable insights into when
> and how to leverage privileged text data to train medical image classifiers
> while highlighting gaps in current research.

