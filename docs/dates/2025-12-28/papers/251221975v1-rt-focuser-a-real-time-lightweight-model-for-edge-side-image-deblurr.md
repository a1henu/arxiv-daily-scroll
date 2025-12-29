---
layout: default
title: RT-Focuser: A Real-Time Lightweight Model for Edge-side Image Deblurring
---

# RT-Focuser: A Real-Time Lightweight Model for Edge-side Image Deblurring
**arXiv**：[2512.21975v1](https://arxiv.org/abs/2512.21975) · [PDF](https://arxiv.org/pdf/2512.21975.pdf)  
**作者**：Zhuoyu Wu, Wenhui Ou, Qiawei Zheng, Jiayan Yang, Quanjun Wang, Wenqi Fang, Zheng Wang, Yongkui Yang, Heshan Li  

**一句话要点**：提出RT-Focuser轻量级U形网络，用于边缘端实时图像去模糊。

**关键词**：图像去模糊, 轻量级网络, 实时处理, 边缘计算, U形网络, 运动模糊

## 3 点简述
- 核心问题：相机或物体运动导致的运动模糊降低图像质量，影响自动驾驶等实时应用。
- 方法要点：设计轻量去模糊块、多级集成聚合模块和跨源融合块，平衡速度与精度。
- 实验或效果：在单模糊输入训练下，PSNR达30.67 dB，参数5.85M，GPU和移动端运行6ms/帧，超140 FPS。

## 摘要（原文）

> Motion blur caused by camera or object movement severely degrades image quality and poses challenges for real-time applications such as autonomous driving, UAV perception, and medical imaging. In this paper, a lightweight U-shaped network tailored for real-time deblurring is presented and named RT-Focuser. To balance speed and accuracy, we design three key components: Lightweight Deblurring Block (LD) for edge-aware feature extraction, Multi-Level Integrated Aggregation module (MLIA) for encoder integration, and Cross-source Fusion Block (X-Fuse) for progressive decoder refinement. Trained on a single blurred input, RT-Focuser achieves 30.67 dB PSNR with only 5.85M parameters and 15.76 GMACs. It runs 6ms per frame on GPU and mobile, exceeds 140 FPS on both, showing strong potential for deployment on the edge. The official code and usage are available on: https://github.com/ReaganWu/RT-Focuser.

