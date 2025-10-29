---
layout: default
title: Deeply-Conditioned Image Compression via Self-Generated Priors
---

# Deeply-Conditioned Image Compression via Self-Generated Priors
**arXiv**：[2510.24437v1](https://arxiv.org/abs/2510.24437) · [PDF](https://arxiv.org/pdf/2510.24437.pdf)  
**作者**：Zhineng Zhao, Zhihai He, Zikun Zhou, Siwei Ma, Yaowei Wang  

**一句话要点**：提出基于自生成先验的深度条件图像压缩框架，以解决低码率下几何变形问题

**关键词**：学习图像压缩, 深度条件编码, 自生成先验, 信息解耦, 低码率优化

## 3 点简述
- 核心问题：现有学习图像压缩方法难以建模自然图像中全局结构与局部纹理的复杂相关性，导致低码率下几何变形
- 方法要点：通过自生成先验编码图像结构，并深度调节压缩流程，实现信息流解耦
- 实验或效果：在多个数据集上显著降低BD-rate，视觉分析显示几何变形得到缓解

## 摘要（原文）

> Learned image compression (LIC) has shown great promise for achieving high
> rate-distortion performance. However, current LIC methods are often limited in
> their capability to model the complex correlation structures inherent in
> natural images, particularly the entanglement of invariant global structures
> with transient local textures within a single monolithic representation. This
> limitation precipitates severe geometric deformation at low bitrates. To
> address this, we introduce a framework predicated on functional decomposition,
> which we term Deeply-Conditioned Image Compression via self-generated priors
> (DCIC-sgp). Our central idea is to first encode a potent, self-generated prior
> to encapsulate the image's structural backbone. This prior is subsequently
> utilized not as mere side-information, but to holistically modulate the entire
> compression pipeline. This deep conditioning, most critically of the analysis
> transform, liberates it to dedicate its representational capacity to the
> residual, high-entropy details. This hierarchical, dependency-driven approach
> achieves an effective disentanglement of information streams. Our extensive
> experiments validate this assertion; visual analysis demonstrates that our
> method substantially mitigates the geometric deformation artifacts that plague
> conventional codecs at low bitrates. Quantitatively, our framework establishes
> highly competitive performance, achieving significant BD-rate reductions of
> 14.4%, 15.7%, and 15.1% against the VVC test model VTM-12.1 on the Kodak, CLIC,
> and Tecnick datasets.

