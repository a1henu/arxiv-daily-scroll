---
layout: default
title: GRAFT: Grid-Aware Load Forecasting with Multi-Source Textual Alignment and Fusion
---

# GRAFT: Grid-Aware Load Forecasting with Multi-Source Textual Alignment and Fusion
**arXiv**：[2512.14400v1](https://arxiv.org/abs/2512.14400) · [PDF](https://arxiv.org/pdf/2512.14400.pdf)  
**作者**：Fangzhou Lin, Guoshun He, Zhenyu Guo, Zhe Huang, Jinsong Tao  

**一句话要点**：提出GRAFT模型，通过多源文本对齐与融合改进电网负荷预测

**关键词**：电网负荷预测, 多源文本对齐, 交叉注意力, 事件驱动预测, 可解释性分析, 基准数据集

## 3 点简述
- 核心问题：电网负荷受天气、事件等多源外生因素影响，需跨时间尺度预测
- 方法要点：严格对齐新闻、社交媒体和政策文本与负荷数据，利用交叉注意力实现文本引导融合
- 实验或效果：在澳大利亚五州基准测试中显著优于基线，支持事件驱动场景和可解释性分析

## 摘要（原文）

> Electric load is simultaneously affected across multiple time scales by exogenous factors such as weather and calendar rhythms, sudden events, and policies. Therefore, this paper proposes GRAFT (GRid-Aware Forecasting with Text), which modifies and improves STanHOP to better support grid-aware forecasting and multi-source textual interventions. Specifically, GRAFT strictly aligns daily-aggregated news, social media, and policy texts with half-hour load, and realizes text-guided fusion to specific time positions via cross-attention during both training and rolling forecasting. In addition, GRAFT provides a plug-and-play external-memory interface to accommodate different information sources in real-world deployment. We construct and release a unified aligned benchmark covering 2019--2021 for five Australian states (half-hour load, daily-aligned weather/calendar variables, and three categories of external texts), and conduct systematic, reproducible evaluations at three scales -- hourly, daily, and monthly -- under a unified protocol for comparison across regions, external sources, and time scales. Experimental results show that GRAFT significantly outperforms strong baselines and reaches or surpasses the state of the art across multiple regions and forecasting horizons. Moreover, the model is robust in event-driven scenarios and enables temporal localization and source-level interpretation of text-to-load effects through attention read-out. We release the benchmark, preprocessing scripts, and forecasting results to facilitate standardized empirical evaluation and reproducibility in power grid load forecasting.

