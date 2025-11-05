---
layout: default
title: IllumFlow: Illumination-Adaptive Low-Light Enhancement via Conditional Rectified Flow and Retinex Decomposition
---

# IllumFlow: Illumination-Adaptive Low-Light Enhancement via Conditional Rectified Flow and Retinex Decomposition
**arXiv**：[2511.02411v1](https://arxiv.org/abs/2511.02411) · [PDF](https://arxiv.org/pdf/2511.02411.pdf)  
**作者**：Wenyang Wei, Yang yang, Xixi Jia, Xiangchu Feng, Weiwei Wang, Renzhen Wang  

**一句话要点**：提出IllumFlow框架，结合条件整流流与Retinex分解以增强低光图像

**关键词**：低光图像增强, Retinex分解, 条件整流流, 光照适应, 反射分量去噪

## 3 点简述
- 核心问题：低光图像存在光照变化和噪声，影响视觉质量。
- 方法要点：基于Retinex理论分解图像，使用条件整流流建模光照变化，并去噪反射分量。
- 实验或效果：在低光增强和曝光校正任务中，定量和定性表现优于现有方法。

## 摘要（原文）

> We present IllumFlow, a novel framework that synergizes conditional Rectified
> Flow (CRF) with Retinex theory for low-light image enhancement (LLIE). Our
> model addresses low-light enhancement through separate optimization of
> illumination and reflectance components, effectively handling both lighting
> variations and noise. Specifically, we first decompose an input image into
> reflectance and illumination components following Retinex theory. To model the
> wide dynamic range of illumination variations in low-light images, we propose a
> conditional rectified flow framework that represents illumination changes as a
> continuous flow field. While complex noise primarily resides in the reflectance
> component, we introduce a denoising network, enhanced by flow-derived data
> augmentation, to remove reflectance noise and chromatic aberration while
> preserving color fidelity. IllumFlow enables precise illumination adaptation
> across lighting conditions while naturally supporting customizable brightness
> enhancement. Extensive experiments on low-light enhancement and exposure
> correction demonstrate superior quantitative and qualitative performance over
> existing methods.

