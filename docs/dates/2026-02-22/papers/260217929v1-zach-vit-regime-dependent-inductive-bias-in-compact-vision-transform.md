---
layout: default
title: ZACH-ViT: Regime-Dependent Inductive Bias in Compact Vision Transformers for Medical Imaging
---

# ZACH-ViT: Regime-Dependent Inductive Bias in Compact Vision Transformers for Medical Imaging
**arXiv**：[2602.17929v1](https://arxiv.org/abs/2602.17929) · [PDF](https://arxiv.org/pdf/2602.17929.pdf)  
**作者**：Athanasios Angelakis  

**一句话要点**：提出ZACH-ViT以解决医学影像中空间先验不一致问题，实现紧凑且排列不变的视觉Transformer。

**关键词**：医学影像分析, 紧凑视觉Transformer, 排列不变性, 自适应残差投影, 少样本学习, 资源受限部署

## 3 点简述
- 核心问题：传统视觉Transformer的位置嵌入和类别令牌在医学影像中可能阻碍泛化，因空间布局信息弱或不一致。
- 方法要点：移除位置嵌入和[CLS]令牌，通过全局平均池化实现排列不变性，自适应残差投影保持训练稳定性。
- 实验或效果：在MedMNIST数据集上评估，ZACH-ViT在参数少、无预训练下保持竞争力，推理时间亚秒级，适合资源受限环境。

## 摘要（原文）

> Vision Transformers rely on positional embeddings and class tokens that encode fixed spatial priors. While effective for natural images, these priors may hinder generalization when spatial layout is weakly informative or inconsistent, a frequent condition in medical imaging and edge-deployed clinical systems. We introduce ZACH-ViT (Zero-token Adaptive Compact Hierarchical Vision Transformer), a compact Vision Transformer that removes both positional embeddings and the [CLS] token, achieving permutation invariance through global average pooling over patch representations. The term "Zero-token" specifically refers to removing the dedicated [CLS] aggregation token and positional embeddings; patch tokens remain unchanged and are processed normally. Adaptive residual projections preserve training stability in compact configurations while maintaining a strict parameter budget.
>   Evaluation is performed across seven MedMNIST datasets spanning binary and multi-class tasks under a strict few-shot protocol (50 samples per class, fixed hyperparameters, five random seeds). The empirical analysis demonstrates regime-dependent behavior: ZACH-ViT (0.25M parameters, trained from scratch) achieves its strongest advantage on BloodMNIST and remains competitive with TransMIL on PathMNIST, while its relative advantage decreases on datasets with strong anatomical priors (OCTMNIST, OrganAMNIST), consistent with the architectural hypothesis. These findings support the view that aligning architectural inductive bias with data structure can be more important than pursuing universal benchmark dominance. Despite its minimal size and lack of pretraining, ZACH-ViT achieves competitive performance while maintaining sub-second inference times, supporting deployment in resource-constrained clinical environments. Code and models are available at https://github.com/Bluesman79/ZACH-ViT.

