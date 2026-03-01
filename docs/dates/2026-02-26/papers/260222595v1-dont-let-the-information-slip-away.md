---
layout: default
title: Don't let the information slip away
---

# Don't let the information slip away
**arXiv**：[2602.22595v1](https://arxiv.org/abs/2602.22595) · [PDF](https://arxiv.org/pdf/2602.22595.pdf)  
**作者**：Taozhe Li  

**一句话要点**：提出Association DETR以利用背景信息提升目标检测性能

**关键词**：目标检测, 背景信息利用, DETR模型, 上下文感知, COCO数据集

## 3 点简述
- 核心问题：现有模型忽略背景上下文信息，导致信息流失
- 方法要点：结合背景关联性，增强模型对场景的理解能力
- 实验或效果：在COCO val2017数据集上实现SOTA结果

## 摘要（原文）

> Real-time object detection has advanced rapidly in recent years. The YOLO series of detectors is among the most well-known CNN-based object detection models and cannot be overlooked. The latest version, YOLOv26, was recently released, while YOLOv12 achieved state-of-the-art (SOTA) performance with 55.2 mAP on the COCO val2017 dataset. Meanwhile, transformer-based object detection models, also known as DEtection TRansformer (DETR), have demonstrated impressive performance. RT-DETR is an outstanding model that outperformed the YOLO series in both speed and accuracy when it was released. Its successor, RT-DETRv2, achieved 53.4 mAP on the COCO val2017 dataset. However, despite their remarkable performance, all these models let information to slip away. They primarily focus on the features of foreground objects while neglecting the contextual information provided by the background. We believe that background information can significantly aid object detection tasks. For example, cars are more likely to appear on roads rather than in offices, while wild animals are more likely to be found in forests or remote areas rather than on busy streets. To address this gap, we propose an object detection model called Association DETR, which achieves state-of-the-art results compared to other object detection models on the COCO val2017 dataset.

