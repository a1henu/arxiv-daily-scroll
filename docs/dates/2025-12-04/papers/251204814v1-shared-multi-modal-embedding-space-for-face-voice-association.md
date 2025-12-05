---
layout: default
title: Shared Multi-modal Embedding Space for Face-Voice Association
---

# Shared Multi-modal Embedding Space for Face-Voice Association
**arXiv**：[2512.04814v1](https://arxiv.org/abs/2512.04814) · [PDF](https://arxiv.org/pdf/2512.04814.pdf)  
**作者**：Christopher Simic, Korbinian Riedhammer, Tobias Bocklet  

**一句话要点**：提出基于共享嵌入空间和自适应角边距损失的方法，以解决多语言环境下人脸-语音关联的跨模态匹配问题。

**关键词**：人脸-语音关联, 共享嵌入空间, 自适应角边距损失, 多模态学习, 跨模态匹配

## 3 点简述
- 核心问题：多语言环境下人脸与语音的跨模态关联，包括未训练语言的测试。
- 方法要点：采用独立单模态处理流程，结合通用特征和年龄-性别特征，投影到共享嵌入空间。
- 实验或效果：在FAME 2026挑战赛中获第一名，平均等错误率为23.99%。

## 摘要（原文）

> The FAME 2026 challenge comprises two demanding tasks: training face-voice associations combined with a multilingual setting that includes testing on languages on which the model was not trained. Our approach consists of separate uni-modal processing pipelines with general face and voice feature extraction, complemented by additional age-gender feature extraction to support prediction. The resulting single-modal features are projected into a shared embedding space and trained with an Adaptive Angular Margin (AAM) loss. Our approach achieved first place in the FAME 2026 challenge, with an average Equal-Error Rate (EER) of 23.99%.

