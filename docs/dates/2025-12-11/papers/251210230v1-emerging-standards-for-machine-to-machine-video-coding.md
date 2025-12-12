---
layout: default
title: Emerging Standards for Machine-to-Machine Video Coding
---

# Emerging Standards for Machine-to-Machine Video Coding
**arXiv**：[2512.10230v1](https://arxiv.org/abs/2512.10230) · [PDF](https://arxiv.org/pdf/2512.10230.pdf)  
**作者**：Md Eimran Hossain Eimon, Velibor Adzic, Hari Kalva, Borko Furht  

**一句话要点**：提出机器对机器视频编码标准VCM和FCM，以优化带宽、隐私和计算卸载。

**关键词**：机器对机器通信, 视频编码标准, 特征压缩, 隐私保护, 计算卸载, MPEG标准

## 3 点简述
- 核心问题：机器对机器系统依赖人类感知优化的编解码器，导致带宽高、扩展性差和隐私风险。
- 方法要点：MPEG开发VCM用于像素域任务感知编码，FCM压缩神经特征以降低比特率并保护隐私。
- 实验效果：FCM在保持边缘推理精度的同时显著减少比特率；H.265和H.266在机器任务中性能相近，H.264较差。

## 摘要（原文）

> Machines are increasingly becoming the primary consumers of visual data, yet most deployments of machine-to-machine systems still rely on remote inference where pixel-based video is streamed using codecs optimized for human perception. Consequently, this paradigm is bandwidth intensive, scales poorly, and exposes raw images to third parties. Recent efforts in the Moving Picture Experts Group (MPEG) redesigned the pipeline for machine-to-machine communication: Video Coding for Machines (VCM) is designed to apply task-aware coding tools in the pixel domain, and Feature Coding for Machines (FCM) is designed to compress intermediate neural features to reduce bitrate, preserve privacy, and support compute offload. Experiments show that FCM is capable of maintaining accuracy close to edge inference while significantly reducing bitrate. Additional analysis of H.26X codecs used as inner codecs in FCM reveals that H.265/High Efficiency Video Coding (HEVC) and H.266/Versatile Video Coding (VVC) achieve almost identical machine task performance, with an average BD-Rate increase of 1.39% when VVC is replaced with HEVC. In contrast, H.264/Advanced Video Coding (AVC) yields an average BD-Rate increase of 32.28% compared to VVC. However, for the tracking task, the impact of codec choice is minimal, with HEVC outperforming VVC and achieving BD Rate of -1.81% and 8.79% for AVC, indicating that existing hardware for already deployed codecs can support machine-to-machine communication without degrading performance.

