---
layout: default
title: Modern Deep Learning Approaches for Cricket Shot Classification: A Comprehensive Baseline Study
---

# Modern Deep Learning Approaches for Cricket Shot Classification: A Comprehensive Baseline Study
**arXiv**：[2510.09187v1](https://arxiv.org/abs/2510.09187) · [PDF](https://arxiv.org/pdf/2510.09187.pdf)  
**作者**：Sungwoo Kang  

**一句话要点**：提出现代深度学习基线研究，系统比较七种方法以解决板球击球分类问题。

**关键词**：板球击球分类, 深度学习基线, 时空特征建模, 标准化评估, 视频序列分析, MLOps实践

## 3 点简述
- 核心问题：板球击球视频分类需有效建模时空特征，现有文献与实际性能存在显著差距。
- 方法要点：比较CNN-LSTM、注意力模型、视觉Transformer、迁移学习及EfficientNet-GRU组合。
- 实验或效果：现代SOTA方法达92.25%准确率，强调标准化评估协议的重要性。

## 摘要（原文）

> Cricket shot classification from video sequences remains a challenging
> problem in sports video analysis, requiring effective modeling of both spatial
> and temporal features. This paper presents the first comprehensive baseline
> study comparing seven different deep learning approaches across four distinct
> research paradigms for cricket shot classification. We implement and
> systematically evaluate traditional CNN-LSTM architectures, attention-based
> models, vision transformers, transfer learning approaches, and modern
> EfficientNet-GRU combinations on a unified benchmark. A critical finding of our
> study is the significant performance gap between claims in academic literature
> and practical implementation results. While previous papers reported accuracies
> of 96\% (Balaji LRCN), 99.2\% (IJERCSE), and 93\% (Sensors), our standardized
> re-implementations achieve 46.0\%, 55.6\%, and 57.7\% respectively. Our modern
> SOTA approach, combining EfficientNet-B0 with a GRU-based temporal model,
> achieves 92.25\% accuracy, demonstrating that substantial improvements are
> possible with modern architectures and systematic optimization. All
> implementations follow modern MLOps practices with PyTorch Lightning, providing
> a reproducible research platform that exposes the critical importance of
> standardized evaluation protocols in sports video analysis research.

