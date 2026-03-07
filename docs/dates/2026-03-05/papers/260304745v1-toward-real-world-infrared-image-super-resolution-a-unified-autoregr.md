---
layout: default
title: Toward Real-world Infrared Image Super-Resolution: A Unified Autoregressive Framework and Benchmark Dataset
---

# Toward Real-world Infrared Image Super-Resolution: A Unified Autoregressive Framework and Benchmark Dataset
**arXiv**：[2603.04745v1](https://arxiv.org/abs/2603.04745) · [PDF](https://arxiv.org/pdf/2603.04745.pdf)  
**作者**：Yang Zou, Jun Ma, Zhidong Jiao, Xingyuan Li, Zhiying Jiang, Jinyuan Liu  

**一句话要点**：提出Real-IISR框架与FLIR-IISR数据集，以解决真实世界红外图像超分辨率中的耦合退化问题。

**关键词**：红外图像超分辨率, 自回归框架, 热结构引导, 真实世界数据集, 条件自适应码本, 热保真度

## 3 点简述
- 核心问题：真实红外图像受光学与传感耦合退化影响，导致结构锐度和热保真度下降。
- 方法要点：采用热结构引导的自回归框架，通过热结构指导模块和条件自适应码本逐步重建细节。
- 实验或效果：在新建的FLIR-IISR数据集上验证，性能优异，为真实世界红外超分辨率提供统一基准。

## 摘要（原文）

> Infrared image super-resolution (IISR) under real-world conditions is a practically significant yet rarely addressed task. Pioneering works are often trained and evaluated on simulated datasets or neglect the intrinsic differences between infrared and visible imaging. In practice, however, real infrared images are affected by coupled optical and sensing degradations that jointly deteriorate both structural sharpness and thermal fidelity. To address these challenges, we propose Real-IISR, a unified autoregressive framework for real-world IISR that progressively reconstructs fine-grained thermal structures and clear backgrounds in a scale-by-scale manner via thermal-structural guided visual autoregression. Specifically, a Thermal-Structural Guidance module encodes thermal priors to mitigate the mismatch between thermal radiation and structural edges. Since non-uniform degradations typically induce quantization bias, Real-IISR adopts a Condition-Adaptive Codebook that dynamically modulates discrete representations based on degradation-aware thermal priors. Also, a Thermal Order Consistency Loss enforces a monotonic relation between temperature and pixel intensity, ensuring relative brightness order rather than absolute values to maintain physical consistency under spatial misalignment and thermal drift. We build FLIR-IISR, a real-world IISR dataset with paired LR-HR infrared images acquired via automated focus variation and motion-induced blur. Extensive experiments demonstrate the promising performance of Real-IISR, providing a unified foundation for real-world IISR and benchmarking. The dataset and code are available at: https://github.com/JZD151/Real-IISR.

