---
layout: default
title: Generic Camera Calibration using Blurry Images
---

# Generic Camera Calibration using Blurry Images
**arXiv**：[2603.05159v1](https://arxiv.org/abs/2603.05159) · [PDF](https://arxiv.org/pdf/2603.05159.pdf)  
**作者**：Zezhun Shi  

**一句话要点**：提出基于模糊图像的通用相机标定方法，利用几何约束和局部参数化光照模型解决特征定位与点扩散函数估计问题。

**关键词**：相机标定, 通用相机模型, 运动模糊, 点扩散函数, 几何约束, 图像去模糊

## 3 点简述
- 核心问题：通用相机标定需大量图像，易产生运动模糊，影响特征提取精度。
- 方法要点：结合几何约束和局部参数化光照模型，同时估计特征位置和空间变化点扩散函数，解决平移模糊问题。
- 实验或效果：实验结果验证了方法的有效性，提升了模糊图像下的标定准确性。

## 摘要（原文）

> Camera calibration is the foundation of 3D vision. Generic camera calibration can yield more accurate results than parametric cam era calibration. However, calibrating a generic camera model using printed calibration boards requires far more images than parametric calibration, making motion blur practically unavoidable for individual users. As a f irst attempt to address this problem, we draw on geometric constraints and a local parametric illumination model to simultaneously estimate feature locations and spatially varying point spread functions, while re solving the translational ambiguity that need not be considered in con ventional image deblurring tasks. Experimental results validate the effectiveness of our approach.

