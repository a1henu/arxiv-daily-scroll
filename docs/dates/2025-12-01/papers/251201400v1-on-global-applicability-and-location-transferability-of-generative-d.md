---
layout: default
title: On Global Applicability and Location Transferability of Generative Deep Learning Models for Precipitation Downscaling
---

# On Global Applicability and Location Transferability of Generative Deep Learning Models for Precipitation Downscaling
**arXiv**：[2512.01400v1](https://arxiv.org/abs/2512.01400) · [PDF](https://arxiv.org/pdf/2512.01400.pdf)  
**作者**：Paula Harder, Christian Lessig, Matthew Chantry, Francis Pelletier, David Rolnick  

**一句话要点**：评估生成式深度学习模型在全球降水降尺度中的泛化性能与位置可迁移性

**关键词**：降水降尺度, 生成式深度学习, 泛化性能, 位置可迁移性, 全球气候数据, ERA5再分析

## 3 点简述
- 核心问题：现有降水降尺度模型多为区域特定，泛化到未见地理区域的能力未知。
- 方法要点：使用全球框架，以ERA5再分析数据为预测因子，IMERG降水估计为目标，进行分层位置数据分割。
- 实验或效果：系统评估模型在全球15个区域的性能，探索生成式模型的泛化能力。

## 摘要（原文）

> Deep learning offers promising capabilities for the statistical downscaling of climate and weather forecasts, with generative approaches showing particular success in capturing fine-scale precipitation patterns. However, most existing models are region-specific, and their ability to generalize to unseen geographic areas remains largely unexplored. In this study, we evaluate the generalization performance of generative downscaling models across diverse regions. Using a global framework, we employ ERA5 reanalysis data as predictors and IMERG precipitation estimates at $0.1^\circ$ resolution as targets. A hierarchical location-based data split enables a systematic assessment of model performance across 15 regions around the world.

