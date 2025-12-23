---
layout: default
title: DIVER-1 : Deep Integration of Vast Electrophysiological Recordings at Scale
---

# DIVER-1 : Deep Integration of Vast Electrophysiological Recordings at Scale
**arXiv**：[2512.19097v1](https://arxiv.org/abs/2512.19097) · [PDF](https://arxiv.org/pdf/2512.19097.pdf)  
**作者**：Danny Dongyeop Han, Yonghyeon Gwon, Ahhyun Lucy Lee, Taeyang Lee, Seong Jin Lee, Jubin Choi, Sebin Lee, Jihyun Bang, Seungju Lee, David Keetae Park, Shinjae Yoo, Chun Kee Chung, Jiook Cha  

**一句话要点**：提出DIVER-1脑电基础模型，通过大规模数据与高效缩放提升性能。

**关键词**：脑电基础模型, 缩放定律分析, 任意变量注意力, 多域重建, 大规模数据集

## 3 点简述
- 核心问题：现有脑电基础模型规模有限，缩放性能证据明确但未充分探索。
- 方法要点：训练于最大多样数据集，引入架构创新如任意变量注意力与多域重建。
- 实验或效果：建立缩放定律，模型在基准测试中达到最先进性能。

## 摘要（原文）

> Electrophysiology signals such as EEG and iEEG are central to neuroscience, brain-computer interfaces, and clinical applications, yet existing foundation models remain limited in scale despite clear evidence that scaling improves performance. We introduce DIVER-1, a family of EEG and iEEG foundation models trained on the largest and most diverse corpus to date-5.3k hours of iEEG and 54k hours of EEG (1.6M channel-hours from over 17.7k subjects)-and scaled up to 1.82B parameters. We present the first systematic scaling law analysis for this domain, showing that they follow data-constrained scaling laws: for a given amount of data and compute, smaller models trained for extended epochs consistently outperform larger models trained briefly. This behavior contrasts with prior electrophysiology foundation models that emphasized model size over training duration. To achieve strong performance, we also design architectural innovations including any-variate attention, sliding temporal conditional positional encoding, and multi-domain reconstruction. DIVER-1 iEEG and EEG models each achieve state-of-the-art performance on their respective benchmarks, establishing a concrete guidelines for efficient scaling and resource allocation in electrophysiology foundation model development.

