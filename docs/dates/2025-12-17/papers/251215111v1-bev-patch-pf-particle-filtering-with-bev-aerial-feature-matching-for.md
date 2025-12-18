---
layout: default
title: BEV-Patch-PF: Particle Filtering with BEV-Aerial Feature Matching for Off-Road Geo-Localization
---

# BEV-Patch-PF: Particle Filtering with BEV-Aerial Feature Matching for Off-Road Geo-Localization
**arXiv**：[2512.15111v1](https://arxiv.org/abs/2512.15111) · [PDF](https://arxiv.org/pdf/2512.15111.pdf)  
**作者**：Dongmyeong Lee, Jesse Quattrociocchi, Christian Ellis, Rwik Rana, Amanda Adkins, Adam Uccello, Garrett Warnell, Joydeep Biswas  

**一句话要点**：提出BEV-Patch-PF，通过粒子滤波与BEV-航拍特征匹配实现无GPS越野地理定位。

**关键词**：无GPS地理定位, 粒子滤波, 鸟瞰图特征匹配, 越野机器人导航, 实时系统

## 3 点简述
- 核心问题：在无GPS环境下，实现越野场景的实时、高精度地理定位，需应对密集树冠和阴影干扰。
- 方法要点：从车载RGB和深度图像构建BEV特征图，与航拍特征图进行粒子级匹配，计算对数似然以更新位姿。
- 实验或效果：在两个真实越野数据集上，绝对轨迹误差比检索基线降低7.5倍（已知路线）和7.0倍（未知路线），实时运行于10 Hz。

## 摘要（原文）

> We propose BEV-Patch-PF, a GPS-free sequential geo-localization system that integrates a particle filter with learned bird's-eye-view (BEV) and aerial feature maps. From onboard RGB and depth images, we construct a BEV feature map. For each 3-DoF particle pose hypothesis, we crop the corresponding patch from an aerial feature map computed from a local aerial image queried around the approximate location. BEV-Patch-PF computes a per-particle log-likelihood by matching the BEV feature to the aerial patch feature. On two real-world off-road datasets, our method achieves 7.5x lower absolute trajectory error (ATE) on seen routes and 7.0x lower ATE on unseen routes than a retrieval-based baseline, while maintaining accuracy under dense canopy and shadow. The system runs in real time at 10 Hz on an NVIDIA Tesla T4, enabling practical robot deployment.

