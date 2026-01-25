---
layout: default
title: Masked Modeling for Human Motion Recovery Under Occlusions
---

# Masked Modeling for Human Motion Recovery Under Occlusions
**arXiv**：[2601.16079v1](https://arxiv.org/abs/2601.16079) · [PDF](https://arxiv.org/pdf/2601.16079.pdf)  
**作者**：Zhiyin Qian, Siwei Zhang, Bharat Lal Bhatnagar, Federica Bogo, Siyu Tang  

**一句话要点**：提出MoRo框架，通过掩码建模解决遮挡下的人体运动恢复问题

**关键词**：人体运动恢复, 掩码建模, 遮挡鲁棒性, 多模态先验, 实时推理

## 3 点简述
- 核心问题：单目视频中遮挡导致人体运动重建困难，现有方法在效率与鲁棒性间存在权衡
- 方法要点：采用掩码建模构建端到端生成框架，融合多模态先验以处理遮挡并实现高效推理
- 实验或效果：在EgoBody和RICH数据集上，遮挡下精度与运动真实感显著优于先进方法，推理速度达70 FPS

## 摘要（原文）

> Human motion reconstruction from monocular videos is a fundamental challenge in computer vision, with broad applications in AR/VR, robotics, and digital content creation, but remains challenging under frequent occlusions in real-world settings.Existing regression-based methods are efficient but fragile to missing observations, while optimization- and diffusion-based approaches improve robustness at the cost of slow inference speed and heavy preprocessing steps. To address these limitations, we leverage recent advances in generative masked modeling and present MoRo: Masked Modeling for human motion Recovery under Occlusions. MoRo is an occlusion-robust, end-to-end generative framework that formulates motion reconstruction as a video-conditioned task, and efficiently recover human motion in a consistent global coordinate system from RGB videos. By masked modeling, MoRo naturally handles occlusions while enabling efficient, end-to-end inference. To overcome the scarcity of paired video-motion data, we design a cross-modality learning scheme that learns multi-modal priors from a set of heterogeneous datasets: (i) a trajectory-aware motion prior trained on MoCap datasets, (ii) an image-conditioned pose prior trained on image-pose datasets, capturing diverse per-frame poses, and (iii) a video-conditioned masked transformer that fuses motion and pose priors, finetuned on video-motion datasets to integrate visual cues with motion dynamics for robust inference. Extensive experiments on EgoBody and RICH demonstrate that MoRo substantially outperforms state-of-the-art methods in accuracy and motion realism under occlusions, while performing on-par in non-occluded scenarios. MoRo achieves real-time inference at 70 FPS on a single H200 GPU.

