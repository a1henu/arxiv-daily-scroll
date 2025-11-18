---
layout: default
title: SpectralAdapt: Semi-Supervised Domain Adaptation with Spectral Priors for Human-Centered Hyperspectral Image Reconstruction
---

# SpectralAdapt: Semi-Supervised Domain Adaptation with Spectral Priors for Human-Centered Hyperspectral Image Reconstruction
**arXiv**：[2511.13020v1](https://arxiv.org/abs/2511.13020) · [PDF](https://arxiv.org/pdf/2511.13020.pdf)  
**作者**：Yufei Wen, Yuting Zhang, Jingdan Kang, Hao Ren, Weibin Cheng, Jintai Chen, Kaishun Wu  

**一句话要点**：提出SpectralAdapt框架以解决人中心高光谱图像重建中的领域适应问题

**关键词**：高光谱图像重建, 半监督领域适应, 光谱先验, 医疗成像, 跨域泛化

## 3 点简述
- 核心问题：人中心高光谱数据稀缺，导致医疗应用受限。
- 方法要点：引入光谱密度掩码和端元表示对齐，提升半监督领域适应。
- 实验或效果：在基准数据集上提高光谱保真度和跨域泛化能力。

## 摘要（原文）

> Hyperspectral imaging (HSI) holds great potential for healthcare due to its rich spectral information. However, acquiring HSI data remains costly and technically demanding. Hyperspectral image reconstruction offers a practical solution by recovering HSI data from accessible modalities, such as RGB. While general domain datasets are abundant, the scarcity of human HSI data limits progress in medical applications. To tackle this, we propose SpectralAdapt, a semi-supervised domain adaptation (SSDA) framework that bridges the domain gap between general and human-centered HSI datasets. To fully exploit limited labels and abundant unlabeled data, we enhance spectral reasoning by introducing Spectral Density Masking (SDM), which adaptively masks RGB channels based on their spectral complexity, encouraging recovery of informative regions from complementary cues during consistency training. Furthermore, we introduce Spectral Endmember Representation Alignment (SERA), which derives physically interpretable endmembers from valuable labeled pixels and employs them as domain-invariant anchors to guide unlabeled predictions, with momentum updates ensuring adaptability and stability. These components are seamlessly integrated into SpectralAdapt, a spectral prior-guided framework that effectively mitigates domain shift, spectral degradation, and data scarcity in HSI reconstruction. Experiments on benchmark datasets demonstrate consistent improvements in spectral fidelity, cross-domain generalization, and training stability, highlighting the promise of SSDA as an efficient solution for hyperspectral imaging in healthcare.

