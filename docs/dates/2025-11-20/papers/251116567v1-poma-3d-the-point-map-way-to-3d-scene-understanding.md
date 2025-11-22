---
layout: default
title: POMA-3D: The Point Map Way to 3D Scene Understanding
---

# POMA-3D: The Point Map Way to 3D Scene Understanding
**arXiv**：[2511.16567v1](https://arxiv.org/abs/2511.16567) · [PDF](https://arxiv.org/pdf/2511.16567.pdf)  
**作者**：Ye Mao, Weixun Luo, Ranran Huang, Junpeng Jing, Krystian Mikolajczyk  

**一句话要点**：提出POMA-3D，通过点图实现自监督3D场景理解，解决3D表示学习中先验和数据稀缺问题。

**关键词**：点图表示, 自监督学习, 3D场景理解, 视图对齐, 几何一致性, 多任务学习

## 3 点简述
- 核心问题：3D表示学习缺乏预训练先验和有限数据，难以迁移2D基础模型优势。
- 方法要点：使用点图编码3D坐标，结合视图对齐和POMA-JEPA架构确保多视图几何一致性。
- 实验效果：在3D问答、导航等任务中表现优异，仅使用几何输入实现通用3D理解。

## 摘要（原文）

> In this paper, we introduce POMA-3D, the first self-supervised 3D representation model learned from point maps. Point maps encode explicit 3D coordinates on a structured 2D grid, preserving global 3D geometry while remaining compatible with the input format of 2D foundation models. To transfer rich 2D priors into POMA-3D, a view-to-scene alignment strategy is designed. Moreover, as point maps are view-dependent with respect to a canonical space, we introduce POMA-JEPA, a joint embedding-predictive architecture that enforces geometrically consistent point map features across multiple views. Additionally, we introduce ScenePoint, a point map dataset constructed from 6.5K room-level RGB-D scenes and 1M 2D image scenes to facilitate large-scale POMA-3D pretraining. Experiments show that POMA-3D serves as a strong backbone for both specialist and generalist 3D understanding. It benefits diverse tasks, including 3D question answering, embodied navigation, scene retrieval, and embodied localization, all achieved using only geometric inputs (i.e., 3D coordinates). Overall, our POMA-3D explores a point map way to 3D scene understanding, addressing the scarcity of pretrained priors and limited data in 3D representation learning. Project Page: https://matchlab-imperial.github.io/poma3d/

