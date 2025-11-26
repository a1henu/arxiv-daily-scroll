---
layout: default
title: Blind Adaptive Local Denoising for CEST Imaging
---

# Blind Adaptive Local Denoising for CEST Imaging
**arXiv**：[2511.20081v1](https://arxiv.org/abs/2511.20081) · [PDF](https://arxiv.org/pdf/2511.20081.pdf)  
**作者**：Chu Chen, Aitor Artola, Yang Liu, Se Weon Park, Raymond H. Chan, Jean-Michel Morel, Kannie W. Y. Chan  

**一句话要点**：提出盲自适应局部去噪方法以解决CEST成像中噪声异方差问题

**关键词**：CEST MRI, 盲去噪, 自适应变换, 局部SVD, 噪声异方差, 分子成像

## 3 点简述
- CEST MRI面临空间变化噪声和异方差性，影响定量对比映射准确性
- 方法利用数据自相似性进行自适应方差稳定变换，并采用局部SVD分解两阶段去噪
- 在体模和活体实验中，去噪指标和下游任务性能优于现有方法

## 摘要（原文）

> Chemical Exchange Saturation Transfer (CEST) MRI enables molecular-level visualization of low-concentration metabolites by leveraging proton exchange dynamics. However, its clinical translation is hindered by inherent challenges: spatially varying noise arising from hardware limitations, and complex imaging protocols introduce heteroscedasticity in CEST data, perturbing the accuracy of quantitative contrast mapping such as amide proton transfer (APT) imaging. Traditional denoising methods are not designed for this complex noise and often alter the underlying information that is critical for biomedical analysis. To overcome these limitations, we propose a new Blind Adaptive Local Denoising (BALD) method. BALD exploits the self-similar nature of CEST data to derive an adaptive variance-stabilizing transform that equalizes the noise distributions across CEST pixels without prior knowledge of noise characteristics. Then, BALD performs two-stage denoising on a linear transformation of data to disentangle molecular signals from noise. A local SVD decomposition is used as a linear transform to prevent spatial and spectral denoising artifacts. We conducted extensive validation experiments on multiple phantoms and \textit{in vivo} CEST scans. In these experiments, BALD consistently outperformed state-of-the-art CEST denoisers in both denoising metrics and downstream tasks such as molecular concentration maps estimation and cancer detection.

