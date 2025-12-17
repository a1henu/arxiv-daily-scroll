---
layout: default
title: Bridging Artificial Intelligence and Data Assimilation: The Data-driven Ensemble Forecasting System ClimaX-LETKF
---

# Bridging Artificial Intelligence and Data Assimilation: The Data-driven Ensemble Forecasting System ClimaX-LETKF
**arXiv**：[2512.14444v1](https://arxiv.org/abs/2512.14444) · [PDF](https://arxiv.org/pdf/2512.14444.pdf)  
**作者**：Akira Takeshima, Kenta Shiraishi, Atsushi Okazaki, Tadashi Tsuyuki, Shunji Kotsuki  

**一句话要点**：提出ClimaX-LETKF数据驱动集合天气预报系统，以解决机器学习天气预测中观测同化和集合预报的不足。

**关键词**：机器学习天气预测, 数据同化, 集合预报, 观测数据, RTPP方法, 数值天气预报

## 3 点简述
- 核心问题：机器学习天气预测模型在真实观测同化和集合预报方面研究有限，影响稳定性和实用性。
- 方法要点：开发首个纯数据驱动的机器学习集合天气预报系统，基于NCEP ADP观测数据，采用RTPP方法增强稳定性。
- 实验或效果：系统在多年运行中表现稳定，RTPP优于RTPS，但恢复大气场吸引子的能力弱于数值天气预报模型。

## 摘要（原文）

> While machine learning-based weather prediction (MLWP) has achieved significant advancements, research on assimilating real observations or ensemble forecasts within MLWP models remains limited. We introduce ClimaX-LETKF, the first purely data-driven ML-based ensemble weather forecasting system. It operates stably over multiple years, independently of numerical weather prediction (NWP) models, by assimilating the NCEP ADP Global Upper Air and Surface Weather Observations. The system demonstrates greater stability and accuracy with relaxation to prior perturbation (RTPP) than with relaxation to prior spread (RTPS), while NWP models tend to be more stable with RTPS. RTPP replaces an analysis perturbation with a weighted blend of analysis and background perturbations, whereas RTPS simply rescales the analysis perturbation. Our experiments reveal that MLWP models are less capable of restoring the atmospheric field to its attractor than NWP models. This work provides valuable insights for enhancing MLWP ensemble forecasting systems and represents a substantial step toward their practical applications.

