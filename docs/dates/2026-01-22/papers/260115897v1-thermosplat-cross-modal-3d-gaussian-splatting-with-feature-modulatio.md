---
layout: default
title: ThermoSplat: Cross-Modal 3D Gaussian Splatting with Feature Modulation and Geometry Decoupling
---

# ThermoSplat: Cross-Modal 3D Gaussian Splatting with Feature Modulation and Geometry Decoupling
**arXiv**：[2601.15897v1](https://arxiv.org/abs/2601.15897) · [PDF](https://arxiv.org/pdf/2601.15897.pdf)  
**作者**：Zhaoqi Su, Shihai Chen, Xinyan Lin, Liqin Huang, Zhipeng Su, Xiaoqiang Lu  

**一句话要点**：提出ThermoSplat框架，通过特征调制与几何解耦实现跨模态3D高斯泼溅，以增强RGB与热红外数据的场景重建

**关键词**：跨模态3D重建, 高斯泼溅, 特征调制, 几何解耦, 热红外感知, 混合渲染

## 3 点简述
- 核心问题：现有3D高斯泼溅方法在多光谱场景中难以有效利用跨模态互补信息，常忽略模态间相关性或共享表示不适应频谱差异
- 方法要点：引入跨模态FiLM调制机制动态调节共享特征，并采用模态自适应几何解耦方案学习独立不透明度偏移，结合混合渲染管道
- 实验或效果：在RGBT-Scenes数据集上验证，ThermoSplat在可见光和热红外频谱均达到先进渲染质量

## 摘要（原文）

> Multi-modal scene reconstruction integrating RGB and thermal infrared data is essential for robust environmental perception across diverse lighting and weather conditions. However, extending 3D Gaussian Splatting (3DGS) to multi-spectral scenarios remains challenging. Current approaches often struggle to fully leverage the complementary information of multi-modal data, typically relying on mechanisms that either tend to neglect cross-modal correlations or leverage shared representations that fail to adaptively handle the complex structural correlations and physical discrepancies between spectrums. To address these limitations, we propose ThermoSplat, a novel framework that enables deep spectral-aware reconstruction through active feature modulation and adaptive geometry decoupling. First, we introduce a Cross-Modal FiLM Modulation mechanism that dynamically conditions shared latent features on thermal structural priors, effectively guiding visible texture synthesis with reliable cross-modal geometric cues. Second, to accommodate modality-specific geometric inconsistencies, we propose a Modality-Adaptive Geometric Decoupling scheme that learns independent opacity offsets and executes an independent rasterization pass for the thermal branch. Additionally, a hybrid rendering pipeline is employed to integrate explicit Spherical Harmonics with implicit neural decoding, ensuring both semantic consistency and high-frequency detail preservation. Extensive experiments on the RGBT-Scenes dataset demonstrate that ThermoSplat achieves state-of-the-art rendering quality across both visible and thermal spectrums.

