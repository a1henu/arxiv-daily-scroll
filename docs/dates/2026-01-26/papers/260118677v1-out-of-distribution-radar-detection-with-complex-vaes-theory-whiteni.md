---
layout: default
title: Out-of-Distribution Radar Detection with Complex VAEs: Theory, Whitening, and ANMF Fusion
---

# Out-of-Distribution Radar Detection with Complex VAEs: Theory, Whitening, and ANMF Fusion
**arXiv**：[2601.18677v1](https://arxiv.org/abs/2601.18677) · [PDF](https://arxiv.org/pdf/2601.18677.pdf)  
**作者**：Yadang Alexis Rouzoumka, Jean Pinsolle, Eugénie Terreaux, Christèle Morisseau, Jean-Philippe Ovarlez, Chengfang Ren  

**一句话要点**：提出基于复变分自编码器的离群检测方法，用于海杂波中弱信号检测，并通过融合增强鲁棒性。

**关键词**：复变分自编码器, 离群检测, 海杂波信号处理, 自适应检测器, 非高斯干扰, 决策融合

## 3 点简述
- 研究海杂波中非高斯、距离变化干扰下的弱复值信号检测问题。
- 利用仅训练于杂波加噪声的复变分自编码器进行离群检测，支持原始和局部白化配置。
- 实验表明，该方法在匹配虚警率下提高检测概率，融合ANMF后增强鲁棒性和虚警控制。

## 摘要（原文）

> We investigate the detection of weak complex-valued signals immersed in non-Gaussian, range-varying interference, with emphasis on maritime radar scenarios. The proposed methodology exploits a Complex-valued Variational AutoEncoder (CVAE) trained exclusively on clutter-plus-noise to perform Out-Of-Distribution detection. By operating directly on in-phase / quadrature samples, the CVAE preserves phase and Doppler structure and is assessed in two configurations: (i) using unprocessed range profiles and (ii) after local whitening, where per-range covariance estimates are obtained from neighboring profiles. Using extensive simulations together with real sea-clutter data from the CSIR maritime dataset, we benchmark performance against classical and adaptive detectors (MF, NMF, AMF-SCM, ANMF-SCM, ANMF-Tyler). In both configurations, the CVAE yields a higher detection probability Pd at matched false-alarm rate Pfa, with the most notable improvements observed under whitening. We further integrate the CVAE with the ANMF through a weighted log-p fusion rule at the decision level, attaining enhanced robustness in strongly non-Gaussian clutter and enabling empirically calibrated Pfa control under H0. Overall, the results demonstrate that statistical normalization combined with complex-valued generative modeling substantively improves detection in realistic sea-clutter conditions, and that the fused CVAE-ANMF scheme constitutes a competitive alternative to established model-based detectors.

