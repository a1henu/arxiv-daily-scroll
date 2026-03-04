---
layout: default
title: Neural Electromagnetic Fields for High-Resolution Material Parameter Reconstruction
---

# Neural Electromagnetic Fields for High-Resolution Material Parameter Reconstruction
**arXiv**：[2603.02582v1](https://arxiv.org/abs/2603.02582) · [PDF](https://arxiv.org/pdf/2603.02582.pdf)  
**作者**：Zhe Chen, Peilin Zheng, Wenshuo Chen, Xiucheng Wang, Yutao Yue, Nan Cheng  

**一句话要点**：提出NEMF框架，通过解耦策略从非侵入数据重建材料参数以构建功能数字孪生

**关键词**：材料参数重建, 数字孪生, 物理反演, 非侵入感知, 解耦学习, 射频信号

## 3 点简述
- 核心问题：现有数字孪生缺乏材料参数，非侵入感知需解决病态物理反演问题
- 方法要点：利用图像几何锚定环境场，结合物理模型解码器输出连续材料参数场
- 实验或效果：在合成数据集上验证，高精度重建材料图，支持高保真物理模拟

## 摘要（原文）

> Creating functional Digital Twins, simulatable 3D replicas of the real world, is a central challenge in computer vision. Current methods like NeRF produce visually rich but functionally incomplete twins. The key barrier is the lack of underlying material properties (e.g., permittivity, conductivity). Acquiring this information for every point in a scene via non-contact, non-invasive sensing is a primary goal, but it demands solving a notoriously ill-posed physical inversion problem. Standard remote signals, like images and radio frequencies (RF), deeply entangle the unknown geometry, ambient field, and target materials. We introduce NEMF, a novel framework for dense, non-invasive physical inversion designed to build functional digital twins. Our key insight is a systematic disentanglement strategy. NEMF leverages high-fidelity geometry from images as a powerful anchor, which first enables the resolution of the ambient field. By constraining both geometry and field using only non-invasive data, the original ill-posed problem transforms into a well-posed, physics-supervised learning task. This transformation unlocks our core inversion module: a decoder. Guided by ambient RF signals and a differentiable layer incorporating physical reflection models, it learns to explicitly output a continuous, spatially-varying field of the scene's underlying material parameters. We validate our framework on high-fidelity synthetic datasets. Experiments show our non-invasive inversion reconstructs these material maps with high accuracy, and the resulting functional twin enables high-fidelity physical simulation. This advance moves beyond passive visual replicas, enabling the creation of truly functional and simulatable models of the physical world.

