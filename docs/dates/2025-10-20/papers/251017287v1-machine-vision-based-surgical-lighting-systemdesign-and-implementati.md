---
layout: default
title: Machine Vision-Based Surgical Lighting System:Design and Implementation
---

# Machine Vision-Based Surgical Lighting System:Design and Implementation
**arXiv**：[2510.17287v1](https://arxiv.org/abs/2510.17287) · [PDF](https://arxiv.org/pdf/2510.17287.pdf)  
**作者**：Amir Gharghabi, Mahdi Hakiminezhad, Maryam Shafaei, Shaghayegh Gharghabi  

**一句话要点**：提出基于YOLOv11的自动手术照明系统以解决手动调整导致的疲劳和照明不一致问题

**关键词**：手术照明系统, YOLOv11目标检测, 伺服电机控制, 机器视觉应用, 医疗自动化

## 3 点简述
- 传统手术照明系统依赖手动调整，易导致外科医生疲劳、颈部劳损和照明漂移阴影问题
- 使用YOLOv11算法检测蓝色标记，通过伺服电机控制LED光源自动对准目标位置
- 在模拟手术场景验证集上，YOLO模型达到96.7% mAP@50，提升照明一致性和手术效果

## 摘要（原文）

> Effortless and ergonomically designed surgical lighting is critical for
> precision and safety during procedures. However, traditional systems often rely
> on manual adjustments, leading to surgeon fatigue, neck strain, and
> inconsistent illumination due to drift and shadowing. To address these
> challenges, we propose a novel surgical lighting system that leverages the
> YOLOv11 object detection algorithm to identify a blue marker placed above the
> target surgical site. A high-power LED light source is then directed to the
> identified location using two servomotors equipped with tilt-pan brackets. The
> YOLO model achieves 96.7% mAP@50 on the validation set consisting of annotated
> images simulating surgical scenes with the blue spherical marker. By automating
> the lighting process, this machine vision-based solution reduces physical
> strain on surgeons, improves consistency in illumination, and supports improved
> surgical outcomes.

