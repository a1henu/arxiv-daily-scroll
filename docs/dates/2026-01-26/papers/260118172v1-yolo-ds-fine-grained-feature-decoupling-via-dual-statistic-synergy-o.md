---
layout: default
title: YOLO-DS: Fine-Grained Feature Decoupling via Dual-Statistic Synergy Operator for Object Detection
---

# YOLO-DS: Fine-Grained Feature Decoupling via Dual-Statistic Synergy Operator for Object Detection
**arXiv**：[2601.18172v1](https://arxiv.org/abs/2601.18172) · [PDF](https://arxiv.org/pdf/2601.18172.pdf)  
**作者**：Lin Huang, Yujuan Tan, Weisheng Li, Shitai Shan, Liu Liu, Bo Liu, Linlin Shen, Jing Yu, Yue Niu  

**一句话要点**：提出YOLO-DS框架，通过双统计协同算子解决目标检测中异构对象响应建模不足的问题。

**关键词**：目标检测, YOLO系列, 特征解耦, 双统计协同算子, 轻量门控模块, MS-COCO基准

## 3 点简述
- 核心问题：现有YOLO检测器在共享特征通道中缺乏对异构对象响应的显式建模，限制性能提升。
- 方法要点：引入双统计协同算子，联合建模通道均值和峰均差，实现特征解耦，并设计轻量门控模块进行特征选择与加权。
- 实验或效果：在MS-COCO基准上，YOLO-DS在五个模型尺度上优于YOLOv8，AP提升1.1%至1.7%，推理延迟仅轻微增加。

## 摘要（原文）

> One-stage object detection, particularly the YOLO series, strikes a favorable balance between accuracy and efficiency. However, existing YOLO detectors lack explicit modeling of heterogeneous object responses within shared feature channels, which limits further performance gains. To address this, we propose YOLO-DS, a framework built around a novel Dual-Statistic Synergy Operator (DSO). The DSO decouples object features by jointly modeling the channel-wise mean and the peak-to-mean difference. Building upon the DSO, we design two lightweight gating modules: the Dual-Statistic Synergy Gating (DSG) module for adaptive channel-wise feature selection, and the Multi-Path Segmented Gating (MSG) module for depth-wise feature weighting. On the MS-COCO benchmark, YOLO-DS consistently outperforms YOLOv8 across five model scales (N, S, M, L, X), achieving AP gains of 1.1% to 1.7% with only a minimal increase in inference latency. Extensive visualization, ablation, and comparative studies validate the effectiveness of our approach, demonstrating its superior capability in discriminating heterogeneous objects with high efficiency.

