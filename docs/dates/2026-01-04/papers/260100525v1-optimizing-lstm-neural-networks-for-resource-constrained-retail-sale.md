---
layout: default
title: Optimizing LSTM Neural Networks for Resource-Constrained Retail Sales Forecasting: A Model Compression Study
---

# Optimizing LSTM Neural Networks for Resource-Constrained Retail Sales Forecasting: A Model Compression Study
**arXiv**：[2601.00525v1](https://arxiv.org/abs/2601.00525) · [PDF](https://arxiv.org/pdf/2601.00525.pdf)  
**作者**：Ravi Teja Pagidoju  

**一句话要点**：通过压缩LSTM模型优化资源受限零售销售预测，实现模型缩小73%且精度提升47%。

**关键词**：LSTM模型压缩, 零售销售预测, 资源受限优化, 隐藏单元减少, Kaggle数据集

## 3 点简述
- 核心问题：标准LSTM模型在零售销售预测中计算资源需求高，中小型零售业难以部署。
- 方法要点：逐步减少LSTM隐藏单元数从128到16，研究模型大小与预测精度的权衡。
- 实验或效果：在Kaggle数据集上，64单元模型MAPE从23.6%降至12.4%，模型大小从280KB减至76KB。

## 摘要（原文）

> Standard LSTM(Long Short-Term Memory) neural networks provide accurate predictions for sales data in the retail industry, but require a lot of computing power. It can be challenging especially for mid to small retail industries. This paper examines LSTM model compression by gradually reducing the number of hidden units from 128 to 16. We used the Kaggle Store Item Demand Forecasting dataset, which has 913,000 daily sales records from 10 stores and 50 items, to look at the trade-off between model size and how accurate the predictions are. Experiments show that lowering the number of hidden LSTM units to 64 maintains the same level of accuracy while also improving it. The mean absolute percentage error (MAPE) ranges from 23.6% for the full 128-unit model to 12.4% for the 64-unit model. The optimized model is 73% smaller (from 280KB to 76KB) and 47% more accurate. These results show that larger models do not always achieve better results.

