---
layout: default
title: Few-Shot Precise Event Spotting via Unified Multi-Entity Graph and Distillation
---

# Few-Shot Precise Event Spotting via Unified Multi-Entity Graph and Distillation
**arXiv**：[2511.14186v1](https://arxiv.org/abs/2511.14186) · [PDF](https://arxiv.org/pdf/2511.14186.pdf)  
**作者**：Zhaoyu Liu, Kan Jiang, Murong Ma, Zhe Hou, Yun Lin, Jin Song Dong  

**一句话要点**：提出统一多实体图网络以解决少样本精确事件定位问题

**关键词**：精确事件定位, 少样本学习, 图卷积网络, 多模态蒸馏, 时空建模

## 3 点简述
- 核心问题：精确事件定位面临快速连续、运动模糊和视觉差异细微的挑战，依赖大标注数据集
- 方法要点：整合人体骨架和物体关键点构建统一图，采用GCN和多尺度时序移位提取时空特征
- 实验或效果：在少样本设置下性能优于基线，通过多模态蒸馏提升视觉表示鲁棒性

## 摘要（原文）

> Precise event spotting (PES) aims to recognize fine-grained events at exact moments and has become a key component of sports analytics. This task is particularly challenging due to rapid succession, motion blur, and subtle visual differences. Consequently, most existing methods rely on domain-specific, end-to-end training with large labeled datasets and often struggle in few-shot conditions due to their dependence on pixel- or pose-based inputs alone. However, obtaining large labeled datasets is practically hard. We propose a Unified Multi-Entity Graph Network (UMEG-Net) for few-shot PES. UMEG-Net integrates human skeletons and sport-specific object keypoints into a unified graph and features an efficient spatio-temporal extraction module based on advanced GCN and multi-scale temporal shift. To further enhance performance, we employ multimodal distillation to transfer knowledge from keypoint-based graphs to visual representations. Our approach achieves robust performance with limited labeled data and significantly outperforms baseline models in few-shot settings, providing a scalable and effective solution for few-shot PES. Code is publicly available at https://github.com/LZYAndy/UMEG-Net.

