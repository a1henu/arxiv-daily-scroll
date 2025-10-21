---
layout: default
title: Botany-Bot: Digital Twin Monitoring of Occluded and Underleaf Plant Structures with Gaussian Splats
---

# Botany-Bot: Digital Twin Monitoring of Occluded and Underleaf Plant Structures with Gaussian Splats
**arXiv**：[2510.17783v1](https://arxiv.org/abs/2510.17783) · [PDF](https://arxiv.org/pdf/2510.17783.pdf)  
**作者**：Simeon Adebola, Chung Min Kim, Justin Kerr, Shuangyu Xie, Prithvi Akella, Jose Luis Susa Rincon, Eugen Solowjow, Ken Goldberg  

**一句话要点**：提出Botany-Bot系统以解决植物叶片遮挡导致的细节感知问题

**关键词**：植物表型监测, 数字孪生, 高斯溅射, 机器人操作, 3D分割, 遮挡处理

## 3 点简述
- 核心问题：固定相机系统因叶片遮挡无法感知植物细节，如茎芽和叶片正反面
- 方法要点：使用立体相机、机器人臂和3D高斯溅射模型构建带注释的数字孪生
- 实验或效果：系统在叶片分割、检测、操作和图像采集任务中准确率达77.3%-90.8%

## 摘要（原文）

> Commercial plant phenotyping systems using fixed cameras cannot perceive many
> plant details due to leaf occlusion. In this paper, we present Botany-Bot, a
> system for building detailed "annotated digital twins" of living plants using
> two stereo cameras, a digital turntable inside a lightbox, an industrial robot
> arm, and 3D segmentated Gaussian Splat models. We also present robot algorithms
> for manipulating leaves to take high-resolution indexable images of occluded
> details such as stem buds and the underside/topside of leaves. Results from
> experiments suggest that Botany-Bot can segment leaves with 90.8% accuracy,
> detect leaves with 86.2% accuracy, lift/push leaves with 77.9% accuracy, and
> take detailed overside/underside images with 77.3% accuracy. Code, videos, and
> datasets are available at https://berkeleyautomation.github.io/Botany-Bot/.

