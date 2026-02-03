---
layout: default
title: FastPhysGS: Accelerating Physics-based Dynamic 3DGS Simulation via Interior Completion and Adaptive Optimization
---

# FastPhysGS: Accelerating Physics-based Dynamic 3DGS Simulation via Interior Completion and Adaptive Optimization
**arXiv**：[2602.01723v1](https://arxiv.org/abs/2602.01723) · [PDF](https://arxiv.org/pdf/2602.01723.pdf)  
**作者**：Yikun Ma, Yiqing Li, Jingwen Ye, Zhongkai Wu, Weidong Zhang, Lin Gao, Zhi Jin  

**一句话要点**：提出FastPhysGS框架，通过内部填充和自适应优化加速基于物理的动态3D高斯泼溅模拟

**关键词**：3D高斯泼溅, 物理模拟, 材料点方法, 自适应优化, 视觉语言模型, 蒙特卡洛采样

## 3 点简述
- 核心问题：现有方法依赖手动调参或视频扩散模型蒸馏，导致泛化性和优化效率受限，且忽略3DGS表面结构，产生不稳定物理行为。
- 方法要点：采用实例感知粒子填充和蒙特卡洛重要性采样高效填充内部粒子，结合双向图解耦优化自适应优化视觉语言模型预测的材料参数。
- 实验或效果：在1分钟内使用7GB内存实现高保真物理模拟，优于先前工作，具有广泛潜在应用。

## 摘要（原文）

> Extending 3D Gaussian Splatting (3DGS) to 4D physical simulation remains challenging. Based on the Material Point Method (MPM), existing methods either rely on manual parameter tuning or distill dynamics from video diffusion models, limiting the generalization and optimization efficiency. Recent attempts using LLMs/VLMs suffer from a text/image-to-3D perceptual gap, yielding unstable physics behavior. In addition, they often ignore the surface structure of 3DGS, leading to implausible motion. We propose FastPhysGS, a fast and robust framework for physics-based dynamic 3DGS simulation:(1) Instance-aware Particle Filling (IPF) with Monte Carlo Importance Sampling (MCIS) to efficiently populate interior particles while preserving geometric fidelity; (2) Bidirectional Graph Decoupling Optimization (BGDO), an adaptive strategy that rapidly optimizes material parameters predicted from a VLM. Experiments show FastPhysGS achieves high-fidelity physical simulation in 1 minute using only 7 GB runtime memory, outperforming prior works with broad potential applications.

