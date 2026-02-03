---
layout: default
title: Spectral Text Fusion: A Frequency-Aware Approach to Multimodal Time-Series Forecasting
---

# Spectral Text Fusion: A Frequency-Aware Approach to Multimodal Time-Series Forecasting
**arXiv**：[2602.01588v1](https://arxiv.org/abs/2602.01588) · [PDF](https://arxiv.org/pdf/2602.01588.pdf)  
**作者**：Huu Hiep Nguyen, Minh Hoang Nguyen, Dung Nguyen, Hung Le  

**一句话要点**：提出SpecTF框架，通过频域融合解决多模态时间序列预测中文本与时间序列的全局上下文不匹配问题。

**关键词**：多模态时间序列预测, 频域融合, 文本嵌入, 跨注意力机制, 轻量级框架

## 3 点简述
- 核心问题：现有方法在融合文本与时间序列时，忽略多尺度时间影响，导致局部对齐与全局上下文不匹配。
- 方法要点：将文本嵌入投影到频域，通过跨注意力机制自适应重加权频带，再映射回时域进行预测。
- 实验或效果：在多个数据集上显著优于先进模型，且参数更少，代码已开源。

## 摘要（原文）

> Multimodal time series forecasting is crucial in real-world applications, where decisions depend on both numerical data and contextual signals. The core challenge is to effectively combine temporal numerical patterns with the context embedded in other modalities, such as text. While most existing methods align textual features with time-series patterns one step at a time, they neglect the multiscale temporal influences of contextual information such as time-series cycles and dynamic shifts. This mismatch between local alignment and global textual context can be addressed by spectral decomposition, which separates time series into frequency components capturing both short-term changes and long-term trends. In this paper, we propose SpecTF, a simple yet effective framework that integrates the effect of textual data on time series in the frequency domain. Our method extracts textual embeddings, projects them into the frequency domain, and fuses them with the time series' spectral components using a lightweight cross-attention mechanism. This adaptively reweights frequency bands based on textual relevance before mapping the results back to the temporal domain for predictions. Experimental results demonstrate that SpecTF significantly outperforms state-of-the-art models across diverse multi-modal time series datasets while utilizing considerably fewer parameters. Code is available at https://github.com/hiepnh137/SpecTF.

