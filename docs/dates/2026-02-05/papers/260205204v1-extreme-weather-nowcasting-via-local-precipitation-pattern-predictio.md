---
layout: default
title: Extreme Weather Nowcasting via Local Precipitation Pattern Prediction
---

# Extreme Weather Nowcasting via Local Precipitation Pattern Prediction
**arXiv**：[2602.05204v1](https://arxiv.org/abs/2602.05204) · [PDF](https://arxiv.org/pdf/2602.05204.pdf)  
**作者**：Changhoon Song, Teng Yuan Chang, Youngjoon Hong  

**一句话要点**：提出exPreCast框架与平衡雷达数据集，以高效预测极端天气降水模式。

**关键词**：极端天气临近预报, 降水模式预测, 局部时空注意力, 平衡雷达数据集, 确定性模型

## 3 点简述
- 核心问题：极端降水临近预报因空间局部性、精细结构复杂和预测时变而具挑战性，现有方法计算昂贵或偏向正常降雨。
- 方法要点：结合局部时空注意力、纹理保持立方双上采样解码器和时域提取器，灵活调整预测时域。
- 实验或效果：在SEVIR、MeteoNet和平衡KMA数据集上实现最先进性能，准确预测正常与极端降雨。

## 摘要（原文）

> Accurate forecasting of extreme weather events such as heavy rainfall or storms is critical for risk management and disaster mitigation. Although high-resolution radar observations have spurred extensive research on nowcasting models, precipitation nowcasting remains particularly challenging due to pronounced spatial locality, intricate fine-scale rainfall structures, and variability in forecasting horizons. While recent diffusion-based generative ensembles show promising results, they are computationally expensive and unsuitable for real-time applications. In contrast, deterministic models are computationally efficient but remain biased toward normal rainfall. Furthermore, the benchmark datasets commonly used in prior studies are themselves skewed--either dominated by ordinary rainfall events or restricted to extreme rainfall episodes--thereby hindering general applicability in real-world settings. In this paper, we propose exPreCast, an efficient deterministic framework for generating finely detailed radar forecasts, and introduce a newly constructed balanced radar dataset from the Korea Meteorological Administration (KMA), which encompasses both ordinary precipitation and extreme events. Our model integrates local spatiotemporal attention, a texture-preserving cubic dual upsampling decoder, and a temporal extractor to flexibly adjust forecasting horizons. Experiments on established benchmarks (SEVIR and MeteoNet) as well as on the balanced KMA dataset demonstrate that our approach achieves state-of-the-art performance, delivering accurate and reliable nowcasts across both normal and extreme rainfall regimes.

