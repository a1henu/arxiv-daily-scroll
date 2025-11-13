---
layout: default
title: OG-PCL: Efficient Sparse Point Cloud Processing for Human Activity Recognition
---

# OG-PCL: Efficient Sparse Point Cloud Processing for Human Activity Recognition
**arXiv**：[2511.08910v1](https://arxiv.org/abs/2511.08910) · [PDF](https://arxiv.org/pdf/2511.08910.pdf)  
**作者**：Jiuqi Yan, Chendong Xu, Dongyu Liu  

**一句话要点**：提出OG-PCL网络以高效处理稀疏雷达点云用于人类活动识别

**关键词**：稀疏点云处理, 人类活动识别, 毫米波雷达, 轻量级网络, 三视图并行结构, 占用门控卷积

## 3 点简述
- 毫米波雷达点云稀疏，传统方法难以高效处理
- 采用三视图并行CNN和Bi-LSTM结构，结合占用门控卷积补偿稀疏性
- 在RadHAR数据集上准确率达91.75%，参数量仅0.83M，优于基线方法

## 摘要（原文）

> Human activity recognition (HAR) with millimeter-wave (mmWave) radar offers a privacy-preserving and robust alternative to camera- and wearable-based approaches. In this work, we propose the Occupancy-Gated Parallel-CNN Bi-LSTM (OG-PCL) network to process sparse 3D radar point clouds produced by mmWave sensing. Designed for lightweight deployment, the parameter size of the proposed OG-PCL is only 0.83M and achieves 91.75 accuracy on the RadHAR dataset, outperforming those existing baselines such as 2D CNN, PointNet, and 3D CNN methods. We validate the advantages of the tri-view parallel structure in preserving spatial information across three dimensions while maintaining efficiency through ablation studies. We further introduce the Occupancy-Gated Convolution (OGConv) block and demonstrate the necessity of its occupancy compensation mechanism for handling sparse point clouds. The proposed OG-PCL thus offers a compact yet accurate framework for real-time radar-based HAR on lightweight platforms.

