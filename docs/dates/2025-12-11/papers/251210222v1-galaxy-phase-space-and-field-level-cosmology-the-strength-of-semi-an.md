---
layout: default
title: Galaxy Phase-Space and Field-Level Cosmology: The Strength of Semi-Analytic Models
---

# Galaxy Phase-Space and Field-Level Cosmology: The Strength of Semi-Analytic Models
**arXiv**：[2512.10222v1](https://arxiv.org/abs/2512.10222) · [PDF](https://arxiv.org/pdf/2512.10222.pdf)  
**作者**：Natalí S. M. de Santi, Francisco Villaescusa-Navarro, Pablo Araya-Araya, Gabriella De Lucia, Fabio Fontanot, Lucia A. Perez, Manuel Arnés-Curto, Violeta Gonzalez-Perez, Ángel Chandro-Gómez, Rachel S. Somerville, Tiago Castro  

**一句话要点**：提出基于图神经网络与矩神经网络的模型，利用星系相空间数据估计宇宙学参数Ω_m。

**关键词**：星系相空间, 图神经网络, 矩神经网络, 宇宙学参数估计, 半解析模型, 机器学习

## 3 点简述
- 核心问题：如何从星系3D位置和径向速度高效估计宇宙学参数Ω_m。
- 方法要点：结合图神经网络和矩神经网络，训练于半解析模型生成的星系目录。
- 实验或效果：模型在多种模拟中泛化良好，精度约10%，对物理变化鲁棒。

## 摘要（原文）

> Semi-analytic models are a widely used approach to simulate galaxy properties within a cosmological framework, relying on simplified yet physically motivated prescriptions. They have also proven to be an efficient alternative for generating accurate galaxy catalogs, offering a faster and less computationally expensive option compared to full hydrodynamical simulations. In this paper, we demonstrate that using only galaxy $3$D positions and radial velocities, we can train a graph neural network coupled to a moment neural network to obtain a robust machine learning based model capable of estimating the matter density parameters, $Ω_{\rm m}$, with a precision of approximately 10%. The network is trained on ($25 h^{-1}$Mpc)$^3$ volumes of galaxy catalogs from L-Galaxies and can successfully extrapolate its predictions to other semi-analytic models (GAEA, SC-SAM, and Shark) and, more remarkably, to hydrodynamical simulations (Astrid, SIMBA, IllustrisTNG, and SWIFT-EAGLE). Our results show that the network is robust to variations in astrophysical and subgrid physics, cosmological and astrophysical parameters, and the different halo-profile treatments used across simulations. This suggests that the physical relationships encoded in the phase-space of semi-analytic models are largely independent of their specific physical prescriptions, reinforcing their potential as tools for the generation of realistic mock catalogs for cosmological parameter inference.

