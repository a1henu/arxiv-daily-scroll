---
layout: default
title: 360DVO: Deep Visual Odometry for Monocular 360-Degree Camera
---

# 360DVO: Deep Visual Odometry for Monocular 360-Degree Camera
**arXiv**：[2601.02309v1](https://arxiv.org/abs/2601.02309) · [PDF](https://arxiv.org/pdf/2601.02309.pdf)  
**作者**：Xiaopeng Guo, Yinzhe Xu, Huajian Huang, Sai-Kit Yeung  

**一句话要点**：提出360DVO，首个基于深度学习的单目360度相机视觉里程计框架，以提升在挑战性场景中的鲁棒性。

**关键词**：单目视觉里程计, 360度相机, 深度学习, 失真感知特征提取, 全向束调整, 鲁棒性评估

## 3 点简述
- 核心问题：现有单目全向视觉里程计方法依赖手工特征或光度目标，在剧烈运动和光照变化等挑战性场景中鲁棒性不足。
- 方法要点：引入失真感知球形特征提取器（DAS-Feat）自适应学习抗失真特征，并结合全向可微分束调整（ODBA）模块进行姿态估计。
- 实验或效果：在新构建的真实世界基准和公开合成数据集上，360DVO超越现有最佳基线，鲁棒性提升50%，精度提升37.5%。

## 摘要（原文）

> Monocular omnidirectional visual odometry (OVO) systems leverage 360-degree cameras to overcome field-of-view limitations of perspective VO systems. However, existing methods, reliant on handcrafted features or photometric objectives, often lack robustness in challenging scenarios, such as aggressive motion and varying illumination. To address this, we present 360DVO, the first deep learning-based OVO framework. Our approach introduces a distortion-aware spherical feature extractor (DAS-Feat) that adaptively learns distortion-resistant features from 360-degree images. These sparse feature patches are then used to establish constraints for effective pose estimation within a novel omnidirectional differentiable bundle adjustment (ODBA) module. To facilitate evaluation in realistic settings, we also contribute a new real-world OVO benchmark. Extensive experiments on this benchmark and public synthetic datasets (TartanAir V2 and 360VO) demonstrate that 360DVO surpasses state-of-the-art baselines (including 360VO and OpenVSLAM), improving robustness by 50% and accuracy by 37.5%. Homepage: https://chris1004336379.github.io/360DVO-homepage

