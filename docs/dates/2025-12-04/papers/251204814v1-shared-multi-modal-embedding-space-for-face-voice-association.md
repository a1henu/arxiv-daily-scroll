---
layout: default
title: Shared Multi-modal Embedding Space for Face-Voice Association
---

# Shared Multi-modal Embedding Space for Face-Voice Association
**arXiv**：[2512.04814v1](https://arxiv.org/abs/2512.04814) · [PDF](https://arxiv.org/pdf/2512.04814.pdf)  
**作者**：Christopher Simic, Korbinian Riedhammer, Tobias Bocklet  

**一句话要点**：提出共享多模态嵌入空间方法，用于跨语言人脸-语音关联任务

**关键词**：人脸-语音关联, 多模态嵌入, 跨语言学习, 自适应角边距损失, 特征提取

## 3 点简述
- 核心问题：在FAME 2026挑战中，需处理跨语言人脸-语音关联，包括未训练语言的测试
- 方法要点：采用独立单模态处理管道，结合年龄-性别特征，使用自适应角边距损失训练共享嵌入空间
- 实验或效果：在挑战中获第一名，平均等错误率为23.99%

## 摘要（原文）

> The FAME 2026 challenge comprises two demanding tasks: training face-voice associations combined with a multilingual setting that includes testing on languages on which the model was not trained. Our approach consists of separate uni-modal processing pipelines with general face and voice feature extraction, complemented by additional age-gender feature extraction to support prediction. The resulting single-modal features are projected into a shared embedding space and trained with an Adaptive Angular Margin (AAM) loss. Our approach achieved first place in the FAME 2026 challenge, with an average Equal-Error Rate (EER) of 23.99%.

