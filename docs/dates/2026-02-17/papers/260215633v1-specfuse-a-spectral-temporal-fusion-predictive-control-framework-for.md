---
layout: default
title: SpecFuse: A Spectral-Temporal Fusion Predictive Control Framework for UAV Landing on Oscillating Marine Platforms
---

# SpecFuse: A Spectral-Temporal Fusion Predictive Control Framework for UAV Landing on Oscillating Marine Platforms
**arXiv**：[2602.15633v1](https://arxiv.org/abs/2602.15633) · [PDF](https://arxiv.org/pdf/2602.15633.pdf)  
**作者**：Haichao Liu, Yufeng Hu, Shuang Wang, Kangjun Guo, Jun Ma, Jinni Zhou  

**一句话要点**：提出SpecFuse框架，通过谱时融合预测控制解决无人机在振荡海洋平台上的自主着陆问题。

**关键词**：无人机自主着陆, 谱时融合预测控制, 波浪谱建模, 分层控制架构, 海洋平台振荡, 运动预测优化

## 3 点简述
- 核心问题：无人机在海洋平台着陆受波浪多频振荡、风扰和预测滞后限制，现有方法性能不足。
- 方法要点：结合频域波浪分解与时域递归状态估计，实现高精度6自由度运动预测，并设计分层控制架构。
- 实验或效果：仿真和湖上实验显示预测误差3.2厘米，着陆偏差4.46厘米，成功率高达98.7%/87.5%，延迟82毫秒。

## 摘要（原文）

> Autonomous landing of Uncrewed Aerial Vehicles (UAVs) on oscillating marine platforms is severely constrained by wave-induced multi-frequency oscillations, wind disturbances, and prediction phase lags in motion prediction. Existing methods either treat platform motion as a general random process or lack explicit modeling of wave spectral characteristics, leading to suboptimal performance under dynamic sea conditions. To address these limitations, we propose SpecFuse: a novel spectral-temporal fusion predictive control framework that integrates frequency-domain wave decomposition with time-domain recursive state estimation for high-precision 6-DoF motion forecasting of Uncrewed Surface Vehicles (USVs). The framework explicitly models dominant wave harmonics to mitigate phase lags, refining predictions in real time via IMU data without relying on complex calibration. Additionally, we design a hierarchical control architecture featuring a sampling-based HPO-RRT* algorithm for dynamic trajectory planning under non-convex constraints and a learning-augmented predictive controller that fuses data-driven disturbance compensation with optimization-based execution. Extensive validations (2,000 simulations + 8 lake experiments) show our approach achieves a 3.2 cm prediction error, 4.46 cm landing deviation, 98.7% / 87.5% success rates (simulation / real-world), and 82 ms latency on embedded hardware, outperforming state-of-the-art methods by 44%-48% in accuracy. Its robustness to wave-wind coupling disturbances supports critical maritime missions such as search and rescue and environmental monitoring. All code, experimental configurations, and datasets will be released as open-source to facilitate reproducibility.

