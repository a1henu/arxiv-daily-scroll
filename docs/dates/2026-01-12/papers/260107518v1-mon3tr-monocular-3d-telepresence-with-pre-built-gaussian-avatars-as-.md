---
layout: default
title: Mon3tr: Monocular 3D Telepresence with Pre-built Gaussian Avatars as Amortization
---

# Mon3tr: Monocular 3D Telepresence with Pre-built Gaussian Avatars as Amortization
**arXiv**：[2601.07518v1](https://arxiv.org/abs/2601.07518) · [PDF](https://arxiv.org/pdf/2601.07518.pdf)  
**作者**：Fangyu Lin, Yingdong Hu, Zhening Liu, Yufan Zhuang, Zehong Lin, Jun Zhang  

**一句话要点**：提出Mon3tr框架，通过单目相机实现实时3D远程呈现，降低硬件与带宽需求。

**关键词**：单目3D远程呈现, 3D高斯泼溅, 参数化人体建模, 实时渲染, 带宽优化, 移动AR/VR

## 3 点简述
- 核心问题：现有远程呈现系统依赖多相机和高带宽，难以在移动设备实时运行。
- 方法要点：采用离线重建与在线推理结合，基于3D高斯泼溅参数化人体模型驱动。
- 实验或效果：PSNR > 28 dB，延迟约80 ms，带宽降低超1000倍，支持60 FPS实时渲染。

## 摘要（原文）

> Immersive telepresence aims to transform human interaction in AR/VR applications by enabling lifelike full-body holographic representations for enhanced remote collaboration. However, existing systems rely on hardware-intensive multi-camera setups and demand high bandwidth for volumetric streaming, limiting their real-time performance on mobile devices. To overcome these challenges, we propose Mon3tr, a novel Monocular 3D telepresence framework that integrates 3D Gaussian splatting (3DGS) based parametric human modeling into telepresence for the first time. Mon3tr adopts an amortized computation strategy, dividing the process into a one-time offline multi-view reconstruction phase to build a user-specific avatar and a monocular online inference phase during live telepresence sessions. A single monocular RGB camera is used to capture body motions and facial expressions in real time to drive the 3DGS-based parametric human model, significantly reducing system complexity and cost. The extracted motion and appearance features are transmitted at < 0.2 Mbps over WebRTC's data channel, allowing robust adaptation to network fluctuations. On the receiver side, e.g., Meta Quest 3, we develop a lightweight 3DGS attribute deformation network to dynamically generate corrective 3DGS attribute adjustments on the pre-built avatar, synthesizing photorealistic motion and appearance at ~ 60 FPS. Extensive experiments demonstrate the state-of-the-art performance of our method, achieving a PSNR of > 28 dB for novel poses, an end-to-end latency of ~ 80 ms, and > 1000x bandwidth reduction compared to point-cloud streaming, while supporting real-time operation from monocular inputs across diverse scenarios. Our demos can be found at https://mon3tr3d.github.io.

