---
layout: default
title: Smart Timing for Mining: A Deep Learning Framework for Bitcoin Hardware ROI Prediction
---

# Smart Timing for Mining: A Deep Learning Framework for Bitcoin Hardware ROI Prediction
**arXiv**：[2512.05402v1](https://arxiv.org/abs/2512.05402) · [PDF](https://arxiv.org/pdf/2512.05402.pdf)  
**作者**：Sithumi Wickramasinghe, Bikramjit Das, Dorien Herremans  

**一句话要点**：提出MineROI-Net，基于Transformer预测比特币矿机购买时机以优化投资回报。

**关键词**：比特币挖矿, 投资回报预测, 时间序列分类, Transformer模型, 硬件获取决策

## 3 点简述
- 核心问题：比特币矿机购买时机决策缺乏计算框架，需应对市场波动和技术过时。
- 方法要点：将硬件获取建模为时间序列分类任务，使用Transformer架构捕捉多尺度盈利模式。
- 实验或效果：在2015-2024年数据上，模型准确率达83.7%，能高精度识别盈利与非盈利期。

## 摘要（原文）

> Bitcoin mining hardware acquisition requires strategic timing due to volatile markets, rapid technological obsolescence, and protocol-driven revenue cycles. Despite mining's evolution into a capital-intensive industry, there is little guidance on when to purchase new Application-Specific Integrated Circuit (ASIC) hardware, and no prior computational frameworks address this decision problem. We address this gap by formulating hardware acquisition as a time series classification task, predicting whether purchasing ASIC machines yields profitable (Return on Investment (ROI) >= 1), marginal (0 < ROI < 1), or unprofitable (ROI <= 0) returns within one year. We propose MineROI-Net, an open source Transformer-based architecture designed to capture multi-scale temporal patterns in mining profitability. Evaluated on data from 20 ASIC miners released between 2015 and 2024 across diverse market regimes, MineROI-Net outperforms LSTM-based and TSLANet baselines, achieving 83.7% accuracy and 83.1% macro F1-score. The model demonstrates strong economic relevance, achieving 93.6% precision in detecting unprofitable periods and 98.5% precision for profitable ones, while avoiding misclassification of profitable scenarios as unprofitable and vice versa. These results indicate that MineROI-Net offers a practical, data-driven tool for timing mining hardware acquisitions, potentially reducing financial risk in capital-intensive mining operations. The model is available through: https://github.com/AMAAI-Lab/MineROI-Net.

