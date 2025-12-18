---
layout: default
title: SLCFormer: Spectral-Local Context Transformer with Physics-Grounded Flare Synthesis for Nighttime Flare Removal
---

# SLCFormer: Spectral-Local Context Transformer with Physics-Grounded Flare Synthesis for Nighttime Flare Removal
**arXiv**：[2512.15221v1](https://arxiv.org/abs/2512.15221) · [PDF](https://arxiv.org/pdf/2512.15221.pdf)  
**作者**：Xiyu Zhu, Wei Wang, Xin Yuan, Xiao Wang  

**一句话要点**：提出SLCFormer光谱-局部上下文Transformer，结合物理基础光晕合成以解决夜间镜头光晕去除问题。

**关键词**：镜头光晕去除, Transformer架构, 频域分析, 物理合成, 夜间图像增强, 散射光晕建模

## 3 点简述
- 核心问题：现有方法难以有效处理非均匀散射光晕，影响复杂真实场景应用。
- 方法要点：集成频域全局上下文建模和空间域局部结构增强模块，并引入基于ZernikeVAE的物理真实光晕合成。
- 实验或效果：在Flare7K++数据集上实现最优性能，定量和感知质量均超越现有方法，泛化至真实夜间场景。

## 摘要（原文）

> Lens flare is a common nighttime artifact caused by strong light sources scattering within camera lenses, leading to hazy streaks, halos, and glare that degrade visual quality. However, existing methods usually fail to effectively address nonuniform scattered flares, which severely reduces their applicability to complex real-world scenarios with diverse lighting conditions. To address this issue, we propose SLCFormer, a novel spectral-local context transformer framework for effective nighttime lens flare removal. SLCFormer integrates two key modules: the Frequency Fourier and Excitation Module (FFEM), which captures efficient global contextual representations in the frequency domain to model flare characteristics, and the Directionally-Enhanced Spatial Module (DESM) for local structural enhancement and directional features in the spatial domain for precise flare removal. Furthermore, we introduce a ZernikeVAE-based scatter flare generation pipeline to synthesize physically realistic scatter flares with spatially varying PSFs, bridging optical physics and data-driven training. Extensive experiments on the Flare7K++ dataset demonstrate that our method achieves state-of-the-art performance, outperforming existing approaches in both quantitative metrics and perceptual visual quality, and generalizing robustly to real nighttime scenes with complex flare artifacts.

