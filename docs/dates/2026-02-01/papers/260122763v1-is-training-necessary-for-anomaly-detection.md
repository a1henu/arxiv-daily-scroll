---
layout: default
title: Is Training Necessary for Anomaly Detection?
---

# Is Training Necessary for Anomaly Detection?
**arXiv**：[2601.22763v1](https://arxiv.org/abs/2601.22763) · [PDF](https://arxiv.org/pdf/2601.22763.pdf)  
**作者**：Xingwu Zhang, Guanxuan Li, Paul Henderson, Gerardo Aragon-Camarasa, Zijun Long  

**一句话要点**：提出基于检索的无训练异常检测方法RAD，解决多类无监督异常检测中的保真度-稳定性困境。

**关键词**：无监督异常检测, 检索方法, 训练免费, 多类检测, 特征匹配

## 3 点简述
- 揭示当前基于重构的异常检测方法存在保真度与稳定性的内在矛盾。
- 提出RAD方法，通过存储无异常特征并多级检索匹配，无需训练即可检测异常。
- 实验显示RAD在多个基准上达到SOTA性能，单张图像即可实现高精度检测。

## 摘要（原文）

> Current state-of-the-art multi-class unsupervised anomaly detection (MUAD) methods rely on training encoder-decoder models to reconstruct anomaly-free features. We first show these approaches have an inherent fidelity-stability dilemma in how they detect anomalies via reconstruction residuals. We then abandon the reconstruction paradigm entirely and propose Retrieval-based Anomaly Detection (RAD). RAD is a training-free approach that stores anomaly-free features in a memory and detects anomalies through multi-level retrieval, matching test patches against the memory. Experiments demonstrate that RAD achieves state-of-the-art performance across four established benchmarks (MVTec-AD, VisA, Real-IAD, 3D-ADAM) under both standard and few-shot settings. On MVTec-AD, RAD reaches 96.7\% Pixel AUROC with just a single anomaly-free image compared to 98.5\% of RAD's full-data performance. We further prove that retrieval-based scores theoretically upper-bound reconstruction-residual scores. Collectively, these findings overturn the assumption that MUAD requires task-specific training, showing that state-of-the-art anomaly detection is feasible with memory-based retrieval. Our code is available at https://github.com/longkukuhi/RAD.

