---
layout: default
title: A Space-Time Transformer for Precipitation Forecasting
---

# A Space-Time Transformer for Precipitation Forecasting
**arXiv**：[2511.11090v1](https://arxiv.org/abs/2511.11090) · [PDF](https://arxiv.org/pdf/2511.11090.pdf)  
**作者**：Levi Harris, Tianlong Chen  

**一句话要点**：提出SaTformer视频变换器，基于全时空注意力预测极端降水

**关键词**：视频变换器, 全时空注意力, 降水预测, 数据不平衡处理, AI天气预报

## 3 点简述
- 传统数值天气预报计算成本高，且在临近预报中性能下降
- 采用视频变换器架构，将降水回归重构为分类问题，使用类别加权损失处理数据不平衡
- 在NeurIPS Weather4Cast 2025挑战赛中获第一名，代码和模型权重已开源

## 摘要（原文）

> Meteorological agencies around the world rely on real-time flood guidance to issue live-saving advisories and warnings. For decades traditional numerical weather prediction (NWP) models have been state-of-the-art for precipitation forecasting. However, physically-parameterized models suffer from a few core limitations: first, solving PDEs to resolve atmospheric dynamics is computationally demanding, and second, these methods degrade in performance at nowcasting timescales (i.e., 0-4 hour lead-times). Motivated by these shortcomings, recent work proposes AI-weather prediction (AI-WP) alternatives that learn to emulate analysis data with neural networks. While these data-driven approaches have enjoyed enormous success across diverse spatial and temporal resolutions, applications of video-understanding architectures for weather forecasting remain underexplored. To address these gaps, we propose SaTformer: a video transformer built on full space-time attention that skillfully forecasts extreme precipitation from satellite radiances. Along with our novel architecture, we introduce techniques to tame long-tailed precipitation datasets. Namely, we reformulate precipitation regression into a classification problem, and employ a class-weighted loss to address label imbalances. Our model scored first place on the NeurIPS Weather4Cast 2025 Cumulative Rainfall challenge. Code and model weights are available: https://github.com/leharris3/satformer

