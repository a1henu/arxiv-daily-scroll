---
layout: default
title: ROI-Packing: Efficient Region-Based Compression for Machine Vision
---

# ROI-Packing: Efficient Region-Based Compression for Machine Vision
**arXiv**：[2512.09258v1](https://arxiv.org/abs/2512.09258) · [PDF](https://arxiv.org/pdf/2512.09258.pdf)  
**作者**：Md Eimran Hossain Eimon, Alena Krause, Ashan Perera, Juan Merlos, Hari Kalva, Velibor Adzic, Borko Furht  

**一句话要点**：提出ROI-Packing方法，针对机器视觉任务实现高效图像压缩。

**关键词**：图像压缩, 机器视觉, 感兴趣区域, 目标检测, 实例分割, 压缩效率

## 3 点简述
- 核心问题：机器视觉中图像压缩需平衡压缩效率与任务准确性。
- 方法要点：优先压缩关键感兴趣区域，丢弃无关数据，无需模型重训练。
- 实验效果：在多个数据集上，相比VVC标准，压缩率提升44.10%，准确性提高8.88%。

## 摘要（原文）

> This paper introduces ROI-Packing, an efficient image compression method tailored specifically for machine vision. By prioritizing regions of interest (ROI) critical to end-task accuracy and packing them efficiently while discarding less relevant data, ROI-Packing achieves significant compression efficiency without requiring retraining or fine-tuning of end-task models. Comprehensive evaluations across five datasets and two popular tasks-object detection and instance segmentation-demonstrate up to a 44.10% reduction in bitrate without compromising end-task accuracy, along with an 8.88 % improvement in accuracy at the same bitrate compared to the state-of-the-art Versatile Video Coding (VVC) codec standardized by the Moving Picture Experts Group (MPEG).

