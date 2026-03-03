---
layout: default
title: YCDa: YCbCr Decoupled Attention for Real-time Realistic Camouflaged Object Detection
---

# YCDa: YCbCr Decoupled Attention for Real-time Realistic Camouflaged Object Detection
**arXiv**：[2603.01602v1](https://arxiv.org/abs/2603.01602) · [PDF](https://arxiv.org/pdf/2603.01602.pdf)  
**作者**：PeiHuang Zheng, Yunlong Zhao, Zheng Cui, Yang Li  

**一句话要点**：提出YCDa策略，通过解耦颜色与亮度信息并动态分配注意力，提升实时伪装物体检测性能。

**关键词**：伪装物体检测, 实时检测, 注意力机制, YCbCr解耦, 特征处理, 性能提升

## 3 点简述
- 核心问题：伪装物体检测中颜色线索不可靠时，需增强亮度与纹理信息以提高感知鲁棒性。
- 方法要点：在输入阶段分离YCbCr颜色与亮度信息，动态调整通道注意力以抑制颜色噪声并放大判别性线索。
- 实验或效果：YCDa可即插即用集成到现有检测器，在COD-D数据集上显著提升mAP，如YCDa-YOLO12s在COD10K-D上mAP提升112%。

## 摘要（原文）

> Human vision exhibits remarkable adaptability in perceiving objects under camouflage. When color cues become unreliable, the visual system instinctively shifts its reliance from chrominance (color) to luminance (brightness and texture), enabling more robust perception in visually confusing environments. Drawing inspiration from this biological mechanism, we propose YCDa, an efficient early-stage feature processing strategy that embeds this "chrominance-luminance decoupling and dynamic attention" principle into modern real-time detectors. Specifically, YCDa separates color and luminance information in the input stage and dynamically allocates attention across channels to amplify discriminative cues while suppressing misleading color noise. The strategy is plug-and-play and can be integrated into existing detectors by simply replacing the first downsampling layer. Extensive experiments on multiple baselines demonstrate that YCDa consistently improves performance with negligible overhead as shown in Fig. Notably, YCDa-YOLO12s achieves a 112% improvement in mAP over the baseline on COD10K-D and sets new state-of-the-art results for real-time camouflaged object detection across COD-D datasets.

