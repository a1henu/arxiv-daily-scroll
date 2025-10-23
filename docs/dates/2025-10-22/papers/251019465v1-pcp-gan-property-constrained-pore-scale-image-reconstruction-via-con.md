---
layout: default
title: PCP-GAN: Property-Constrained Pore-scale image reconstruction via conditional Generative Adversarial Networks
---

# PCP-GAN: Property-Constrained Pore-scale image reconstruction via conditional Generative Adversarial Networks
**arXiv**：[2510.19465v1](https://arxiv.org/abs/2510.19465) · [PDF](https://arxiv.org/pdf/2510.19465.pdf)  
**作者**：Ali Sadeghkhani, Brandon Bennett, Masoud Babaei, Arash Rabbani  

**一句话要点**：提出PCP-GAN多条件生成对抗网络，以生成具有精确控制属性的代表性孔隙尺度图像，解决地下表征中的代表性和数据稀缺问题。

**关键词**：生成对抗网络, 孔隙尺度图像重建, 多条件生成, 地下表征, 数字岩石物理, 孔隙网络控制

## 3 点简述
- 核心问题：地下孔隙图像代表性不足，自然异质性导致子图像偏离核心测量值，且物理样本稀缺。
- 方法要点：使用多条件GAN，同时约束孔隙率和深度参数，生成统一模型捕获通用孔隙网络和深度特定地质特征。
- 实验或效果：模型实现高精度孔隙控制（R²=0.95），形态验证保留关键孔隙特征，生成图像代表性强，误差远低于随机提取图像。

## 摘要（原文）

> Obtaining truly representative pore-scale images that match bulk formation
> properties remains a fundamental challenge in subsurface characterization, as
> natural spatial heterogeneity causes extracted sub-images to deviate
> significantly from core-measured values. This challenge is compounded by data
> scarcity, where physical samples are only available at sparse well locations.
> This study presents a multi-conditional Generative Adversarial Network (cGAN)
> framework that generates representative pore-scale images with precisely
> controlled properties, addressing both the representativeness challenge and
> data availability constraints. The framework was trained on thin section
> samples from four depths (1879.50-1943.50 m) of a carbonate formation,
> simultaneously conditioning on porosity values and depth parameters within a
> single unified model. This approach captures both universal pore network
> principles and depth-specific geological characteristics, from grainstone
> fabrics with interparticle-intercrystalline porosity to crystalline textures
> with anhydrite inclusions. The model achieved exceptional porosity control
> (R^2=0.95) across all formations with mean absolute errors of 0.0099-0.0197.
> Morphological validation confirmed preservation of critical pore network
> characteristics including average pore radius, specific surface area, and
> tortuosity, with statistical differences remaining within acceptable geological
> tolerances. Most significantly, generated images demonstrated superior
> representativeness with dual-constraint errors of 1.9-11.3% compared to
> 36.4-578% for randomly extracted real sub-images. This capability provides
> transformative tools for subsurface characterization, particularly valuable for
> carbon storage, geothermal energy, and groundwater management applications
> where knowing the representative morphology of the pore space is critical for
> implementing digital rock physics.

