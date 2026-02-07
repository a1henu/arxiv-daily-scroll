---
layout: default
title: Unified Sensor Simulation for Autonomous Driving
---

# Unified Sensor Simulation for Autonomous Driving
**arXiv**：[2602.05617v1](https://arxiv.org/abs/2602.05617) · [PDF](https://arxiv.org/pdf/2602.05617.pdf)  
**作者**：Nikolay Patakin, Arsenii Shirokov, Anton Konushin, Dmitry Senushkin  

**一句话要点**：提出XSIM传感器模拟框架，通过扩展3DGUT splatting解决自动驾驶中球形相机投影问题。

**关键词**：传感器模拟, 自动驾驶, 3DGUT splatting, 球形相机, 相位建模, 3D高斯表示

## 3 点简述
- 核心问题：现有3DGUT splatting在球形相机（如LiDAR）上因方位边界循环投影和时间不连续导致粒子投影错误。
- 方法要点：引入相位建模机制处理方位边界的高斯投影不连续，并扩展3D高斯表示以解决几何与颜色分布不匹配。
- 实验或效果：在Waymo、Argoverse 2和PandaSet等数据集上评估，性能优于基线，达到最先进水平。

## 摘要（原文）

> In this work, we introduce \textbf{XSIM}, a sensor simulation framework for autonomous driving. XSIM extends 3DGUT splatting with a generalized rolling-shutter modeling tailored for autonomous driving applications. Our framework provides a unified and flexible formulation for appearance and geometric sensor modeling, enabling rendering of complex sensor distortions in dynamic environments. We identify spherical cameras, such as LiDARs, as a critical edge case for existing 3DGUT splatting due to cyclic projection and time discontinuities at azimuth boundaries leading to incorrect particle projection. To address this issue, we propose a phase modeling mechanism that explicitly accounts temporal and shape discontinuities of Gaussians projected by the Unscented Transform at azimuth borders. In addition, we introduce an extended 3D Gaussian representation that incorporates two distinct opacity parameters to resolve mismatches between geometry and color distributions. As a result, our framework provides enhanced scene representations with improved geometric consistency and photorealistic appearance. We evaluate our framework extensively on multiple autonomous driving datasets, including Waymo Open Dataset, Argoverse 2, and PandaSet. Our framework consistently outperforms strong recent baselines and achieves state-of-the-art performance across all datasets. The source code is publicly available at \href{https://github.com/whesense/XSIM}{https://github.com/whesense/XSIM}.

