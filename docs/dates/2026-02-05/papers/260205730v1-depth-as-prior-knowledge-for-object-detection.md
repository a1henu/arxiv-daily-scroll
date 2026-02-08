---
layout: default
title: Depth as Prior Knowledge for Object Detection
---

# Depth as Prior Knowledge for Object Detection
**arXiv**：[2602.05730v1](https://arxiv.org/abs/2602.05730) · [PDF](https://arxiv.org/pdf/2602.05730.pdf)  
**作者**：Moussa Kassem Sbeyti, Nadja Klein  

**一句话要点**：提出DepthPrior框架，利用深度作为先验知识提升小目标检测性能，无需修改检测器架构。

**关键词**：小目标检测, 深度先验, 损失加权, 置信度阈值, 无架构修改, 安全关键应用

## 3 点简述
- 核心问题：小目标和远距离物体检测因尺度变化、低分辨率和背景干扰而困难，影响安全关键应用。
- 方法要点：通过深度信息作为先验知识，引入训练时的深度损失加权与分层，以及推理时的深度感知置信度阈值。
- 实验或效果：在多个基准和检测器上验证，小目标mAP提升达9%，推理恢复率高达95:1，无额外传感器或架构修改。

## 摘要（原文）

> Detecting small and distant objects remains challenging for object detectors due to scale variation, low resolution, and background clutter. Safety-critical applications require reliable detection of these objects for safe planning. Depth information can improve detection, but existing approaches require complex, model-specific architectural modifications. We provide a theoretical analysis followed by an empirical investigation of the depth-detection relationship. Together, they explain how depth causes systematic performance degradation and why depth-informed supervision mitigates it. We introduce DepthPrior, a framework that uses depth as prior knowledge rather than as a fused feature, providing comparable benefits without modifying detector architectures. DepthPrior consists of Depth-Based Loss Weighting (DLW) and Depth-Based Loss Stratification (DLS) during training, and Depth-Aware Confidence Thresholding (DCT) during inference. The only overhead is the initial cost of depth estimation. Experiments across four benchmarks (KITTI, MS COCO, VisDrone, SUN RGB-D) and two detectors (YOLOv11, EfficientDet) demonstrate the effectiveness of DepthPrior, achieving up to +9% mAP$_S$ and +7% mAR$_S$ for small objects, with inference recovery rates as high as 95:1 (true vs. false detections). DepthPrior offers these benefits without additional sensors, architectural changes, or performance costs. Code is available at https://github.com/mos-ks/DepthPrior.

