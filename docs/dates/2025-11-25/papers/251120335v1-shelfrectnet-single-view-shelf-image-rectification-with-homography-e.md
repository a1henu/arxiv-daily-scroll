---
layout: default
title: ShelfRectNet: Single View Shelf Image Rectification with Homography Estimation
---

# ShelfRectNet: Single View Shelf Image Rectification with Homography Estimation
**arXiv**：[2511.20335v1](https://arxiv.org/abs/2511.20335) · [PDF](https://arxiv.org/pdf/2511.20335.pdf)  
**作者**：Onur Berk Tore, Ibrahim Samil Yalciner, Server Calap  

**一句话要点**：提出ShelfRectNet以解决单视角货架图像校正问题

**关键词**：单应性估计, 图像校正, 深度学习, 零售视觉, 数据增强

## 3 点简述
- 核心问题：单图像单应性估计在零售监控中因视角限制而具挑战性
- 方法要点：使用ConvNeXt骨干网络和归一化坐标回归预测4点参数化单应性矩阵
- 实验或效果：在测试集上平均角点误差1.298像素，精度和推理速度具竞争力

## 摘要（原文）

> Estimating homography from a single image remains a challenging yet practically valuable task, particularly in domains like retail, where only one viewpoint is typically available for shelf monitoring and product alignment. In this paper, we present a deep learning framework that predicts a 4-point parameterized homography matrix to rectify shelf images captured from arbitrary angles. Our model leverages a ConvNeXt-based backbone for enhanced feature representation and adopts normalized coordinate regression for improved stability. To address data scarcity and promote generalization, we introduce a novel augmentation strategy by modeling and sampling synthetic homographies. Our method achieves a mean corner error of 1.298 pixels on the test set. When compared with both classical computer vision and deep learning-based approaches, our method demonstrates competitive performance in both accuracy and inference speed. Together, these results establish our approach as a robust and efficient solution for realworld single-view rectification. To encourage further research in this domain, we will make our dataset, ShelfRectSet, and code publicly available

