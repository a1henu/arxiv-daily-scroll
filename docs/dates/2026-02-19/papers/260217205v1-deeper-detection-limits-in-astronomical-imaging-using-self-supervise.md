---
layout: default
title: Deeper detection limits in astronomical imaging using self-supervised spatiotemporal denoising
---

# Deeper detection limits in astronomical imaging using self-supervised spatiotemporal denoising
**arXiv**：[2602.17205v1](https://arxiv.org/abs/2602.17205) · [PDF](https://arxiv.org/pdf/2602.17205.pdf)  
**作者**：Yuduo Guo, Hao Zhang, Mingyu Li, Fujiang Yu, Yunjing Wu, Yuhan Hao, Song Huang, Yongming Liang, Xiaojing Lin, Xinyang Li, Jiamin Wu, Zheng Cai, Qionghai Dai  

**一句话要点**：提出自监督时空去噪算法ASTERIS以提升天文成像的探测极限

**关键词**：天文成像去噪, 自监督学习, Transformer模型, 时空信息整合, 探测极限提升

## 3 点简述
- 天文成像探测极限受限于像素和曝光间的相关噪声
- ASTERIS基于Transformer整合多曝光时空信息进行自监督去噪
- 在模拟和真实数据中显著提升探测能力并保持光度准确性

## 摘要（原文）

> The detection limit of astronomical imaging observations is limited by several noise sources. Some of that noise is correlated between neighbouring image pixels and exposures, so in principle could be learned and corrected. We present an astronomical self-supervised transformer-based denoising algorithm (ASTERIS), that integrates spatiotemporal information across multiple exposures. Benchmarking on mock data indicates that ASTERIS improves detection limits by 1.0 magnitude at 90% completeness and purity, while preserving the point spread function and photometric accuracy. Observational validation using data from the James Webb Space Telescope (JWST) and Subaru telescope identifies previously undetectable features, including low-surface-brightness galaxy structures and gravitationally-lensed arcs. Applied to deep JWST images, ASTERIS identifies three times more redshift > 9 galaxy candidates, with rest-frame ultraviolet luminosity 1.0 magnitude fainter, than previous methods.

