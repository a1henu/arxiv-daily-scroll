---
layout: default
title: Non-invasive Growth Monitoring of Small Freshwater Fish in Home Aquariums via Stereo Vision
---

# Non-invasive Growth Monitoring of Small Freshwater Fish in Home Aquariums via Stereo Vision
**arXiv**：[2603.06421v1](https://arxiv.org/abs/2603.06421) · [PDF](https://arxiv.org/pdf/2603.06421.pdf)  
**作者**：Clemens Seibold, Anna Hilsmann, Peter Eisert  

**一句话要点**：提出折射感知立体视觉方法以非侵入式监测家庭水族箱中小型淡水鱼生长

**关键词**：立体视觉, 折射感知, 非侵入式监测, 鱼体测量, 关键点检测, 3D重建

## 3 点简述
- 核心问题：水族箱环境中小型鱼体测量受折射畸变干扰，传统方法难以精确。
- 方法要点：使用YOLOv11-Pose检测鱼体关键点，结合折射感知极线约束和3D三角化估计长度。
- 实验或效果：在濒危苏拉威西米鱼数据集验证，过滤低质量检测提升长度估计准确性。

## 摘要（原文）

> Monitoring fish growth behavior provides relevant information about fish health in aquaculture and home aquariums. Yet, monitoring fish sizes poses different challenges, as fish are small and subject to strong refractive distortions in aquarium environments. Image-based measurement offers a practical, non-invasive alternative that allows frequent monitoring without disturbing the fish. In this paper, we propose a non-invasive refraction-aware stereo vision method to estimate fish length in aquariums. Our approach uses a YOLOv11-Pose network to detect fish and predict anatomical keypoints on the fish in each stereo image. A refraction-aware epipolar constraint accounting for the air-glass-water interfaces enables robust matching, and unreliable detections are removed using a learned quality score. A subsequent refraction-aware 3D triangulation recovers 3D keypoints, from which fish length is measured. We validate our approach on a new stereo dataset of endangered Sulawesi ricefish captured under aquarium-like conditions and demonstrate that filtering low-quality detections is essential for accurate length estimation. The proposed system offers a simple and practical solution for non-invasive growth monitoring and can be easily applied in home aquariums.

