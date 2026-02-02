---
layout: default
title: HeatMat: Simulation of City Material Impact on Urban Heat Island Effect
---

# HeatMat: Simulation of City Material Impact on Urban Heat Island Effect
**arXiv**：[2601.22796v1](https://arxiv.org/abs/2601.22796) · [PDF](https://arxiv.org/pdf/2601.22796.pdf)  
**作者**：Marie Reinbigler, Romain Rouffet, Peter Naylor, Mikolaj Czerkawski, Nikolaos Dionelis, Elisabeth Brunet, Catalin Fetita, Rosalie Martin  

**一句话要点**：提出HeatMat方法，基于开放数据高分辨率模拟城市材料对热岛效应的影响。

**关键词**：城市热岛效应模拟, 建筑材料估计, 视觉语言模型, 2.5D模拟器, 开放数据

## 3 点简述
- 核心问题：城市热岛效应研究受限于传感器数据分辨率，难以分析材料个体影响。
- 方法要点：利用街景图像和预训练视觉语言模型估计建筑材料，结合2.5D模拟器建模热传递。
- 实验或效果：实现多分辨率表面温度随机访问模拟，相比3D模拟加速20倍。

## 摘要（原文）

> The Urban Heat Island (UHI) effect, defined as a significant increase in temperature in urban environments compared to surrounding areas, is difficult to study in real cities using sensor data (satellites or in-situ stations) due to their coarse spatial and temporal resolution. Among the factors contributing to this effect are the properties of urban materials, which differ from those in rural areas. To analyze their individual impact and to test new material configurations, a high-resolution simulation at the city scale is required. Estimating the current materials used in a city, including those on building facades, is also challenging. We propose HeatMat, an approach to analyze at high resolution the individual impact of urban materials on the UHI effect in a real city, relying only on open data. We estimate building materials using street-view images and a pre-trained vision-language model (VLM) to supplement existing OpenStreetMap data, which describes the 2D geometry and features of buildings. We further encode this information into a set of 2D maps that represent the city's vertical structure and material characteristics. These maps serve as inputs for our 2.5D simulator, which models coupled heat transfers and enables random-access surface temperature estimation at multiple resolutions, reaching an x20 speedup compared to an equivalent simulation in 3D.

