---
layout: default
title: AfroBeats Dance Movement Analysis Using Computer Vision: A Proof-of-Concept Framework Combining YOLO and Segment Anything Model
---

# AfroBeats Dance Movement Analysis Using Computer Vision: A Proof-of-Concept Framework Combining YOLO and Segment Anything Model
**arXiv**：[2512.03509v1](https://arxiv.org/abs/2512.03509) · [PDF](https://arxiv.org/pdf/2512.03509.pdf)  
**作者**：Kwaku Opoku-Ware, Gideon Opoku  

**一句话要点**：提出结合YOLO与SAM的框架，用于无标记自动分析非洲节拍舞蹈动作

**关键词**：舞蹈动作分析, 目标检测, 图像分割, 运动量化, 计算机视觉框架

## 3 点简述
- 核心问题：自动化舞蹈动作分析，无需专业设备或标记，量化视频中的舞者运动
- 方法要点：集成YOLOv8/v11检测舞者，SAM进行精确分割，实现动作跟踪与量化
- 实验或效果：在单视频测试中，检测精度约94%，分割IoU约83%，量化显示主舞者动作更频繁

## 摘要（原文）

> This paper presents a preliminary investigation into automated dance movement analysis using contemporary computer vision techniques. We propose a proof-of-concept framework that integrates YOLOv8 and v11 for dancer detection with the Segment Anything Model (SAM) for precise segmentation, enabling the tracking and quantification of dancer movements in video recordings without specialized equipment or markers. Our approach identifies dancers within video frames, counts discrete dance steps, calculates spatial coverage patterns, and measures rhythm consistency across performance sequences. Testing this framework on a single 49-second recording of Ghanaian AfroBeats dance demonstrates technical feasibility, with the system achieving approximately 94% detection precision and 89% recall on manually inspected samples. The pixel-level segmentation provided by SAM, achieving approximately 83% intersection-over-union with visual inspection, enables motion quantification that captures body configuration changes beyond what bounding-box approaches can represent. Analysis of this preliminary case study indicates that the dancer classified as primary by our system executed 23% more steps with 37% higher motion intensity and utilized 42% more performance space compared to dancers classified as secondary. However, this work represents an early-stage investigation with substantial limitations including single-video validation, absence of systematic ground truth annotations, and lack of comparison with existing pose estimation methods. We present this framework to demonstrate technical feasibility, identify promising directions for quantitative dance metrics, and establish a foundation for future systematic validation studies.

