---
layout: default
title: Optical Inversion and Spectral Unmixing of Spectroscopic Photoacoustic Images with Physics-Informed Neural Networks
---

# Optical Inversion and Spectral Unmixing of Spectroscopic Photoacoustic Images with Physics-Informed Neural Networks
**arXiv**：[2602.16357v1](https://arxiv.org/abs/2602.16357) · [PDF](https://arxiv.org/pdf/2602.16357.pdf)  
**作者**：Sarkis Ter Martirosyan, Xinyue Huang, David Qin, Anthony Yu, Stanislav Emelianov  

**一句话要点**：提出SPOI-AE以解决光谱光声成像中的光学反演和光谱解混问题

**关键词**：光谱光声成像, 光学反演, 光谱解混, 物理信息神经网络, 色团浓度估计

## 3 点简述
- 核心问题：光谱光声成像中非线性与不适定性导致色团浓度估计困难
- 方法要点：使用物理信息神经网络SPOI-AE，无需假设线性关系
- 实验或效果：在体内小鼠淋巴结图像上验证，优于传统算法，提供生物一致参数

## 摘要（原文）

> Accurate estimation of the relative concentrations of chromophores in a spectroscopic photoacoustic (sPA) image can reveal immense structural, functional, and molecular information about physiological processes. However, due to nonlinearities and ill-posedness inherent to sPA imaging, concentration estimation is intractable. The Spectroscopic Photoacoustic Optical Inversion Autoencoder (SPOI-AE) aims to address the sPA optical inversion and spectral unmixing problems without assuming linearity. Herein, SPOI-AE was trained and tested on \textit{in vivo} mouse lymph node sPA images with unknown ground truth chromophore concentrations. SPOI-AE better reconstructs input sPA pixels than conventional algorithms while providing biologically coherent estimates for optical parameters, chromophore concentrations, and the percent oxygen saturation of tissue. SPOI-AE's unmixing accuracy was validated using a simulated mouse lymph node phantom ground truth.

