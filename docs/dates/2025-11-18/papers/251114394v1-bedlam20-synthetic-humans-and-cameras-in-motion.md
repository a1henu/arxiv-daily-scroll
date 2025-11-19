---
layout: default
title: BEDLAM2.0: Synthetic Humans and Cameras in Motion
---

# BEDLAM2.0: Synthetic Humans and Cameras in Motion
**arXiv**：[2511.14394v1](https://arxiv.org/abs/2511.14394) · [PDF](https://arxiv.org/pdf/2511.14394.pdf)  
**作者**：Joachim Tesch, Giorgio Becherini, Prerana Achar, Anastasios Yiannakidis, Muhammed Kocabas, Priyanka Patel, Michael J. Black  

**一句话要点**：提出BEDLAM2.0数据集以解决视频中3D人体和相机运动估计问题

**关键词**：3D人体运动估计, 合成数据集, 世界坐标系, 相机运动, 视频分析

## 3 点简述
- 核心问题：缺乏真实视频数据，难以估计世界坐标系中的人体和相机运动
- 方法要点：扩展BEDLAM数据集，增加多样性人体、相机、环境和服装
- 实验或效果：训练方法在BEDLAM2.0上显著提升估计准确性

## 摘要（原文）

> Inferring 3D human motion from video remains a challenging problem with many applications. While traditional methods estimate the human in image coordinates, many applications require human motion to be estimated in world coordinates. This is particularly challenging when there is both human and camera motion. Progress on this topic has been limited by the lack of rich video data with ground truth human and camera movement. We address this with BEDLAM2.0, a new dataset that goes beyond the popular BEDLAM dataset in important ways. In addition to introducing more diverse and realistic cameras and camera motions, BEDLAM2.0 increases diversity and realism of body shape, motions, clothing, hair, and 3D environments. Additionally, it adds shoes, which were missing in BEDLAM. BEDLAM has become a key resource for training 3D human pose and motion regressors today and we show that BEDLAM2.0 is significantly better, particularly for training methods that estimate humans in world coordinates. We compare state-of-the art methods trained on BEDLAM and BEDLAM2.0, and find that BEDLAM2.0 significantly improves accuracy over BEDLAM. For research purposes, we provide the rendered videos, ground truth body parameters, and camera motions. We also provide the 3D assets to which we have rights and links to those from third parties.

