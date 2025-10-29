---
layout: default
title: Beyond Objects: Contextual Synthetic Data Generation for Fine-Grained Classification
---

# Beyond Objects: Contextual Synthetic Data Generation for Fine-Grained Classification
**arXiv**：[2510.24078v1](https://arxiv.org/abs/2510.24078) · [PDF](https://arxiv.org/pdf/2510.24078.pdf)  
**作者**：William Yang, Xindi Wu, Zhiwei Deng, Esin Tureci, Olga Russakovsky  

**一句话要点**：提出BOB方法以解决细粒度分类中合成数据过拟合与多样性不足问题

**关键词**：细粒度分类, 合成数据生成, 文本到图像模型, 低样本学习, 条件生成

## 3 点简述
- 核心问题：文本到图像模型生成合成数据时易过拟合且多样性降低
- 方法要点：提取类无关属性并条件化微调，生成时边缘化以保留先验
- 实验效果：在多个数据集上实现SOTA，提升分类准确率并减少真实数据需求

## 摘要（原文）

> Text-to-image (T2I) models are increasingly used for synthetic dataset
> generation, but generating effective synthetic training data for classification
> remains challenging. Fine-tuning a T2I model with a few real examples can help
> improve the quality of synthetic training data; however, it may also cause
> overfitting and reduce diversity in the generated samples. We propose a
> fine-tuning strategy BOB (BeyondOBjects) to mitigate these concerns for
> fine-grained classification. Given a small set of real examples, we first
> extract class-agnostic attributes such as scene background and object pose. We
> then explicitly condition on these attributes during fine-tuning of the T2I
> model and marginalize them out during generation. This design mitigates
> overfitting, preserves the T2I model's generative prior, reduces estimation
> errors, and further minimizes unintended inter-class associations. Extensive
> experiments across multiple T2I models, backbones, and datasets show that our
> method achieves state-of-the-art performance in low-shot fine-grained
> classification when augmented with synthetic data. Concretely, BOB outperforms
> DataDream by 7.4% on the Aircraft dataset (from 50.0% to 57.4% when fine-tuning
> a CLIP classifier with five real images augmented with 100 synthetic images).
> In three of the four benchmarks, fine-tuning downstream models with 5 real
> images augmented with BOB achieves better performance than fine-tuning with 10
> real images. Collectively, BOB outperforms prior art in 18 of 24 experimental
> settings, with 2+% accuracy improvements in 14 of these settings.

