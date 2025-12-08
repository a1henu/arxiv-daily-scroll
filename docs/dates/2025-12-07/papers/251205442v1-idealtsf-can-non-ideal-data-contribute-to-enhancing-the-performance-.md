---
layout: default
title: IdealTSF: Can Non-Ideal Data Contribute to Enhancing the Performance of Time Series Forecasting Models?
---

# IdealTSF: Can Non-Ideal Data Contribute to Enhancing the Performance of Time Series Forecasting Models?
**arXiv**：[2512.05442v1](https://arxiv.org/abs/2512.05442) · [PDF](https://arxiv.org/pdf/2512.05442.pdf)  
**作者**：Hua Wang, Jinghao Lu, Fan Zhang  

**一句话要点**：提出IdealTSF框架，利用非理想负样本增强时间序列预测模型性能

**关键词**：时间序列预测, 负样本学习, 对抗优化, 注意力机制, 数据增强

## 3 点简述
- 核心问题：时间序列数据中的缺失值和异常值阻碍深度学习预测性能提升
- 方法要点：通过预训练、训练和优化三步骤，整合理想正负样本进行预测
- 实验或效果：实验表明负样本数据能显著提升基础注意力架构的预测潜力

## 摘要（原文）

> Deep learning has shown strong performance in time series forecasting tasks. However, issues such as missing values and anomalies in sequential data hinder its further development in prediction tasks. Previous research has primarily focused on extracting feature information from sequence data or addressing these suboptimal data as positive samples for knowledge transfer. A more effective approach would be to leverage these non-ideal negative samples to enhance event prediction. In response, this study highlights the advantages of non-ideal negative samples and proposes the IdealTSF framework, which integrates both ideal positive and negative samples for time series forecasting. IdealTSF consists of three progressive steps: pretraining, training, and optimization. It first pretrains the model by extracting knowledge from negative sample data, then transforms the sequence data into ideal positive samples during training. Additionally, a negative optimization mechanism with adversarial disturbances is applied. Extensive experiments demonstrate that negative sample data unlocks significant potential within the basic attention architecture for time series forecasting. Therefore, IdealTSF is particularly well-suited for applications with noisy samples or low-quality data.

