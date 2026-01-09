---
layout: default
title: Intraday spatiotemporal PV power prediction at national scale using satellite-based solar forecast models
---

# Intraday spatiotemporal PV power prediction at national scale using satellite-based solar forecast models
**arXiv**：[2601.04751v1](https://arxiv.org/abs/2601.04751) · [PDF](https://arxiv.org/pdf/2601.04751.pdf)  
**作者**：Luca Lanzilao, Angela Meyer  

**一句话要点**：提出国家尺度时空光伏功率预测框架，评估七种日内预报模型性能

**关键词**：光伏功率预测, 卫星预报模型, 时空预测, 机器学习转换, 国家尺度评估, 不确定性校准

## 3 点简述
- 研究国家尺度时空光伏功率预测，首次大规模评估卫星与数值天气模型
- 结合卫星辐照度预测与站点机器学习转换，验证6434个光伏站数据
- 结果显示卫星方法优于数值预报，SolarSTEPS和SHADECast表现最佳

## 摘要（原文）

> We present a novel framework for spatiotemporal photovoltaic (PV) power forecasting and use it to evaluate the reliability, sharpness, and overall performance of seven intraday PV power nowcasting models. The model suite includes satellite-based deep learning and optical-flow approaches and physics-based numerical weather prediction models, covering both deterministic and probabilistic formulations. Forecasts are first validated against satellite-derived surface solar irradiance (SSI). Irradiance fields are then converted into PV power using station-specific machine learning models, enabling comparison with production data from 6434 PV stations across Switzerland. To our knowledge, this is the first study to investigate spatiotemporal PV forecasting at a national scale. We additionally provide the first visualizations of how mesoscale cloud systems shape national PV production on hourly and sub-hourly timescales. Our results show that satellite-based approaches outperform the Integrated Forecast System (IFS-ENS), particularly at short lead times. Among them, SolarSTEPS and SHADECast deliver the most accurate SSI and PV power predictions, with SHADECast providing the most reliable ensemble spread. The deterministic model IrradianceNet achieves the lowest root mean square error, while probabilistic forecasts of SolarSTEPS and SHADECast provide better-calibrated uncertainty. Forecast skill generally decreases with elevation. At a national scale, satellite-based models forecast the daily total PV generation with relative errors below 10% for 82% of the days in 2019-2020, demonstrating robustness and their potential for operational use.

