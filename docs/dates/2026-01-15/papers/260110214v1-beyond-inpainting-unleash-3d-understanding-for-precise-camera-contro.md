---
layout: default
title: Beyond Inpainting: Unleash 3D Understanding for Precise Camera-Controlled Video Generation
---

# Beyond Inpainting: Unleash 3D Understanding for Precise Camera-Controlled Video Generation
**arXiv**：[2601.10214v1](https://arxiv.org/abs/2601.10214) · [PDF](https://arxiv.org/pdf/2601.10214.pdf)  
**作者**：Dong-Yu Chen, Yixin Guo, Shuojin Yang, Tai-Jiang Mu, Shi-Min Hu  

**一句话要点**：提出DepthDirector框架，通过深度视频引导实现精确相机控制的视频重渲染

**关键词**：相机控制视频生成, 视频重渲染, 深度引导, 视频扩散模型, 3D理解, 多相机数据集

## 3 点简述
- 核心问题：现有方法依赖3D表示扭曲，易陷入修复陷阱，导致主体不一致和生成质量下降
- 方法要点：设计视图-内容双流条件机制，注入源视频和目标视角的扭曲深度序列，利用预训练视频扩散模型
- 实验或效果：在MultiCam-WarpData数据集上验证，优于现有方法，提升相机可控性和视觉质量

## 摘要（原文）

> Camera control has been extensively studied in conditioned video generation; however, performing precisely altering the camera trajectories while faithfully preserving the video content remains a challenging task. The mainstream approach to achieving precise camera control is warping a 3D representation according to the target trajectory. However, such methods fail to fully leverage the 3D priors of video diffusion models (VDMs) and often fall into the Inpainting Trap, resulting in subject inconsistency and degraded generation quality. To address this problem, we propose DepthDirector, a video re-rendering framework with precise camera controllability. By leveraging the depth video from explicit 3D representation as camera-control guidance, our method can faithfully reproduce the dynamic scene of an input video under novel camera trajectories. Specifically, we design a View-Content Dual-Stream Condition mechanism that injects both the source video and the warped depth sequence rendered under the target viewpoint into the pretrained video generation model. This geometric guidance signal enables VDMs to comprehend camera movements and leverage their 3D understanding capabilities, thereby facilitating precise camera control and consistent content generation. Next, we introduce a lightweight LoRA-based video diffusion adapter to train our framework, fully preserving the knowledge priors of VDMs. Additionally, we construct a large-scale multi-camera synchronized dataset named MultiCam-WarpData using Unreal Engine 5, containing 8K videos across 1K dynamic scenes. Extensive experiments show that DepthDirector outperforms existing methods in both camera controllability and visual quality. Our code and dataset will be publicly available.

