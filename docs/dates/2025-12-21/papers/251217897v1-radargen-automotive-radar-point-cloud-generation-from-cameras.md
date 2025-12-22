---
layout: default
title: RadarGen: Automotive Radar Point Cloud Generation from Cameras
---

# RadarGen: Automotive Radar Point Cloud Generation from Cameras
**arXiv**：[2512.17897v1](https://arxiv.org/abs/2512.17897) · [PDF](https://arxiv.org/pdf/2512.17897.pdf)  
**作者**：Tomer Borreda, Fangqiang Ding, Sanja Fidler, Shengyu Huang, Or Litany  

**一句话要点**：提出RadarGen扩散模型，从多视角相机图像生成逼真汽车雷达点云

**关键词**：雷达点云生成, 扩散模型, 多模态仿真, 鸟瞰图表示, 自动驾驶感知

## 3 点简述
- 核心问题：如何从视觉数据合成物理合理的雷达点云，以支持多模态生成式仿真
- 方法要点：采用鸟瞰图表示雷达测量，结合深度、语义和运动线索引导扩散过程
- 实验或效果：在大规模驾驶数据上评估，捕获雷达测量分布并缩小与真实数据训练的感知模型差距

## 摘要（原文）

> We present RadarGen, a diffusion model for synthesizing realistic automotive radar point clouds from multi-view camera imagery. RadarGen adapts efficient image-latent diffusion to the radar domain by representing radar measurements in bird's-eye-view form that encodes spatial structure together with radar cross section (RCS) and Doppler attributes. A lightweight recovery step reconstructs point clouds from the generated maps. To better align generation with the visual scene, RadarGen incorporates BEV-aligned depth, semantic, and motion cues extracted from pretrained foundation models, which guide the stochastic generation process toward physically plausible radar patterns. Conditioning on images makes the approach broadly compatible, in principle, with existing visual datasets and simulation frameworks, offering a scalable direction for multimodal generative simulation. Evaluations on large-scale driving data show that RadarGen captures characteristic radar measurement distributions and reduces the gap to perception models trained on real data, marking a step toward unified generative simulation across sensing modalities.

