---
layout: default
title: Motion-aware Event Suppression for Event Cameras
---

# Motion-aware Event Suppression for Event Cameras
**arXiv**：[2602.23204v1](https://arxiv.org/abs/2602.23204) · [PDF](https://arxiv.org/pdf/2602.23204.pdf)  
**作者**：Roberto Pellerito, Nico Messikommer, Giovanni Cioffi, Marco Cannici, Davide Scaramuzza  

**一句话要点**：提出运动感知事件抑制框架，实时过滤事件相机中的独立运动物体和自运动事件。

**关键词**：事件相机, 运动感知, 事件抑制, 实时处理, 视觉Transformer加速, 视觉里程计

## 3 点简述
- 核心问题：事件相机易受独立运动物体和自运动干扰，影响下游应用性能。
- 方法要点：联合分割当前事件流中的独立运动物体并预测其未来运动，实现前瞻性事件抑制。
- 实验或效果：在EVIMO基准上分割精度提升67%，推理速度达173 Hz，加速下游视觉Transformer推理83%。

## 摘要（原文）

> In this work, we introduce the first framework for Motion-aware Event Suppression, which learns to filter events triggered by IMOs and ego-motion in real time. Our model jointly segments IMOs in the current event stream while predicting their future motion, enabling anticipatory suppression of dynamic events before they occur. Our lightweight architecture achieves 173 Hz inference on consumer-grade GPUs with less than 1 GB of memory usage, outperforming previous state-of-the-art methods on the challenging EVIMO benchmark by 67\% in segmentation accuracy while operating at a 53\% higher inference rate. Moreover, we demonstrate significant benefits for downstream applications: our method accelerates Vision Transformer inference by 83\% via token pruning and improves event-based visual odometry accuracy, reducing Absolute Trajectory Error (ATE) by 13\%.

