---
layout: default
title: FSAG: Enhancing Human-to-Dexterous-Hand Finger-Specific Affordance Grounding via Diffusion Models
---

# FSAG: Enhancing Human-to-Dexterous-Hand Finger-Specific Affordance Grounding via Diffusion Models
**arXiv**：[2601.08246v1](https://arxiv.org/abs/2601.08246) · [PDF](https://arxiv.org/pdf/2601.08246.pdf)  
**作者**：Yifan Han, Pengfei Yi, Junyan Li, Hanqing Wang, Gaojing Zhang, Qi Peng Liu, Wenzhao Lian  

**一句话要点**：提出FSAG框架，利用扩散模型从人类视频提取语义先验，实现数据高效的多指灵巧手抓取合成。

**关键词**：灵巧手抓取合成, 扩散模型, 语义可操作性提取, 运动学重定向, 数据高效学习, 跨硬件泛化

## 3 点简述
- 核心问题：多指灵巧手抓取合成因高维度和硬件多样性，依赖大规模数据集，可扩展性受限。
- 方法要点：从人类视频提取细粒度抓取可操作性，结合深度图像几何，通过运动学感知重定向模块泛化到不同灵巧手。
- 实验或效果：系统在常见物体和工具上生成稳定抓取，泛化到未见物体实例、姿态变化和多种手部模型。

## 摘要（原文）

> Dexterous grasp synthesis remains a central challenge: the high dimensionality and kinematic diversity of multi-fingered hands prevent direct transfer of algorithms developed for parallel-jaw grippers. Existing approaches typically depend on large, hardware-specific grasp datasets collected in simulation or through costly real-world trials, hindering scalability as new dexterous hand designs emerge. To this end, we propose a data-efficient framework, which is designed to bypass robot grasp data collection by exploiting the rich, object-centric semantic priors latent in pretrained generative diffusion models. Temporally aligned and fine-grained grasp affordances are extracted from raw human video demonstrations and fused with 3D scene geometry from depth images to infer semantically grounded contact targets. A kinematics-aware retargeting module then maps these affordance representations to diverse dexterous hands without per-hand retraining. The resulting system produces stable, functionally appropriate multi-contact grasps that remain reliably successful across common objects and tools, while exhibiting strong generalization across previously unseen object instances within a category, pose variations, and multiple hand embodiments. This work (i) introduces a semantic affordance extraction pipeline leveraging vision-language generative priors for dexterous grasping, (ii) demonstrates cross-hand generalization without constructing hardware-specific grasp datasets, and (iii) establishes that a single depth modality suffices for high-performance grasp synthesis when coupled with foundation-model semantics. Our results highlight a path toward scalable, hardware-agnostic dexterous manipulation driven by human demonstrations and pretrained generative models.

