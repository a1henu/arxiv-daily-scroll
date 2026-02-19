---
layout: default
title: AIFL: A Global Daily Streamflow Forecasting Model Using Deterministic LSTM Pre-trained on ERA5-Land and Fine-tuned on IFS
---

# AIFL: A Global Daily Streamflow Forecasting Model Using Deterministic LSTM Pre-trained on ERA5-Land and Fine-tuned on IFS
**arXiv**：[2602.16579v1](https://arxiv.org/abs/2602.16579) · [PDF](https://arxiv.org/pdf/2602.16579.pdf)  
**作者**：Maria Luisa Taccari, Kenza Tazi, Oisín M. Morrison, Andreas Grafberger, Juan Colonese, Corentin Carton de Wiart, Christel Prudhomme, Cinzia Mazzetti, Matthew Chantry, Florian Pappenberger  

**一句话要点**：提出AIFL模型，通过两阶段训练策略解决全球日径流预测中再分析到预报的领域偏移问题。

**关键词**：全球径流预测, LSTM模型, 两阶段训练, 领域适应, 洪水预报, 水文建模

## 3 点简述
- 核心问题：数据驱动模型从历史再分析过渡到操作预报时存在性能差距，影响全球径流预测可靠性。
- 方法要点：采用确定性LSTM，先在ERA5-Land再分析数据上预训练，再在IFS操作预报上微调，以桥接领域偏移。
- 实验或效果：在独立测试集上，AIFL达到中位KGE' 0.66和NSE 0.53，与当前先进系统竞争，极端事件检测可靠。

## 摘要（原文）

> Reliable global streamflow forecasting is essential for flood preparedness and water resource management, yet data-driven models often suffer from a performance gap when transitioning from historical reanalysis to operational forecast products. This paper introduces AIFL (Artificial Intelligence for Floods), a deterministic LSTM-based model designed for global daily streamflow forecasting. Trained on 18,588 basins curated from the CARAVAN dataset, AIFL utilises a novel two-stage training strategy to bridge the reanalysis-to-forecast domain shift. The model is first pre-trained on 40 years of ERA5-Land reanalysis (1980-2019) to capture robust hydrological processes, then fine-tuned on operational Integrated Forecasting System (IFS) control forecasts (2016-2019) to adapt to the specific error structures and biases of operational numerical weather prediction. To our knowledge, this is the first global model trained end-to-end within the CARAVAN ecosystem. On an independent temporal test set (2021-2024), AIFL achieves high predictive skill with a median modified Kling-Gupta Efficiency (KGE') of 0.66 and a median Nash-Sutcliffe Efficiency (NSE) of 0.53. Benchmarking results show that AIFL is highly competitive with current state-of-the-art global systems, achieving comparable accuracy while maintaining a transparent and reproducible forcing pipeline. The model demonstrates exceptional reliability in extreme-event detection, providing a streamlined and operationally robust baseline for the global hydrological community.

