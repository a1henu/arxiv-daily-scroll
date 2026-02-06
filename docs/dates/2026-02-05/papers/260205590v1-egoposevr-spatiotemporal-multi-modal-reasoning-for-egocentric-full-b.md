---
layout: default
title: EgoPoseVR: Spatiotemporal Multi-Modal Reasoning for Egocentric Full-Body Pose in Virtual Reality
---

# EgoPoseVR: Spatiotemporal Multi-Modal Reasoning for Egocentric Full-Body Pose in Virtual Reality
**arXiv**：[2602.05590v1](https://arxiv.org/abs/2602.05590) · [PDF](https://arxiv.org/pdf/2602.05590.pdf)  
**作者**：Haojie Cheng, Shaun Jing Heng Ong, Shaoyu Cai, Aiden Tat Yang Koh, Fuxi Ouyang, Eng Tat Khoo  

**一句话要点**：提出EgoPoseVR框架，通过多模态融合解决VR中第一人称全身姿态估计的准确性与稳定性问题。

**关键词**：第一人称姿态估计, 虚拟现实, 多模态融合, 时空编码, 运动学优化, 合成数据集

## 3 点简述
- 核心问题：VR头显中第一人称姿态估计存在时间不稳定、下半身不准确和实时性不足的挑战。
- 方法要点：集成头显运动线索与RGB-D观测，通过时空编码器和跨注意力实现多模态融合，并引入运动学优化模块。
- 实验或效果：在合成数据集上超越现有方法，用户研究显示在准确性、稳定性等方面获得更高主观评分。

## 摘要（原文）

> Immersive virtual reality (VR) applications demand accurate, temporally coherent full-body pose tracking. Recent head-mounted camera-based approaches show promise in egocentric pose estimation, but encounter challenges when applied to VR head-mounted displays (HMDs), including temporal instability, inaccurate lower-body estimation, and the lack of real-time performance. To address these limitations, we present EgoPoseVR, an end-to-end framework for accurate egocentric full-body pose estimation in VR that integrates headset motion cues with egocentric RGB-D observations through a dual-modality fusion pipeline. A spatiotemporal encoder extracts frame- and joint-level representations, which are fused via cross-attention to fully exploit complementary motion cues across modalities. A kinematic optimization module then imposes constraints from HMD signals, enhancing the accuracy and stability of pose estimation. To facilitate training and evaluation, we introduce a large-scale synthetic dataset of over 1.8 million temporally aligned HMD and RGB-D frames across diverse VR scenarios. Experimental results show that EgoPoseVR outperforms state-of-the-art egocentric pose estimation models. A user study in real-world scenes further shows that EgoPoseVR achieved significantly higher subjective ratings in accuracy, stability, embodiment, and intention for future use compared to baseline methods. These results show that EgoPoseVR enables robust full-body pose tracking, offering a practical solution for accurate VR embodiment without requiring additional body-worn sensors or room-scale tracking systems.

