---
layout: default
title: TimesNet-Gen: Deep Learning-based Site Specific Strong Motion Generation
---

# TimesNet-Gen: Deep Learning-based Site Specific Strong Motion Generation
**arXiv**：[2512.04694v1](https://arxiv.org/abs/2512.04694) · [PDF](https://arxiv.org/pdf/2512.04694.pdf)  
**作者**：Baris Yilmaz, Bevan Deniz Cilgin, Erdem Akagündüz, Salih Tileylioglu  

**一句话要点**：提出TimesNet-Gen以解决基于时域加速度记录生成站点特定强震动的需求

**关键词**：强震动生成, 站点特定建模, 时域生成器, 地震风险评估, 深度学习应用

## 3 点简述
- 核心问题：地震风险评估需准确站点特定评估，需模型捕捉局部场地条件对震动特征的影响
- 方法要点：引入时域条件生成器TimesNet-Gen，使用站点特定潜在瓶颈从记录中学习场地控制特征
- 实验或效果：通过比较HVSR曲线和f0分布评估生成效果，在站点对齐方面表现优于基于频谱图的VAE基线

## 摘要（原文）

> Effective earthquake risk reduction relies on accurate site-specific evaluations. This requires models that can represent the influence of local site conditions on ground motion characteristics. In this context, data driven approaches that learn site controlled signatures from recorded ground motions offer a promising direction. We address strong ground motion generation from time-domain accelerometer records and introduce the TimesNet-Gen, a time-domain conditional generator. The approach uses a station specific latent bottleneck. We evaluate generation by comparing HVSR curves and fundamental site-frequency $f_0$ distributions between real and generated records per station, and summarize station specificity with a score based on the $f_0$ distribution confusion matrices. TimesNet-Gen achieves strong station-wise alignment and compares favorably with a spectrogram-based conditional VAE baseline for site-specific strong motion synthesis. Our codes are available via https://github.com/brsylmz23/TimesNet-Gen.

