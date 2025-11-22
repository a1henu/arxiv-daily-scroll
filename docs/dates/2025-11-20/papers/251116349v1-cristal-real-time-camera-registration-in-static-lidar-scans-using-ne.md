---
layout: default
title: CRISTAL: Real-time Camera Registration in Static LiDAR Scans using Neural Rendering
---

# CRISTAL: Real-time Camera Registration in Static LiDAR Scans using Neural Rendering
**arXiv**：[2511.16349v1](https://arxiv.org/abs/2511.16349) · [PDF](https://arxiv.org/pdf/2511.16349.pdf)  
**作者**：Joni Vanherck, Steven Moonen, Brent Zoomers, Kobe Werner, Jeroen Put, Lode Jorissen, Nick Michiels  

**一句话要点**：提出CRISTAL方法，在静态LiDAR点云中实现实时相机定位，解决漂移和尺度模糊问题。

**关键词**：相机定位, 神经渲染, LiDAR点云, 实时跟踪, 2D-3D对应

## 3 点简述
- 核心问题：现有视觉定位方法存在漂移、尺度模糊，依赖标记或闭环。
- 方法要点：使用神经渲染合成视图，建立2D-3D对应，减少合成与真实图像差异。
- 实验或效果：在ScanNet++数据集上优于现有SLAM，实现无漂移、正确尺度的跟踪。

## 摘要（原文）

> Accurate camera localization is crucial for robotics and Extended Reality (XR), enabling reliable navigation and alignment of virtual and real content. Existing visual methods often suffer from drift, scale ambiguity, and depend on fiducials or loop closure. This work introduces a real-time method for localizing a camera within a pre-captured, highly accurate colored LiDAR point cloud. By rendering synthetic views from this cloud, 2D-3D correspondences are established between live frames and the point cloud. A neural rendering technique narrows the domain gap between synthetic and real images, reducing occlusion and background artifacts to improve feature matching. The result is drift-free camera tracking with correct metric scale in the global LiDAR coordinate system. Two real-time variants are presented: Online Render and Match, and Prebuild and Localize. We demonstrate improved results on the ScanNet++ dataset and outperform existing SLAM pipelines.

