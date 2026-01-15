---
layout: default
title: Frequency Error-Guided Under-sampling Optimization for Multi-Contrast MRI Reconstruction
---

# Frequency Error-Guided Under-sampling Optimization for Multi-Contrast MRI Reconstruction
**arXiv**：[2601.09316v1](https://arxiv.org/abs/2601.09316) · [PDF](https://arxiv.org/pdf/2601.09316.pdf)  
**作者**：Xinming Fang, Chaoyan Huang, Juncheng Li, Jun Wang, Jun Shi, Guixu Zhang  

**一句话要点**：提出频率误差引导的欠采样优化框架，以提升多对比MRI重建质量与效率。

**关键词**：多对比MRI重建, 频率误差先验, 欠采样优化, 扩散模型, 深度展开网络, 医学图像处理

## 3 点简述
- 针对多对比MRI重建中参考信息融合浅层、互补信息利用不足及固定欠采样模式的问题。
- 采用条件扩散模型学习频率误差先验，联合优化欠采样模式与重建网络，结合模型驱动与数据驱动方法。
- 在多种成像模态、加速比和采样方案下验证，定量指标与视觉质量均优于现有方法。

## 摘要（原文）

> Magnetic resonance imaging (MRI) plays a vital role in clinical diagnostics, yet it remains hindered by long acquisition times and motion artifacts. Multi-contrast MRI reconstruction has emerged as a promising direction by leveraging complementary information from fully-sampled reference scans. However, existing approaches suffer from three major limitations: (1) superficial reference fusion strategies, such as simple concatenation, (2) insufficient utilization of the complementary information provided by the reference contrast, and (3) fixed under-sampling patterns. We propose an efficient and interpretable frequency error-guided reconstruction framework to tackle these issues. We first employ a conditional diffusion model to learn a Frequency Error Prior (FEP), which is then incorporated into a unified framework for jointly optimizing both the under-sampling pattern and the reconstruction network. The proposed reconstruction model employs a model-driven deep unfolding framework that jointly exploits frequency- and image-domain information. In addition, a spatial alignment module and a reference feature decomposition strategy are incorporated to improve reconstruction quality and bridge model-based optimization with data-driven learning for improved physical interpretability. Comprehensive validation across multiple imaging modalities, acceleration rates (4-30x), and sampling schemes demonstrates consistent superiority over state-of-the-art methods in both quantitative metrics and visual quality. All codes are available at https://github.com/fangxinming/JUF-MRI.

