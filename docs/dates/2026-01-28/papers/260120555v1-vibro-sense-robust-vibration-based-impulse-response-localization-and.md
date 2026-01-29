---
layout: default
title: Vibro-Sense: Robust Vibration-based Impulse Response Localization and Trajectory Tracking for Robotic Hands
---

# Vibro-Sense: Robust Vibration-based Impulse Response Localization and Trajectory Tracking for Robotic Hands
**arXiv**：[2601.20555v1](https://arxiv.org/abs/2601.20555) · [PDF](https://arxiv.org/pdf/2601.20555.pdf)  
**作者**：Wadhah Zai El Amri, Nicolás Navarro-Guerrero  

**一句话要点**：提出基于振动感知的机器人手触觉定位与轨迹跟踪方法，以低成本实现高精度接触感知。

**关键词**：振动感知, 触觉定位, 轨迹跟踪, 机器人手, 低成本传感器, 音频频谱变换器

## 3 点简述
- 核心问题：传统触觉皮肤成本高、集成复杂，限制了机器人触觉感知的普及。
- 方法要点：使用七个低成本压电麦克风采集振动信号，结合音频频谱变换器解码接触动态。
- 实验或效果：静态定位误差低于5毫米，材料特性影响显著，系统对机器人自身运动具有鲁棒性。

## 摘要（原文）

> Rich contact perception is crucial for robotic manipulation, yet traditional tactile skins remain expensive and complex to integrate. This paper presents a scalable alternative: high-accuracy whole-body touch localization via vibro-acoustic sensing. By equipping a robotic hand with seven low-cost piezoelectric microphones and leveraging an Audio Spectrogram Transformer, we decode the vibrational signatures generated during physical interaction. Extensive evaluation across stationary and dynamic tasks reveals a localization error of under 5 mm in static conditions. Furthermore, our analysis highlights the distinct influence of material properties: stiff materials (e.g., metal) excel in impulse response localization due to sharp, high-bandwidth responses, whereas textured materials (e.g., wood) provide superior friction-based features for trajectory tracking. The system demonstrates robustness to the robot's own motion, maintaining effective tracking even during active operation. Our primary contribution is demonstrating that complex physical contact dynamics can be effectively decoded from simple vibrational signals, offering a viable pathway to widespread, affordable contact perception in robotics. To accelerate research, we provide our full datasets, models, and experimental setups as open-source resources.

