---
layout: default
title: LiftAvatar: Kinematic-Space Completion for Expression-Controlled 3D Gaussian Avatar Animation
---

# LiftAvatar: Kinematic-Space Completion for Expression-Controlled 3D Gaussian Avatar Animation
**arXiv**：[2603.02129v1](https://arxiv.org/abs/2603.02129) · [PDF](https://arxiv.org/pdf/2603.02129.pdf)  
**作者**：Hualiang Wei, Shunran Jia, Jialun Liu, Wenhui Li  

**一句话要点**：提出LiftAvatar以通过运动学空间补全增强单目视频驱动的3D高斯化身动画

**关键词**：3D化身动画, 运动学空间补全, 表达控制, 视频扩散Transformer, 多参考条件, 高斯溅射

## 3 点简述
- 核心问题：单目视频中稀疏运动学线索导致3D高斯化身动画表达受限和重建伪影
- 方法要点：基于多粒度表达控制和多参考条件机制，在运动学空间补全稀疏观测以驱动高质量化身动画
- 实验或效果：作为即插即用增强器，显著提升现有3D化身方法的动画质量和量化指标，尤其在极端未见表达下

## 摘要（原文）

> We present LiftAvatar, a new paradigm that completes sparse monocular observations in kinematic space (e.g., facial expressions and head pose) and uses the completed signals to drive high-fidelity avatar animation. LiftAvatar is a fine-grained, expression-controllable large-scale video diffusion Transformer that synthesizes high-quality, temporally coherent expression sequences conditioned on single or multiple reference images. The key idea is to lift incomplete input data into a richer kinematic representation, thereby strengthening both reconstruction and animation in downstream 3D avatar pipelines. To this end, we introduce (i) a multi-granularity expression control scheme that combines shading maps with expression coefficients for precise and stable driving, and (ii) a multi-reference conditioning mechanism that aggregates complementary cues from multiple frames, enabling strong 3D consistency and controllability. As a plug-and-play enhancer, LiftAvatar directly addresses the limited expressiveness and reconstruction artifacts of 3D Gaussian Splatting-based avatars caused by sparse kinematic cues in everyday monocular videos. By expanding incomplete observations into diverse pose-expression variations, LiftAvatar also enables effective prior distillation from large-scale video generative models into 3D pipelines, leading to substantial gains. Extensive experiments show that LiftAvatar consistently boosts animation quality and quantitative metrics of state-of-the-art 3D avatar methods, especially under extreme, unseen expressions.

