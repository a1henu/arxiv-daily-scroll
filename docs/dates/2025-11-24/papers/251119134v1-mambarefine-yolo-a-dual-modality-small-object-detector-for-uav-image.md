---
layout: default
title: MambaRefine-YOLO: A Dual-Modality Small Object Detector for UAV Imagery
---

# MambaRefine-YOLO: A Dual-Modality Small Object Detector for UAV Imagery
**arXiv**：[2511.19134v1](https://arxiv.org/abs/2511.19134) · [PDF](https://arxiv.org/pdf/2511.19134.pdf)  
**作者**：Shuyu Cao, Minxin Chen, Yucheng Song, Zhaozhong Chen, Xinyou Zhang  

**一句话要点**：提出MambaRefine-YOLO以解决无人机图像中小物体检测的挑战

**关键词**：小物体检测, 无人机图像, 双模态融合, YOLO改进, 特征增强, 实时应用

## 3 点简述
- 核心问题：无人机图像中小物体检测受低分辨率和背景杂波影响，现有方法难以平衡跨模态交互与计算效率。
- 方法要点：引入DGC-MFM模块通过光照和差异感知门控机制自适应融合RGB和红外模态，HFAN采用“精炼后融合”策略增强多尺度特征。
- 实验或效果：在DroneVehicle数据集上mAP达83.2%，提升7.9%；VisDrone数据集上仅用HFAN也显著改进，平衡精度与速度。

## 摘要（原文）

> Small object detection in Unmanned Aerial Vehicle (UAV) imagery is a persistent challenge, hindered by low resolution and background clutter. While fusing RGB and infrared (IR) data offers a promising solution, existing methods often struggle with the trade-off between effective cross-modal interaction and computational efficiency. In this letter, we introduce MambaRefine-YOLO. Its core contributions are a Dual-Gated Complementary Mamba fusion module (DGC-MFM) that adaptively balances RGB and IR modalities through illumination-aware and difference-aware gating mechanisms, and a Hierarchical Feature Aggregation Neck (HFAN) that uses a ``refine-then-fuse'' strategy to enhance multi-scale features. Our comprehensive experiments validate this dual-pronged approach. On the dual-modality DroneVehicle dataset, the full model achieves a state-of-the-art mAP of 83.2%, an improvement of 7.9% over the baseline. On the single-modality VisDrone dataset, a variant using only the HFAN also shows significant gains, demonstrating its general applicability. Our work presents a superior balance between accuracy and speed, making it highly suitable for real-world UAV applications.

