---
layout: default
title: WaveSim: A Wavelet-based Multi-scale Similarity Metric for Weather and Climate Fields
---

# WaveSim: A Wavelet-based Multi-scale Similarity Metric for Weather and Climate Fields
**arXiv**：[2512.14656v1](https://arxiv.org/abs/2512.14656) · [PDF](https://arxiv.org/pdf/2512.14656.pdf)  
**作者**：Gabriele Accarino, Viviana Acquaviva, Sara Shamekh, Duncan Watson-Parris, David Lawrence  

**一句话要点**：提出WaveSim，一种基于小波的多尺度相似性度量，用于评估天气和气候空间场。

**关键词**：小波变换, 多尺度相似性度量, 天气气候场评估, 模型评估, 空间场分析, PyTorch实现

## 3 点简述
- 传统点对点度量无法将误差归因于物理尺度或差异模式。
- WaveSim利用小波变换分解场，通过幅度、位移和结构三个正交分量计算多尺度相似性。
- 在合成测试和地球系统模型气候变率案例中验证其敏感性和适用性。

## 摘要（原文）

> We introduce WaveSim, a multi-scale similarity metric for the evaluation of spatial fields in weather and climate applications. WaveSim exploits wavelet transforms to decompose input fields into scale-specific wavelet coefficients. The metric is built by multiplying three orthogonal components derived from these coefficients: Magnitude, which quantifies similarities in the energy distribution of the coefficients, i.e., the intensity of the field; Displacement, which captures spatial shift by comparing the centers of mass of normalized energy distributions; and Structure, which assesses pattern organization independent of location and amplitude. Each component yields a scale-specific similarity score ranging from 0 (no similarity) to 1 (perfect similarity), which are then combined across scales to produce an overall similarity measure. We first evaluate WaveSim using synthetic test cases, applying controlled spatial and temporal perturbations to systematically assess its sensitivity and expected behavior. We then demonstrate its applicability to physically relevant case studies of key modes of climate variability in Earth System Models. Traditional point-wise metrics lack a mechanism for attributing errors to physical scales or modes of dissimilarity. By operating in the wavelet domain and decomposing the signal along independent axes, WaveSim bypasses these limitations and provides an interpretable and diagnostically rich framework for assessing similarity in complex fields. Additionally, the WaveSim framework allows users to place emphasis on a specific scale or component, and lends itself to user-specific model intercomparison, model evaluation, and calibration and training of forecasting systems. We provide a PyTorch-ready implementation of WaveSim, along with all evaluation scripts, at: https://github.com/gabrieleaccarino/wavesim.

