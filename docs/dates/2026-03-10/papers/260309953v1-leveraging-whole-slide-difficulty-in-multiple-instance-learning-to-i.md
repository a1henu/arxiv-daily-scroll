---
layout: default
title: Leveraging whole slide difficulty in Multiple Instance Learning to improve prostate cancer grading
---

# Leveraging whole slide difficulty in Multiple Instance Learning to improve prostate cancer grading
**arXiv**：[2603.09953v1](https://arxiv.org/abs/2603.09953) · [PDF](https://arxiv.org/pdf/2603.09953.pdf)  
**作者**：Marie Arrivat, Rémy Peyret, Elsa Angelini, Pietro Gori  

**一句话要点**：提出全切片难度概念以提升前列腺癌分级性能

**关键词**：全切片图像, 多实例学习, 前列腺癌分级, 全切片难度, 加权损失, 病理学诊断

## 3 点简述
- 核心问题：全切片图像诊断存在专家与非专家间分歧，影响多实例学习分类准确性。
- 方法要点：基于专家与非专家病理学家分歧定义全切片难度，采用多任务和加权分类损失方法。
- 实验或效果：集成全切片难度训练提升分类性能，尤其对高级别Gleason分级效果显著。

## 摘要（原文）

> Multiple Instance Learning (MIL) has been widely applied in histopathology to classify Whole Slide Images (WSIs) with slide-level diagnoses. While the ground truth is established by expert pathologists, the slides can be difficult to diagnose for non-experts and lead to disagreements between the annotators. In this paper, we introduce the notion of Whole Slide Difficulty (WSD), based on the disagreement between an expert and a non-expert pathologist. We propose two different methods to leverage WSD, a multi-task approach and a weighted classification loss approach, and we apply them to Gleason grading of prostate cancer slides. Results show that integrating WSD during training consistently improves the classification performance across different feature encoders and MIL methods, particularly for higher Gleason grades (i.e. worse diagnosis).

