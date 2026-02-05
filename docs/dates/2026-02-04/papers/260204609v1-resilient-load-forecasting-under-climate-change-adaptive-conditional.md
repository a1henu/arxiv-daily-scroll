---
layout: default
title: Resilient Load Forecasting under Climate Change: Adaptive Conditional Neural Processes for Few-Shot Extreme Load Forecasting
---

# Resilient Load Forecasting under Climate Change: Adaptive Conditional Neural Processes for Few-Shot Extreme Load Forecasting
**arXiv**：[2602.04609v1](https://arxiv.org/abs/2602.04609) · [PDF](https://arxiv.org/pdf/2602.04609.pdf)  
**作者**：Chenxi Hu, Yue Ma, Yifan Wu, Yunhe Hou  

**一句话要点**：提出AdaCNP以解决极端天气下电力负荷预测中样本稀缺和分布突变的问题。

**关键词**：电力负荷预测, 极端事件预测, 少样本学习, 条件神经过程, 概率预测, 自适应模型

## 3 点简述
- 核心问题：极端天气导致电力负荷模式突变，但相关样本稀缺，使预测不可靠。
- 方法要点：AdaCNP在共享嵌入空间学习相似性，自适应加权历史上下文，实现少样本适应。
- 实验或效果：在真实数据上，AdaCNP比基线更稳健，均方误差降低22%，概率输出更可靠。

## 摘要（原文）

> Extreme weather can substantially change electricity consumption behavior, causing load curves to exhibit sharp spikes and pronounced volatility. If forecasts are inaccurate during those periods, power systems are more likely to face supply shortfalls or localized overloads, forcing emergency actions such as load shedding and increasing the risk of service disruptions and public-safety impacts. This problem is inherently difficult because extreme events can trigger abrupt regime shifts in load patterns, while relevant extreme samples are rare and irregular, making reliable learning and calibration challenging. We propose AdaCNP, a probabilistic forecasting model for data-scarce condition. AdaCNP learns similarity in a shared embedding space. For each target data, it evaluates how relevant each historical context segment is to the current condition and reweights the context information accordingly. This design highlights the most informative historical evidence even when extreme samples are rare. It enables few-shot adaptation to previously unseen extreme patterns. AdaCNP also produces predictive distributions for risk-aware decision-making without expensive fine-tuning on the target domain. We evaluate AdaCNP on real-world power-system load data and compare it against a range of representative baselines. The results show that AdaCNP is more robust during extreme periods, reducing the mean squared error by 22\% relative to the strongest baseline while achieving the lowest negative log-likelihood, indicating more reliable probabilistic outputs. These findings suggest that AdaCNP can effectively mitigate the combined impact of abrupt distribution shifts and scarce extreme samples, providing a more trustworthy forecasting for resilient power system operation under extreme events.

