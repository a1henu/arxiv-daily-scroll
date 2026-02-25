---
layout: default
title: Boosting Instance Awareness via Cross-View Correlation with 4D Radar and Camera for 3D Object Detection
---

# Boosting Instance Awareness via Cross-View Correlation with 4D Radar and Camera for 3D Object Detection
**arXiv**：[2602.20632v1](https://arxiv.org/abs/2602.20632) · [PDF](https://arxiv.org/pdf/2602.20632.pdf)  
**作者**：Xiaokai Bai, Lianqing Zheng, Si-Yuan Cao, Xiaohan Zhang, Zhe Wu, Beinan Yu, Fang Wang, Jie Bai, Hui-Liang Shen  

**一句话要点**：提出SIFormer，通过跨视图激活机制增强实例感知，以解决4D雷达稀疏几何下的3D目标检测问题。

**关键词**：4D雷达-相机融合, 3D目标检测, 跨视图激活, BEV空间, 实例感知增强, 自动驾驶感知

## 3 点简述
- 核心问题：4D雷达稀疏几何导致实例激活困难，现有雷达-相机融合范式在全局与局部间存在权衡。
- 方法要点：引入分割和深度引导的视图变换抑制背景噪声，跨视图激活注入2D实例线索至BEV空间。
- 实验或效果：在View-of-Delft、TJ4DRadSet和NuScenes数据集上实现最先进性能，代码开源。

## 摘要（原文）

> 4D millimeter-wave radar has emerged as a promising sensing modality for autonomous driving due to its robustness and affordability. However, its sparse and weak geometric cues make reliable instance activation difficult, limiting the effectiveness of existing radar-camera fusion paradigms. BEV-level fusion offers global scene understanding but suffers from weak instance focus, while perspective-level fusion captures instance details but lacks holistic context. To address these limitations, we propose SIFormer, a scene-instance aware transformer for 3D object detection using 4D radar and camera. SIFormer first suppresses background noise during view transformation through segmentation- and depth-guided localization. It then introduces a cross-view activation mechanism that injects 2D instance cues into BEV space, enabling reliable instance awareness under weak radar geometry. Finally, a transformer-based fusion module aggregates complementary image semantics and radar geometry for robust perception. As a result, with the aim of enhancing instance awareness, SIFormer bridges the gap between the two paradigms, combining their complementary strengths to address inherent sparse nature of radar and improve detection accuracy. Experiments demonstrate that SIFormer achieves state-of-the-art performance on View-of-Delft, TJ4DRadSet and NuScenes datasets. Source code is available at github.com/shawnnnkb/SIFormer.

