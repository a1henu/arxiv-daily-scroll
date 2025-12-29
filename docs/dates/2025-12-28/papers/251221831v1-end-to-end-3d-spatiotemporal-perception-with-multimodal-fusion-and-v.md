---
layout: default
title: End-to-End 3D Spatiotemporal Perception with Multimodal Fusion and V2X Collaboration
---

# End-to-End 3D Spatiotemporal Perception with Multimodal Fusion and V2X Collaboration
**arXiv**：[2512.21831v1](https://arxiv.org/abs/2512.21831) · [PDF](https://arxiv.org/pdf/2512.21831.pdf)  
**作者**：Zhenwei Yang, Yibo Ai, Weidong Zhang  

**一句话要点**：提出XET-V2X框架，通过多模态融合与V2X协作实现自动驾驶中的端到端3D时空感知。

**关键词**：自动驾驶感知, 多模态融合, V2X协作, 3D时空理解, 端到端跟踪

## 3 点简述
- 核心问题：自动驾驶中多视角协作感知与多模态融合在遮挡、视角限制和V2X通信延迟下的挑战。
- 方法要点：引入基于多尺度可变形注意力的双层空间交叉注意力模块，统一多视角多模态感知于共享时空表示。
- 实验或效果：在V2X-Seq-SPD等数据集上验证，检测与跟踪性能提升，实现复杂交通场景下的鲁棒感知。

## 摘要（原文）

> Multi-view cooperative perception and multimodal fusion are essential for reliable 3D spatiotemporal understanding in autonomous driving, especially under occlusions, limited viewpoints, and communication delays in V2X scenarios. This paper proposes XET-V2X, a multi-modal fused end-to-end tracking framework for v2x collaboration that unifies multi-view multimodal sensing within a shared spatiotemporal representation. To efficiently align heterogeneous viewpoints and modalities, XET-V2X introduces a dual-layer spatial cross-attention module based on multi-scale deformable attention. Multi-view image features are first aggregated to enhance semantic consistency, followed by point cloud fusion guided by the updated spatial queries, enabling effective cross-modal interaction while reducing computational overhead. Experiments on the real-world V2X-Seq-SPD dataset and the simulated V2X-Sim-V2V and V2X-Sim-V2I benchmarks demonstrate consistent improvements in detection and tracking performance under varying communication delays. Both quantitative results and qualitative visualizations indicate that XET-V2X achieves robust and temporally stable perception in complex traffic scenarios.

