---
layout: default
title: Enabling Low-Latency Machine learning on Radiation-Hard FPGAs with hls4ml
---

# Enabling Low-Latency Machine learning on Radiation-Hard FPGAs with hls4ml
**arXiv**：[2602.15751v1](https://arxiv.org/abs/2602.15751) · [PDF](https://arxiv.org/pdf/2602.15751.pdf)  
**作者**：Katya Govorkova, Julian Garcia Pardinas, Vladimir Loncar, Victoria Nguyen, Sebastian Schmitt, Marco Pizzichemi, Loris Martinazzoli, Eluned Anne Smith  

**一句话要点**：提出hls4ml新后端以在抗辐射FPGA上实现低延迟机器学习，应用于高能物理实验

**关键词**：抗辐射FPGA, 低延迟机器学习, 硬件感知量化, 高能物理实验, hls4ml扩展, 自编码器压缩

## 3 点简述
- 核心问题：高能物理社区标准工具hls4ml缺乏对抗辐射FPGA的支持，阻碍探测器上机器学习应用。
- 方法要点：开发轻量级自编码器压缩时序数据，并引入硬件感知量化策略，将模型权重降至10位。
- 实验或效果：在Microchip PolarFire FPGA上合成自编码器，实现25纳秒延迟，资源占用低，可置于FPGA保护逻辑内。

## 摘要（原文）

> This paper presents the first demonstration of a viable, ultra-fast, radiation-hard machine learning (ML) application on FPGAs, which could be used in future high-energy physics experiments. We present a three-fold contribution, with the PicoCal calorimeter, planned for the LHCb Upgrade II experiment, used as a test case. First, we develop a lightweight autoencoder to compress a 32-sample timing readout, representative of that of the PicoCal, into a two-dimensional latent space. Second, we introduce a systematic, hardware-aware quantization strategy and show that the model can be reduced to 10-bit weights with minimal performance loss. Third, as a barrier to the adoption of on-detector ML is the lack of support for radiation-hard FPGAs in the High-Energy Physics community's standard ML synthesis tool, hls4ml, we develop a new backend for this library. This new back-end enables the automatic translation of ML models into High-Level Synthesis (HLS) projects for the Microchip PolarFire family of FPGAs, one of the few commercially available and radiation hard FPGAs. We present the synthesis of the autoencoder on a target PolarFire FPGA, which indicates that a latency of 25 ns can be achieved. We show that the resources utilized are low enough that the model can be placed within the inherently protected logic of the FPGA. Our extension to hls4ml is a significant contribution, paving the way for broader adoption of ML on FPGAs in high-radiation environments.

