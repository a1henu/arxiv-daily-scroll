---
layout: default
title: CMSA-Net: Causal Multi-scale Aggregation with Adaptive Multi-source Reference for Video Polyp Segmentation
---

# CMSA-Net: Causal Multi-scale Aggregation with Adaptive Multi-source Reference for Video Polyp Segmentation
**arXiv**：[2602.22821v1](https://arxiv.org/abs/2602.22821) · [PDF](https://arxiv.org/pdf/2602.22821.pdf)  
**作者**：Tong Wang, Yaolei Qi, Siwen Wang, Imran Razzak, Guanyu Yang, Yutong Xie  

**一句话要点**：提出CMSA-Net，通过因果多尺度聚合与自适应多源参考解决视频息肉分割中的语义弱区分和尺度变化问题。

**关键词**：视频息肉分割, 因果注意力, 多尺度聚合, 自适应参考选择, 实时推理, 医学图像分析

## 3 点简述
- 核心问题：视频息肉分割中息肉与黏膜相似导致语义区分弱，且帧间位置和尺度变化大，影响分割稳定性。
- 方法要点：引入因果多尺度聚合模块，按时间顺序聚合历史帧多尺度语义信息；设计动态多源参考策略，自适应选择可靠参考帧提供多帧指导。
- 实验或效果：在SUN-SEG数据集上实现先进性能，平衡分割精度与实时临床适用性。

## 摘要（原文）

> Video polyp segmentation (VPS) is an important task in computer-aided colonoscopy, as it helps doctors accurately locate and track polyps during examinations. However, VPS remains challenging because polyps often look similar to surrounding mucosa, leading to weak semantic discrimination. In addition, large changes in polyp position and scale across video frames make stable and accurate segmentation difficult. To address these challenges, we propose a robust VPS framework named CMSA-Net. The proposed network introduces a Causal Multi-scale Aggregation (CMA) module to effectively gather semantic information from multiple historical frames at different scales. By using causal attention, CMA ensures that temporal feature propagation follows strict time order, which helps reduce noise and improve feature reliability. Furthermore, we design a Dynamic Multi-source Reference (DMR) strategy that adaptively selects informative and reliable reference frames based on semantic separability and prediction confidence. This strategy provides strong multi-frame guidance while keeping the model efficient for real-time inference. Extensive experiments on the SUN-SEG dataset demonstrate that CMSA-Net achieves state-of-the-art performance, offering a favorable balance between segmentation accuracy and real-time clinical applicability.

