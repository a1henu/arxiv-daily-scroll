---
layout: default
title: StereoVLA: Enhancing Vision-Language-Action Models with Stereo Vision
---

# StereoVLA: Enhancing Vision-Language-Action Models with Stereo Vision
**arXiv**：[2512.21970v1](https://arxiv.org/abs/2512.21970) · [PDF](https://arxiv.org/pdf/2512.21970.pdf)  
**作者**：Shengliang Deng, Mi Yan, Yixin Zheng, Jiayi Su, Wenhao Zhang, Xiaoguang Zhao, Heming Cui, Zhizheng Zhang, He Wang  

**一句话要点**：提出StereoVLA模型，利用立体视觉增强视觉-语言-动作模型的空间感知能力

**关键词**：立体视觉, 视觉-语言-动作模型, 几何特征提取, 深度估计, 机器人操作, 空间感知

## 3 点简述
- 核心问题：立体视觉在视觉-语言-动作模型中应用不足，缺乏有效利用几何线索的方法
- 方法要点：设计几何-语义特征提取模块，融合立体视图的几何特征和单视图的语义特征
- 实验或效果：在立体设置下多任务中大幅超越基线，对相机姿态变化展现强鲁棒性

## 摘要（原文）

> Stereo cameras closely mimic human binocular vision, providing rich spatial cues critical for precise robotic manipulation. Despite their advantage, the adoption of stereo vision in vision-language-action models (VLAs) remains underexplored. In this work, we present StereoVLA, a VLA model that leverages rich geometric cues from stereo vision. We propose a novel Geometric-Semantic Feature Extraction module that utilizes vision foundation models to extract and fuse two key features: 1) geometric features from subtle stereo-view differences for spatial perception; 2) semantic-rich features from the monocular view for instruction following. Additionally, we propose an auxiliary Interaction-Region Depth Estimation task to further enhance spatial perception and accelerate model convergence. Extensive experiments show that our approach outperforms baselines by a large margin in diverse tasks under the stereo setting and demonstrates strong robustness to camera pose variations.

