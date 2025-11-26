---
layout: default
title: MSTN: Fast and Efficient Multivariate Time Series Model
---

# MSTN: Fast and Efficient Multivariate Time Series Model
**arXiv**：[2511.20577v1](https://arxiv.org/abs/2511.20577) · [PDF](https://arxiv.org/pdf/2511.20577.pdf)  
**作者**：Sumit S Shevtekar, Chandresh K Maurya, Gourab Sil  

**一句话要点**：提出MSTN以解决多变量时间序列中多尺度动态建模不足的问题

**关键词**：多变量时间序列, 多尺度建模, 门控融合, 长程依赖, 时间序列预测, 深度学习架构

## 3 点简述
- 现有模型依赖固定结构先验，难以适应多尺度时间变化和突发高幅事件
- MSTN集成多尺度卷积编码、序列建模和门控融合机制，实现自适应特征整合
- 在32个基准数据集上24个达到SOTA，验证了其在预测、插补和分类中的有效性

## 摘要（原文）

> Real-world time-series data is highly non stationary and complex in dynamics that operate across multiple timescales, ranging from fast, short-term changes to slow, long-term trends. Most existing models rely on fixed-scale structural priors, such as patch-based tokenization, fixed frequency transformations, or frozen backbone architectures. This often leads to over-regularization of temporal dynamics, which limits their ability to adaptively model the full spectrum of temporal variations and impairs their performance on unpredictable, Sudden, high-magnitude events. To address this, we introduce the Multi-scale Temporal Network (MSTN), a novel deep learning architecture founded on a hierarchical multi-scale and sequence modeling principle. The MSTN framework integrates: (i) a multi-scale convolutional encoder that constructs a hierarchical feature pyramid for local patterns (ii) a sequence modeling component for long-range temporal dependencies. We empirically validate this with BiLSTM and Transformer variants, establishing a flexible foundation for future architectural advancements. and (iii) a gated fusion mechanism augmented with squeeze-and-excitation (SE) and multi-head temporal attention (MHTA) for dynamic, context-aware feature integration. This design enables MSTN to adaptively model temporal patterns from milliseconds to long-range dependencies within a unified framework. Extensive evaluations across time-series long-horizon forecasting, imputation, classification and generalizability study demonstrate that MSTN achieves competitive state-of-the-art (SOTA) performance, showing improvements over contemporary approaches including EMTSF, LLM4TS, HiMTM, TIME-LLM, MTST, SOFTS, iTransformer, TimesNet, and PatchTST. In total, MSTN establishes new SOTA performance on 24 of 32 benchmark datasets, demonstrating its consistent performance across diverse temporal tasks.

