---
layout: default
title: Affordable Data Collection System for UAVs Taxi Vibration Testing
---

# Affordable Data Collection System for UAVs Taxi Vibration Testing
**arXiv**：[2601.07783v1](https://arxiv.org/abs/2601.07783) · [PDF](https://arxiv.org/pdf/2601.07783.pdf)  
**作者**：Chaoyi Lin Yang, Gabriele Dessena, Oscar E. Bonilla-Manrique  

**一句话要点**：提出低成本多传感器数据采集系统，用于小型固定翼无人机滑行振动测试。

**关键词**：无人机振动测试, 低成本数据采集, MEMS传感器, 功率谱密度估计, 结构振动分析

## 3 点简述
- 商业数据采集系统昂贵复杂，限制小型研究应用。
- 集成OrangePi 3 LTS单板计算机与LSM6DS3TR-C MEMS传感器，基于Python主从架构。
- 通过滑行振动测试验证系统可靠性，硬件成本低于600欧元。

## 摘要（原文）

> Structural vibration testing plays a key role in aerospace engineering for evaluating dynamic behaviour, ensuring reliability and verifying structural integrity. These tests rely on accurate and robust data acquisition systems (DAQ) to capture high-quality acceleration data. However, commercial DAQs that provide the required performance and features are often expensive and complex, limiting their accessibility for small-scale research and experimental applications. This work presents the design and experimental validation of an affordable and in-house-developed acceleration DAQ, tested on a small fixed-wing UAV through several Taxi Vibration Test (TVT) runs and ambient vibration measurements. The proposed system integrates several OrangePi 3 LTS single-board computers with multiple LSM6DS3TR-C MEMS inertial measurement units operating simultaneously via an Inter-Integrated Circuit (I2C) communication interface, managed under a Python-based master/slave architecture. Data is acquired at a stable sampling rate of approximately 208 Hz and post-processed using Welch's method to estimate their Power Spectral Density (PSD). Results confirm the system ability to provide consistent multi-sensor acceleration data and repeatable PSD profiles under the same test conditions; thus, demonstrating its reliability. With a total hardware cost below 600 EUR (approximately 690 USD), the developed DAQ offers a compact, scalable and cost-effective alternative for aerospace vibration analysis and structural testing.

