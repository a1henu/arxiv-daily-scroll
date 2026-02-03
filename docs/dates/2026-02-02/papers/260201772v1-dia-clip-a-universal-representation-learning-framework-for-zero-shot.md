---
layout: default
title: DIA-CLIP: a universal representation learning framework for zero-shot DIA proteomics
---

# DIA-CLIP: a universal representation learning framework for zero-shot DIA proteomics
**arXiv**：[2602.01772v1](https://arxiv.org/abs/2602.01772) · [PDF](https://arxiv.org/pdf/2602.01772.pdf)  
**作者**：Yucheng Liao, Han Wen, Weinan E, Weijie Zhang  

**一句话要点**：提出DIA-CLIP框架，通过跨模态表示学习实现零样本DIA蛋白质组学分析

**关键词**：DIA质谱分析, 零样本学习, 跨模态表示学习, 蛋白质组学, 对比学习

## 3 点简述
- 核心问题：现有DIA分析框架依赖半监督训练，易过拟合且跨物种泛化性差
- 方法要点：结合双编码器对比学习和编码器-解码器架构，统一肽段与光谱特征表示
- 实验或效果：在多个基准测试中优于现有工具，蛋白质识别提升45%，误识别减少12%

## 摘要（原文）

> Data-independent acquisition mass spectrometry (DIA-MS) has established itself as a cornerstone of proteomic profiling and large-scale systems biology, offering unparalleled depth and reproducibility. Current DIA analysis frameworks, however, require semi-supervised training within each run for peptide-spectrum match (PSM) re-scoring. This approach is prone to overfitting and lacks generalizability across diverse species and experimental conditions. Here, we present DIA-CLIP, a pre-trained model shifting the DIA analysis paradigm from semi-supervised training to universal cross-modal representation learning. By integrating dual-encoder contrastive learning framework with encoder-decoder architecture, DIA-CLIP establishes a unified cross-modal representation for peptides and corresponding spectral features, achieving high-precision, zero-shot PSM inference. Extensive evaluations across diverse benchmarks demonstrate that DIA-CLIP consistently outperforms state-of-the-art tools, yielding up to a 45% increase in protein identification while achieving a 12% reduction in entrapment identifications. Moreover, DIA-CLIP holds immense potential for diverse practical applications, such as single-cell and spatial proteomics, where its enhanced identification depth facilitates the discovery of novel biomarkers and the elucidates of intricate cellular mechanisms.

