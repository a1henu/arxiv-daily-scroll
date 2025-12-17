---
layout: default
title: FusAD: Time-Frequency Fusion with Adaptive Denoising for General Time Series Analysis
---

# FusAD: Time-Frequency Fusion with Adaptive Denoising for General Time Series Analysis
**arXiv**：[2512.14078v1](https://arxiv.org/abs/2512.14078) · [PDF](https://arxiv.org/pdf/2512.14078.pdf)  
**作者**：Da Zhang, Bingyu Li, Zhiyuan Zhao, Feiping Nie, Junyu Gao, Xuelong Li  

**一句话要点**：提出FusAD统一框架，通过自适应时频融合与去噪解决多任务时间序列分析难题。

**关键词**：时间序列分析, 自适应时频融合, 自适应去噪, 多任务学习, 统一框架

## 3 点简述
- 核心问题：现有方法难以统一处理多任务和多样时间序列类型，且受噪声和复杂动态模式影响。
- 方法要点：结合傅里叶与小波变换进行自适应时频融合，并集成自适应去噪机制以增强特征鲁棒性。
- 实验或效果：在主流基准上，FusAD在分类、预测和异常检测任务中优于先进模型，保持高效和可扩展性。

## 摘要（原文）

> Time series analysis plays a vital role in fields such as finance, healthcare, industry, and meteorology, underpinning key tasks including classification, forecasting, and anomaly detection. Although deep learning models have achieved remarkable progress in these areas in recent years, constructing an efficient, multi-task compatible, and generalizable unified framework for time series analysis remains a significant challenge. Existing approaches are often tailored to single tasks or specific data types, making it difficult to simultaneously handle multi-task modeling and effectively integrate information across diverse time series types. Moreover, real-world data are often affected by noise, complex frequency components, and multi-scale dynamic patterns, which further complicate robust feature extraction and analysis. To ameliorate these challenges, we propose FusAD, a unified analysis framework designed for diverse time series tasks. FusAD features an adaptive time-frequency fusion mechanism, integrating both Fourier and Wavelet transforms to efficiently capture global-local and multi-scale dynamic features. With an adaptive denoising mechanism, FusAD automatically senses and filters various types of noise, highlighting crucial sequence variations and enabling robust feature extraction in complex environments. In addition, the framework integrates a general information fusion and decoding structure, combined with masked pre-training, to promote efficient learning and transfer of multi-granularity representations. Extensive experiments demonstrate that FusAD consistently outperforms state-of-the-art models on mainstream time series benchmarks for classification, forecasting, and anomaly detection tasks, while maintaining high efficiency and scalability. Code is available at https://github.com/zhangda1018/FusAD.

