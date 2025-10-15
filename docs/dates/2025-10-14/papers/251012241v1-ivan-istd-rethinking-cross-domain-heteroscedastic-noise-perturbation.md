---
layout: default
title: Ivan-ISTD: Rethinking Cross-domain Heteroscedastic Noise Perturbations in Infrared Small Target Detection
---

# Ivan-ISTD: Rethinking Cross-domain Heteroscedastic Noise Perturbations in Infrared Small Target Detection
**arXiv**：[2510.12241v1](https://arxiv.org/abs/2510.12241) · [PDF](https://arxiv.org/pdf/2510.12241.pdf)  
**作者**：Yuehui Li, Yahao Lu, Haoyuan Wu, Sen Zhang, Liang Lin, Yukai Shi  

**一句话要点**：提出Ivan-ISTD框架以解决红外小目标检测中的跨域偏移和异方差噪声扰动问题

**关键词**：红外小目标检测, 跨域学习, 小波变换, 噪声不变性学习, 动态数据集

## 3 点简述
- 核心问题：红外小目标检测面临跨域分布偏移和异方差噪声扰动双重挑战
- 方法要点：采用小波引导的跨域合成和真实噪声不变性学习，构建动态噪声库
- 实验或效果：在动态ISTD基准上优于现有方法，展现跨域场景下的强鲁棒性

## 摘要（原文）

> In the multimedia domain, Infrared Small Target Detection (ISTD) plays a
> important role in drone-based multi-modality sensing. To address the dual
> challenges of cross-domain shift and heteroscedastic noise perturbations in
> ISTD, we propose a doubly wavelet-guided Invariance learning
> framework(Ivan-ISTD). In the first stage, we generate training samples aligned
> with the target domain using Wavelet-guided Cross-domain Synthesis. This
> wavelet-guided alignment machine accurately separates the target background
> through multi-frequency wavelet filtering. In the second stage, we introduce
> Real-domain Noise Invariance Learning, which extracts real noise
> characteristics from the target domain to build a dynamic noise library. The
> model learns noise invariance through self-supervised loss, thereby overcoming
> the limitations of distribution bias in traditional artificial noise modeling.
> Finally, we create the Dynamic-ISTD Benchmark, a cross-domain dynamic
> degradation dataset that simulates the distribution shifts encountered in
> real-world applications. Additionally, we validate the versatility of our
> method using other real-world datasets. Experimental results demonstrate that
> our approach outperforms existing state-of-the-art methods in terms of many
> quantitative metrics. In particular, Ivan-ISTD demonstrates excellent
> robustness in cross-domain scenarios. The code for this work can be found at:
> https://github.com/nanjin1/Ivan-ISTD.

