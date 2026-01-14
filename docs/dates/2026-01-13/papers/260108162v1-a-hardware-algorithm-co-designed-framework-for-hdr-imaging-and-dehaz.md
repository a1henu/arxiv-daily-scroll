---
layout: default
title: A Hardware-Algorithm Co-Designed Framework for HDR Imaging and Dehazing in Extreme Rocket Launch Environments
---

# A Hardware-Algorithm Co-Designed Framework for HDR Imaging and Dehazing in Extreme Rocket Launch Environments
**arXiv**：[2601.08162v1](https://arxiv.org/abs/2601.08162) · [PDF](https://arxiv.org/pdf/2601.08162.pdf)  
**作者**：Jing Tao, Banglei Guan, Pengju Sun, Taihang Lei, Yang Shang, Qifeng Yu  

**一句话要点**：提出硬件算法协同设计框架，以解决火箭发射极端环境下的HDR成像与去雾问题。

**关键词**：硬件算法协同设计, HDR成像, 去雾算法, 火箭发射环境, SVE传感器, 物理感知计算

## 3 点简述
- 核心问题：火箭发射时极端成像条件（如浓雾和超120 dB亮度变化）导致关键机械参数测量困难。
- 方法要点：结合定制SVE传感器和物理感知去雾算法，单次拍摄获取多曝光数据，动态估计雾密度并优化光照。
- 实验或效果：在真实发射图像和受控实验中验证，能有效恢复羽流和发动机区域的物理准确视觉信息。

## 摘要（原文）

> Quantitative optical measurement of critical mechanical parameters -- such as plume flow fields, shock wave structures, and nozzle oscillations -- during rocket launch faces severe challenges due to extreme imaging conditions. Intense combustion creates dense particulate haze and luminance variations exceeding 120 dB, degrading image data and undermining subsequent photogrammetric and velocimetric analyses. To address these issues, we propose a hardware-algorithm co-design framework that combines a custom Spatially Varying Exposure (SVE) sensor with a physics-aware dehazing algorithm. The SVE sensor acquires multi-exposure data in a single shot, enabling robust haze assessment without relying on idealized atmospheric models. Our approach dynamically estimates haze density, performs region-adaptive illumination optimization, and applies multi-scale entropy-constrained fusion to effectively separate haze from scene radiance. Validated on real launch imagery and controlled experiments, the framework demonstrates superior performance in recovering physically accurate visual information of the plume and engine region. This offers a reliable image basis for extracting key mechanical parameters, including particle velocity, flow instability frequency, and structural vibration, thereby supporting precise quantitative analysis in extreme aerospace environments.

