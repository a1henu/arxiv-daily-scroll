---
layout: default
title: Low-Cost Underwater In-Pipe Centering and Inspection Using a Minimal-Sensing Robot
---

# Low-Cost Underwater In-Pipe Centering and Inspection Using a Minimal-Sensing Robot
**arXiv**：[2602.05265v1](https://arxiv.org/abs/2602.05265) · [PDF](https://arxiv.org/pdf/2602.05265.pdf)  
**作者**：Kalvik Jakkala, Jason O'Kane  

**一句话要点**：提出基于最小传感的水下机器人管道居中与巡检方法，以解决受限环境中的自主导航挑战。

**关键词**：水下机器人, 管道巡检, 最小传感, 声纳处理, 自主导航, 几何控制

## 3 点简述
- 核心问题：水下管道巡检面临几何受限、浑浊环境和定位信号稀缺的挑战。
- 方法要点：使用IMU、压力传感器和两个声纳，通过几何模型和自适应PD控制器实现管道居中。
- 实验或效果：在46厘米直径淹没管道中实验，机器人能稳定居中并完成全管道穿越，适应流动和变形。

## 摘要（原文）

> Autonomous underwater inspection of submerged pipelines is challenging due to confined geometries, turbidity, and the scarcity of reliable localization cues. This paper presents a minimal-sensing strategy that enables a free-swimming underwater robot to center itself and traverse a flooded pipe of known radius using only an IMU, a pressure sensor, and two sonars: a downward-facing single-beam sonar and a rotating 360 degree sonar. We introduce a computationally efficient method for extracting range estimates from single-beam sonar intensity data, enabling reliable wall detection in noisy and reverberant conditions. A closed-form geometric model leverages the two sonar ranges to estimate the pipe center, and an adaptive, confidence-weighted proportional-derivative (PD) controller maintains alignment during traversal. The system requires no Doppler velocity log, external tracking, or complex multi-sensor arrays. Experiments in a submerged 46 cm-diameter pipe using a Blue Robotics BlueROV2 heavy remotely operated vehicle demonstrate stable centering and successful full-pipe traversal despite ambient flow and structural deformations. These results show that reliable in-pipe navigation and inspection can be achieved with a lightweight, computationally efficient sensing and processing architecture, advancing the practicality of autonomous underwater inspection in confined environments.

