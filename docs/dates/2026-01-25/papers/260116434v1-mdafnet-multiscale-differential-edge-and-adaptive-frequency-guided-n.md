---
layout: default
title: MDAFNet: Multiscale Differential Edge and Adaptive Frequency Guided Network for Infrared Small Target Detection
---

# MDAFNet: Multiscale Differential Edge and Adaptive Frequency Guided Network for Infrared Small Target Detection
**arXiv**：[2601.16434v1](https://arxiv.org/abs/2601.16434) · [PDF](https://arxiv.org/pdf/2601.16434.pdf)  
**作者**：Shuying Li, Qiang Ma, San Zhang, Wuwei Wang, Chuang Yang  

**一句话要点**：提出MDAFNet以解决红外小目标检测中边缘信息丢失和频率干扰问题

**关键词**：红外小目标检测, 多尺度边缘增强, 自适应频率处理, 双域特征融合, 深度学习网络

## 3 点简述
- 核心问题：网络层数增加导致目标边缘像素退化，传统卷积难以区分频率分量，低频背景和高频噪声干扰检测
- 方法要点：集成多尺度差分边缘模块补偿边缘信息损失，双域自适应特征增强模块结合频域和空间域处理以增强高频目标并抑制噪声
- 实验或效果：在多个数据集上验证了MDAFNet的优越检测性能

## 摘要（原文）

> Infrared small target detection (IRSTD) plays a crucial role in numerous military and civilian applications. However, existing methods often face the gradual degradation of target edge pixels as the number of network layers increases, and traditional convolution struggles to differentiate between frequency components during feature extraction, leading to low-frequency backgrounds interfering with high-frequency targets and high-frequency noise triggering false detections. To address these limitations, we propose MDAFNet (Multi-scale Differential Edge and Adaptive Frequency Guided Network for Infrared Small Target Detection), which integrates the Multi-Scale Differential Edge (MSDE) module and Dual-Domain Adaptive Feature Enhancement (DAFE) module. The MSDE module, through a multi-scale edge extraction and enhancement mechanism, effectively compensates for the cumulative loss of target edge information during downsampling. The DAFE module combines frequency domain processing mechanisms with simulated frequency decomposition and fusion mechanisms in the spatial domain to effectively improve the network's capability to adaptively enhance high-frequency targets and selectively suppress high-frequency noise. Experimental results on multiple datasets demonstrate the superior detection performance of MDAFNet.

