---
layout: default
title: Region of interest detection for efficient aortic segmentation
---

# Region of interest detection for efficient aortic segmentation
**arXiv**：[2601.08683v1](https://arxiv.org/abs/2601.08683) · [PDF](https://arxiv.org/pdf/2601.08683.pdf)  
**作者**：Loris Giordano, Ine Dirks, Tom Lenaerts, Jef Vandemeulebroucke  

**一句话要点**：提出基于ROI检测的高效主动脉分割方法，以降低计算成本并提升临床适用性。

**关键词**：主动脉分割, ROI检测, 多任务学习, 编码器-解码器架构, 医学图像分析, 深度学习

## 3 点简述
- 核心问题：主动脉疾病诊断中，3D图像分割耗时且深度学习模型在复杂病例中效果有限。
- 方法要点：设计多任务检测模型，结合编码器-解码器分割和瓶颈层全连接网络进行ROI检测。
- 实验或效果：相比完整图像分割，计算资源减少三分之二，平均Dice系数达0.944，所有病例均超过0.9。

## 摘要（原文）

> Thoracic aortic dissection and aneurysms are the most lethal diseases of the aorta. The major hindrance to treatment lies in the accurate analysis of the medical images. More particularly, aortic segmentation of the 3D image is often tedious and difficult. Deep-learning-based segmentation models are an ideal solution, but their inability to deliver usable outputs in difficult cases and their computational cost cause their clinical adoption to stay limited. This study presents an innovative approach for efficient aortic segmentation using targeted region of interest (ROI) detection. In contrast to classical detection models, we propose a simple and efficient detection model that can be widely applied to detect a single ROI. Our detection model is trained as a multi-task model, using an encoder-decoder architecture for segmentation and a fully connected network attached to the bottleneck for detection. We compare the performance of a one-step segmentation model applied to a complete image, nnU-Net and our cascade model composed of a detection and a segmentation step. We achieve a mean Dice similarity coefficient of 0.944 with over 0.9 for all cases using a third of the computing power. This simple solution achieves state-of-the-art performance while being compact and robust, making it an ideal solution for clinical applications.

