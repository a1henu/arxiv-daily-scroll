---
layout: default
title: Blur2Sharp: Human Novel Pose and View Synthesis with Generative Prior Refinement
---

# Blur2Sharp: Human Novel Pose and View Synthesis with Generative Prior Refinement
**arXiv**：[2512.08215v1](https://arxiv.org/abs/2512.08215) · [PDF](https://arxiv.org/pdf/2512.08215.pdf)  
**作者**：Chia-Hern Lai, I-Hsuan Lo, Yen-Ku Yeh, Thanh-Nguyen Truong, Ching-Chun Huang  

**一句话要点**：提出Blur2Sharp框架，通过生成先验细化从单视图生成几何一致且清晰的新姿态和视角图像。

**关键词**：人类姿态合成, 新视角生成, 神经渲染, 扩散模型, 几何一致性, SMPL先验

## 3 点简述
- 核心问题：现有方法在生成人类新姿态和视角时，常导致几何不一致或模糊输出，尤其在复杂运动和视角下。
- 方法要点：结合Human NeRF和扩散模型，先生成几何一致的多视图渲染，再通过条件扩散模型细化细节，并融合SMPL先验提升质量。
- 实验或效果：在挑战性场景如宽松衣物和遮挡下，Blur2Sharp超越现有技术，生成更清晰、几何一致的新姿态和视角图像。

## 摘要（原文）

> The creation of lifelike human avatars capable of realistic pose variation and viewpoint flexibility remains a fundamental challenge in computer vision and graphics. Current approaches typically yield either geometrically inconsistent multi-view images or sacrifice photorealism, resulting in blurry outputs under diverse viewing angles and complex motions. To address these issues, we propose Blur2Sharp, a novel framework integrating 3D-aware neural rendering and diffusion models to generate sharp, geometrically consistent novel-view images from only a single reference view. Our method employs a dual-conditioning architecture: initially, a Human NeRF model generates geometrically coherent multi-view renderings for target poses, explicitly encoding 3D structural guidance. Subsequently, a diffusion model conditioned on these renderings refines the generated images, preserving fine-grained details and structural fidelity. We further enhance visual quality through hierarchical feature fusion, incorporating texture, normal, and semantic priors extracted from parametric SMPL models to simultaneously improve global coherence and local detail accuracy. Extensive experiments demonstrate that Blur2Sharp consistently surpasses state-of-the-art techniques in both novel pose and view generation tasks, particularly excelling under challenging scenarios involving loose clothing and occlusions.

