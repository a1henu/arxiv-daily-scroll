---
layout: default
title: Quality-Aware Framework for Video-Derived Respiratory Signals
---

# Quality-Aware Framework for Video-Derived Respiratory Signals
**arXiv**：[2512.14093v1](https://arxiv.org/abs/2512.14093) · [PDF](https://arxiv.org/pdf/2512.14093.pdf)  
**作者**：Nhi Nguyen, Constantino Álvarez Casado, Le Nguyen, Manuel Lage Cañellas, Miguel Bordallo López  

**一句话要点**：提出质量感知框架以提升视频呼吸信号估计的可靠性

**关键词**：视频呼吸率估计, 质量感知框架, 信号融合, 远程光电容积描记术, 机器学习模型, 光谱估计

## 3 点简述
- 视频呼吸率估计因信号质量不一致而不可靠
- 集成多源信号并动态评估可靠性，训练模型预测准确性
- 在三个公开数据集上验证，降低估计误差，性能提升依赖数据集特性

## 摘要（原文）

> Video-based respiratory rate (RR) estimation is often unreliable due to inconsistent signal quality across extraction methods. We present a predictive, quality-aware framework that integrates heterogeneous signal sources with dynamic assessment of reliability. Ten signals are extracted from facial remote photoplethysmography (rPPG), upper-body motion, and deep learning pipelines, and analyzed using four spectral estimators: Welch's method, Multiple Signal Classification (MUSIC), Fast Fourier Transform (FFT), and peak detection. Segment-level quality indices are then used to train machine learning models that predict accuracy or select the most reliable signal. This enables adaptive signal fusion and quality-based segment filtering. Experiments on three public datasets (OMuSense-23, COHFACE, MAHNOB-HCI) show that the proposed framework achieves lower RR estimation errors than individual methods in most cases, with performance gains depending on dataset characteristics. These findings highlight the potential of quality-driven predictive modeling to deliver scalable and generalizable video-based respiratory monitoring solutions.

