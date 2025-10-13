---
layout: default
title: Utilizing dynamic sparsity on pretrained DETR
---

# Utilizing dynamic sparsity on pretrained DETR
**arXiv**：[2510.09380v1](https://arxiv.org/abs/2510.09380) · [PDF](https://arxiv.org/pdf/2510.09380.pdf)  
**作者**：Reza Sedghi, Anand Subramoney, David Kappel  
**一句话要点**：提出动态稀疏化方法以提升预训练DETR在目标检测中的推理效率
**关键词**：动态稀疏化, DETR模型, 目标检测, 推理效率, 预训练模型, COCO数据集

## 3 点简述
- 核心问题：Transformer模型在视觉任务中推理效率低，尤其DETR的MLP层存在固有稀疏性。
- 方法要点：引入SIBS和MGS方法，利用固定或动态预测实现激活稀疏化，无需重新训练模型。
- 实验或效果：在COCO数据集上，MGS实现85-95%稀疏度，保持或提升性能并显著减少计算。

## 摘要（原文）

> Efficient inference with transformer-based models remains a challenge,
> especially in vision tasks like object detection. We analyze the inherent
> sparsity in the MLP layers of DETR and introduce two methods to exploit it
> without retraining. First, we propose Static Indicator-Based Sparsification
> (SIBS), a heuristic method that predicts neuron inactivity based on fixed
> activation patterns. While simple, SIBS offers limited gains due to the
> input-dependent nature of sparsity. To address this, we introduce Micro-Gated
> Sparsification (MGS), a lightweight gating mechanism trained on top of a
> pretrained DETR. MGS predicts dynamic sparsity using a small linear layer and
> achieves up to 85 to 95% activation sparsity. Experiments on the COCO dataset
> show that MGS maintains or even improves performance while significantly
> reducing computation. Our method offers a practical, input-adaptive approach to
> sparsification, enabling efficient deployment of pretrained vision transformers
> without full model retraining.

