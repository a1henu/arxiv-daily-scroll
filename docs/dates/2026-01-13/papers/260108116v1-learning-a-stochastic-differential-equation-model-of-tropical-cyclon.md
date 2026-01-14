---
layout: default
title: Learning a Stochastic Differential Equation Model of Tropical Cyclone Intensification from Reanalysis and Observational Data
---

# Learning a Stochastic Differential Equation Model of Tropical Cyclone Intensification from Reanalysis and Observational Data
**arXiv**：[2601.08116v1](https://arxiv.org/abs/2601.08116) · [PDF](https://arxiv.org/pdf/2601.08116.pdf)  
**作者**：Kenneth Gee, Sai Ravela  

**一句话要点**：提出基于数据的10项立方随机微分方程模型，以模拟热带气旋强度变化

**关键词**：热带气旋强度模型, 随机微分方程, 系统辨识, 数据驱动建模, 环境特征工程

## 3 点简述
- 核心问题：能否从数据中学习物理合理且简单的微分方程模型来描述热带气旋强度变化？
- 方法要点：使用IBTrACS和ERA5再分析数据，训练依赖环境特征的随机微分方程模型。
- 实验或效果：模型生成的合成强度序列能捕捉北半球历史强度统计和灾害估计的多个方面。

## 摘要（原文）

> Tropical cyclones are dangerous natural hazards, but their hazard is challenging to quantify directly from historical datasets due to limited dataset size and quality. Models of cyclone intensification fill this data gap by simulating huge ensembles of synthetic hurricanes based on estimates of the storm's large scale environment. Both physics-based and statistical/ML intensification models have been developed to tackle this problem, but an open question is: can a physically reasonable and simple physics-style differential equation model of intensification be learned from data? In this paper, we answer this question in the affirmative by presenting a 10-term cubic stochastic differential equation model of Tropical Cyclone intensification. The model depends on a well-vetted suite of engineered environmental features known to drive intensification and is trained using a high quality dataset of hurricane intensity (IBTrACS) with estimates of the cyclone's large scale environment from a data-assimilated simulation (ERA5 reanalysis), restricted to the Northern Hemisphere. The model generates synthetic intensity series which capture many aspects of historical intensification statistics and hazard estimates in the Northern Hemisphere. Our results show promise that interpretable, physics style models of complex earth system dynamics can be learned using automated system identification techniques.

