---
layout: default
title: Universal Pose Pretraining for Generalizable Vision-Language-Action Policies
---

# Universal Pose Pretraining for Generalizable Vision-Language-Action Policies
**arXiv**：[2602.19710v1](https://arxiv.org/abs/2602.19710) · [PDF](https://arxiv.org/pdf/2602.19710.pdf)  
**作者**：Haitao Lin, Hanyang Yu, Jingshun Huang, He Zhang, Yonggen Ling, Ping Tan, Xiangyang Xue, Yanwei Fu  

**一句话要点**：提出Pose-VLA范式，通过解耦训练解决VLA模型特征崩溃与训练效率低的问题

**关键词**：视觉-语言-动作模型, 姿态预训练, 机器人策略, 3D空间表示, 解耦训练

## 3 点简述
- 现有VLA模型因高层感知与稀疏动作监督纠缠，导致特征崩溃和训练效率低
- 提出两阶段训练范式：预训练提取通用3D空间先验，后训练进行机器人特定动作空间对齐
- 在RoboTwin 2.0和LIBERO基准上取得先进性能，仅需少量演示即可实现鲁棒泛化

## 摘要（原文）

> Existing Vision-Language-Action (VLA) models often suffer from feature collapse and low training efficiency because they entangle high-level perception with sparse, embodiment-specific action supervision. Since these models typically rely on VLM backbones optimized for Visual Question Answering (VQA), they excel at semantic identification but often overlook subtle 3D state variations that dictate distinct action patterns.
>   To resolve these misalignments, we propose Pose-VLA, a decoupled paradigm that separates VLA training into a pre-training phase for extracting universal 3D spatial priors in a unified camera-centric space, and a post-training phase for efficient embodiment alignment within robot-specific action space. By introducing discrete pose tokens as a universal representation, Pose-VLA seamlessly integrates spatial grounding from diverse 3D datasets with geometry-level trajectories from robotic demonstrations. Our framework follows a two-stage pre-training pipeline, establishing fundamental spatial grounding via poses followed by motion alignment through trajectory supervision.
>   Extensive evaluations demonstrate that Pose-VLA achieves state-of-the-art results on RoboTwin 2.0 with a 79.5% average success rate and competitive performance on LIBERO at 96.0%. Real-world experiments further showcase robust generalization across diverse objects using only 100 demonstrations per task, validating the efficiency of our pre-training paradigm.

