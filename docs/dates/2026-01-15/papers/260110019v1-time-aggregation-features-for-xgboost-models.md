---
layout: default
title: Time Aggregation Features for XGBoost Models
---

# Time Aggregation Features for XGBoost Models
**arXiv**：[2601.10019v1](https://arxiv.org/abs/2601.10019) · [PDF](https://arxiv.org/pdf/2601.10019.pdf)  
**作者**：Mykola Pinchuk  

**一句话要点**：研究时间聚合特征以提升XGBoost模型在点击率预测中的性能

**关键词**：点击率预测, XGBoost模型, 时间聚合特征, 目标编码, 窗口设计, Avazu数据集

## 3 点简述
- 核心问题：在严格时间分割和无前瞻特征约束下，如何有效利用历史数据提升点击率预测精度。
- 方法要点：比较时间感知目标编码基线，并测试多种窗口设计（如拖尾窗口、事件计数窗口）的时间聚合特征。
- 实验或效果：拖尾窗口在ROC AUC和PR AUC上带来小幅提升，事件计数窗口提供额外增益，但其他窗口设计表现不佳。

## 摘要（原文）

> This paper studies time aggregation features for XGBoost models in click-through rate prediction. The setting is the Avazu click-through rate prediction dataset with strict out-of-time splits and a no-lookahead feature constraint. Features for hour H use only impressions from hours strictly before H. This paper compares a strong time-aware target encoding baseline to models augmented with entity history time aggregation under several window designs. Across two rolling-tail folds on a deterministic ten percent sample, a trailing window specification improves ROC AUC by about 0.0066 to 0.0082 and PR AUC by about 0.0084 to 0.0094 relative to target encoding alone. Within the time aggregation design grid, event count windows provide the only consistent improvement over trailing windows, and the gain is small. Gap windows and bucketized windows underperform simple trailing windows in this dataset and protocol. These results support a practical default of trailing windows, with an optional event count window when marginal ROC AUC gains matter.

