---
layout: default
title: Rapid Augmentations for Time Series (RATS): A High-Performance Library for Time Series Augmentation
---

# Rapid Augmentations for Time Series (RATS): A High-Performance Library for Time Series Augmentation
**arXiv**：[2601.03159v1](https://arxiv.org/abs/2601.03159) · [PDF](https://arxiv.org/pdf/2601.03159.pdf)  
**作者**：Wadie Skaf, Felix Kern, Aryamaan Basu Roy, Tejas Pradhan, Roman Kalkreuth, Holger Hoos  

**一句话要点**：提出RATS高性能时间序列增强库，以解决现有Python库在大规模数据下的性能瓶颈问题。

**关键词**：时间序列增强, 高性能计算, Rust编程, 数据增强库, 并行处理

## 3 点简述
- 核心问题：现有时间序列增强库（如tsaug）基于Python，在大数据集上运行时间指数增长，限制生产级应用。
- 方法要点：RATS用Rust编写，提供Python绑定（RATSpy），实现多种增强方法，支持统一流水线和并行化。
- 实验或效果：在143个数据集上，RATSpy比tsaug平均提速74.5%，内存使用峰值降低达47.9%。

## 摘要（原文）

> Time series augmentation is critical for training robust deep learning models, particularly in domains where labelled data is scarce and expensive to obtain. However, existing augmentation libraries for time series, mainly written in Python, suffer from performance bottlenecks, where running time grows exponentially as dataset sizes increase -- an aspect limiting their applicability in large-scale, production-grade systems. We introduce RATS (Rapid Augmentations for Time Series), a high-performance library for time series augmentation written in Rust with Python bindings (RATSpy). RATS implements multiple augmentation methods spanning basic transformations, frequency-domain operations and time warping techniques, all accessible through a unified pipeline interface with built-in parallelisation. Comprehensive benchmarking of RATSpy versus a commonly used library (tasug) on 143 datasets demonstrates that RATSpy achieves an average speedup of 74.5\% over tsaug (up to 94.8\% on large datasets), with up to 47.9\% less peak memory usage.

