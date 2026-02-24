---
layout: default
title: Enhancing Automatic Chord Recognition via Pseudo-Labeling and Knowledge Distillation
---

# Enhancing Automatic Chord Recognition via Pseudo-Labeling and Knowledge Distillation
**arXiv**：[2602.19778v1](https://arxiv.org/abs/2602.19778) · [PDF](https://arxiv.org/pdf/2602.19778.pdf)  
**作者**：Nghia Phan, Rong Jin, Gang Liu, Xiao Dong  

**一句话要点**：提出两阶段训练方法，通过伪标签和知识蒸馏增强自动和弦识别性能

**关键词**：自动和弦识别, 伪标签训练, 知识蒸馏, 两阶段学习, 音频处理

## 3 点简述
- 核心问题：自动和弦识别受限于对齐和弦标签的稀缺性，标注成本高。
- 方法要点：第一阶段使用预训练模型生成伪标签训练学生模型，第二阶段结合真实标签和选择性知识蒸馏进行微调。
- 实验或效果：学生模型在伪标签训练后接近教师性能，最终超越传统监督基线，在稀有和弦上表现显著提升。

## 摘要（原文）

> Automatic Chord Recognition (ACR) is constrained by the scarcity of aligned chord labels, as well-aligned annotations are costly to acquire. At the same time, open-weight pre-trained models are currently more accessible than their proprietary training data. In this work, we present a two-stage training pipeline that leverages pre-trained models together with unlabeled audio. The proposed method decouples training into two stages. In the first stage, we use a pre-trained BTC model as a teacher to generate pseudo-labels for over 1,000 hours of diverse unlabeled audio and train a student model solely on these pseudo-labels. In the second stage, the student is continually trained on ground-truth labels as they become available, with selective knowledge distillation (KD) from the teacher applied as a regularizer to prevent catastrophic forgetting of the representations learned in the first stage. In our experiments, two models (BTC, 2E1D) were used as students. In stage 1, using only pseudo-labels, the BTC student achieves over 98% of the teacher's performance, while the 2E1D model achieves about 96% across seven standard mir_eval metrics. After a single training run for both students in stage 2, the resulting BTC student model surpasses the traditional supervised learning baseline by 2.5% and the original pre-trained teacher model by 1.55% on average across all metrics. And the resulting 2E1D student model improves from the traditional supervised learning baseline by 3.79% on average and achieves almost the same performance as the teacher. Both cases show the large gains on rare chord qualities.

