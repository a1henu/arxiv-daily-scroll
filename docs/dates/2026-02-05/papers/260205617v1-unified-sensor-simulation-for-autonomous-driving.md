---
layout: default
title: Unified Sensor Simulation for Autonomous Driving
---

# Unified Sensor Simulation for Autonomous Driving
**arXiv**：[2602.05617v1](https://arxiv.org/abs/2602.05617) · [PDF](https://arxiv.org/pdf/2602.05617.pdf)  
**作者**：Nikolay Patakin, Arsenii Shirokov, Anton Konushin, Dmitry Senushkin  

**一句话要点**：提出XSIM框架以解决自动驾驶中传感器模拟的几何与外观失真问题

**关键词**：传感器模拟, 自动驾驶, 3DGUT splatting, 几何一致性, 外观建模, 球形相机

## 3 点简述
- 核心问题：现有3DGUT splatting在球形相机（如LiDAR）模拟中存在投影错误和时间不连续性问题
- 方法要点：扩展3DGUT splatting，引入相位建模机制和双不透明度参数以增强几何一致性和外观真实感
- 实验或效果：在Waymo等数据集上评估，性能优于基线，达到最先进水平

## 摘要（原文）

> In this work, we introduce \textbf{XSIM}, a sensor simulation framework for autonomous driving. XSIM extends 3DGUT splatting with a generalized rolling-shutter modeling tailored for autonomous driving applications. Our framework provides a unified and flexible formulation for appearance and geometric sensor modeling, enabling rendering of complex sensor distortions in dynamic environments. We identify spherical cameras, such as LiDARs, as a critical edge case for existing 3DGUT splatting due to cyclic projection and time discontinuities at azimuth boundaries leading to incorrect particle projection. To address this issue, we propose a phase modeling mechanism that explicitly accounts temporal and shape discontinuities of Gaussians projected by the Unscented Transform at azimuth borders. In addition, we introduce an extended 3D Gaussian representation that incorporates two distinct opacity parameters to resolve mismatches between geometry and color distributions. As a result, our framework provides enhanced scene representations with improved geometric consistency and photorealistic appearance. We evaluate our framework extensively on multiple autonomous driving datasets, including Waymo Open Dataset, Argoverse 2, and PandaSet. Our framework consistently outperforms strong recent baselines and achieves state-of-the-art performance across all datasets. The source code is publicly available at \href{https://github.com/whesense/XSIM}{https://github.com/whesense/XSIM}.

