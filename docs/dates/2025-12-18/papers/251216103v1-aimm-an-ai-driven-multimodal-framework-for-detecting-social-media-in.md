---
layout: default
title: AIMM: An AI-Driven Multimodal Framework for Detecting Social-Media-Influenced Stock Market Manipulation
---

# AIMM: An AI-Driven Multimodal Framework for Detecting Social-Media-Influenced Stock Market Manipulation
**arXiv**：[2512.16103v1](https://arxiv.org/abs/2512.16103) · [PDF](https://arxiv.org/pdf/2512.16103.pdf)  
**作者**：Sandeep Neela  

**一句话要点**：提出AIMM框架以检测社交媒体驱动的股市操纵，融合多模态数据生成每日风险评分。

**关键词**：股市操纵检测, 多模态融合, 社交媒体分析, 风险评分, AI驱动框架, 市场监控

## 3 点简述
- 核心问题：社交媒体协调活动导致股市操纵，需工具连接在线叙事与市场行为。
- 方法要点：融合Reddit活动、机器人指标和OHLCV市场特征，构建AIMM风险评分系统。
- 实验或效果：在GME事件中提前22天预警，初步展示判别能力，但标注数据规模较小。

## 摘要（原文）

> Market manipulation now routinely originates from coordinated social media campaigns, not isolated trades. Retail investors, regulators, and brokerages need tools that connect online narratives and coordination patterns to market behavior. We present AIMM, an AI-driven framework that fuses Reddit activity, bot and coordination indicators, and OHLCV market features into a daily AIMM Manipulation Risk Score for each ticker.
>   The system uses a parquet-native pipeline with a Streamlit dashboard that allows analysts to explore suspicious windows, inspect underlying posts and price action, and log model outputs over time. Due to Reddit API restrictions, we employ calibrated synthetic social features matching documented event characteristics; market data (OHLCV) uses real historical data from Yahoo Finance. This release makes three contributions. First, we build the AIMM Ground Truth dataset (AIMM-GT): 33 labeled ticker-days spanning eight equities, drawing from SEC enforcement actions, community-verified manipulation cases, and matched normal controls. Second, we implement forward-walk evaluation and prospective prediction logging for both retrospective and deployment-style assessment. Third, we analyze lead times and show that AIMM flagged GME 22 days before the January 2021 squeeze peak.
>   The current labeled set is small (33 ticker-days, 3 positive events), but results show preliminary discriminative capability and early warnings for the GME incident. We release the code, dataset schema, and dashboard design to support research on social media-driven market surveillance.

