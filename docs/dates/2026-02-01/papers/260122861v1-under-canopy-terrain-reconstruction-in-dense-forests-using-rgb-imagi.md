---
layout: default
title: Under-Canopy Terrain Reconstruction in Dense Forests Using RGB Imaging and Neural 3D Reconstruction
---

# Under-Canopy Terrain Reconstruction in Dense Forests Using RGB Imaging and Neural 3D Reconstruction
**arXiv**：[2601.22861v1](https://arxiv.org/abs/2601.22861) · [PDF](https://arxiv.org/pdf/2601.22861.pdf)  
**作者**：Refael Sheffer, Chen Pinchover, Haim Zisman, Dror Ozeri, Roee Litman  

**一句话要点**：提出基于RGB图像与神经辐射场的森林冠层下地形重建方法，用于搜索救援与森林调查。

**关键词**：森林地形重建, 神经辐射场, RGB图像处理, 搜索救援, 森林调查, 遮挡去除

## 3 点简述
- 核心问题：密集森林冠层遮挡导致地面地形与林下植被难以用常规RGB图像重建。
- 方法要点：结合神经辐射场、低光照损失与射线积分控制，去除冠层遮挡并重建真实感地面视图。
- 实验或效果：在搜索救援任务中实现与热合成孔径摄影可比的人员检测，并展示树计数等森林调查潜力。

## 摘要（原文）

> Mapping the terrain and understory hidden beneath dense forest canopies is of great interest for numerous applications such as search and rescue, trail mapping, forest inventory tasks, and more. Existing solutions rely on specialized sensors: either heavy, costly airborne LiDAR, or Airborne Optical Sectioning (AOS), which uses thermal synthetic aperture photography and is tailored for person detection.
>   We introduce a novel approach for the reconstruction of canopy-free, photorealistic ground views using only conventional RGB images. Our solution is based on the celebrated Neural Radiance Fields (NeRF), a recent 3D reconstruction method. Additionally, we include specific image capture considerations, which dictate the needed illumination to successfully expose the scene beneath the canopy. To better cope with the poorly lit understory, we employ a low light loss. Finally, we propose two complementary approaches to remove occluding canopy elements by controlling per-ray integration procedure.
>   To validate the value of our approach, we present two possible downstream tasks. For the task of search and rescue (SAR), we demonstrate that our method enables person detection which achieves promising results compared to thermal AOS (using only RGB images). Additionally, we show the potential of our approach for forest inventory tasks like tree counting. These results position our approach as a cost-effective, high-resolution alternative to specialized sensors for SAR, trail mapping, and forest-inventory tasks.

