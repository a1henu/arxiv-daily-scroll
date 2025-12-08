---
layout: default
title: TS-HINT: Enhancing Semiconductor Time Series Regression Using Attention Hints From Large Language Model Reasoning
---

# TS-HINT: Enhancing Semiconductor Time Series Regression Using Attention Hints From Large Language Model Reasoning
**arXiv**：[2512.05419v1](https://arxiv.org/abs/2512.05419) · [PDF](https://arxiv.org/pdf/2512.05419.pdf)  
**作者**：Jonathan Adam Rico, Nagarajan Raghavan, Senthilnath Jayavelu  

**一句话要点**：提出TS-HINT框架，通过大语言模型推理提供注意力提示，增强半导体时间序列回归在有限数据下的性能。

**关键词**：时间序列基础模型, 注意力机制, 少样本学习, 半导体制造, 多元时间序列回归

## 3 点简述
- 现有方法依赖静态特征提取，导致时间动态信息丢失，且需要大量训练数据。
- TS-HINT结合链式思维推理，基于注意力机制和显著性数据提供训练中的注意力提示。
- 实验显示模型在少样本学习中有效，可直接从多元时间序列特征学习。

## 摘要（原文）

> Existing data-driven methods rely on the extraction of static features from time series to approximate the material removal rate (MRR) of semiconductor manufacturing processes such as chemical mechanical polishing (CMP). However, this leads to a loss of temporal dynamics. Moreover, these methods require a large amount of data for effective training. In this paper, we propose TS-Hint, a Time Series Foundation Model (TSFM) framework, integrated with chain-of-thought reasoning which provides attention hints during training based on attention mechanism data and saliency data. Experimental results demonstrate the effectiveness of our model in limited data settings via few-shot learning and can learn directly from multivariate time series features.

