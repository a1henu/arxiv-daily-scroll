---
layout: default
title: Deep Hybrid Model for Region of Interest Detection in Omnidirectional Videos
---

# Deep Hybrid Model for Region of Interest Detection in Omnidirectional Videos
**arXiv**：[2511.18856v1](https://arxiv.org/abs/2511.18856) · [PDF](https://arxiv.org/pdf/2511.18856.pdf)  
**作者**：Sana Alamgeer  

**一句话要点**：提出混合显著性模型以预测360度视频中的感兴趣区域，优化流媒体带宽与观看体验。

**关键词**：360度视频, 感兴趣区域检测, 混合显著性模型, 视频流媒体优化, 头戴设备观看

## 3 点简述
- 核心问题：360度视频中感兴趣区域检测对带宽优化和头戴设备观看体验至关重要。
- 方法要点：设计混合显著性模型，包括预处理、模型预测和后处理步骤。
- 实验或效果：在360RAT数据集上评估模型性能，并与主观标注进行比较。

## 摘要（原文）

> The main goal of the project is to design a new model that predicts regions of interest in 360$^{\circ}$ videos. The region of interest (ROI) plays an important role in 360$^{\circ}$ video streaming. For example, ROIs are used to predict view-ports, intelligently cut the videos for live streaming, etc so that less bandwidth is used. Detecting view-ports in advance helps reduce the movement of the head while streaming and watching a video via the head-mounted device. Whereas, intelligent cuts of the videos help improve the efficiency of streaming the video to users and enhance the quality of their viewing experience. This report illustrates the secondary task to identify ROIs, in which, we design, train, and test a hybrid saliency model. In this work, we refer to saliency regions to represent the regions of interest. The method includes the processes as follows: preprocessing the video to obtain frames, developing a hybrid saliency model for predicting the region of interest, and finally post-processing the output predictions of the hybrid saliency model to obtain the output region of interest for each frame. Then, we compare the performance of the proposed method with the subjective annotations of the 360RAT dataset.

