---
layout: default
title: Weighted Contrastive Learning for Anomaly-Aware Time-Series Forecasting
---

# Weighted Contrastive Learning for Anomaly-Aware Time-Series Forecasting
**arXiv**：[2512.07569v1](https://arxiv.org/abs/2512.07569) · [PDF](https://arxiv.org/pdf/2512.07569.pdf)  
**作者**：Joel Ekstrand, Tor Mattsson, Zahra Taghiyarrenani, Slawomir Nowaczyk, Jens Lundström, Mikael Lindén  

**一句话要点**：提出加权对比适应方法以增强ATM现金物流等场景中异常条件下的时间序列预测可靠性

**关键词**：时间序列预测, 异常检测, 对比学习, 分布偏移, ATM现金物流, 加权适应

## 3 点简述
- 核心问题：现代深度预测模型在正常数据上准确，但在分布偏移或异常条件下表现不佳，影响如ATM交易等应用。
- 方法要点：提出加权对比适应，通过加权对比目标对齐正常与异常增强表示，保留异常相关信息并保持良性变化下的一致性。
- 实验或效果：在带领域知识异常注入的ATM数据集上评估，相比正常训练基线，异常数据SMAPE提升6.1个百分点，正常数据性能几乎无下降。

## 摘要（原文）

> Reliable forecasting of multivariate time series under anomalous conditions is crucial in applications such as ATM cash logistics, where sudden demand shifts can disrupt operations. Modern deep forecasters achieve high accuracy on normal data but often fail when distribution shifts occur. We propose Weighted Contrastive Adaptation (WECA), a Weighted contrastive objective that aligns normal and anomaly-augmented representations, preserving anomaly-relevant information while maintaining consistency under benign variations. Evaluations on a nationwide ATM transaction dataset with domain-informed anomaly injection show that WECA improves SMAPE on anomaly-affected data by 6.1 percentage points compared to a normally trained baseline, with negligible degradation on normal data. These results demonstrate that WECA enhances forecasting reliability under anomalies without sacrificing performance during regular operations.

