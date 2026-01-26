---
layout: default
title: Using Shadows in Circular Synthetic Aperture Sonar Imaging for Target Analysis
---

# Using Shadows in Circular Synthetic Aperture Sonar Imaging for Target Analysis
**arXiv**：[2601.16733v1](https://arxiv.org/abs/2601.16733) · [PDF](https://arxiv.org/pdf/2601.16733.pdf)  
**作者**：Yann Le Gall, Nicolas Burlet, Mathieu Simon, Fabien Novella, Samantha Dugelay, Jean-Philippe Malkasse  

**一句话要点**：提出利用子孔径滤波和固定焦点阴影增强方法，从圆形合成孔径声纳数据中提取阴影信息以改进目标分析和三维重建。

**关键词**：圆形合成孔径声纳, 阴影增强, 三维重建, 目标识别, 子孔径滤波, 空间雕刻

## 3 点简述
- 核心问题：圆形合成孔径声纳处理中阴影信息丢失，影响目标识别和三维重建。
- 方法要点：采用子孔径滤波获取多视角图像，应用固定焦点阴影增强技术恢复清晰阴影。
- 实验或效果：通过空间雕刻方法从分割阴影推断三维形状，验证阴影在目标分析中的潜力。

## 摘要（原文）

> Circular Synthetic Aperture Sonar (CSAS) provides a 360° azimuth view of the seabed, surpassing the limited aperture and mono-view image of conventional side-scan SAS. This makes CSAS a valuable tool for target recognition in mine warfare where the diversity of point of view is essential for reducing false alarms. CSAS processing typically produces a very high-resolution two-dimensional image. However, the parallax introduced by the circular displacement of the illuminator fill-in the shadow regions, and the shadow cast by an object on the seafloor is lost in favor of azimuth coverage and resolution. Yet the shadows provide complementary information on target shape useful for target recognition. In this paper, we explore a way to retrieve shadow information from CSAS data to improve target analysis and carry 3D reconstruction. Sub-aperture filtering is used to get a collection of images at various points of view along the circular trajectory and fixed focus shadow enhancement (FFSE) is applied to obtain sharp shadows. An interactive interface is also proposed to allow human operators to visualize these shadows along the circular trajectory. A space-carving reconstruction method is applied to infer the 3D shape of the object from the segmented shadows. The results demonstrate the potential of shadows in circular SAS for improving target analysis and 3D reconstruction.

