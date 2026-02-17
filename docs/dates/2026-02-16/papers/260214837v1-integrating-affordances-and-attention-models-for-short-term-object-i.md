---
layout: default
title: Integrating Affordances and Attention models for Short-Term Object Interaction Anticipation
---

# Integrating Affordances and Attention models for Short-Term Object Interaction Anticipation
**arXiv**：[2602.14837v1](https://arxiv.org/abs/2602.14837) · [PDF](https://arxiv.org/pdf/2602.14837.pdf)  
**作者**：Lorenzo Mur Labadia, Ruben Martinez-Cantin, Jose J. Guerrero, Giovanni M. Farinella, Antonino Furnari  

**一句话要点**：提出STAformer++架构与可负担性模块，以提升短时物体交互预测性能

**关键词**：短时物体交互预测, 注意力机制, 可负担性建模, 第一人称视频, STAformer, 多尺度特征融合

## 3 点简述
- 核心问题：短时物体交互预测需从第一人称视频中定位交互物体、类别及时间
- 方法要点：结合注意力机制与可负担性建模，包括环境可负担性记忆和交互热点预测
- 实验或效果：在Ego4D和EPIC-Kitchens数据集上显著提升Top-5 mAP，最高增益达31个百分点

## 摘要（原文）

> Short Term object-interaction Anticipation consists in detecting the location of the next active objects, the noun and verb categories of the interaction, as well as the time to contact from the observation of egocentric video. This ability is fundamental for wearable assistants to understand user goals and provide timely assistance, or to enable human-robot interaction. In this work, we present a method to improve the performance of STA predictions. Our contributions are two-fold: 1 We propose STAformer and STAformer plus plus, two novel attention-based architectures integrating frame-guided temporal pooling, dual image-video attention, and multiscale feature fusion to support STA predictions from an image-input video pair; 2 We introduce two novel modules to ground STA predictions on human behavior by modeling affordances. First, we integrate an environment affordance model which acts as a persistent memory of interactions that can take place in a given physical scene. We explore how to integrate environment affordances via simple late fusion and with an approach which adaptively learns how to best fuse affordances with end-to-end predictions. Second, we predict interaction hotspots from the observation of hands and object trajectories, increasing confidence in STA predictions localized around the hotspot. Our results show significant improvements on Overall Top-5 mAP, with gain up to +23p.p on Ego4D and +31p.p on a novel set of curated EPIC-Kitchens STA labels. We released the code, annotations, and pre-extracted affordances on Ego4D and EPIC-Kitchens to encourage future research in this area.

