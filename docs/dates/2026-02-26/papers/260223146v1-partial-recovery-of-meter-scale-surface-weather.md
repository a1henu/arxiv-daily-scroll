---
layout: default
title: Partial recovery of meter-scale surface weather
---

# Partial recovery of meter-scale surface weather
**arXiv**：[2602.23146v1](https://arxiv.org/abs/2602.23146) · [PDF](https://arxiv.org/pdf/2602.23146.pdf)  
**作者**：Jonathan Giezendanner, Qidong Yang, Eric Schmitt, Anirban Chandra, Daniel Salles Civitarese, Johannes Jakubik, Jeremy Vila, Detlef Hohl, Campbell Watson, Sherrie Wang  

**一句话要点**：提出基于观测数据与高分辨率地球观测的统计推断方法，实现米级近地表天气场的部分恢复。

**关键词**：米级天气恢复, 近地表气象推断, 高分辨率地球观测, 统计条件推断, 空间连续场

## 3 点简述
- 核心问题：米级近地表天气变异性是否可预测，当前天气分析缺乏此尺度信息。
- 方法要点：利用稀疏地面站测量和高分辨率地球观测数据，对粗尺度大气状态进行条件推断。
- 实验或效果：在美国大陆实现10米分辨率推断，相比ERA5降低风误差29%，温度露点误差6%。

## 摘要（原文）

> Near-surface atmospheric conditions can differ sharply over tens to hundreds of meters due to land cover and topography, yet this variability is absent from current weather analyses and forecasts. It is unclear whether such meter-scale variability reflects irreducibly chaotic dynamics or contains a component predictable from surface characteristics and large-scale atmospheric forcing. Here we show that a substantial, physically coherent component of meter-scale near-surface weather is statistically recoverable from existing observations. By conditioning coarse atmospheric state on sparse surface station measurements and high-resolution Earth observation data, we infer spatially continuous fields of near-surface wind, temperature, and humidity at 10 m resolution across the contiguous United States. Relative to ERA5, the inferred fields reduce wind error by 29% and temperature and dewpoint error by 6%, while explaining substantially more spatial variance at fixed time steps. They also exhibit physically interpretable structure, including urban heat islands, evapotranspiration-driven humidity contrasts, and wind speed differences across land cover types. Our findings expand the frontier of weather modeling by demonstrating a computationally feasible approach to continental-scale meter-resolution inference. More broadly, they illustrate how conditioning coarse dynamical models on static fine-scale features can reveal previously unresolved components of the Earth system.

