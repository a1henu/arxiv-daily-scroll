---
layout: default
title: Algorithmic Compliance and Regulatory Loss in Digital Assets
---

# Algorithmic Compliance and Regulatory Loss in Digital Assets
**arXiv**：[2603.04328v1](https://arxiv.org/abs/2603.04328) · [PDF](https://arxiv.org/pdf/2603.04328.pdf)  
**作者**：Khem Raj Bhatt, Krishna Sharma  

**一句话要点**：揭示机器学习反洗钱系统在加密货币中的部署性能不足，强调动态评估框架的必要性。

**关键词**：加密货币反洗钱, 机器学习部署, 时间非平稳性, 监管损失, 动态评估, 决策规则校准

## 3 点简述
- 核心问题：静态分类指标高估加密货币反洗钱系统的实际监管效果，导致持续超额损失。
- 方法要点：基于比特币交易数据，采用前瞻性和滚动评估分析时间非平稳性对执行阈值的影响。
- 实验或效果：发现决策规则校准错误是主要失败原因，而非预测准确性下降，突显固定政策的脆弱性。

## 摘要（原文）

> We study the deployment performance of machine learning based enforcement systems used in cryptocurrency anti money laundering (AML). Using forward looking and rolling evaluations on Bitcoin transaction data, we show that strong static classification metrics substantially overstate real world regulatory effectiveness. Temporal nonstationarity induces pronounced instability in cost sensitive enforcement thresholds, generating large and persistent excess regulatory losses relative to dynamically optimal benchmarks. The core failure arises from miscalibration of decision rules rather than from declining predictive accuracy per se. These findings underscore the fragility of fixed AML enforcement policies in evolving digital asset markets and motivate loss-based evaluation frameworks for regulatory oversight.

