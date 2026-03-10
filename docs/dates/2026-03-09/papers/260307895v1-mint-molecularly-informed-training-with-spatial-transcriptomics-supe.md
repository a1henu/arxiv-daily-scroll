---
layout: default
title: MINT: Molecularly Informed Training with Spatial Transcriptomics Supervision for Pathology Foundation Models
---

# MINT: Molecularly Informed Training with Spatial Transcriptomics Supervision for Pathology Foundation Models
**arXiv**：[2603.07895v1](https://arxiv.org/abs/2603.07895) · [PDF](https://arxiv.org/pdf/2603.07895.pdf)  
**作者**：Minsoo Lee, Jonghyun Kim, Juseung Yun, Sunwoo Yu, Jongseong Jang  

**一句话要点**：提出MINT框架，通过空间转录组学监督微调病理学基础模型，以增强分子状态捕获能力。

**关键词**：病理学基础模型, 空间转录组学, 视觉Transformer, 跨模态监督, 微调框架, 基因表达预测

## 3 点简述
- 病理学基础模型缺乏对组织分子状态的显式建模，空间转录组学技术提供跨模态监督信号。
- MINT在预训练ViT中引入可学习的ST令牌，结合DINO自蒸馏和特征锚定，防止灾难性遗忘。
- 在HEST数据集上训练，MINT在基因表达预测和通用病理任务中均取得最佳性能。

## 摘要（原文）

> Pathology foundation models learn morphological representations through self-supervised pretraining on large-scale whole-slide images, yet they do not explicitly capture the underlying molecular state of the tissue. Spatial transcriptomics technologies bridge this gap by measuring gene expression in situ, offering a natural cross-modal supervisory signal. We propose MINT (Molecularly Informed Training), a fine-tuning framework that incorporates spatial transcriptomics supervision into pretrained pathology Vision Transformers. MINT appends a learnable ST token to the ViT input to encode transcriptomic information separately from the morphological CLS token, preventing catastrophic forgetting through DINO self-distillation and explicit feature anchoring to the frozen pretrained encoder. Gene expression regression at both spot-level (Visium) and patch-level (Xenium) resolutions provides complementary supervision across spatial scales. Trained on 577 publicly available HEST samples, MINT achieves the best overall performance on both HEST-Bench for gene expression prediction (mean Pearson r = 0.440) and EVA for general pathology tasks (0.803), demonstrating that spatial transcriptomics supervision complements morphology-centric self-supervised pretraining.

