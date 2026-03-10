---
layout: default
title: FlowTouch: View-Invariant Visuo-Tactile Prediction
---

# FlowTouch: View-Invariant Visuo-Tactile Prediction
**arXiv**：[2603.08255v1](https://arxiv.org/abs/2603.08255) · [PDF](https://arxiv.org/pdf/2603.08255.pdf)  
**作者**：Seongjin Bien, Carlo Kneissl, Tobias Jülg, Frank Fundel, Thomas Ressler-Antal, Florian Walter, Björn Ommer, Gitta Kutyniok, Wolfram Burgard  

**一句话要点**：提出FlowTouch模型，通过局部3D网格实现视角不变的视觉-触觉预测，以解决触觉信息仅在接触时可用的问题。

**关键词**：视觉-触觉预测, 视角不变性, 局部3D网格, Flow Matching, 场景重建, 抓取稳定性

## 3 点简述
- 核心问题：触觉传感器仅在接触时提供反馈，限制了其在任务规划和初始执行阶段的应用。
- 方法要点：利用对象的局部3D网格编码信息，结合场景重建和基于Flow Matching的图像生成模型，实现视角不变的触觉预测。
- 实验或效果：模型能弥合仿真到现实的差距，泛化到新传感器实例，并可用于下游抓取稳定性预测。

## 摘要（原文）

> Tactile sensation is essential for contact-rich manipulation tasks. It provides direct feedback on object geometry, surface properties, and interaction forces, enhancing perception and enabling fine-grained control. An inherent limitation of tactile sensors is that readings are available only when an object is touched. This precludes their use during planning and the initial execution phase of a task. Predicting tactile information from visual information can bridge this gap. A common approach is to learn a direct mapping from camera images to the output of vision-based tactile sensors. However, the resulting model will depend strongly on the specific setup and on how well the camera can capture the area where an object is touched. In this work, we introduce FlowTouch, a novel model for view-invariant visuo-tactile prediction. Our key idea is to use an object's local 3D mesh to encode rich information for predicting tactile patterns while abstracting away from scene-dependent details. FlowTouch integrates scene reconstruction and Flow Matching-based models for image generation. Our results show that FlowTouch is able to bridge the sim-to-real gap and generalize to new sensor instances. We further show that the resulting tactile images can be used for downstream grasp stability prediction. Our code, datasets and videos are available at https://flowtouch.github.io/

