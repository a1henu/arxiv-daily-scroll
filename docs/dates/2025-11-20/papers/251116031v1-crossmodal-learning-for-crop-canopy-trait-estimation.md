---
layout: default
title: Crossmodal learning for Crop Canopy Trait Estimation
---

# Crossmodal learning for Crop Canopy Trait Estimation
**arXiv**：[2511.16031v1](https://arxiv.org/abs/2511.16031) · [PDF](https://arxiv.org/pdf/2511.16031.pdf)  
**作者**：Timilehin T. Ayanlade, Anirudha Powadi, Talukder Z. Jubery, Baskar Ganapathysubramanian, Soumik Sarkar  

**一句话要点**：提出跨模态学习策略，利用卫星图像生成无人机级细节以估计作物冠层性状

**关键词**：跨模态学习, 作物冠层性状估计, 卫星图像增强, 无人机图像, 农业监测, 光谱空间对应

## 3 点简述
- 卫星图像空间分辨率低，限制其在微地块管理农业中的应用
- 方法学习卫星与无人机图像间的精细光谱空间对应关系
- 生成图像在产量和氮预测任务中优于真实卫星图像

## 摘要（原文）

> Recent advances in plant phenotyping have driven widespread adoption of multi sensor platforms for collecting crop canopy reflectance data. This includes the collection of heterogeneous data across multiple platforms, with Unmanned Aerial Vehicles (UAV) seeing significant usage due to their high performance in crop monitoring, forecasting, and prediction tasks. Similarly, satellite missions have been shown to be effective for agriculturally relevant tasks. In contrast to UAVs, such missions are bound to the limitation of spatial resolution, which hinders their effectiveness for modern farming systems focused on micro-plot management. In this work, we propose a cross modal learning strategy that enriches high-resolution satellite imagery with UAV level visual detail for crop canopy trait estimation. Using a dataset of approximately co registered satellite UAV image pairs collected from replicated plots of 84 hybrid maize varieties across five distinct locations in the U.S. Corn Belt, we train a model that learns fine grained spectral spatial correspondences between sensing modalities. Results show that the generated UAV-like representations from satellite inputs consistently outperform real satellite imagery on multiple downstream tasks, including yield and nitrogen prediction, demonstrating the potential of cross-modal correspondence learning to bridge the gap between satellite and UAV sensing in agricultural monitoring.

