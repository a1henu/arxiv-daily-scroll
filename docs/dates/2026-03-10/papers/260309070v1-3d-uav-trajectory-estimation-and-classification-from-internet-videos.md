---
layout: default
title: 3D UAV Trajectory Estimation and Classification from Internet Videos via Language Model
---

# 3D UAV Trajectory Estimation and Classification from Internet Videos via Language Model
**arXiv**：[2603.09070v1](https://arxiv.org/abs/2603.09070) · [PDF](https://arxiv.org/pdf/2603.09070.pdf)  
**作者**：Haoxiang Lei, Daotong Wang, Shenghai Yuan, Jianbo Su  

**一句话要点**：提出基于语言模型从互联网视频估计和分类无人机3D轨迹的无监督框架，用于反无人机系统。

**关键词**：无人机轨迹估计, 跨模态学习, 无监督学习, 语言模型, 物理约束优化, 零样本迁移

## 3 点简述
- 核心问题：无人机3D轨迹估计需大规模标注数据，成本高昂，本文旨在无监督解决。
- 方法要点：通过语言驱动采集视频，跨模态生成轨迹假设，物理约束优化轨迹平滑性。
- 实验或效果：零样本迁移实验显示数据量增加提升性能，接近当前最优方法，适用于实际场景。

## 摘要（原文）

> Reliable 3D trajectory estimation of unmanned aerial vehicles (UAVs) is a fundamental requirement for anti-UAV systems, yet the acquisition of large-scale and accurately annotated trajectory data remains prohibitively expensive. In this work, we present a novel framework that derives UAV 3D trajectories and category information directly from Internet-scale UAV videos, without relying on manual annotations. First, language-driven data acquisition is employed to autonomously discover and collect UAV-related videos, while vision-language reasoning progressively filters task-relevant segments. Second, a training-free cross-modal label generation module is introduced to infer 3D trajectory hypotheses and UAV type cues. Third, a physics-informed refinement process is designed to impose temporal smoothness and kinematic consistency on the estimated trajectories. The resulting video clips and trajectory annotations can be readily utilized for downstream anti-UAV tasks. To assess effectiveness and generalization, we conduct zero-shot transfer experiments on a public, well-annotated 3D UAV benchmark. Results reveal a clear data scaling behavior: as the amount of online video data increases, zero-shot transfer performance on the target dataset improves consistently, without any target-domain training. The proposed method closely approaches the current state-of-the-art, highlighting its robustness and applicability to real-world anti-UAV scenarios. Code and datasets will be released upon acceptance.

