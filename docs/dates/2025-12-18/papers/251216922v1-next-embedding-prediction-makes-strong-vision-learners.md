---
layout: default
title: Next-Embedding Prediction Makes Strong Vision Learners
---

# Next-Embedding Prediction Makes Strong Vision Learners
**arXiv**：[2512.16922v1](https://arxiv.org/abs/2512.16922) · [PDF](https://arxiv.org/pdf/2512.16922.pdf)  
**作者**：Sihan Xu, Ziqiao Ma, Wenhao Chai, Xuweiyi Chen, Weiyang Jin, Joyce Chai, Saining Xie, Stella X. Yu  

**一句话要点**：提出Next-Embedding Predictive Autoregression以简化视觉自监督学习

**关键词**：视觉自监督学习, 生成式预训练, 嵌入预测, Transformer, 图像分类, 语义分割

## 3 点简述
- 核心问题：探索生成式预训练能否替代传统视觉自监督学习方法
- 方法要点：使用因果掩码和停止梯度训练模型预测未来补丁嵌入
- 实验或效果：在ImageNet-1K微调后ViT-B和ViT-L分别达到83.8%和85.3%准确率

## 摘要（原文）

> Inspired by the success of generative pretraining in natural language, we ask whether the same principles can yield strong self-supervised visual learners. Instead of training models to output features for downstream use, we train them to generate embeddings to perform predictive tasks directly. This work explores such a shift from learning representations to learning models. Specifically, models learn to predict future patch embeddings conditioned on past ones, using causal masking and stop gradient, which we refer to as Next-Embedding Predictive Autoregression (NEPA). We demonstrate that a simple Transformer pretrained on ImageNet-1k with next embedding prediction as its sole learning objective is effective - no pixel reconstruction, discrete tokens, contrastive loss, or task-specific heads. This formulation retains architectural simplicity and scalability, without requiring additional design complexity. NEPA achieves strong results across tasks, attaining 83.8% and 85.3% top-1 accuracy on ImageNet-1K with ViT-B and ViT-L backbones after fine-tuning, and transferring effectively to semantic segmentation on ADE20K. We believe generative pretraining from embeddings provides a simple, scalable, and potentially modality-agnostic alternative to visual self-supervised learning.

