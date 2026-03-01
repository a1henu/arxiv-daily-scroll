---
layout: default
title: SPMamba-YOLO: An Underwater Object Detection Network Based on Multi-Scale Feature Enhancement and Global Context Modeling
---

# SPMamba-YOLO: An Underwater Object Detection Network Based on Multi-Scale Feature Enhancement and Global Context Modeling
**arXiv**：[2602.22674v1](https://arxiv.org/abs/2602.22674) · [PDF](https://arxiv.org/pdf/2602.22674.pdf)  
**作者**：Guanghao Liao, Zhen Liu, Liyuan Cao, Yonghui Yang, Qi Li  

**一句话要点**：提出SPMamba-YOLO网络，通过多尺度特征增强和全局上下文建模提升水下目标检测性能。

**关键词**：水下目标检测, 多尺度特征增强, 全局上下文建模, 状态空间模型, YOLO网络

## 3 点简述
- 核心问题：水下目标检测面临光线衰减、颜色失真、背景杂乱和小目标等挑战。
- 方法要点：集成SPPELAN模块增强多尺度特征聚合，PSA机制提升特征判别力，Mamba模块捕获长程依赖。
- 实验或效果：在URPC2022数据集上，mAP@0.5比YOLOv8n提升超过4.9%，尤其对小而密集目标有效。

## 摘要（原文）

> Underwater object detection is a critical yet challenging research problem owing to severe light attenuation, color distortion, background clutter, and the small scale of underwater targets. To address these challenges, we propose SPMamba-YOLO, a novel underwater object detection network that integrates multi-scale feature enhancement with global context modeling. Specifically, a Spatial Pyramid Pooling Enhanced Layer Aggregation Network (SPPELAN) module is introduced to strengthen multi-scale feature aggregation and expand the receptive field, while a Pyramid Split Attention (PSA) mechanism enhances feature discrimination by emphasizing informative regions and suppressing background interference. In addition, a Mamba-based state space modeling module is incorporated to efficiently capture long-range dependencies and global contextual information, thereby improving detection robustness in complex underwater environments. Extensive experiments on the URPC2022 dataset demonstrate that SPMamba-YOLO outperforms the YOLOv8n baseline by more than 4.9\% in mAP@0.5, particularly for small and densely distributed underwater objects, while maintaining a favorable balance between detection accuracy and computational cost.

