---
layout: default
title: REVNET: Rotation-Equivariant Point Cloud Completion via Vector Neuron Anchor Transformer
---

# REVNET: Rotation-Equivariant Point Cloud Completion via Vector Neuron Anchor Transformer
**arXiv**：[2601.08558v1](https://arxiv.org/abs/2601.08558) · [PDF](https://arxiv.org/pdf/2601.08558.pdf)  
**作者**：Zhifan Ni, Eckehard Steinbach  

**一句话要点**：提出REVNET以解决任意旋转下点云补全的鲁棒性问题

**关键词**：点云补全, 旋转等变性, 向量神经元网络, 锚点变换器, 三维视觉

## 3 点简述
- 问题：现有方法依赖规范姿态训练，旋转不变性差，限制实际应用。
- 方法：基于向量神经元网络，设计旋转等变锚点变换器，预测缺失锚点位置与特征。
- 效果：在合成数据集上优于现有方法，在真实数据集上无需姿态对齐即具竞争力。

## 摘要（原文）

> Incomplete point clouds captured by 3D sensors often result in the loss of both geometric and semantic information. Most existing point cloud completion methods are built on rotation-variant frameworks trained with data in canonical poses, limiting their applicability in real-world scenarios. While data augmentation with random rotations can partially mitigate this issue, it significantly increases the learning burden and still fails to guarantee robust performance under arbitrary poses. To address this challenge, we propose the Rotation-Equivariant Anchor Transformer (REVNET), a novel framework built upon the Vector Neuron (VN) network for robust point cloud completion under arbitrary rotations. To preserve local details, we represent partial point clouds as sets of equivariant anchors and design a VN Missing Anchor Transformer to predict the positions and features of missing anchors. Furthermore, we extend VN networks with a rotation-equivariant bias formulation and a ZCA-based layer normalization to improve feature expressiveness. Leveraging the flexible conversion between equivariant and invariant VN features, our model can generate point coordinates with greater stability. Experimental results show that our method outperforms state-of-the-art approaches on the synthetic MVP dataset in the equivariant setting. On the real-world KITTI dataset, REVNET delivers competitive results compared to non-equivariant networks, without requiring input pose alignment. The source code will be released on GitHub under URL: https://github.com/nizhf/REVNET.

