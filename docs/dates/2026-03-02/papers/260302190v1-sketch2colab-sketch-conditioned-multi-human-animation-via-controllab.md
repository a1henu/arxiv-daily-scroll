---
layout: default
title: Sketch2Colab: Sketch-Conditioned Multi-Human Animation via Controllable Flow Distillation
---

# Sketch2Colab: Sketch-Conditioned Multi-Human Animation via Controllable Flow Distillation
**arXiv**：[2603.02190v1](https://arxiv.org/abs/2603.02190) · [PDF](https://arxiv.org/pdf/2603.02190.pdf)  
**作者**：Divyanshu Daiya, Aniket Bera  

**一句话要点**：提出Sketch2Colab，通过可控流蒸馏将故事板草图转化为可控多人体动画

**关键词**：草图驱动动画, 可控流蒸馏, 多人体运动生成, 物理约束优化, 连续时间马尔可夫链规划

## 3 点简述
- 核心问题：传统扩散模型难以精确满足多实体交互约束，且训练成本高、采样不稳定
- 方法要点：先学习草图驱动扩散先验，再蒸馏为高效整流流学生模型，结合可微分能量和CTMC规划器增强控制
- 实验或效果：在CORE4D和InterHuman数据集上实现最佳约束遵循和感知质量，推理速度显著快于纯扩散基线

## 摘要（原文）

> We present Sketch2Colab, which turns storyboard-style 2D sketches into coherent, object-aware 3D multi-human motion with fine-grained control over agents, joints, timing, and contacts. Conventional diffusion-based motion generators have advanced realism; however, achieving precise adherence to rich interaction constraints typically demands extensive training and/or costly posterior guidance, and performance can degrade under strong multi-entity conditioning. Sketch2Colab instead first learns a sketch-driven diffusion prior and then distills it into an efficient rectified-flow student operating in latent space for fast, stable sampling. Differentiable energies over keyframes, trajectories, and physics-based constraints directly shape the student's transport field, steering samples toward motions that faithfully satisfy the storyboard while remaining physically plausible. To capture coordinated interaction, we augment the continuous flow with a continuous-time Markov chain (CTMC) planner that schedules discrete events such as touches, grasps, and handoffs, modulating the dynamics to produce crisp, well-phased human-object-human collaborations. Experiments on CORE4D and InterHuman show that Sketch2Colab achieves state-of-the-art constraint adherence and perceptual quality while offering significantly faster inference than diffusion-only baselines.

