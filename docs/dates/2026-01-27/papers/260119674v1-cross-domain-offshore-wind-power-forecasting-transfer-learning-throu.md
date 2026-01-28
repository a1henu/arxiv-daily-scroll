---
layout: default
title: Cross-Domain Offshore Wind Power Forecasting: Transfer Learning Through Meteorological Clusters
---

# Cross-Domain Offshore Wind Power Forecasting: Transfer Learning Through Meteorological Clusters
**arXiv**：[2601.19674v1](https://arxiv.org/abs/2601.19674) · [PDF](https://arxiv.org/pdf/2601.19674.pdf)  
**作者**：Dominic Weisser, Chloé Hashimoto-Cullen, Benjamin Guedj  

**一句话要点**：提出基于气象聚类的迁移学习框架，以解决新海上风电场数据稀缺下的功率预测问题。

**关键词**：海上风电功率预测, 迁移学习, 气象聚类, 专家模型, 数据稀缺

## 3 点简述
- 核心问题：新海上风电场缺乏站点特定数据，难以训练高性能机器学习预测模型。
- 方法要点：通过气象特征聚类，训练专家模型集合，每个模型专注于特定天气模式，实现高效迁移。
- 实验或效果：在八个风电场评估，仅需不到五个月数据，MAE达3.52%，验证了无需全年数据的可靠预测。

## 摘要（原文）

> Ambitious decarbonisation targets are catalysing growth in orders of new offshore wind farms. For these newly commissioned plants to run, accurate power forecasts are needed from the onset. These allow grid stability, good reserve management and efficient energy trading. Despite machine learning models having strong performances, they tend to require large volumes of site-specific data that new farms do not yet have. To overcome this data scarcity, we propose a novel transfer learning framework that clusters power output according to covariate meteorological features. Rather than training a single, general-purpose model, we thus forecast with an ensemble of expert models, each trained on a cluster. As these pre-trained models each specialise in a distinct weather pattern, they adapt efficiently to new sites and capture transferable, climate-dependent dynamics. Through the expert models' built-in calibration to seasonal and meteorological variability, we remove the industry-standard requirement of local measurements over a year. Our contributions are two-fold - we propose this novel framework and comprehensively evaluate it on eight offshore wind farms, achieving accurate cross-domain forecasting with under five months of site-specific data. Our experiments achieve a MAE of 3.52\%, providing empirical verification that reliable forecasts do not require a full annual cycle. Beyond power forecasting, this climate-aware transfer learning method opens new opportunities for offshore wind applications such as early-stage wind resource assessment, where reducing data requirements can significantly accelerate project development whilst effectively mitigating its inherent risks.

