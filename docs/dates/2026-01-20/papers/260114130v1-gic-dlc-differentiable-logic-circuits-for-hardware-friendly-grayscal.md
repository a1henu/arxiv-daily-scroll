---
layout: default
title: GIC-DLC: Differentiable Logic Circuits for Hardware-Friendly Grayscale Image Compression
---

# GIC-DLC: Differentiable Logic Circuits for Hardware-Friendly Grayscale Image Compression
**arXiv**：[2601.14130v1](https://arxiv.org/abs/2601.14130) · [PDF](https://arxiv.org/pdf/2601.14130.pdf)  
**作者**：Till Aczel, David F. Jenny, Simon Bührer, Andreas Plesner, Antonio Di Maio, Roger Wattenhofer  

**一句话要点**：提出GIC-DLC，结合神经网络灵活性与布尔运算效率，实现硬件友好的灰度图像压缩。

**关键词**：灰度图像压缩, 可微逻辑电路, 硬件友好编解码, 低功耗设备, 查找表训练, 布尔运算

## 3 点简述
- 核心问题：神经图像编解码器压缩比高但计算开销大，限制在智能手机等低功耗设备部署。
- 方法要点：训练查找表，利用可微逻辑电路，将神经网络灵活性与布尔运算效率结合。
- 实验或效果：在灰度基准数据集上，压缩效率优于传统编解码器，同时显著降低能耗和延迟。

## 摘要（原文）

> Neural image codecs achieve higher compression ratios than traditional hand-crafted methods such as PNG or JPEG-XL, but often incur substantial computational overhead, limiting their deployment on energy-constrained devices such as smartphones, cameras, and drones. We propose Grayscale Image Compression with Differentiable Logic Circuits (GIC-DLC), a hardware-aware codec where we train lookup tables to combine the flexibility of neural networks with the efficiency of Boolean operations. Experiments on grayscale benchmark datasets show that GIC-DLC outperforms traditional codecs in compression efficiency while allowing substantial reductions in energy consumption and latency. These results demonstrate that learned compression can be hardware-friendly, offering a promising direction for low-power image compression on edge devices.

