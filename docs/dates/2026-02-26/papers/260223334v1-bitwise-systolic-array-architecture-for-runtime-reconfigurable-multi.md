---
layout: default
title: Bitwise Systolic Array Architecture for Runtime-Reconfigurable Multi-precision Quantized Multiplication on Hardware Accelerators
---

# Bitwise Systolic Array Architecture for Runtime-Reconfigurable Multi-precision Quantized Multiplication on Hardware Accelerators
**arXiv**：[2602.23334v1](https://arxiv.org/abs/2602.23334) · [PDF](https://arxiv.org/pdf/2602.23334.pdf)  
**作者**：Yuhao Liu, Salim Ullah, Akash Kumar  

**一句话要点**：提出运行时可重配置多精度比特级脉动阵列，以支持硬件加速器上的混合精度量化神经网络推理。

**关键词**：硬件加速器, 量化神经网络, 混合精度, 脉动阵列, 运行时重配置, FPGA实现

## 3 点简述
- 核心问题：硬件乘法器无法在运行时支持混合精度量化神经网络模型的精度重配置。
- 方法要点：设计多通道比特级脉动阵列，实现运行时多精度乘法运算的可重配置性。
- 实验或效果：在Ultra96 FPGA上实现，推理速度提升1.3185至3.5671倍，支持更高时钟频率（250MHz）。

## 摘要（原文）

> Neural network accelerators have been widely applied to edge devices for complex tasks like object tracking, image recognition, etc. Previous works have explored the quantization technologies in related lightweight accelerator designs to reduce hardware resource consumption. However, low precision leads to high accuracy loss in inference. Therefore, mixed-precision quantization becomes an alternative solution by applying different precision in different layers to trade off resource consumption and accuracy. Because regular designs for multiplication on hardware cannot support the precision reconfiguration for a multi-precision Quantized Neural Network (QNN) model in runtime, we propose a runtime reconfigurable multi-precision multi-channel bitwise systolic array design for QNN accelerators. We have implemented and evaluated our work on the Ultra96 FPGA platform. Results show that our work can achieve 1.3185 to 3.5671 times speedup in inferring mixed-precision models and has less critical path delay, supporting a higher clock frequency (250MHz).

