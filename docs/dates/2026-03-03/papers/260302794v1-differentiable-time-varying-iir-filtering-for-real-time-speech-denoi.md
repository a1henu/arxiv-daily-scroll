---
layout: default
title: Differentiable Time-Varying IIR Filtering for Real-Time Speech Denoising
---

# Differentiable Time-Varying IIR Filtering for Real-Time Speech Denoising
**arXiv**：[2603.02794v1](https://arxiv.org/abs/2603.02794) · [PDF](https://arxiv.org/pdf/2603.02794.pdf)  
**作者**：Riccardo Rota, Kiril Ratmanski, Jozef Coldenhoff, Milos Cernak  

**一句话要点**：提出可微分时变IIR滤波方法，用于实时语音去噪，结合DSP可解释性与深度学习适应性。

**关键词**：语音增强, 可微分滤波, 实时处理, 可解释AI, IIR滤波器

## 3 点简述
- 核心问题：传统滤波方法难以适应非平稳噪声，而深度学习模型缺乏可解释性。
- 方法要点：使用轻量神经网络实时预测35带IIR滤波器系数，实现动态自适应滤波。
- 实验或效果：在Valentini-Botinhao数据集上验证，相比静态DDSP和全深度学习方案，能有效适应变化噪声。

## 摘要（原文）

> We present TVF (Time-Varying Filtering), a low-latency speech enhancement model with 1 million parameters. Combining the interpretability of Digital Signal Processing (DSP) with the adaptability of deep learning, TVF bridges the gap between traditional filtering and modern neural speech modeling. The model utilizes a lightweight neural network backbone to predict the coefficients of a differentiable 35-band IIR filter cascade in real time, allowing it to adapt dynamically to non-stationary noise. Unlike ``black-box'' deep learning approaches, TVF offers a completely interpretable processing chain, where spectral modifications are explicit and adjustable. We demonstrate the efficacy of this approach on a speech denoising task using the Valentini-Botinhao dataset and compare the results to a static DDSP approach and a fully deep-learning-based solution, showing that TVF achieves effective adaptation to changing noise conditions.

