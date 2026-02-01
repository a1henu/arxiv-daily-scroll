---
layout: default
title: Conditional Generative Framework with Peak-Aware Attention for Robust Chemical Detection under Interferences
---

# Conditional Generative Framework with Peak-Aware Attention for Robust Chemical Detection under Interferences
**arXiv**：[2601.21246v1](https://arxiv.org/abs/2601.21246) · [PDF](https://arxiv.org/pdf/2601.21246.pdf)  
**作者**：Namkyung Yoon, Sanghong Kim, Hwangnam Kim  

**一句话要点**：提出基于峰值感知条件生成框架以提升干扰下GC-MS化学检测的可靠性

**关键词**：化学检测, 条件生成对抗网络, 峰值感知, GC-MS, 干扰物质, 合成数据生成

## 3 点简述
- 核心问题：GC-MS在干扰物质存在时可靠性下降，导致灵敏度降低和误报。
- 方法要点：采用峰值感知机制和条件生成对抗网络，生成合成GC-MS信号以扩充数据集。
- 实验或效果：生成数据验证有效性，提升AI判别模型性能，减少误报并保持峰值多样性。

## 摘要（原文）

> Gas chromatography-mass spectrometry (GC-MS) is a widely used analytical method for chemical substance detection, but measurement reliability tends to deteriorate in the presence of interfering substances. In particular, interfering substances cause nonspecific peaks, residence time shifts, and increased background noise, resulting in reduced sensitivity and false alarms. To overcome these challenges, in this paper, we propose an artificial intelligence discrimination framework based on a peak-aware conditional generative model to improve the reliability of GC-MS measurements under interference conditions. The framework is learned with a novel peak-aware mechanism that highlights the characteristic peaks of GC-MS data, allowing it to generate important spectral features more faithfully. In addition, chemical and solvent information is encoded in a latent vector embedded with it, allowing a conditional generative adversarial neural network (CGAN) to generate a synthetic GC-MS signal consistent with the experimental conditions. This generates an experimental dataset that assumes indirect substance situations in chemical substance data, where acquisition is limited without conducting real experiments. These data are used for the learning of AI-based GC-MS discrimination models to help in accurate chemical substance discrimination. We conduct various quantitative and qualitative evaluations of the generated simulated data to verify the validity of the proposed framework. We also verify how the generative model improves the performance of the AI discrimination framework. Representatively, the proposed method is shown to consistently achieve cosine similarity and Pearson correlation coefficient values above 0.9 while preserving peak number diversity and reducing false alarms in the discrimination model.

