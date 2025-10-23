---
layout: default
title: Multi-Camera Worker Tracking in Logistics Warehouse Considering Wide-Angle Distortion
---

# Multi-Camera Worker Tracking in Logistics Warehouse Considering Wide-Angle Distortion
**arXiv**：[2510.19432v1](https://arxiv.org/abs/2510.19432) · [PDF](https://arxiv.org/pdf/2510.19432.pdf)  
**作者**：Yuki Mori, Kazuma Kano, Yusuke Asai, Shin Katayama, Kenta Urano, Takuro Yonezawa, Nobuo Kawaguchi  

**一句话要点**：提出基于多相机和脚部对齐的方法，以解决物流仓库中广角畸变下的工人跟踪问题。

**关键词**：多相机跟踪, 广角畸变校正, 物流仓库监控, 工人位置对齐, 数字孪生

## 3 点简述
- 核心问题：单相机视野有限，广角相机边缘畸变影响工人位置准确采集。
- 方法要点：使用19个广角相机，基于脚部位置对齐，减少图像畸变影响。
- 实验或效果：跟踪精度提升超过20%，验证了外观特征利用方法的有效性。

## 摘要（原文）

> With the spread of e-commerce, the logistics market is growing around the
> world. Therefore, improving the efficiency of warehouse operations is
> essential. To achieve this, various approaches have been explored, and among
> them, the use of digital twins is gaining attention. To make this approach
> possible, it is necessary to accurately collect the positions of workers in a
> warehouse and reflect them in a virtual space. However, a single camera has
> limitations in its field of view, therefore sensing with multiple cameras is
> necessary. In this study, we explored a method to track workers using 19
> wide-angle cameras installed on the ceiling, looking down at the floor of the
> logistics warehouse. To understand the relationship between the camera
> coordinates and the actual positions in the warehouse, we performed alignment
> based on the floor surface. However, due to the characteristics of wide-angle
> cameras, significant distortion occurs at the edges of the image, particularly
> in the vertical direction. To address this, the detected worker positions from
> each camera were aligned based on foot positions, reducing the effects of image
> distortion, and enabling accurate position alignment across cameras. As a
> result, we confirmed an improvement of over 20% in tracking accuracy.
> Furthermore, we compared multiple methods for utilizing appearance features and
> validated the effectiveness of the proposed approach.

