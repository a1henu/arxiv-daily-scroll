---
layout: default
title: A Learning-based Framework for Spatial Impulse Response Compensation in 3D Photoacoustic Computed Tomography
---

# A Learning-based Framework for Spatial Impulse Response Compensation in 3D Photoacoustic Computed Tomography
**arXiv**：[2601.20291v1](https://arxiv.org/abs/2601.20291) · [PDF](https://arxiv.org/pdf/2601.20291.pdf)  
**作者**：Kaiyi Yang, Seonyeong Park, Gangwon Jeong, Hsuan-Kai Huang, Alexander A. Oraevsky, Umberto Villa, Mark A. Anastasio  

**一句话要点**：提出基于学习的空间脉冲响应补偿框架，以提升三维光声计算断层成像的快速重建精度

**关键词**：光声计算断层成像, 空间脉冲响应补偿, 深度学习, 三维成像, 图像重建, 数据域学习

## 3 点简述
- 核心问题：使用忽略空间脉冲响应的解析重建方法会降低图像分辨率，而优化方法计算成本高。
- 方法要点：在数据域学习补偿模型，将含空间脉冲响应的测量数据映射到理想点状换能器数据。
- 实验或效果：虚拟研究验证了分辨率提升和鲁棒性，体内乳腺成像显示能揭示被伪影掩盖的精细结构。

## 摘要（原文）

> Photoacoustic computed tomography (PACT) is a promising imaging modality that combines the advantages of optical contrast with ultrasound detection. Utilizing ultrasound transducers with larger surface areas can improve detection sensitivity. However, when computationally efficient analytic reconstruction methods that neglect the spatial impulse responses (SIRs) of the transducer are employed, the spatial resolution of the reconstructed images will be compromised. Although optimization-based reconstruction methods can explicitly account for SIR effects, their computational cost is generally high, particularly in three-dimensional (3D) applications. To address the need for accurate but rapid 3D PACT image reconstruction, this study presents a framework for establishing a learned SIR compensation method that operates in the data domain. The learned compensation method maps SIR-corrupted PACT measurement data to compensated data that would have been recorded by idealized point-like transducers. Subsequently, the compensated data can be used with a computationally efficient reconstruction method that neglects SIR effects. Two variants of the learned compensation model are investigated that employ a U-Net model and a specifically designed, physics-inspired model, referred to as Deconv-Net. A fast and analytical training data generation procedure is also a component of the presented framework. The framework is rigorously validated in virtual imaging studies, demonstrating resolution improvement and robustness to noise variations, object complexity, and sound speed heterogeneity. When applied to in-vivo breast imaging data, the learned compensation models revealed fine structures that had been obscured by SIR-induced artifacts. To our knowledge, this is the first demonstration of learned SIR compensation in 3D PACT imaging.

