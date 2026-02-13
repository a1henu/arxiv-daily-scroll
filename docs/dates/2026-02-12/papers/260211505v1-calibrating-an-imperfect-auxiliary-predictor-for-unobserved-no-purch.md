---
layout: default
title: Calibrating an Imperfect Auxiliary Predictor for Unobserved No-Purchase Choice
---

# Calibrating an Imperfect Auxiliary Predictor for Unobserved No-Purchase Choice
**arXiv**：[2602.11505v1](https://arxiv.org/abs/2602.11505) · [PDF](https://arxiv.org/pdf/2602.11505.pdf)  
**作者**：Jiangkai Xiong, Kalyan Talluri, Hanzhao Wang  

**一句话要点**：提出校准方法以利用不完美辅助预测器估计未观测的无购买选择概率

**关键词**：无购买选择估计, 辅助预测器校准, 多项式逻辑模型, 品类优化, 误差界限分析, 机器学习应用

## 3 点简述
- 核心问题：企业仅记录交易数据时，无法观测消费者无购买等外部选项，导致市场大小和偏好估计困难。
- 方法要点：在仿射误校准下，通过简单回归识别参数；在弱单调条件下，提出基于排序的校准方法，并推导误差界限。
- 实验或效果：数值实验显示无购买估计和下游品类决策改进，并讨论多预测器稳健聚合扩展。

## 摘要（原文）

> Firms typically cannot observe key consumer actions: whether customers buy from a competitor, choose not to buy, or even fully consider the firm's offer. This missing outside-option information makes market-size and preference estimation difficult even in simple multinomial logit (MNL) models, and it is a central obstacle in practice when only transaction data are recorded. Existing approaches often rely on auxiliary market-share, aggregated, or cross-market data. We study a complementary setting in which a black-box auxiliary predictor provides outside-option probabilities, but is potentially biased or miscalibrated because it was trained in a different channel, period, or population, or produced by an external machine-learning system. We develop calibration methods that turn such imperfect predictions into statistically valid no-purchase estimates using purchase-only data from the focal environment. First, under affine miscalibration in logit space, we show that a simple regression identifies outside-option utility parameters and yields consistent recovery of no-purchase probabilities without collecting new labels for no-purchase events. Second, under a weaker nearly monotone condition, we propose a rank-based calibration method and derive finite-sample error bounds that cleanly separate auxiliary-predictor quality from first-stage utility-learning error over observed in-set choices. Our analysis also translates estimation error into downstream decision quality for assortment optimization, quantifying how calibration accuracy affects revenue performance. The bounds provide explicit dependence on predictor alignment and utility-learning error, clarifying when each source dominates. Numerical experiments demonstrate improvements in no-purchase estimation and downstream assortment decisions, and we discuss robust aggregation extensions for combining multiple auxiliary predictors.

