---
layout: default
title: YOLO and SGBM Integration for Autonomous Tree Branch Detection and Depth Estimation in Radiata Pine Pruning Applications
---

# YOLO and SGBM Integration for Autonomous Tree Branch Detection and Depth Estimation in Radiata Pine Pruning Applications
**arXiv**：[2512.05412v1](https://arxiv.org/abs/2512.05412) · [PDF](https://arxiv.org/pdf/2512.05412.pdf)  
**作者**：Yida Lin, Bing Xue, Mengjie Zhang, Sam Schofield, Richard Green  

**一句话要点**：提出集成YOLO与SGBM的计算机视觉框架，用于辐射松修剪中的自主树枝检测与深度估计。

**关键词**：自主修剪, YOLO检测, SGBM立体视觉, 深度估计, 计算机视觉框架, 林业应用

## 3 点简述
- 核心问题：手动修剪辐射松树存在高空和复杂地形带来的安全风险。
- 方法要点：结合YOLO目标检测和SGBM立体视觉，仅用立体相机实现精确树枝定位。
- 实验或效果：YOLO在分支分割上达到82.0% mAPmask50-95，系统在2米范围内准确定位，每帧处理时间小于1秒。

## 摘要（原文）

> Manual pruning of radiata pine trees poses significant safety risks due to extreme working heights and challenging terrain. This paper presents a computer vision framework that integrates YOLO object detection with Semi-Global Block Matching (SGBM) stereo vision for autonomous drone-based pruning operations. Our system achieves precise branch detection and depth estimation using only stereo camera input, eliminating the need for expensive LiDAR sensors. Experimental evaluation demonstrates YOLO's superior performance over Mask R-CNN, achieving 82.0% mAPmask50-95 for branch segmentation. The integrated system accurately localizes branches within a 2 m operational range, with processing times under one second per frame. These results establish the feasibility of cost-effective autonomous pruning systems that enhance worker safety and operational efficiency in commercial forestry.

