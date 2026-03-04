---
layout: default
title: TinyIceNet: Low-Power SAR Sea Ice Segmentation for On-Board FPGA Inference
---

# TinyIceNet: Low-Power SAR Sea Ice Segmentation for On-Board FPGA Inference
**arXiv**：[2603.03075v1](https://arxiv.org/abs/2603.03075) · [PDF](https://arxiv.org/pdf/2603.03075.pdf)  
**作者**：Mhd Rashed Al Koutayni, Mohamed Selim, Gerd Reis, Alain Pagani, Didier Stricker  

**一句话要点**：提出TinyIceNet低功耗网络，用于星载FPGA实时海冰分割以解决数据传输限制。

**关键词**：海冰分割, 合成孔径雷达, 低功耗网络, 星载处理, FPGA部署, 硬件算法协同设计

## 3 点简述
- 核心问题：极地海冰快速变化需实时监测，但传统地面处理受限于卫星数据传输带宽和能耗。
- 方法要点：结合SAR感知架构简化和低精度量化，设计紧凑分割网络，适配星载硬件约束。
- 实验或效果：在AI4Arctic数据集上实现75.216% F1分数，FPGA部署能耗比全精度GPU降低2倍。

## 摘要（原文）

> Accurate sea ice mapping is essential for safe maritime navigation in polar regions, where rapidly changing ice conditions require timely and reliable information. While Sentinel-1 Synthetic Aperture Radar (SAR) provides high-resolution, all-weather observations of sea ice, conventional ground-based processing is limited by downlink bandwidth, latency, and energy costs associated with transmitting large volumes of raw data. On-board processing, enabled by dedicated inference chips integrated directly within the satellite payload, offers a transformative alternative by generating actionable sea ice products in orbit. In this context, we present TinyIceNet, a compact semantic segmentation network co-designed for on-board Stage of Development (SOD) mapping from dual-polarized Sentinel-1 SAR imagery under strict hardware and power constraints. Trained on the AI4Arctic dataset, TinyIceNet combines SAR-aware architectural simplifications with low-precision quantization to balance accuracy and efficiency. The model is synthesized using High-Level Synthesis and deployed on a Xilinx Zynq UltraScale+ FPGA platform, demonstrating near-real-time inference with significantly reduced energy consumption. Experimental results show that TinyIceNet achieves 75.216% F1 score on SOD segmentation while reducing energy consumption by 2x compared to full-precision GPU baselines, underscoring the potential of chip-level hardware-algorithm co-design for future spaceborne and edge AI systems.

