---
layout: default
title: D-FINE-seg: Object Detection and Instance Segmentation Framework with multi-backend deployment
---

# D-FINE-seg: Object Detection and Instance Segmentation Framework with multi-backend deployment
**arXiv**：[2602.23043v1](https://arxiv.org/abs/2602.23043) · [PDF](https://arxiv.org/pdf/2602.23043.pdf)  
**作者**：Argo Saakyan, Dmitry Solntsev  

**一句话要点**：提出D-FINE-seg框架，扩展D-FINE以实现实时实例分割与多后端部署优化。

**关键词**：实时实例分割, Transformer检测, 多后端部署, 掩码损失优化, 开源框架

## 3 点简述
- 核心问题：基于Transformer的实时实例分割方法较少，需平衡精度与延迟。
- 方法要点：添加轻量掩码头、分割感知训练（如BCE和Dice损失）及优化匹配成本。
- 实验或效果：在TACO数据集上，相比YOLO26提升F1分数，保持竞争性延迟，并提供开源多后端部署管道。

## 摘要（原文）

> Transformer-based real-time object detectors achieve strong accuracy-latency trade-offs, and D-FINE is among the top-performing recent architectures. However, real-time instance segmentation with transformers is still less common. We present D-FINE-seg, an instance segmentation extension of D-FINE that adds: a lightweight mask head, segmentation-aware training, including box cropped BCE and dice mask losses, auxiliary and denoising mask supervision, and adapted Hungarian matching cost. On the TACO dataset, D-FINE-seg improves F1-score over Ultralytics YOLO26 under a unified TensorRT FP16 end-to-end benchmarking protocol, while maintaining competitive latency. Second contribution is an end-to-end pipeline for training, exporting, and optimized inference across ONNX, TensorRT, OpenVINO for both object detection and instance segmentation tasks. This framework is released as open-source under the Apache-2.0 license. GitHub repository - https://github.com/ArgoHA/D-FINE-seg.

