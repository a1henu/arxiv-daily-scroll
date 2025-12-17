---
layout: default
title: Pattern Recognition of Aluminium Arbitrage in Global Trade Data
---

# Pattern Recognition of Aluminium Arbitrage in Global Trade Data
**arXiv**：[2512.14410v1](https://arxiv.org/abs/2512.14410) · [PDF](https://arxiv.org/pdf/2512.14410.pdf)  
**作者**：Muhammad Sukri Bin Ramli  

**一句话要点**：提出无监督机器学习框架以检测全球铝贸易数据中的异常模式

**关键词**：无监督学习, 贸易异常检测, 网络科学, 深度自编码器, 价格偏差分析, 海关执法

## 3 点简述
- 核心问题：全球铝贸易中因碳边境调节机制等政策导致价格套利扩大，引发贸易异常如硬件掩蔽和贸易洗钱
- 方法要点：采用四层分析管道，结合法证统计、孤立森林、网络科学和深度自编码器进行异常检测与分类
- 实验或效果：实证结果显示价格偏差是异常的主要预测因子，需海关执法从物理量检查转向动态算法估值审计

## 摘要（原文）

> As the global economy transitions toward decarbonization, the aluminium sector has become a focal point for strategic resource management. While policies such as the Carbon Border Adjustment Mechanism (CBAM) aim to reduce emissions, they have inadvertently widened the price arbitrage between primary metal, scrap, and semi-finished goods, creating new incentives for market optimization. This study presents a unified, unsupervised machine learning framework to detect and classify emerging trade anomalies within UN Comtrade data (2020 to 2024). Moving beyond traditional rule-based monitoring, we apply a four-layer analytical pipeline utilizing Forensic Statistics, Isolation Forests, Network Science, and Deep Autoencoders. Contrary to the hypothesis that Sustainability Arbitrage would be the primary driver, empirical results reveal a contradictory and more severe phenomenon of Hardware Masking. Illicit actors exploit bi-directional tariff incentives by misclassifying scrap as high-count heterogeneous goods to justify extreme unit-price outliers of >$160/kg, a 1,900% markup indicative of Trade-Based Money Laundering (TBML) rather than commercial arbitrage. Topologically, risk is not concentrated in major exporters but in high-centrality Shadow Hubs that function as pivotal nodes for illicit rerouting. These actors execute a strategy of Void-Shoring, systematically suppressing destination data to Unspecified Code to fracture mirror statistics and sever forensic trails. Validated by SHAP (Shapley Additive Explanations), the results confirm that price deviation is the dominant predictor of anomalies, necessitating a paradigm shift in customs enforcement from physical volume checks to dynamic, algorithmic valuation auditing.

