---
layout: default
title: CollabOD: Collaborative Multi-Backbone with Cross-scale Vision for UAV Small Object Detection
---

# CollabOD: Collaborative Multi-Backbone with Cross-scale Vision for UAV Small Object Detection
**arXiv**：[2603.05905v1](https://arxiv.org/abs/2603.05905) · [PDF](https://arxiv.org/pdf/2603.05905.pdf)  
**作者**：Xuecheng Bai, Yuxiang Wang, Chuanzhi Xu, Boyu Hu, Kang Han, Ruijie Pan, Xiaowei Niu, Xiaotian Guan, Liqiang Fu, Pengfei Ye  

**一句话要点**：提出CollabOD框架以解决无人机图像中小目标检测的尺度变化和细节退化问题。

**关键词**：无人机目标检测, 小目标检测, 多尺度特征融合, 轻量化设计, 结构细节保留

## 3 点简述
- 核心问题：无人机图像中小目标检测面临尺度变化、结构细节退化和计算资源限制的挑战。
- 方法要点：采用结构细节保留、跨路径特征对齐和定位感知轻量化设计策略，优化特征表示。
- 实验或效果：增强表示稳定性，保持高效推理，通过统一细节感知检测头提升回归鲁棒性。

## 摘要（原文）

> Small object detection in unmanned aerial vehicle (UAV) imagery is challenging, mainly due to scale variation, structural detail degradation, and limited computational resources. In high-altitude scenarios, fine-grained features are further weakened during hierarchical downsampling and cross-scale fusion, resulting in unstable localization and reduced robustness. To address this issue, we propose CollabOD, a lightweight collaborative detection framework that explicitly preserves structural details and aligns heterogeneous feature streams before multi-scale fusion. The framework integrates Structural Detail Preservation, Cross-Path Feature Alignment, and Localization-Aware Lightweight Design strategies. From the perspectives of image processing, channel structure, and lightweight design, it optimizes the architecture of conventional UAV perception models. The proposed design enhances representation stability while maintaining efficient inference. A unified detail-aware detection head further improves regression robustness without introducing additional deployment overhead. The code is available at: https://github.com/Bai-Xuecheng/CollabOD.

