---
layout: default
title: Retrieve and Segment: Are a Few Examples Enough to Bridge the Supervision Gap in Open-Vocabulary Segmentation?
---

# Retrieve and Segment: Are a Few Examples Enough to Bridge the Supervision Gap in Open-Vocabulary Segmentation?
**arXiv**：[2602.23339v1](https://arxiv.org/abs/2602.23339) · [PDF](https://arxiv.org/pdf/2602.23339.pdf)  
**作者**：Tilemachos Aravanis, Vladan Stojnić, Bill Psomas, Nikos Komodakis, Giorgos Tolias  

**一句话要点**：提出检索增强测试时适配器，通过少量标注图像提升开放词汇分割性能

**关键词**：开放词汇分割, 少样本学习, 检索增强, 测试时适配, 视觉语言模型

## 3 点简述
- 核心问题：开放词汇分割因图像级监督粗粒度和语言歧义而落后于全监督方法
- 方法要点：引入少样本设置，融合文本与视觉支持特征学习轻量级分类器
- 实验或效果：显著缩小零样本与监督分割差距，保持开放词汇能力

## 摘要（原文）

> Open-vocabulary segmentation (OVS) extends the zero-shot recognition capabilities of vision-language models (VLMs) to pixel-level prediction, enabling segmentation of arbitrary categories specified by text prompts. Despite recent progress, OVS lags behind fully supervised approaches due to two challenges: the coarse image-level supervision used to train VLMs and the semantic ambiguity of natural language. We address these limitations by introducing a few-shot setting that augments textual prompts with a support set of pixel-annotated images. Building on this, we propose a retrieval-augmented test-time adapter that learns a lightweight, per-image classifier by fusing textual and visual support features. Unlike prior methods relying on late, hand-crafted fusion, our approach performs learned, per-query fusion, achieving stronger synergy between modalities. The method supports continually expanding support sets, and applies to fine-grained tasks such as personalized segmentation. Experiments show that we significantly narrow the gap between zero-shot and supervised segmentation while preserving open-vocabulary ability.

