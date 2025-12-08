---
layout: default
title: A Residual Variance Matching Recursive Least Squares Filter for Real-time UAV Terrain Following
---

# A Residual Variance Matching Recursive Least Squares Filter for Real-time UAV Terrain Following
**arXiv**：[2512.05918v1](https://arxiv.org/abs/2512.05918) · [PDF](https://arxiv.org/pdf/2512.05918.pdf)  
**作者**：Xiaobo Wu, Youmin Zhang  

**一句话要点**：提出残差方差匹配递归最小二乘滤波器以解决无人机实时地形跟随中的航点估计问题

**关键词**：无人机地形跟随, 实时滤波, 残差方差匹配, 递归最小二乘, 航点估计, 野火巡逻

## 3 点简述
- 核心问题：现有实时滤波算法在非线性时变系统中难以在测量噪声下保持航点估计精度，影响飞行安全和野火检测。
- 方法要点：基于残差方差匹配估计准则，设计自适应滤波器以估计非线性时变无人机地形跟随系统的实时航点。
- 实验或效果：在模拟地形环境中验证，相比基准算法，航点估计精度提升约88%，展示了方法先进性和实用潜力。

## 摘要（原文）

> Accurate real-time waypoints estimation for the UAV-based online Terrain Following during wildfire patrol missions is critical to ensuring flight safety and enabling wildfire detection. However, existing real-time filtering algorithms struggle to maintain accurate waypoints under measurement noise in nonlinear and time-varying systems, posing risks of flight instability and missed wildfire detections during UAV-based terrain following. To address this issue, a Residual Variance Matching Recursive Least Squares (RVM-RLS) filter, guided by a Residual Variance Matching Estimation (RVME) criterion, is proposed to adaptively estimate the real-time waypoints of nonlinear, time-varying UAV-based terrain following systems. The proposed method is validated using a UAV-based online terrain following system within a simulated terrain environment. Experimental results show that the RVM-RLS filter improves waypoints estimation accuracy by approximately 88$\%$ compared with benchmark algorithms across multiple evaluation metrics. These findings demonstrate both the methodological advances in real-time filtering and the practical potential of the RVM-RLS filter for UAV-based online wildfire patrol.

