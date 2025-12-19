---
layout: default
title: YOLO11-4K: An Efficient Architecture for Real-Time Small Object Detection in 4K Panoramic Images
---

# YOLO11-4K: An Efficient Architecture for Real-Time Small Object Detection in 4K Panoramic Images
**arXiv**：[2512.16493v1](https://arxiv.org/abs/2512.16493) · [PDF](https://arxiv.org/pdf/2512.16493.pdf)  
**作者**：Huma Hafeez, Matthew Garratt, Jo Plested, Sankaran Iyer, Arcot Sowmya  

**一句话要点**：提出YOLO11-4K以高效实时检测4K全景图像中的小物体

**关键词**：全景图像检测, 小物体检测, 实时检测, 4K分辨率, 多尺度检测, GhostConv

## 3 点简述
- 核心问题：4K全景图像因空间扭曲、宽视场和高分辨率，导致传统检测器计算负担重且小物体检测困难。
- 方法要点：采用多尺度检测头（含P2层）增强小物体敏感性，以及GhostConv骨干网络降低计算复杂度。
- 实验或效果：在CVIP360数据集上达到0.95 mAP（IoU 0.50），每帧推理时间28.3毫秒，比YOLO11快75%且精度更高。

## 摘要（原文）

> The processing of omnidirectional 360-degree images poses significant challenges for object detection due to inherent spatial distortions, wide fields of view, and ultra-high-resolution inputs. Conventional detectors such as YOLO are optimised for standard image sizes (for example, 640x640 pixels) and often struggle with the computational demands of 4K or higher-resolution imagery typical of 360-degree vision. To address these limitations, we introduce YOLO11-4K, an efficient real-time detection framework tailored for 4K panoramic images. The architecture incorporates a novel multi-scale detection head with a P2 layer to improve sensitivity to small objects often missed at coarser scales, and a GhostConv-based backbone to reduce computational complexity without sacrificing representational power. To enable evaluation, we manually annotated the CVIP360 dataset, generating 6,876 frame-level bounding boxes and producing a publicly available, detection-ready benchmark for 4K panoramic scenes. YOLO11-4K achieves 0.95 mAP at 0.50 IoU with 28.3 milliseconds inference per frame, representing a 75 percent latency reduction compared to YOLO11 (112.3 milliseconds), while also improving accuracy (mAP at 0.50 of 0.95 versus 0.908). This balance of efficiency and precision enables robust object detection in expansive 360-degree environments, making the framework suitable for real-world high-resolution panoramic applications. While this work focuses on 4K omnidirectional images, the approach is broadly applicable to high-resolution detection tasks in autonomous navigation, surveillance, and augmented reality.

