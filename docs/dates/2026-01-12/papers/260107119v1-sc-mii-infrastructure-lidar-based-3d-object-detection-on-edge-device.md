---
layout: default
title: SC-MII: Infrastructure LiDAR-based 3D Object Detection on Edge Devices for Split Computing with Multiple Intermediate Outputs Integration
---

# SC-MII: Infrastructure LiDAR-based 3D Object Detection on Edge Devices for Split Computing with Multiple Intermediate Outputs Integration
**arXiv**：[2601.07119v1](https://arxiv.org/abs/2601.07119) · [PDF](https://arxiv.org/pdf/2601.07119.pdf)  
**作者**：Taisuke Noguchi, Takayuki Nishio, Takuya Azumi  

**一句话要点**：提出SC-MII方法，通过多基础设施LiDAR和分割计算在边缘设备上实现高效3D物体检测

**关键词**：3D物体检测, LiDAR点云, 分割计算, 边缘计算, 中间输出集成

## 3 点简述
- 核心问题：边缘设备部署3D物体检测模型面临高计算需求和单LiDAR盲点问题
- 方法要点：边缘设备处理初始DNN层，服务器集成中间输出完成推理，降低延迟和设备负载
- 实验或效果：真实数据集上实现2.19倍加速，边缘处理时间减少71.6%，精度下降最多1.09%

## 摘要（原文）

> 3D object detection using LiDAR-based point cloud data and deep neural networks is essential in autonomous driving technology. However, deploying state-of-the-art models on edge devices present challenges due to high computational demands and energy consumption. Additionally, single LiDAR setups suffer from blind spots. This paper proposes SC-MII, multiple infrastructure LiDAR-based 3D object detection on edge devices for Split Computing with Multiple Intermediate outputs Integration. In SC-MII, edge devices process local point clouds through the initial DNN layers and send intermediate outputs to an edge server. The server integrates these features and completes inference, reducing both latency and device load while improving privacy. Experimental results on a real-world dataset show a 2.19x speed-up and a 71.6% reduction in edge device processing time, with at most a 1.09% drop in accuracy.

