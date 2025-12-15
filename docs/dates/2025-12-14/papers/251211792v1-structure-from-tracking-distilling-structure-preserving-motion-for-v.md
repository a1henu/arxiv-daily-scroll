---
layout: default
title: Structure From Tracking: Distilling Structure-Preserving Motion for Video Generation
---

# Structure From Tracking: Distilling Structure-Preserving Motion for Video Generation
**arXiv**：[2512.11792v1](https://arxiv.org/abs/2512.11792) · [PDF](https://arxiv.org/pdf/2512.11792.pdf)  
**作者**：Yang Fei, George Stoica, Jingyuan Liu, Qifeng Chen, Ranjay Krishna, Xiaojuan Wang, Benlin Liu  

**一句话要点**：提出SAM2VideoX方法，通过蒸馏结构保持运动先验以提升视频生成质量

**关键词**：视频生成, 结构保持运动, 蒸馏训练, 扩散模型, 运动先验

## 3 点简述
- 核心问题：现有视频生成模型难以产生结构保持的逼真运动，尤其在关节和可变形物体上。
- 方法要点：从自回归视频跟踪模型SAM2蒸馏运动先验，结合双向特征融合模块和局部Gram流损失。
- 实验效果：在VBench上提升2.60%，FVD降低21-22%，人类偏好率达71.4%。

## 摘要（原文）

> Reality is a dance between rigid constraints and deformable structures. For video models, that means generating motion that preserves fidelity as well as structure. Despite progress in diffusion models, producing realistic structure-preserving motion remains challenging, especially for articulated and deformable objects such as humans and animals. Scaling training data alone, so far, has failed to resolve physically implausible transitions. Existing approaches rely on conditioning with noisy motion representations, such as optical flow or skeletons extracted using an external imperfect model. To address these challenges, we introduce an algorithm to distill structure-preserving motion priors from an autoregressive video tracking model (SAM2) into a bidirectional video diffusion model (CogVideoX). With our method, we train SAM2VideoX, which contains two innovations: (1) a bidirectional feature fusion module that extracts global structure-preserving motion priors from a recurrent model like SAM2; (2) a Local Gram Flow loss that aligns how local features move together. Experiments on VBench and in human studies show that SAM2VideoX delivers consistent gains (+2.60\% on VBench, 21-22\% lower FVD, and 71.4\% human preference) over prior baselines. Specifically, on VBench, we achieve 95.51\%, surpassing REPA (92.91\%) by 2.60\%, and reduce FVD to 360.57, a 21.20\% and 22.46\% improvement over REPA- and LoRA-finetuning, respectively. The project website can be found at https://sam2videox.github.io/ .

