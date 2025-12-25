---
layout: default
title: AirGS: Real-Time 4D Gaussian Streaming for Free-Viewpoint Video Experiences
---

# AirGS: Real-Time 4D Gaussian Streaming for Free-Viewpoint Video Experiences
**arXiv**：[2512.20943v1](https://arxiv.org/abs/2512.20943) · [PDF](https://arxiv.org/pdf/2512.20943.pdf)  
**作者**：Zhe Wang, Jinghang Li, Yifei Zhu  

**一句话要点**：提出AirGS以优化4D高斯泼溅的流式传输，实现高质量低延迟的自由视点视频体验。

**关键词**：自由视点视频, 4D高斯泼溅, 流式传输优化, 关键帧识别, 带宽效率, 实时渲染

## 3 点简述
- 核心问题：现有4DGS方法在长序列中质量下降，带宽和存储开销大，限制实时应用。
- 方法要点：将高斯视频流转换为多通道2D格式，结合关键帧识别、时间一致性和膨胀损失优化训练与传输。
- 实验或效果：减少PSNR质量偏差超20%，训练加速6倍，每帧传输大小降低近50%。

## 摘要（原文）

> Free-viewpoint video (FVV) enables immersive viewing experiences by allowing users to view scenes from arbitrary perspectives. As a prominent reconstruction technique for FVV generation, 4D Gaussian Splatting (4DGS) models dynamic scenes with time-varying 3D Gaussian ellipsoids and achieves high-quality rendering via fast rasterization. However, existing 4DGS approaches suffer from quality degradation over long sequences and impose substantial bandwidth and storage overhead, limiting their applicability in real-time and wide-scale deployments. Therefore, we present AirGS, a streaming-optimized 4DGS framework that rearchitects the training and delivery pipeline to enable high-quality, low-latency FVV experiences. AirGS converts Gaussian video streams into multi-channel 2D formats and intelligently identifies keyframes to enhance frame reconstruction quality. It further combines temporal coherence with inflation loss to reduce training time and representation size. To support communication-efficient transmission, AirGS models 4DGS delivery as an integer linear programming problem and design a lightweight pruning level selection algorithm to adaptively prune the Gaussian updates to be transmitted, balancing reconstruction quality and bandwidth consumption. Extensive experiments demonstrate that AirGS reduces quality deviation in PSNR by more than 20% when scene changes, maintains frame-level PSNR consistently above 30, accelerates training by 6 times, reduces per-frame transmission size by nearly 50% compared to the SOTA 4DGS approaches.

