---
layout: default
title: Anytime-Valid Conformal Risk Control
---

# Anytime-Valid Conformal Risk Control
**arXiv**：[2602.04364v1](https://arxiv.org/abs/2602.04364) · [PDF](https://arxiv.org/pdf/2602.04364.pdf)  
**作者**：Bror Hultberg, Dave Zachariah, Antônio H. Ribeiro  

**一句话要点**：提出任意时间有效的保形风险控制方法，以解决累积校准数据下的统计保证问题。

**关键词**：保形预测, 风险控制, 任意时间有效性, 累积校准, 分布偏移, 统计保证

## 3 点简述
- 核心问题：标准保形预测仅在固定大小校准数据集上平均控制误差，缺乏任意时间点的概率保证。
- 方法要点：基于分位数论证，扩展保形风险控制，确保在累积增长校准数据下高概率有效。
- 实验或效果：通过模拟和真实数据验证方法性能，并证明保证渐近紧致且适用于分布偏移场景。

## 摘要（原文）

> Prediction sets provide a means of quantifying the uncertainty in predictive tasks. Using held out calibration data, conformal prediction and risk control can produce prediction sets that exhibit statistically valid error control in a computationally efficient manner. However, in the standard formulations, the error is only controlled on average over many possible calibration datasets of fixed size. In this paper, we extend the control to remain valid with high probability over a cumulatively growing calibration dataset at any time point. We derive such guarantees using quantile-based arguments and illustrate the applicability of the proposed framework to settings involving distribution shift. We further establish a matching lower bound and show that our guarantees are asymptotically tight. Finally, we demonstrate the practical performance of our methods through both simulations and real-world numerical examples.

