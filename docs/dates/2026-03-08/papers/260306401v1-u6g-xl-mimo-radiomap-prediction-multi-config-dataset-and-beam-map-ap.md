---
layout: default
title: U6G XL-MIMO Radiomap Prediction: Multi-Config Dataset and Beam Map Approach
---

# U6G XL-MIMO Radiomap Prediction: Multi-Config Dataset and Beam Map Approach
**arXiv**：[2603.06401v1](https://arxiv.org/abs/2603.06401) · [PDF](https://arxiv.org/pdf/2603.06401.pdf)  
**作者**：Xiaojie Li, Yu Han, Zhizheng Lu, Shi Jin, Chao-Kai Wen  

**一句话要点**：提出波束图方法以解决XL-MIMO无线地图预测的数据稀缺与泛化难题

**关键词**：XL-MIMO无线地图预测, 波束图方法, 多配置数据集, 6G通信, 物理信息特征, 泛化能力

## 3 点简述
- 核心问题：现有数据集和方法无法支持6G XL-MIMO大规模定向阵列的无线地图预测，泛化能力差。
- 方法要点：构建首个多配置XL-MIMO数据集，并提出基于物理的波束图特征，解耦阵列辐射与传播学习。
- 实验或效果：波束图集成使未见配置和环境下的平均绝对误差降低达60.0%和50.5%。

## 摘要（原文）

> The upper 6 GHz (U6G) band with XL-MIMO is a key enabler for sixth-generation wireless systems, yet intelligent radiomap prediction for such systems remains challenging. Existing datasets support only small-scale arrays (up to 8x8) with predominantly isotropic antennas, far from the 1024-element directional arrays envisioned for 6G. Moreover, current methods encode array configurations as scalar parameters, forcing neural networks to extrapolate array-specific radiation patterns, which fails when predicting radiomaps for configurations absent from training data. To jointly address data scarcity and generalization limitations, this paper advances XL-MIMO radiomap prediction from three aspects. To overcome data limitations, we construct the first XL-MIMO radiomap dataset containing 78400 radiomaps across 800 urban scenes, five frequency bands (1.8-6.7 GHz), and nine array configurations up to 32x32 uniform planar arrays with directional elements. To enable systematic evaluation, we establish a comprehensive benchmark framework covering practical scenarios from coverage estimation without field measurements to generalization across unseen configurations and environments. To enable generalization to arbitrary beam configurations without retraining, we propose the beam map, a physics-informed spatial feature that analytically computes array-specific coverage patterns. By decoupling deterministic array radiation from data learned multipath propagation, beam maps shift generalization from neural network extrapolation to physics-based computation. Integrating beam maps into existing architectures reduces mean absolute error by up to 60.0% when generalizing to unseen configurations and up to 50.5% when transferring to unseen environments. The complete dataset and code are publicly available at https://lxj321.github.io/MulticonfigRadiomapDataset/.

