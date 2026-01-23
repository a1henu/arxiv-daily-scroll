---
layout: default
title: RadJEPA: Radiology Encoder for Chest X-Rays via Joint Embedding Predictive Architecture
---

# RadJEPA: Radiology Encoder for Chest X-Rays via Joint Embedding Predictive Architecture
**arXiv**：[2601.15891v1](https://arxiv.org/abs/2601.15891) · [PDF](https://arxiv.org/pdf/2601.15891.pdf)  
**作者**：Anas Anwarul Haq Khan, Mariam Husain, Kshitij Jadhav  

**一句话要点**：提出RadJEPA自监督框架，无需语言监督学习胸片X光图像编码器。

**关键词**：自监督学习, 医学图像编码, 联合嵌入预测, 胸片X光, 潜在表示预测

## 3 点简述
- 核心问题：医学视觉语言模型依赖配对图像文本数据，限制鲁棒性。
- 方法要点：基于联合嵌入预测架构，通过预测掩码区域潜在表示进行自监督学习。
- 实验或效果：在疾病分类、语义分割和报告生成任务中超越现有方法。

## 摘要（原文）

> Recent advances in medical vision language models guide the learning of visual representations; however, this form of supervision is constrained by the availability of paired image text data, raising the question of whether robust radiology encoders can be learned without relying on language supervision. In this work, we introduce RadJEPA, a self-supervised framework built on a Joint Embedding Predictive Architecture that learns without language supervision. Pre-trained solely on unlabeled chest X-ray images, the model learns to predict latent representations of masked image regions. This predictive objective differs fundamentally from both image text pre-training and DINO-style self-distillation: rather than aligning global representations across views or modalities, RadJEPA explicitly models latent-space prediction. We evaluate the learned encoder on disease classification, semantic segmentation, and report generation tasks. Across benchmarks, RadJEPA achieves performance exceeding state-of-the-art approaches, including Rad-DINO.

