---
layout: default
title: Single-View Shape Completion for Robotic Grasping in Clutter
---

# Single-View Shape Completion for Robotic Grasping in Clutter
**arXiv**：[2512.16449v1](https://arxiv.org/abs/2512.16449) · [PDF](https://arxiv.org/pdf/2512.16449.pdf)  
**作者**：Abhishek Kashyap, Yuxuan Yang, Henrik Andreasson, Todor Stoyanov  

**一句话要点**：提出基于扩散模型的单视角形状补全方法，以提升杂乱场景中机器人抓取成功率。

**关键词**：单视角形状补全, 扩散模型, 机器人抓取, 杂乱场景, 3D重建

## 3 点简述
- 核心问题：单视角相机在杂乱场景中仅能捕获物体部分几何，导致抓取算法性能受限。
- 方法要点：利用扩散模型从单视角深度观测进行类别级3D形状补全，重建完整物体几何。
- 实验或效果：在杂乱场景评估中，抓取成功率比无补全基线高23%，比现有方法高19%。

## 摘要（原文）

> In vision-based robot manipulation, a single camera view can only capture one side of objects of interest, with additional occlusions in cluttered scenes further restricting visibility. As a result, the observed geometry is incomplete, and grasp estimation algorithms perform suboptimally. To address this limitation, we leverage diffusion models to perform category-level 3D shape completion from partial depth observations obtained from a single view, reconstructing complete object geometries to provide richer context for grasp planning. Our method focuses on common household items with diverse geometries, generating full 3D shapes that serve as input to downstream grasp inference networks. Unlike prior work, which primarily considers isolated objects or minimal clutter, we evaluate shape completion and grasping in realistic clutter scenarios with household objects. In preliminary evaluations on a cluttered scene, our approach consistently results in better grasp success rates than a naive baseline without shape completion by 23% and over a recent state of the art shape completion approach by 19%. Our code is available at https://amm.aass.oru.se/shape-completion-grasping/.

