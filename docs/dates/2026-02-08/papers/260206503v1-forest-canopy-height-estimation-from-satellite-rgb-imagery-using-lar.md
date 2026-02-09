---
layout: default
title: Forest canopy height estimation from satellite RGB imagery using large-scale airborne LiDAR-derived training data and monocular depth estimation
---

# Forest canopy height estimation from satellite RGB imagery using large-scale airborne LiDAR-derived training data and monocular depth estimation
**arXiv**：[2602.06503v1](https://arxiv.org/abs/2602.06503) · [PDF](https://arxiv.org/pdf/2602.06503.pdf)  
**作者**：Yongkang Lai, Xihan Mu, Tim R. McVicar, Dasheng Fan, Donghui Xie, Shanxin Guo, Wenli Huang, Tianjie Zhao, Guangjian Yan  

**一句话要点**：提出Depth2CHM模型，利用大规模机载LiDAR训练数据从卫星RGB图像估计森林冠层高度

**关键词**：森林冠层高度估计, 单目深度估计, 机载LiDAR, 卫星RGB图像, 大规模训练数据, 高分辨率制图

## 3 点简述
- 核心问题：现有星载LiDAR数据稀疏且不确定，难以实现高分辨率连续森林冠层高度制图
- 方法要点：使用约16,000 km²机载LiDAR冠层高度模型训练Depth Anything V2模型，从PlanetScope RGB图像直接估计高度
- 实验或效果：在中国和美国站点验证，偏差0.59 m和0.41 m，RMSE 2.54 m和5.75 m，优于现有全球产品

## 摘要（原文）

> Large-scale, high-resolution forest canopy height mapping plays a crucial role in understanding regional and global carbon and water cycles. Spaceborne LiDAR missions, including the Ice, Cloud, and Land Elevation Satellite-2 (ICESat-2) and the Global Ecosystem Dynamics Investigation (GEDI), provide global observations of forest structure but are spatially sparse and subject to inherent uncertainties. In contrast, near-surface LiDAR platforms, such as airborne and unmanned aerial vehicle (UAV) LiDAR systems, offer much finer measurements of forest canopy structure, and a growing number of countries have made these datasets openly available. In this study, a state-of-the-art monocular depth estimation model, Depth Anything V2, was trained using approximately 16,000 km2 of canopy height models (CHMs) derived from publicly available airborne LiDAR point clouds and related products across multiple countries, together with 3 m resolution PlanetScope and airborne RGB imagery. The trained model, referred to as Depth2CHM, enables the estimation of spatially continuous CHMs directly from PlanetScope RGB imagery. Independent validation was conducted at sites in China (approximately 1 km2) and the United States (approximately 116 km2). The results showed that Depth2CHM could accurately estimate canopy height, with biases of 0.59 m and 0.41 m and root mean square errors (RMSEs) of 2.54 m and 5.75 m for these two sites, respectively. Compared with an existing global meter-resolution CHM product, the mean absolute error is reduced by approximately 1.5 m and the RMSE by approximately 2 m. These results demonstrated that monocular depth estimation networks trained with large-scale airborne LiDAR-derived canopy height data provide a promising and scalable pathway for high-resolution, spatially continuous forest canopy height estimation from satellite RGB imagery.

