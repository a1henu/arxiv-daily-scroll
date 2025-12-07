---
layout: default
title: STeP-Diff: Spatio-Temporal Physics-Informed Diffusion Models for Mobile Fine-Grained Pollution Forecasting
---

# STeP-Diff: Spatio-Temporal Physics-Informed Diffusion Models for Mobile Fine-Grained Pollution Forecasting
**arXiv**：[2512.04385v1](https://arxiv.org/abs/2512.04385) · [PDF](https://arxiv.org/pdf/2512.04385.pdf)  
**作者**：Nan Zhou, Weijie Hong, Huandong Wang, Jianfeng Zheng, Qiuhua Wang, Yali Song, Xiao-Ping Zhang, Yong Li, Xinlei Chen  

**一句话要点**：提出STeP-Diff以解决移动平台细粒度污染预测中数据不完整与时空不一致问题。

**关键词**：细粒度污染预测, 扩散模型, 物理信息学习, 时空建模, 移动传感器数据

## 3 点简述
- 核心问题：移动传感器数据因平台随机移动导致不完整和时空不一致。
- 方法要点：结合DeepONet和PDE约束扩散模型，通过反过程训练预测时空场。
- 实验或效果：部署59个设备收集数据，模型在MAE、RMSE和MAPE上显著优于次优算法。

## 摘要（原文）

> Fine-grained air pollution forecasting is crucial for urban management and the development of healthy buildings. Deploying portable sensors on mobile platforms such as cars and buses offers a low-cost, easy-to-maintain, and wide-coverage data collection solution. However, due to the random and uncontrollable movement patterns of these non-dedicated mobile platforms, the resulting sensor data are often incomplete and temporally inconsistent. By exploring potential training patterns in the reverse process of diffusion models, we propose Spatio-Temporal Physics-Informed Diffusion Models (STeP-Diff). STeP-Diff leverages DeepONet to model the spatial sequence of measurements along with a PDE-informed diffusion model to forecast the spatio-temporal field from incomplete and time-varying data. Through a PDE-constrained regularization framework, the denoising process asymptotically converges to the convection-diffusion dynamics, ensuring that predictions are both grounded in real-world measurements and aligned with the fundamental physics governing pollution dispersion. To assess the performance of the system, we deployed 59 self-designed portable sensing devices in two cities, operating for 14 days to collect air pollution data. Compared to the second-best performing algorithm, our model achieved improvements of up to 89.12% in MAE, 82.30% in RMSE, and 25.00% in MAPE, with extensive evaluations demonstrating that STeP-Diff effectively captures the spatio-temporal dependencies in air pollution fields.

