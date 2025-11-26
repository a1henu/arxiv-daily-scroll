---
layout: default
title: 3D-Aware Multi-Task Learning with Cross-View Correlations for Dense Scene Understanding
---

# 3D-Aware Multi-Task Learning with Cross-View Correlations for Dense Scene Understanding
**arXiv**：[2511.20646v1](https://arxiv.org/abs/2511.20646) · [PDF](https://arxiv.org/pdf/2511.20646.pdf)  
**作者**：Xiaoye Wang, Chen Tang, Xiangyu Yue, Wei-Hong Li  

**一句话要点**：提出跨视图模块以增强多任务学习中的3D感知，提升密集场景理解性能

**关键词**：多任务学习, 3D感知, 跨视图相关性, 密集场景理解, 几何一致性

## 3 点简述
- 核心问题：现有多任务学习方法在2D空间建模任务关系，缺乏3D感知导致特征不结构化
- 方法要点：引入轻量级跨视图模块，利用成本体积捕捉跨视图相关性，注入几何一致性
- 实验或效果：在NYUv2和PASCAL-Context数据集上验证，有效提升现有方法性能

## 摘要（原文）

> This paper addresses the challenge of training a single network to jointly perform multiple dense prediction tasks, such as segmentation and depth estimation, i.e., multi-task learning (MTL). Current approaches mainly capture cross-task relations in the 2D image space, often leading to unstructured features lacking 3D-awareness. We argue that 3D-awareness is vital for modeling cross-task correlations essential for comprehensive scene understanding. We propose to address this problem by integrating correlations across views, i.e., cost volume, as geometric consistency in the MTL network. Specifically, we introduce a lightweight Cross-view Module (CvM), shared across tasks, to exchange information across views and capture cross-view correlations, integrated with a feature from MTL encoder for multi-task predictions. This module is architecture-agnostic and can be applied to both single and multi-view data. Extensive results on NYUv2 and PASCAL-Context demonstrate that our method effectively injects geometric consistency into existing MTL methods to improve performance.

