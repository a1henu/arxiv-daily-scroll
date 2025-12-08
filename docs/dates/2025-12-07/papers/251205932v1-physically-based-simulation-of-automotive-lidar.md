---
layout: default
title: Physically-Based Simulation of Automotive LiDAR
---

# Physically-Based Simulation of Automotive LiDAR
**arXiv**：[2512.05932v1](https://arxiv.org/abs/2512.05932) · [PDF](https://arxiv.org/pdf/2512.05932.pdf)  
**作者**：L. Dudzik, M. Roschani, A. Sielemann, K. Trampert, J. Ziehn, J. Beyerer, C. Neumann  

**一句话要点**：提出基于物理的汽车激光雷达仿真模型，通过实验室测量系统化确定参数。

**关键词**：激光雷达仿真, 基于物理的渲染, 飞行时间测量, 汽车传感器, 近红外域, 参数校准

## 3 点简述
- 核心问题：模拟汽车飞行时间激光雷达，需包含光晕、回波脉冲宽度和环境光等物理效应。
- 方法要点：使用近红外域基于物理的渲染，结合光束转向模式和接收二极管灵敏度建模。
- 实验或效果：针对Valeo Scala Gen. 2和Blickfeld Cube 1系统校准测试，成功提取模型参数。

## 摘要（原文）

> We present an analytic model for simulating automotive time-of-flight (ToF) LiDAR that includes blooming, echo pulse width, and ambient light, along with steps to determine model parameters systematically through optical laboratory measurements. The model uses physically based rendering (PBR) in the near-infrared domain. It assumes single-bounce reflections and retroreflections over rasterized rendered images from shading or ray tracing, including light emitted from the sensor as well as stray light from other, non-correlated sources such as sunlight. Beams from the sensor and sensitivity of the receiving diodes are modeled with flexible beam steering patterns and with non-vanishing diameter.
>   Different (all non-real time) computational approaches can be chosen based on system properties, computing capabilities, and desired output properties.
>   Model parameters include system-specific properties, namely the physical spread of the LiDAR beam, combined with the sensitivity of the receiving diode; the intensity of the emitted light; the conversion between the intensity of reflected light and the echo pulse width; and scenario parameters such as environment lighting, positioning, and surface properties of the target(s) in the relevant infrared domain. System-specific properties of the model are determined from laboratory measurements of the photometric luminance on different target surfaces aligned with a goniometer at 0.01° resolution, which marks the best available resolution for measuring the beam pattern.
>   The approach is calibrated for and tested on two automotive LiDAR systems, the Valeo Scala Gen. 2 and the Blickfeld Cube 1. Both systems differ notably in their properties and available interfaces, but the relevant model parameters could be extracted successfully.

