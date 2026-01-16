---
layout: default
title: Reinforcement Learning to Discover a NorthEast Monsoon Index for Monthly Rainfall Prediction in Thailand
---

# Reinforcement Learning to Discover a NorthEast Monsoon Index for Monthly Rainfall Prediction in Thailand
**arXiv**：[2601.10181v1](https://arxiv.org/abs/2601.10181) · [PDF](https://arxiv.org/pdf/2601.10181.pdf)  
**作者**：Kiattikun Chobtham  

**一句话要点**：提出基于强化学习的东北季风指数优化方法，以提升泰国月度降雨预测精度。

**关键词**：强化学习, 气候指数优化, 降雨预测, 长短期记忆网络, 泰国气候

## 3 点简述
- 问题：泰国缺乏本地气候指数，影响长期降雨预测准确性。
- 方法：使用深度Q网络强化学习优化海温计算区域，构建东北季风指数。
- 效果：优化指数结合LSTM模型，显著降低12个月预测的均方根误差。

## 摘要（原文）

> Climate prediction is a challenge due to the intricate spatiotemporal patterns within Earth systems. Global climate indices, such as the El Niño Southern Oscillation, are standard input features for long-term rainfall prediction. However, a significant gap persists regarding local-scale indices capable of improving predictive accuracy in specific regions of Thailand. This paper introduces a novel NorthEast monsoon climate index calculated from sea surface temperature to reflect the climatology of the boreal winter monsoon. To optimise the calculated areas used for this index, a Deep Q-Network reinforcement learning agent explores and selects the most effective rectangles based on their correlation with seasonal rainfall. Rainfall stations were classified into 12 distinct clusters to distinguish rainfall patterns between southern and upper Thailand. Experimental results show that incorporating the optimised index into Long Short-Term Memory models significantly improves long-term monthly rainfall prediction skill in most cluster areas. This approach effectively reduces the Root Mean Square Error for 12-month-ahead forecasts.

