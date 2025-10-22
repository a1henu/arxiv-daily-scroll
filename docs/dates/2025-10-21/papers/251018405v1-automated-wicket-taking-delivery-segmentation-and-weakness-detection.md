---
layout: default
title: Automated Wicket-Taking Delivery Segmentation and Weakness Detection in Cricket Videos Using OCR-Guided YOLOv8 and Trajectory Modeling
---

# Automated Wicket-Taking Delivery Segmentation and Weakness Detection in Cricket Videos Using OCR-Guided YOLOv8 and Trajectory Modeling
**arXiv**：[2510.18405v1](https://arxiv.org/abs/2510.18405) · [PDF](https://arxiv.org/pdf/2510.18405.pdf)  
**作者**：Mst Jannatun Ferdous, Masum Billah, Joy Karmoker, Mohd Ruhul Ameen, Akif Islam, Md. Omar Faruqe  

**一句话要点**：提出基于OCR引导YOLOv8与轨迹建模的自动化板球视频分析系统，用于提取三柱门投球和检测击球弱点。

**关键词**：板球视频分析, YOLOv8目标检测, OCR文本提取, 球轨迹建模, 深度学习应用, 自动化弱点检测

## 3 点简述
- 核心问题：自动化分析板球视频以提取三柱门投球和检测击球弱点。
- 方法要点：使用YOLOv8检测球场和球，结合OCR提取记分牌，建模球轨迹。
- 实验或效果：球场检测mAP50达99.5%，球检测mAP50达99.18%，验证系统有效性。

## 摘要（原文）

> This paper presents an automated system for cricket video analysis that
> leverages deep learning techniques to extract wicket-taking deliveries, detect
> cricket balls, and model ball trajectories. The system employs the YOLOv8
> architecture for pitch and ball detection, combined with optical character
> recognition (OCR) for scorecard extraction to identify wicket-taking moments.
> Through comprehensive image preprocessing, including grayscale transformation,
> power transformation, and morphological operations, the system achieves robust
> text extraction from video frames. The pitch detection model achieved 99.5%
> mean Average Precision at 50% IoU (mAP50) with a precision of 0.999, while the
> ball detection model using transfer learning attained 99.18% mAP50 with 0.968
> precision and 0.978 recall. The system enables trajectory modeling on detected
> pitches, providing data-driven insights for identifying batting weaknesses.
> Experimental results on multiple cricket match videos demonstrate the
> effectiveness of this approach for automated cricket analytics, offering
> significant potential for coaching and strategic decision-making.

