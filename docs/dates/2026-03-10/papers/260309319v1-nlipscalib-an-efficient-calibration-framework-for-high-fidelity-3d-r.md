---
layout: default
title: NLiPsCalib: An Efficient Calibration Framework for High-Fidelity 3D Reconstruction of Curved Visuotactile Sensors
---

# NLiPsCalib: An Efficient Calibration Framework for High-Fidelity 3D Reconstruction of Curved Visuotactile Sensors
**arXiv**：[2603.09319v1](https://arxiv.org/abs/2603.09319) · [PDF](https://arxiv.org/pdf/2603.09319.pdf)  
**作者**：Xuhao Qin, Feiyu Zhao, Yatao Leng, Runze Hu, Chenxi Xiao  

**一句话要点**：提出NLiPsCalib框架以简化曲面视觉触觉传感器的高保真三维重建校准

**关键词**：视觉触觉传感器, 三维重建, 光度立体法, 传感器校准, 近场光源

## 3 点简述
- 核心问题：曲面视觉触觉传感器因非均匀光照导致重建精度下降，现有校准方法依赖昂贵定制设备。
- 方法要点：集成可控近场光源和近光光度立体法，通过日常物体简单接触实现高效校准。
- 实验或效果：开发NLiPsTac传感器验证，实验显示能简化校准并提升多种曲面形态的重建保真度。

## 摘要（原文）

> Recent advances in visuotactile sensors increasingly employ biomimetic curved surfaces to enhance sensorimotor capabilities. Although such curved visuotactile sensors enable more conformal object contact, their perceptual quality is often degraded by non-uniform illumination, which reduces reconstruction accuracy and typically necessitates calibration. Existing calibration methods commonly rely on customized indenters and specialized devices to collect large-scale photometric data, but these processes are expensive and labor-intensive. To overcome these calibration challenges, we present NLiPsCalib, a physics-consistent and efficient calibration framework for curved visuotactile sensors. NLiPsCalib integrates controllable near-field light sources and leverages Near-Light Photometric Stereo (NLiPs) to estimate contact geometry, simplifying calibration to just a few simple contacts with everyday objects. We further introduce NLiPsTac, a controllable-light-source tactile sensor developed to validate our framework. Experimental results demonstrate that our approach enables high-fidelity 3D reconstruction across diverse curved form factors with a simple calibration procedure. We emphasize that our approach lowers the barrier to developing customized visuotactile sensors of diverse geometries, thereby making visuotactile sensing more accessible to the broader community.

