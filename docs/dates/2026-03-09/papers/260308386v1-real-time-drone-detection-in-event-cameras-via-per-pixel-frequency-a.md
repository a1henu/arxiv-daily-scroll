---
layout: default
title: Real-Time Drone Detection in Event Cameras via Per-Pixel Frequency Analysis
---

# Real-Time Drone Detection in Event Cameras via Per-Pixel Frequency Analysis
**arXiv**：[2603.08386v1](https://arxiv.org/abs/2603.08386) · [PDF](https://arxiv.org/pdf/2603.08386.pdf)  
**作者**：Michael Bezick, Majid Sahin  

**一句话要点**：提出基于非均匀离散傅里叶变换的逐像素频率分析框架，以实时检测事件相机中的无人机。

**关键词**：事件相机, 无人机检测, 非均匀傅里叶变换, 实时定位, 频率分析, 谐波指纹

## 3 点简述
- 核心问题：事件相机数据稀疏异步，传统均匀采样傅里叶变换不适用，难以检测快速移动的无人机。
- 方法要点：使用非均匀离散傅里叶变换进行逐像素时域分析，通过谐波指纹识别无人机旋翼的频率特征。
- 实验或效果：在多种速度和场景下，相比YOLO，准确率提升至90.89% F1分数，延迟降至2.39ms每帧。

## 摘要（原文）

> Detecting fast-moving objects, such as unmanned aerial vehicle (UAV), from event camera data is challenging due to the sparse, asynchronous nature of the input. Traditional Discrete Fourier Transforms (DFT) are effective at identifying periodic signals, such as spinning rotors, but they assume uniformly sampled data, which event cameras do not provide. We propose a novel per-pixel temporal analysis framework using the Non-uniform Discrete Fourier Transform (NDFT), which we call Drone Detection via Harmonic Fingerprinting (DDHF). Our method uses purely analytical techniques that identify the frequency signature of drone rotors, as characterized by frequency combs in their power spectra, enabling a tunable and generalizable algorithm that achieves accurate real-time localization of UAV. We compare against a YOLO detector under equivalent conditions, demonstrating improvement in accuracy and latency across a difficult array of drone speeds, distances, and scenarios. DDHF achieves an average localization F1 score of 90.89% and average latency of 2.39ms per frame, while YOLO achieves an F1 score of 66.74% and requires 12.40ms per frame. Through utilization of purely analytic techniques, DDHF is quickly tuned on small data, easily interpretable, and achieves competitive accuracies and latencies to deep learning alternatives.

