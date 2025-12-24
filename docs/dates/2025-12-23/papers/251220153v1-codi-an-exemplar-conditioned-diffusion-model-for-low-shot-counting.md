---
layout: default
title: CoDi -- an exemplar-conditioned diffusion model for low-shot counting
---

# CoDi -- an exemplar-conditioned diffusion model for low-shot counting
**arXiv**：[2512.20153v1](https://arxiv.org/abs/2512.20153) · [PDF](https://arxiv.org/pdf/2512.20153.pdf)  
**作者**：Grega Šuštar, Jer Pelhan, Alan Lukežič, Matej Kristan  

**一句话要点**：提出CoDi，一种基于潜在扩散和示例条件化的低样本计数模型，用于生成高质量密度图以定位对象。

**关键词**：低样本计数, 扩散模型, 示例条件化, 密度图生成, 对象定位, 基准测试

## 3 点简述
- 核心问题：低样本对象计数在密集小对象区域中，现有方法在定位或大规模计数上存在局限。
- 方法要点：引入示例条件化模块，调整对象原型到去噪网络中间层，实现准确位置估计。
- 实验或效果：在FSC和MCAC基准上，MAE指标显著优于现有方法，代码已开源。

## 摘要（原文）

> Low-shot object counting addresses estimating the number of previously unobserved objects in an image using only few or no annotated test-time exemplars. A considerable challenge for modern low-shot counters are dense regions with small objects. While total counts in such situations are typically well addressed by density-based counters, their usefulness is limited by poor localization capabilities. This is better addressed by point-detection-based counters, which are based on query-based detectors. However, due to limited number of pre-trained queries, they underperform on images with very large numbers of objects, and resort to ad-hoc techniques like upsampling and tiling. We propose CoDi, the first latent diffusion-based low-shot counter that produces high-quality density maps on which object locations can be determined by non-maxima suppression. Our core contribution is the new exemplar-based conditioning module that extracts and adjusts the object prototypes to the intermediate layers of the denoising network, leading to accurate object location estimation. On FSC benchmark, CoDi outperforms state-of-the-art by 15% MAE, 13% MAE and 10% MAE in the few-shot, one-shot, and reference-less scenarios, respectively, and sets a new state-of-the-art on MCAC benchmark by outperforming the top method by 44% MAE. The code is available at https://github.com/gsustar/CoDi.

