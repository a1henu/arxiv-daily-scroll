---
layout: default
title: Depth to Anatomy: Learning Internal Organ Locations from Surface Depth Images
---

# Depth to Anatomy: Learning Internal Organ Locations from Surface Depth Images
**arXiv**：[2601.18260v1](https://arxiv.org/abs/2601.18260) · [PDF](https://arxiv.org/pdf/2601.18260.pdf)  
**作者**：Eytan Kats, Kai Geissler, Daniel Mensing, Jochen G. Hirsch, Stefan Heldman, Mattias P. Heinrich  

**一句话要点**：提出基于深度学习的框架，从体表深度图像预测内部器官位置，以优化放射学扫描中的患者定位。

**关键词**：深度图像分析, 器官定位, 卷积神经网络, 放射学自动化, 患者定位优化

## 3 点简述
- 核心问题：自动化患者定位在放射学扫描中至关重要，但传统方法依赖表面重建，效率低。
- 方法要点：利用大规模全身MRI数据集合成深度图像，训练卷积神经网络直接预测多器官的3D位置和形状。
- 实验或效果：方法能准确定位骨骼和软组织，无需显式表面重建，展示了深度传感器集成到工作流的潜力。

## 摘要（原文）

> Automated patient positioning plays an important role in optimizing scanning procedure and improving patient throughput. Leveraging depth information captured by RGB-D cameras presents a promising approach for estimating internal organ positions, thereby enabling more accurate and efficient positioning. In this work, we propose a learning-based framework that directly predicts the 3D locations and shapes of multiple internal organs from single 2D depth images of the body surface. Utilizing a large-scale dataset of full-body MRI scans, we synthesize depth images paired with corresponding anatomical segmentations to train a unified convolutional neural network architecture. Our method accurately localizes a diverse set of anatomical structures, including bones and soft tissues, without requiring explicit surface reconstruction. Experimental results demonstrate the potential of integrating depth sensors into radiology workflows to streamline scanning procedures and enhance patient experience through automated patient positioning.

