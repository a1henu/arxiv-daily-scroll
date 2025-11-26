---
layout: default
title: Exo2EgoSyn: Unlocking Foundation Video Generation Models for Exocentric-to-Egocentric Video Synthesis
---

# Exo2EgoSyn: Unlocking Foundation Video Generation Models for Exocentric-to-Egocentric Video Synthesis
**arXiv**：[2511.20186v1](https://arxiv.org/abs/2511.20186) · [PDF](https://arxiv.org/pdf/2511.20186.pdf)  
**作者**：Mohammad Mahdi, Yuqian Fu, Nedko Savov, Jiancheng Pan, Danda Pani Paudel, Luc Van Gool  

**一句话要点**：提出Exo2EgoSyn以解锁基础视频生成模型的外中心到内中心视频合成

**关键词**：跨视角视频合成, 基础视频生成模型, 视图对齐, 多视角条件, 姿态注入, 外中心到内中心转换

## 3 点简述
- 核心问题：基础视频生成模型局限于同视角生成，无法实现跨视角合成。
- 方法要点：通过视图对齐、多视角条件输入和姿态注入模块，适配WAN 2.2模型。
- 实验或效果：在ExoEgo4D数据集上验证，显著提升跨视角合成质量。

## 摘要（原文）

> Foundation video generation models such as WAN 2.2 exhibit strong text- and image-conditioned synthesis abilities but remain constrained to the same-view generation setting. In this work, we introduce Exo2EgoSyn, an adaptation of WAN 2.2 that unlocks Exocentric-to-Egocentric(Exo2Ego) cross-view video synthesis. Our framework consists of three key modules. Ego-Exo View Alignment(EgoExo-Align) enforces latent-space alignment between exocentric and egocentric first-frame representations, reorienting the generative space from the given exo view toward the ego view. Multi-view Exocentric Video Conditioning (MultiExoCon) aggregates multi-view exocentric videos into a unified conditioning signal, extending WAN2.2 beyond its vanilla single-image or text conditioning. Furthermore, Pose-Aware Latent Injection (PoseInj) injects relative exo-to-ego camera pose information into the latent state, guiding geometry-aware synthesis across viewpoints. Together, these modules enable high-fidelity ego view video generation from third-person observations without retraining from scratch. Experiments on ExoEgo4D validate that Exo2EgoSyn significantly improves Ego2Exo synthesis, paving the way for scalable cross-view video generation with foundation models. Source code and models will be released publicly.

