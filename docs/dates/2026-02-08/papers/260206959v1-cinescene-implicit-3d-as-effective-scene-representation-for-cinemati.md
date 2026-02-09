---
layout: default
title: CineScene: Implicit 3D as Effective Scene Representation for Cinematic Video Generation
---

# CineScene: Implicit 3D as Effective Scene Representation for Cinematic Video Generation
**arXiv**：[2602.06959v1](https://arxiv.org/abs/2602.06959) · [PDF](https://arxiv.org/pdf/2602.06959.pdf)  
**作者**：Kaiyi Huang, Yukun Huang, Yu Li, Jianhong Bai, Xintao Wang, Zinan Lin, Xuefei Ning, Jiwen Yu, Pengfei Wan, Yu Wang, Xihui Liu  

**一句话要点**：提出CineScene框架，利用隐式3D场景表示解决电影视频生成中的场景一致性问题。

**关键词**：电影视频生成, 隐式3D表示, 场景一致性, 相机轨迹控制, 数据集构建, 视觉特征注入

## 3 点简述
- 核心问题：电影视频生成需控制场景-主体构图和相机运动，但实景拍摄成本高，缺乏场景解耦的训练数据。
- 方法要点：通过VGGT编码场景图像，以隐式方式注入3D感知特征到预训练文本到视频模型，支持相机轨迹控制的视频合成。
- 实验或效果：在构建的Unreal Engine 5数据集上验证，实现场景一致的高质量视频生成，处理大相机运动并泛化到多样环境。

## 摘要（原文）

> Cinematic video production requires control over scene-subject composition and camera movement, but live-action shooting remains costly due to the need for constructing physical sets. To address this, we introduce the task of cinematic video generation with decoupled scene context: given multiple images of a static environment, the goal is to synthesize high-quality videos featuring dynamic subject while preserving the underlying scene consistency and following a user-specified camera trajectory. We present CineScene, a framework that leverages implicit 3D-aware scene representation for cinematic video generation. Our key innovation is a novel context conditioning mechanism that injects 3D-aware features in an implicit way: By encoding scene images into visual representations through VGGT, CineScene injects spatial priors into a pretrained text-to-video generation model by additional context concatenation, enabling camera-controlled video synthesis with consistent scenes and dynamic subjects. To further enhance the model's robustness, we introduce a simple yet effective random-shuffling strategy for the input scene images during training. To address the lack of training data, we construct a scene-decoupled dataset with Unreal Engine 5, containing paired videos of scenes with and without dynamic subjects, panoramic images representing the underlying static scene, along with their camera trajectories. Experiments show that CineScene achieves state-of-the-art performance in scene-consistent cinematic video generation, handling large camera movements and demonstrating generalization across diverse environments.

