---
layout: default
title: DMSORT: An efficient parallel maritime multi-object tracking architecture for unmanned vessel platforms
---

# DMSORT: An efficient parallel maritime multi-object tracking architecture for unmanned vessel platforms
**arXiv**：[2511.04128v1](https://arxiv.org/abs/2511.04128) · [PDF](https://arxiv.org/pdf/2511.04128.pdf)  
**作者**：Shengyu Tang, Zeyuan Lu, Jiazhi Dong, Changdong Yu, Xiaoyu Wang, Yaohui Lyu, Weihao Xia  

**一句话要点**：提出DMSORT并行多目标跟踪方法，以解决海上复杂环境下的跟踪挑战。

**关键词**：多目标跟踪, 海上环境感知, 相机运动补偿, 重识别, 并行架构, Kalman滤波

## 3 点简述
- 核心问题：海上环境相机运动和视觉退化导致多目标跟踪困难。
- 方法要点：采用并行分支，结合检测、重识别和相机运动补偿。
- 实验效果：在新加坡海事数据集上实现SOTA性能，运行速度最快。

## 摘要（原文）

> Accurate perception of the marine environment through robust multi-object
> tracking (MOT) is essential for ensuring safe vessel navigation and effective
> maritime surveillance. However, the complicated maritime environment often
> causes camera motion and subsequent visual degradation, posing significant
> challenges to MOT. To address this challenge, we propose an efficient
> Dual-branch Maritime SORT (DMSORT) method for maritime MOT. The core of the
> framework is a parallel tracker with affine compensation, which incorporates an
> object detection and re-identification (ReID) branch, along with a dedicated
> branch for dynamic camera motion estimation. Specifically, a Reversible
> Columnar Detection Network (RCDN) is integrated into the detection module to
> leverage multi-level visual features for robust object detection. Furthermore,
> a lightweight Transformer-based appearance extractor (Li-TAE) is designed to
> capture global contextual information and generate robust appearance features.
> Another branch decouples platform-induced and target-intrinsic motion by
> constructing a projective transformation, applying platform-motion compensation
> within the Kalman filter, and thereby stabilizing true object trajectories.
> Finally, a clustering-optimized feature fusion module effectively combines
> motion and appearance cues to ensure identity consistency under noise,
> occlusion, and drift. Extensive evaluations on the Singapore Maritime Dataset
> demonstrate that DMSORT achieves state-of-the-art performance. Notably, DMSORT
> attains the fastest runtime among existing ReID-based MOT frameworks while
> maintaining high identity consistency and robustness to jitter and occlusion.
> Code is available at:
> https://github.com/BiscuitsLzy/DMSORT-An-efficient-parallel-maritime-multi-object-tracking-architecture-.

