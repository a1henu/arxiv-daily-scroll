---
layout: default
title: Enhancing Inverse Perspective Mapping for Automatic Vectorized Road Map Generation
---

# Enhancing Inverse Perspective Mapping for Automatic Vectorized Road Map Generation
**arXiv**：[2601.19536v1](https://arxiv.org/abs/2601.19536) · [PDF](https://arxiv.org/pdf/2601.19536.pdf)  
**作者**：Hongji Liu, Linwei Zheng, Yongjian Li, Mingkai Tang, Xiaoyang Yan, Ming Liu, Jun Ma  

**一句话要点**：提出增强逆透视映射框架以自动生成高精度矢量道路地图

**关键词**：逆透视映射, 矢量道路制图, 实例分割, 位姿优化, 高精度地图

## 3 点简述
- 核心问题：逆透视映射在矢量道路制图中存在误差和共面性假设限制
- 方法要点：利用Catmull-Rom样条和多边形表征道路元素，结合实例分割优化控制点和位姿
- 实验或效果：在两种实际场景中测试，实现近厘米级精度，优化后矩阵精度接近人工校准

## 摘要（原文）

> In this study, we present a low-cost and unified framework for vectorized road mapping leveraging enhanced inverse perspective mapping (IPM). In this framework, Catmull-Rom splines are utilized to characterize lane lines, and all the other ground markings are depicted using polygons uniformly. The results from instance segmentation serve as references to refine the three-dimensional position of spline control points and polygon corner points. In conjunction with this process, the homography matrix of IPM and vehicle poses are optimized simultaneously. Our proposed framework significantly reduces the mapping errors associated with IPM. It also improves the accuracy of the initial IPM homography matrix and the predicted vehicle poses. Furthermore, it addresses the limitations imposed by the coplanarity assumption in IPM. These enhancements enable IPM to be effectively applied to vectorized road mapping, which serves a cost-effective solution with enhanced accuracy. In addition, our framework generalizes road map elements to include all common ground markings and lane lines. The proposed framework is evaluated in two different practical scenarios, and the test results show that our method can automatically generate high-precision maps with near-centimeter-level accuracy. Importantly, the optimized IPM matrix achieves an accuracy comparable to that of manual calibration, while the accuracy of vehicle poses is also significantly improved.

