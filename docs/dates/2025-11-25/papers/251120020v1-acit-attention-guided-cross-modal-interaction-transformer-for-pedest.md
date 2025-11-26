---
layout: default
title: ACIT: Attention-Guided Cross-Modal Interaction Transformer for Pedestrian Crossing Intention Prediction
---

# ACIT: Attention-Guided Cross-Modal Interaction Transformer for Pedestrian Crossing Intention Prediction
**arXiv**：[2511.20020v1](https://arxiv.org/abs/2511.20020) · [PDF](https://arxiv.org/pdf/2511.20020.pdf)  
**作者**：Yuanzhe Li, Steffen Müller  

**一句话要点**：提出注意力引导跨模态交互Transformer以预测行人过街意图

**关键词**：行人意图预测, 跨模态交互, 注意力机制, Transformer, 自动驾驶安全

## 3 点简述
- 核心问题：从多模态数据中有效提取和整合互补线索预测行人过街意图。
- 方法要点：使用六种模态分组为三对，通过注意力机制增强模态间交互。
- 实验效果：在JAADbeh和JAADall数据集上准确率分别达70%和89%。

## 摘要（原文）

> Predicting pedestrian crossing intention is crucial for autonomous vehicles to prevent pedestrian-related collisions. However, effectively extracting and integrating complementary cues from different types of data remains one of the major challenges. This paper proposes an attention-guided cross-modal interaction Transformer (ACIT) for pedestrian crossing intention prediction. ACIT leverages six visual and motion modalities, which are grouped into three interaction pairs: (1) Global semantic map and global optical flow, (2) Local RGB image and local optical flow, and (3) Ego-vehicle speed and pedestrian's bounding box. Within each visual interaction pair, a dual-path attention mechanism enhances salient regions within the primary modality through intra-modal self-attention and facilitates deep interactions with the auxiliary modality (i.e., optical flow) via optical flow-guided attention. Within the motion interaction pair, cross-modal attention is employed to model the cross-modal dynamics, enabling the effective extraction of complementary motion features. Beyond pairwise interactions, a multi-modal feature fusion module further facilitates cross-modal interactions at each time step. Furthermore, a Transformer-based temporal feature aggregation module is introduced to capture sequential dependencies. Experimental results demonstrate that ACIT outperforms state-of-the-art methods, achieving accuracy rates of 70% and 89% on the JAADbeh and JAADall datasets, respectively. Extensive ablation studies are further conducted to investigate the contribution of different modules of ACIT.

