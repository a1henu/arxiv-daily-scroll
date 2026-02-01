---
layout: default
title: SR$^{2}$-Net: A General Plug-and-Play Model for Spectral Refinement in Hyperspectral Image Super-Resolution
---

# SR$^{2}$-Net: A General Plug-and-Play Model for Spectral Refinement in Hyperspectral Image Super-Resolution
**arXiv**：[2601.21338v1](https://arxiv.org/abs/2601.21338) · [PDF](https://arxiv.org/pdf/2601.21338.pdf)  
**作者**：Ji-Xuan He, Guohang Zhuang, Junge Bo, Tingyi Li, Chen Ling, Yanan Qiao  

**一句话要点**：提出SR²-Net作为通用即插即用模型，以解决高光谱图像超分辨率中的光谱一致性问题。

**关键词**：高光谱图像超分辨率, 光谱一致性, 即插即用模型, 注意力机制, 流形学习, 退化一致性损失

## 3 点简述
- 核心问题：现有方法忽视光谱一致性，导致伪振荡和物理不合理的伪影。
- 方法要点：采用增强后校正流程，结合分层光谱-空间协同注意力和流形一致性校正。
- 实验或效果：在多个基准和骨干网络上验证，提升光谱保真度和重建质量，计算开销可忽略。

## 摘要（原文）

> HSI-SR aims to enhance spatial resolution while preserving spectrally faithful and physically plausible characteristics. Recent methods have achieved great progress by leveraging spatial correlations to enhance spatial resolution. However, these methods often neglect spectral consistency across bands, leading to spurious oscillations and physically implausible artifacts. While spectral consistency can be addressed by designing the network architecture, it results in a loss of generality and flexibility. To address this issue, we propose a lightweight plug-and-play rectifier, physically priors Spectral Rectification Super-Resolution Network (SR$^{2}$-Net), which can be attached to a wide range of HSI-SR models without modifying their architectures. SR$^{2}$-Net follows an enhance-then-rectify pipeline consisting of (i) Hierarchical Spectral-Spatial Synergy Attention (H-S$^{3}$A) to reinforce cross-band interactions and (ii) Manifold Consistency Rectification (MCR) to constrain the reconstructed spectra to a compact, physically plausible spectral manifold. In addition, we introduce a degradation-consistency loss to enforce data fidelity by encouraging the degraded SR output to match the observed low resolution input. Extensive experiments on multiple benchmarks and diverse backbones demonstrate consistent improvements in spectral fidelity and overall reconstruction quality with negligible computational overhead. Our code will be released upon publication.

