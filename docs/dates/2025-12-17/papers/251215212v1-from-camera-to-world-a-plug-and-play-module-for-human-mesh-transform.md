---
layout: default
title: From Camera to World: A Plug-and-Play Module for Human Mesh Transformation
---

# From Camera to World: A Plug-and-Play Module for Human Mesh Transformation
**arXiv**：[2512.15212v1](https://arxiv.org/abs/2512.15212) · [PDF](https://arxiv.org/pdf/2512.15212.pdf)  
**作者**：Changhai Ma, Ziyu Wu, Yunkang Zhang, Qijun Ying, Boyan Liu, Xiaohui Cai  

**一句话要点**：提出Mesh-Plug模块，通过人体中心方法从相机坐标转换到世界坐标以解决相机旋转未知问题

**关键词**：3D人体重建, 相机坐标转换, 网格调整, 深度图渲染, 人体中心方法, 世界坐标系

## 3 点简述
- 核心问题：从野外图像重建世界坐标系下的3D人体网格时，缺乏相机旋转信息导致转换误差显著
- 方法要点：利用RGB图像和深度图，基于人体空间配置预测相机俯仰角，并调整根关节方向和姿态
- 实验或效果：在SPEC-SYN和SPEC-MTP数据集上优于现有方法，验证了模块的有效性

## 摘要（原文）

> Reconstructing accurate 3D human meshes in the world coordinate system from in-the-wild images remains challenging due to the lack of camera rotation information. While existing methods achieve promising results in the camera coordinate system by assuming zero camera rotation, this simplification leads to significant errors when transforming the reconstructed mesh to the world coordinate system. To address this challenge, we propose Mesh-Plug, a plug-and-play module that accurately transforms human meshes from camera coordinates to world coordinates. Our key innovation lies in a human-centered approach that leverages both RGB images and depth maps rendered from the initial mesh to estimate camera rotation parameters, eliminating the dependency on environmental cues. Specifically, we first train a camera rotation prediction module that focuses on the human body's spatial configuration to estimate camera pitch angle. Then, by integrating the predicted camera parameters with the initial mesh, we design a mesh adjustment module that simultaneously refines the root joint orientation and body pose. Extensive experiments demonstrate that our framework outperforms state-of-the-art methods on the benchmark datasets SPEC-SYN and SPEC-MTP.

