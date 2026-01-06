---
layout: default
title: Hunting for "Oddballs" with Machine Learning: Detecting Anomalous Exoplanets Using a Deep-Learned Low-Dimensional Representation of Transit Spectra with Autoencoders
---

# Hunting for "Oddballs" with Machine Learning: Detecting Anomalous Exoplanets Using a Deep-Learned Low-Dimensional Representation of Transit Spectra with Autoencoders
**arXiv**：[2601.02324v1](https://arxiv.org/abs/2601.02324) · [PDF](https://arxiv.org/pdf/2601.02324.pdf)  
**作者**：Alexander Roman, Emilie Panek, Roy T. Forestano, Eyup B. Unlu, Katia Matcheva, Konstantin T. Matchev  

**一句话要点**：提出基于自编码器降维的异常检测方法，用于识别系外行星大气中的化学异常目标

**关键词**：异常检测, 自编码器, 系外行星大气, 降维表示, 机器学习

## 3 点简述
- 核心问题：如何在大规模系外行星光谱数据中高效检测化学异常（如CO2富集大气）
- 方法要点：使用自编码器学习低维表示，在潜在空间应用K-means聚类等异常检测策略
- 实验或效果：潜在空间方法在高达30 ppm噪声下保持稳健，性能优于原始光谱空间

## 摘要（原文）

> This study explores the application of autoencoder-based machine learning techniques for anomaly detection to identify exoplanet atmospheres with unconventional chemical signatures using a low-dimensional data representation. We use the Atmospheric Big Challenge (ABC) database, a publicly available dataset with over 100,000 simulated exoplanet spectra, to construct an anomaly detection scenario by defining CO2-rich atmospheres as anomalies and CO2-poor atmospheres as the normal class. We benchmarked four different anomaly detection strategies: Autoencoder Reconstruction Loss, One-Class Support Vector Machine (1 class-SVM), K-means Clustering, and Local Outlier Factor (LOF). Each method was evaluated in both the original spectral space and the autoencoder's latent space using Receiver Operating Characteristic (ROC) curves and Area Under the Curve (AUC) metrics. To test the performance of the different methods under realistic conditions, we introduced Gaussian noise levels ranging from 10 to 50 ppm. Our results indicate that anomaly detection is consistently more effective when performed within the latent space across all noise levels. Specifically, K-means clustering in the latent space emerged as a stable and high-performing method. We demonstrate that this anomaly detection approach is robust to noise levels up to 30 ppm (consistent with realistic space-based observations) and remains viable even at 50 ppm when leveraging latent space representations. On the other hand, the performance of the anomaly detection methods applied directly in the raw spectral space degrades significantly with increasing the level of noise. This suggests that autoencoder-driven dimensionality reduction offers a robust methodology for flagging chemically anomalous targets in large-scale surveys where exhaustive retrievals are computationally prohibitive.

