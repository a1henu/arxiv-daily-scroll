---
layout: default
title: InFlux: A Benchmark for Self-Calibration of Dynamic Intrinsics of Video Cameras
---

# InFlux: A Benchmark for Self-Calibration of Dynamic Intrinsics of Video Cameras
**arXiv**：[2510.23589v1](https://arxiv.org/abs/2510.23589) · [PDF](https://arxiv.org/pdf/2510.23589.pdf)  
**作者**：Erich Liang, Roma Bhattacharjee, Sreemanti Dey, Rafael Moschopoulos, Caitlin Wang, Michel Liao, Grace Tan, Andrew Wang, Karhan Kayan, Stamatis Alexandropoulos, Jia Deng  

**一句话要点**：提出InFlux基准以解决动态相机内参自校准的评估问题

**关键词**：相机内参自校准, 动态内参基准, 视频3D理解, Kalibr工具扩展, 逐帧标注

## 3 点简述
- 核心问题：现有3D算法假设相机内参恒定，但真实视频中内参常变，缺乏动态内参基准。
- 方法要点：构建InFlux基准，提供逐帧真实内参标注，扩展Kalibr工具提升精度。
- 实验或效果：评估基线方法，发现多数在动态内参视频上预测不准，基准含143K+帧。

## 摘要（原文）

> Accurately tracking camera intrinsics is crucial for achieving 3D
> understanding from 2D video. However, most 3D algorithms assume that camera
> intrinsics stay constant throughout a video, which is often not true for many
> real-world in-the-wild videos. A major obstacle in this field is a lack of
> dynamic camera intrinsics benchmarks--existing benchmarks typically offer
> limited diversity in scene content and intrinsics variation, and none provide
> per-frame intrinsic changes for consecutive video frames. In this paper, we
> present Intrinsics in Flux (InFlux), a real-world benchmark that provides
> per-frame ground truth intrinsics annotations for videos with dynamic
> intrinsics. Compared to prior benchmarks, InFlux captures a wider range of
> intrinsic variations and scene diversity, featuring 143K+ annotated frames from
> 386 high-resolution indoor and outdoor videos with dynamic camera intrinsics.
> To ensure accurate per-frame intrinsics, we build a comprehensive lookup table
> of calibration experiments and extend the Kalibr toolbox to improve its
> accuracy and robustness. Using our benchmark, we evaluate existing baseline
> methods for predicting camera intrinsics and find that most struggle to achieve
> accurate predictions on videos with dynamic intrinsics. For the dataset, code,
> videos, and submission, please visit https://influx.cs.princeton.edu/.

