---
layout: default
title: RoEL: Robust Event-based 3D Line Reconstruction
---

# RoEL: Robust Event-based 3D Line Reconstruction
**arXiv**：[2602.18258v1](https://arxiv.org/abs/2602.18258) · [PDF](https://arxiv.org/pdf/2602.18258.pdf)  
**作者**：Gwangtak Bae, Jaeho Shin, Seunggu Kang, Junho Kim, Ayoung Kim, Young Min Kim  

**一句话要点**：提出RoEL方法，通过稳健的线提取与几何优化解决事件相机在3D线重建中的噪声与误差问题。

**关键词**：事件相机, 3D线重建, 几何优化, 姿态估计, 多模态融合, 稳健表示

## 3 点简述
- 事件相机在运动中检测物体边界或纹理边缘，但稀疏线特征易受估计误差影响，导致性能下降。
- 方法利用多时间切片事件观察线变化，设计几何成本函数优化3D线图和相机姿态，消除投影失真和深度模糊。
- 实验表明，该方法在多样数据集上显著提升事件基映射和姿态细化性能，并可灵活应用于多模态场景。

## 摘要（原文）

> Event cameras in motion tend to detect object boundaries or texture edges, which produce lines of brightness changes, especially in man-made environments. While lines can constitute a robust intermediate representation that is consistently observed, the sparse nature of lines may lead to drastic deterioration with minor estimation errors. Only a few previous works, often accompanied by additional sensors, utilize lines to compensate for the severe domain discrepancies of event sensors along with unpredictable noise characteristics. We propose a method that can stably extract tracks of varying appearances of lines using a clever algorithmic process that observes multiple representations from various time slices of events, compensating for potential adversaries within the event data. We then propose geometric cost functions that can refine the 3D line maps and camera poses, eliminating projective distortions and depth ambiguities. The 3D line maps are highly compact and can be equipped with our proposed cost function, which can be adapted for any observations that can detect and extract line structures or projections of them, including 3D point cloud maps or image observations. We demonstrate that our formulation is powerful enough to exhibit a significant performance boost in event-based mapping and pose refinement across diverse datasets, and can be flexibly applied to multimodal scenarios. Our results confirm that the proposed line-based formulation is a robust and effective approach for the practical deployment of event-based perceptual modules. Project page: https://gwangtak.github.io/roel/

