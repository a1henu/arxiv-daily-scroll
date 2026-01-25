---
layout: default
title: CamPilot: Improving Camera Control in Video Diffusion Model with Efficient Camera Reward Feedback
---

# CamPilot: Improving Camera Control in Video Diffusion Model with Efficient Camera Reward Feedback
**arXiv**：[2601.16214v1](https://arxiv.org/abs/2601.16214) · [PDF](https://arxiv.org/pdf/2601.16214.pdf)  
**作者**：Wenhang Ge, Guibao Shen, Jiawei Feng, Luozhou Wang, Hao Lu, Xingye Tian, Xin Tao, Ying-Cong Chen  

**一句话要点**：提出CamPilot，通过高效相机奖励反馈改进视频扩散模型中的相机控制

**关键词**：视频扩散模型, 相机控制, 奖励反馈学习, 3D解码器, 几何扭曲, 像素一致性

## 3 点简述
- 核心问题：现有相机控制视频扩散模型对齐能力有限，且Reward Feedback Learning面临奖励模型不足、计算开销大和3D信息忽略的挑战。
- 方法要点：引入相机感知3D解码器，将视频潜变量和相机姿态解码为3D高斯表示，通过渲染视图与真实视图的像素一致性优化奖励。
- 实验或效果：在RealEstate10K和WorldScore基准上验证了方法的有效性，提升了相机可控性。

## 摘要（原文）

> Recent advances in camera-controlled video diffusion models have significantly improved video-camera alignment. However, the camera controllability still remains limited. In this work, we build upon Reward Feedback Learning and aim to further improve camera controllability. However, directly borrowing existing ReFL approaches faces several challenges. First, current reward models lack the capacity to assess video-camera alignment. Second, decoding latent into RGB videos for reward computation introduces substantial computational overhead. Third, 3D geometric information is typically neglected during video decoding. To address these limitations, we introduce an efficient camera-aware 3D decoder that decodes video latent into 3D representations for reward quantization. Specifically, video latent along with the camera pose are decoded into 3D Gaussians. In this process, the camera pose not only acts as input, but also serves as a projection parameter. Misalignment between the video latent and camera pose will cause geometric distortions in the 3D structure, resulting in blurry renderings. Based on this property, we explicitly optimize pixel-level consistency between the rendered novel views and ground-truth ones as reward. To accommodate the stochastic nature, we further introduce a visibility term that selectively supervises only deterministic regions derived via geometric warping. Extensive experiments conducted on RealEstate10K and WorldScore benchmarks demonstrate the effectiveness of our proposed method. Project page: \href{https://a-bigbao.github.io/CamPilot/}{CamPilot Page}.

