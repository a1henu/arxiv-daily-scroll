---
layout: default
title: LiveSense: A Real-Time Wi-Fi Sensing Platform for Range-Doppler on COTS Laptop
---

# LiveSense: A Real-Time Wi-Fi Sensing Platform for Range-Doppler on COTS Laptop
**arXiv**：[2603.06545v1](https://arxiv.org/abs/2603.06545) · [PDF](https://arxiv.org/pdf/2603.06545.pdf)  
**作者**：Jessica Sanson, Rahul C. Shah, Maximilian Pinaroc, Cagri Tanriover, Valerio Frascolla  

**一句话要点**：提出LiveSense平台，将商用Wi-Fi网卡转化为厘米级距离-多普勒传感器，同时保持通信能力。

**关键词**：Wi-Fi感知, 距离-多普勒, 实时系统, 商用硬件, 信道状态信息, 微动检测

## 3 点简述
- 核心问题：商用Wi-Fi带宽有限，难以实现高精度距离感知。
- 方法要点：在笔记本电脑上实时提取同步CSI，进行时间相位对齐和自干扰消除。
- 实验或效果：可检测距离、径向速度、微动和手势，首次在商用Wi-Fi上实现准确测距。

## 摘要（原文）

> We present LiveSense - a cross-platform that transforms a commercial off-the-shelf (COTS) Wi-Fi Network Interface Card (NIC) on a laptop into a centimeter-level Range-Doppler sensor while preserving simultaneous communication capability. The laptops are equipped with COTS Intel AX211 (Wi-Fi 6E) or Intel BE201 (Wi-Fi 7) NICs. LiveSense can (i) Extract fully-synchronized channel state information (CSI) at >= 40 Hz, (ii) Perform time-phase alignment and self-interference cancellation on-device, and (iii) Provide a real-time stream of range, Doppler, subcarrier magnitude/phase and annotated video frames to a Python/Qt Graphical User Interface (GUI). The demo will showcase the ability to detect (i) Distance and radial velocity of attendees within a few meters of the device, (ii) Micro-motion (respiration), and (iii) Hand-gesture ranging. To the best of our knowledge, this is the first-ever demo to obtain accurate range information of targets from commercial Wi-Fi, despite the limited 160 MHz bandwidth.

