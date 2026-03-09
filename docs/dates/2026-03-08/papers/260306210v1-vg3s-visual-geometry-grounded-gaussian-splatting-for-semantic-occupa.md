---
layout: default
title: VG3S: Visual Geometry Grounded Gaussian Splatting for Semantic Occupancy Prediction
---

# VG3S: Visual Geometry Grounded Gaussian Splatting for Semantic Occupancy Prediction
**arXiv**：[2603.06210v1](https://arxiv.org/abs/2603.06210) · [PDF](https://arxiv.org/pdf/2603.06210.pdf)  
**作者**：Xiaoyang Yan, Muleilan Pei, Shaojie Shen  

**一句话要点**：提出VG3S框架，通过视觉基础模型的几何先验增强高斯溅射的语义占据预测能力

**关键词**：3D语义占据预测, 高斯溅射, 视觉基础模型, 几何先验, 自动驾驶感知, 跨视图几何

## 3 点简述
- 问题：基于视觉的3D高斯溅射方法缺乏准确几何线索，影响占据预测质量
- 方法：设计分层几何特征适配器，将预训练视觉基础模型的3D几何先验注入高斯建模
- 效果：在nuScenes基准上IoU提升12.6%，mIoU提升7.5%，且能泛化到不同视觉基础模型

## 摘要（原文）

> 3D semantic occupancy prediction has become a crucial perception task for comprehensive scene understanding in autonomous driving. While recent advances have explored 3D Gaussian splatting for occupancy modeling to substantially reduce computational overhead, the generation of high-quality 3D Gaussians relies heavily on accurate geometric cues, which are often insufficient in purely vision-centric paradigms. To bridge this gap, we advocate for injecting the strong geometric grounding capability from Vision Foundation Models (VFMs) into occupancy prediction. In this regard, we introduce Visual Geometry Grounded Gaussian Splatting (VG3S), a novel framework that empowers Gaussian-based occupancy prediction with cross-view 3D geometric grounding. Specifically, to fully exploit the rich 3D geometric priors from a frozen VFM, we propose a plug-and-play hierarchical geometric feature adapter, which can effectively transform generic VFM tokens via feature aggregation, task-specific alignment, and multi-scale restructuring. Extensive experiments on the nuScenes occupancy benchmark demonstrate that VG3S achieves remarkable improvements of 12.6% in IoU and 7.5% in mIoU over the baseline. Furthermore, we show that VG3S generalizes seamlessly across diverse VFMs, consistently enhancing occupancy prediction accuracy and firmly underscoring the immense value of integrating priors derived from powerful, pre-trained geometry-grounded VFMs.

