---
layout: default
title: Cross Pseudo Labeling For Weakly Supervised Video Anomaly Detection
---

# Cross Pseudo Labeling For Weakly Supervised Video Anomaly Detection
**arXiv**：[2602.17077v1](https://arxiv.org/abs/2602.17077) · [PDF](https://arxiv.org/pdf/2602.17077.pdf)  
**作者**：Lee Dayeon, Kim Dongheyong, Park Chaewon, Woo Sungmin, Lee Sangyoun  

**一句话要点**：提出CPL-VAD框架，通过交叉伪标签解决弱监督视频异常检测中的定位与分类问题。

**关键词**：弱监督学习, 视频异常检测, 交叉伪标签, 双分支框架, 视觉语言对齐

## 3 点简述
- 核心问题：弱监督视频异常检测需仅用视频级标签定位异常片段并识别类别。
- 方法要点：双分支框架结合异常检测与分类，通过交叉伪标签互补时序精度与语义判别。
- 实验或效果：在XD-Violence和UCF-Crime数据集上实现异常检测和分类的先进性能。

## 摘要（原文）

> Weakly supervised video anomaly detection aims to detect anomalies and identify abnormal categories with only video-level labels. We propose CPL-VAD, a dual-branch framework with cross pseudo labeling. The binary anomaly detection branch focuses on snippet-level anomaly localization, while the category classification branch leverages vision-language alignment to recognize abnormal event categories. By exchanging pseudo labels, the two branches transfer complementary strengths, combining temporal precision with semantic discrimination. Experiments on XD-Violence and UCF-Crime demonstrate that CPL-VAD achieves state-of-the-art performance in both anomaly detection and abnormal category classification.

