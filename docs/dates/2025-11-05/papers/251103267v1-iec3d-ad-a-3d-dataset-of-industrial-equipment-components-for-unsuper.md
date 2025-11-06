---
layout: default
title: IEC3D-AD: A 3D Dataset of Industrial Equipment Components for Unsupervised Point Cloud Anomaly Detection
---

# IEC3D-AD: A 3D Dataset of Industrial Equipment Components for Unsupervised Point Cloud Anomaly Detection
**arXiv**：[2511.03267v1](https://arxiv.org/abs/2511.03267) · [PDF](https://arxiv.org/pdf/2511.03267.pdf)  
**作者**：Bingyang Guo, Hongjie Li, Ruiyun Yu, Hanzhe Liang, Jinbao Wang  

**一句话要点**：提出IEC3D-AD数据集和GMANet方法以解决工业设备3D点云异常检测问题

**关键词**：3D点云异常检测, 工业设备组件, 几何形态分析, 合成数据生成, 空间差异优化

## 3 点简述
- 现有3D数据集无法捕捉工业设备复杂缺陷，限制异常检测研究
- 基于几何形态分析生成合成点云，优化空间差异以提升检测性能
- 在IEC3D-AD等数据集上实验验证方法有效性

## 摘要（原文）

> 3D anomaly detection (3D-AD) plays a critical role in industrial
> manufacturing, particularly in ensuring the reliability and safety of core
> equipment components. Although existing 3D datasets like Real3D-AD and MVTec
> 3D-AD offer broad application support, they fall short in capturing the
> complexities and subtle defects found in real industrial environments. This
> limitation hampers precise anomaly detection research, especially for
> industrial equipment components (IEC) such as bearings, rings, and bolts. To
> address this challenge, we have developed a point cloud anomaly detection
> dataset (IEC3D-AD) specific to real industrial scenarios. This dataset is
> directly collected from actual production lines, ensuring high fidelity and
> relevance. Compared to existing datasets, IEC3D-AD features significantly
> improved point cloud resolution and defect annotation granularity, facilitating
> more demanding anomaly detection tasks. Furthermore, inspired by generative
> 2D-AD methods, we introduce a novel 3D-AD paradigm (GMANet) on IEC3D-AD. This
> paradigm generates synthetic point cloud samples based on geometric
> morphological analysis, then reduces the margin and increases the overlap
> between normal and abnormal point-level features through spatial discrepancy
> optimization. Extensive experiments demonstrate the effectiveness of our method
> on both IEC3D-AD and other datasets.

