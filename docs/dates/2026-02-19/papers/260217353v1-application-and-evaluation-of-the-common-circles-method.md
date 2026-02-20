---
layout: default
title: Application and Evaluation of the Common Circles Method
---

# Application and Evaluation of the Common Circles Method
**arXiv**：[2602.17353v1](https://arxiv.org/abs/2602.17353) · [PDF](https://arxiv.org/pdf/2602.17353.pdf)  
**作者**：Michael Quellmalz, Mia Kvåle Løvmo, Simon Moser, Franziska Strasser, Monika Ritsch-Marte  

**一句话要点**：应用公共圆方法估计亚毫米生物组织光学衍射层析中的样本运动

**关键词**：光学衍射层析, 样本运动估计, 公共圆方法, Ewald球交点, 时间一致性约束, 计算高效

## 3 点简述
- 核心问题：亚毫米生物组织在无接触声学力场中运动，需从图像估计运动参数。
- 方法要点：利用傅里叶空间Ewald球交点识别旋转运动，加入时间一致性约束实现稳定重建。
- 实验或效果：模拟和真实数据验证公共圆方法为运动检测提供计算高效替代方案。

## 摘要（原文）

> We investigate the application of the common circle method for estimating sample motion in optical diffraction tomography (ODT) of sub-millimeter sized biological tissue. When samples are confined via contact-free acoustical force fields, their motion must be estimated from the captured images. The common circle method identifies intersections of Ewald spheres in Fourier space to determine rotational motion. This paper presents a practical implementation, incorporating temporal consistency constraints to achieve stable reconstructions. Our results on both simulated and real-world data demonstrate that the common circle method provides a computationally efficient alternative to full optimization methods for motion detection.

