---
layout: default
title: Transformer-based Parameter Fitting of Models derived from Bloch-McConnell Equations for CEST MRI Analysis
---

# Transformer-based Parameter Fitting of Models derived from Bloch-McConnell Equations for CEST MRI Analysis
**arXiv**：[2602.06574v1](https://arxiv.org/abs/2602.06574) · [PDF](https://arxiv.org/pdf/2602.06574.pdf)  
**作者**：Christof Duhme, Chris Lippe, Verena Hoerr, Xiaoyi Jiang  

**一句话要点**：提出基于Transformer的神经网络，以拟合CEST MRI中Bloch-McConnell模型参数，提升体外光谱分析精度。

**关键词**：CEST MRI分析, Transformer神经网络, 参数拟合, Bloch-McConnell方程, 自监督训练

## 3 点简述
- CEST MRI量化困难，因信号受多生理变量复杂交互影响。
- 采用自监督训练的Transformer网络拟合代谢物浓度、交换与弛豫率等参数。
- 实验显示，该方法明显优于传统基于梯度的求解器。

## 摘要（原文）

> Chemical exchange saturation transfer (CEST) MRI is a non-invasive imaging modality for detecting metabolites. It offers higher resolution and sensitivity compared to conventional magnetic resonance spectroscopy (MRS). However, quantification of CEST data is challenging because the measured signal results from a complex interplay of many physiological variables. Here, we introduce a transformer-based neural network to fit parameters such as metabolite concentrations, exchange and relaxation rates of a physical model derived from Bloch-McConnell equations to in-vitro CEST spectra. We show that our self-supervised trained neural network clearly outperforms the solution of classical gradient-based solver.

