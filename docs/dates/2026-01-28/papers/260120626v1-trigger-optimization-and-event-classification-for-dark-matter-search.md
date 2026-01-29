---
layout: default
title: Trigger Optimization and Event Classification for Dark Matter Searches in the CYGNO Experiment Using Machine Learning
---

# Trigger Optimization and Event Classification for Dark Matter Searches in the CYGNO Experiment Using Machine Learning
**arXiv**：[2601.20626v1](https://arxiv.org/abs/2601.20626) · [PDF](https://arxiv.org/pdf/2601.20626.pdf)  
**作者**：F. D. Amaro, R. Antonietti, E. Baracchini, L. Benussi, C. Capoccia, M. Caponero, L. G. M. de Carvalho, G. Cavoto, I. A. Costa, A. Croce, M. D'Astolfo, G. D'Imperio, G. Dho, E. Di Marco, J. M. F. dos Santos, D. Fiorina, F. Iacoangeli, Z. Islam, E. Kemp, H. P. Lima, G. Maccarrone, R. D. P. Mano, D. J. G. Marques, G. Mazzitelli, P. Meloni, A. Messina, C. M. B. Monteiro, R. A. Nobrega, G. M. Oppedisano, I. F. Pains, E. Paoletti, F. Petrucci, S. Piacentini, D. Pierluigi, D. Pinci, F. Renga, A. Russo, G. Saviano, P. A. O. C. Silva, N. J. Spooner, R. Tesauro, S. Tomassini, D. Tozzi  

**一句话要点**：提出基于机器学习的无监督数据压缩和弱监督事件分类方法，以优化CYGNO实验的触发与背景鉴别。

**关键词**：暗物质探测, 光学读出TPC, 无监督学习, 弱监督分类, 数据压缩, 事件分类

## 3 点简述
- 核心问题：光学读出TPC产生稀疏大图像，实时触发与背景鉴别困难。
- 方法要点：使用卷积自编码器无监督压缩数据，基于CWoLa弱监督分类核反冲事件。
- 实验或效果：数据压缩保留93%信号强度，分类性能接近理论极限，支持实时处理。

## 摘要（原文）

> The CYGNO experiment employs an optical-readout Time Projection Chamber (TPC) to search for rare low-energy interactions using finely resolved scintillation images. While the optical readout provides rich topological information, it produces large, sparse megapixel images that challenge real-time triggering, data reduction, and background discrimination.
>   We summarize two complementary machine-learning approaches developed within CYGNO. First, we present a fast and fully unsupervised strategy for online data reduction based on reconstruction-based anomaly detection. A convolutional autoencoder trained exclusively on pedestal images (i.e. frames acquired with GEM amplification disabled) learns the detector noise morphology and highlights particle-induced structures through localized reconstruction residuals, from which compact Regions of Interest (ROIs) are extracted. On real prototype data, the selected configuration retains (93.0 +/- 0.2)% of reconstructed signal intensity while discarding (97.8 +/- 0.1)% of the image area, with ~25 ms per-frame inference time on a consumer GPU.
>   Second, we report a weakly supervised application of the Classification Without Labels (CWoLa) framework to data acquired with an Americium--Beryllium neutron source. Using only mixed AmBe and standard datasets (no event-level labels), a convolutional classifier learns to identify nuclear-recoil-like topologies. The achieved performance approaches the theoretical limit imposed by the mixture composition and isolates a high-score population with compact, approximately circular morphologies consistent with nuclear recoils.

