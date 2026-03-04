---
layout: default
title: Adapting Time Series Foundation Models through Data Mixtures
---

# Adapting Time Series Foundation Models through Data Mixtures
**arXiv**：[2603.02840v1](https://arxiv.org/abs/2603.02840) · [PDF](https://arxiv.org/pdf/2603.02840.pdf)  
**作者**：Thomas L. Lee, Edoardo M. Ponti, Amos Storkey  

**一句话要点**：提出MixFT通过数据混合适应时间序列基础模型以提升零样本预测

**关键词**：时间序列基础模型, 零样本预测, 数据混合, 贝叶斯混合, 微调策略

## 3 点简述
- 核心问题：时间序列基础模型在新领域零样本预测性能下降，因数据分布异质性。
- 方法要点：使用贝叶斯混合重新划分数据为同质子域，并分别微调模块。
- 实验或效果：MixFT优于按数据集微调方法，提升零样本预测准确性。

## 摘要（原文）

> Time series foundation models (TSFMs) have become increasingly popular for zero-shot forecasting. However, for a new time series domain not fully covered by the pretraining set, performance can suffer. Therefore, when a practitioner cares about a new domain and has access to a set of related datasets, the question arises: how best to fine-tune a TSFM to improve zero-shot forecasting? A typical approach to this type of problem is to fine-tune a LoRA module on all datasets or separately on each dataset. Tuning a separate module on each dataset allows for the specialisation of the TSFM to different types of data distribution, by selecting differing combinations of per-dataset modules for different time series contexts. However, we find that, using per-dataset modules might not be optimal, since a time series dataset can contain data from several types of distributions, i.e. sub-domains. This can be due to the distribution shifting or having differing distributions for different dimensions of the time series. Hence, we propose MixFT which re-divides the data using Bayesian mixtures into sets that best represent the sub-domains present in the data, and fine-tunes separately on each of these sets. This re-division of the data ensures that each set is more homogeneous, leading to fine-tuned modules focused on specific sub-domains. Our experiments show that MixFT performs better than per-dataset methods and when fine-tuning a single module on all the data. This suggests that by re-partitioning the data to represent sub-domains we can better specialise TSFMs to improve zero-shot forecasting.

