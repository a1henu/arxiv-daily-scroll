---
layout: default
title: Sim2real Image Translation Enables Viewpoint-Robust Policies from Fixed-Camera Datasets
---

# Sim2real Image Translation Enables Viewpoint-Robust Policies from Fixed-Camera Datasets
**arXiv**：[2601.09605v1](https://arxiv.org/abs/2601.09605) · [PDF](https://arxiv.org/pdf/2601.09605.pdf)  
**作者**：Jeremiah Coholich, Justin Wit, Robert Azarcon, Zsolt Kira  

**一句话要点**：提出MANGO图像翻译方法以增强机器人视觉策略的视角鲁棒性

**关键词**：图像翻译, 机器人视觉, 视角鲁棒性, 模拟到真实, 无配对学习, 模仿学习

## 3 点简述
- 核心问题：机器人视觉策略对相机视角变化敏感，真实数据稀缺且视角单一。
- 方法要点：基于分割条件InfoNCE损失、正则化判别器和改进PatchNCE损失的无配对图像翻译。
- 实验或效果：在模拟到真实翻译中保持视角一致性，提升策略在未见视角上的成功率至60%。

## 摘要（原文）

> Vision-based policies for robot manipulation have achieved significant recent success, but are still brittle to distribution shifts such as camera viewpoint variations. Robot demonstration data is scarce and often lacks appropriate variation in camera viewpoints. Simulation offers a way to collect robot demonstrations at scale with comprehensive coverage of different viewpoints, but presents a visual sim2real challenge. To bridge this gap, we propose MANGO -- an unpaired image translation method with a novel segmentation-conditioned InfoNCE loss, a highly-regularized discriminator design, and a modified PatchNCE loss. We find that these elements are crucial for maintaining viewpoint consistency during sim2real translation. When training MANGO, we only require a small amount of fixed-camera data from the real world, but show that our method can generate diverse unseen viewpoints by translating simulated observations. In this domain, MANGO outperforms all other image translation methods we tested. Imitation-learning policies trained on data augmented by MANGO are able to achieve success rates as high as 60\% on views that the non-augmented policy fails completely on.

