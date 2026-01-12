---
layout: default
title: Phase4DFD: Multi-Domain Phase-Aware Attention for Deepfake Detection
---

# Phase4DFD: Multi-Domain Phase-Aware Attention for Deepfake Detection
**arXiv**：[2601.05861v1](https://arxiv.org/abs/2601.05861) · [PDF](https://arxiv.org/pdf/2601.05861.pdf)  
**作者**：Zhen-Xin Lin, Shang-Kuan Chen  

**一句话要点**：提出Phase4DFD框架，通过相位感知注意力增强深度伪造检测在频率域的性能。

**关键词**：深度伪造检测, 频率域分析, 相位感知注意力, 多域表示, FFT幅度, LBP特征

## 3 点简述
- 现有方法主要依赖频谱幅度，忽略了相位信息在检测深度伪造中的潜在作用。
- 引入相位感知注意力模块，利用相位不连续性引导模型关注最指示伪造的频率模式。
- 在CIFAKE和DFFD数据集上优于现有方法，并通过消融研究验证相位建模的互补性。

## 摘要（原文）

> Recent deepfake detection methods have increasingly explored frequency domain representations to reveal manipulation artifacts that are difficult to detect in the spatial domain. However, most existing approaches rely primarily on spectral magnitude, implicitly under exploring the role of phase information. In this work, we propose Phase4DFD, a phase aware frequency domain deepfake detection framework that explicitly models phase magnitude interactions via a learnable attention mechanism. Our approach augments standard RGB input with Fast Fourier Transform (FFT) magnitude and local binary pattern (LBP) representations to expose subtle synthesis artifacts that remain indistinguishable under spatial analysis alone. Crucially, we introduce an input level phase aware attention module that uses phase discontinuities commonly introduced by synthetic generation to guide the model toward frequency patterns that are most indicative of manipulation before backbone feature extraction. The attended multi domain representation is processed by an efficient BNext M backbone, with optional channel spatial attention applied for semantic feature refinement. Extensive experiments on the CIFAKE and DFFD datasets demonstrate that our proposed model Phase4DFD outperforms state of the art spatial and frequency-based detectors while maintaining low computational overhead. Comprehensive ablation studies further confirm that explicit phase modeling provides complementary and non-redundant information beyond magnitude-only frequency representations.

