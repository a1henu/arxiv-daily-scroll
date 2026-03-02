---
layout: default
title: Hybrid Quantum Temporal Convolutional Networks
---

# Hybrid Quantum Temporal Convolutional Networks
**arXiv**：[2602.23578v1](https://arxiv.org/abs/2602.23578) · [PDF](https://arxiv.org/pdf/2602.23578.pdf)  
**作者**：Junghoon Justin Park, Maria Pak, Sebin Lee, Samuel Yen-Chi Chen, Shinjae Yoo, Huan-Hsin Tseng, Jiook Cha  

**一句话要点**：提出混合量子时序卷积网络以解决多元时序数据参数效率问题

**关键词**：量子机器学习, 时序卷积网络, 多元时序分析, 参数效率, 长程依赖捕获

## 3 点简述
- 量子机器学习处理复杂多元时序数据面临可扩展性挑战
- 结合经典时序窗口与量子卷积核心，通过共享量子电路捕获长程依赖并减少参数
- 在合成NARMA序列和高维EEG数据上验证，多元任务表现优于经典基线，数据有限时参数效率高

## 摘要（原文）

> Quantum machine learning models for sequential data face scalability challenges with complex multivariate signals. We introduce the Hybrid Quantum Temporal Convolutional Network (HQTCN), which combines classical temporal windowing with a quantum convolutional neural network core. By applying a shared quantum circuit across temporal windows, HQTCN captures long-range dependencies while achieving significant parameter reduction. Evaluated on synthetic NARMA sequences and high-dimensional EEG time-series, HQTCN performs competitively with classical baselines on univariate data and outperforms all baselines on multivariate tasks. The model demonstrates particular strength under data-limited conditions, maintaining high performance with substantially fewer parameters than conventional approaches. These results establish HQTCN as a parameter-efficient approach for multivariate time-series analysis.

