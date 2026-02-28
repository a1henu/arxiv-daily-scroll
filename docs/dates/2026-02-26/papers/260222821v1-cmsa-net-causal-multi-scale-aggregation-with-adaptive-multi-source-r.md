---
layout: default
title: CMSA-Net: Causal Multi-scale Aggregation with Adaptive Multi-source Reference for Video Polyp Segmentation
---

# CMSA-Net: Causal Multi-scale Aggregation with Adaptive Multi-source Reference for Video Polyp Segmentation
**arXiv**：[2602.22821v1](https://arxiv.org/abs/2602.22821) · [PDF](https://arxiv.org/pdf/2602.22821.pdf)  
**作者**：Tong Wang, Yaolei Qi, Siwen Wang, Imran Razzak, Guanyu Yang, Yutong Xie  

**一句话要点**：提出CMSA-Net以解决视频息肉分割中语义相似性和尺度变化问题

**关键词**：视频息肉分割, 因果注意力, 多尺度特征聚合, 动态参考选择, 实时推理

## 3 点简述
- 核心问题：息肉与周围黏膜语义相似，且视频中位置和尺度变化大，导致分割困难。
- 方法要点：引入因果多尺度聚合模块，按时间顺序聚合历史帧特征，并设计动态多源参考策略自适应选择参考帧。
- 实验或效果：在SUN-SEG数据集上实现先进性能，平衡分割精度与实时临床适用性。

## 摘要（原文）

> Video polyp segmentation (VPS) is an important task in computer-aided colonoscopy, as it helps doctors accurately locate and track polyps during examinations. However, VPS remains challenging because polyps often look similar to surrounding mucosa, leading to weak semantic discrimination. In addition, large changes in polyp position and scale across video frames make stable and accurate segmentation difficult. To address these challenges, we propose a robust VPS framework named CMSA-Net. The proposed network introduces a Causal Multi-scale Aggregation (CMA) module to effectively gather semantic information from multiple historical frames at different scales. By using causal attention, CMA ensures that temporal feature propagation follows strict time order, which helps reduce noise and improve feature reliability. Furthermore, we design a Dynamic Multi-source Reference (DMR) strategy that adaptively selects informative and reliable reference frames based on semantic separability and prediction confidence. This strategy provides strong multi-frame guidance while keeping the model efficient for real-time inference. Extensive experiments on the SUN-SEG dataset demonstrate that CMSA-Net achieves state-of-the-art performance, offering a favorable balance between segmentation accuracy and real-time clinical applicability.

