---
layout: default
title: MTPano: Multi-Task Panoramic Scene Understanding via Label-Free Integration of Dense Prediction Priors
---

# MTPano: Multi-Task Panoramic Scene Understanding via Label-Free Integration of Dense Prediction Priors
**arXiv**：[2602.05330v1](https://arxiv.org/abs/2602.05330) · [PDF](https://arxiv.org/pdf/2602.05330.pdf)  
**作者**：Jingdong Zhang, Xiaohang Zhan, Lingzhi Zhang, Yizhou Wang, Zhengming Yu, Jionghao Wang, Wenping Wang, Xin Li  

**一句话要点**：提出MTPano，通过无标签训练集成密集预测先验，实现多任务全景场景理解。

**关键词**：全景场景理解, 多任务学习, 无标签训练, 密集预测, 几何失真处理, 基础模型

## 3 点简述
- 核心问题：全景场景理解面临数据稀缺、几何失真和任务间干扰挑战。
- 方法要点：利用透视先验生成伪标签，通过全景双桥网络分离旋转不变与旋转变任务特征。
- 实验或效果：在多个基准测试中达到最先进性能，与任务专用模型竞争。

## 摘要（原文）

> Comprehensive panoramic scene understanding is critical for immersive applications, yet it remains challenging due to the scarcity of high-resolution, multi-task annotations. While perspective foundation models have achieved success through data scaling, directly adapting them to the panoramic domain often fails due to severe geometric distortions and coordinate system discrepancies. Furthermore, the underlying relations between diverse dense prediction tasks in spherical spaces are underexplored. To address these challenges, we propose MTPano, a robust multi-task panoramic foundation model established by a label-free training pipeline. First, to circumvent data scarcity, we leverage powerful perspective dense priors. We project panoramic images into perspective patches to generate accurate, domain-gap-free pseudo-labels using off-the-shelf foundation models, which are then re-projected to serve as patch-wise supervision. Second, to tackle the interference between task types, we categorize tasks into rotation-invariant (e.g., depth, segmentation) and rotation-variant (e.g., surface normals) groups. We introduce the Panoramic Dual BridgeNet, which disentangles these feature streams via geometry-aware modulation layers that inject absolute position and ray direction priors. To handle the distortion from equirectangular projections (ERP), we incorporate ERP token mixers followed by a dual-branch BridgeNet for interactions with gradient truncation, facilitating beneficial cross-task information sharing while blocking conflicting gradients from incompatible task attributes. Additionally, we introduce auxiliary tasks (image gradient, point map, etc.) to fertilize the cross-task learning process. Extensive experiments demonstrate that MTPano achieves state-of-the-art performance on multiple benchmarks and delivers competitive results against task-specific panoramic specialist foundation models.

