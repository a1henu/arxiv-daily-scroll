---
layout: default
title: True Self-Supervised Novel View Synthesis is Transferable
---

# True Self-Supervised Novel View Synthesis is Transferable
**arXiv**：[2510.13063v1](https://arxiv.org/abs/2510.13063) · [PDF](https://arxiv.org/pdf/2510.13063.pdf)  
**作者**：Thomas W. Mitchel, Hyunwoo Ryu, Vincent Sitzmann  

**一句话要点**：提出XFactor实现可转移自监督新视角合成，无需几何先验。

**关键词**：新视角合成, 自监督学习, 姿态估计, 可转移性, 几何推理, 潜变量模型

## 3 点简述
- 核心问题：现有自监督新视角合成模型姿态预测不可转移，导致不同场景轨迹不一致。
- 方法要点：结合成对姿态估计与输入输出增强，解耦相机姿态与场景内容。
- 实验或效果：XFactor显著优于先前方法，潜变量姿态与真实姿态高度相关。

## 摘要（原文）

> In this paper, we identify that the key criterion for determining whether a
> model is truly capable of novel view synthesis (NVS) is transferability:
> Whether any pose representation extracted from one video sequence can be used
> to re-render the same camera trajectory in another. We analyze prior work on
> self-supervised NVS and find that their predicted poses do not transfer: The
> same set of poses lead to different camera trajectories in different 3D scenes.
> Here, we present XFactor, the first geometry-free self-supervised model capable
> of true NVS. XFactor combines pair-wise pose estimation with a simple
> augmentation scheme of the inputs and outputs that jointly enables
> disentangling camera pose from scene content and facilitates geometric
> reasoning. Remarkably, we show that XFactor achieves transferability with
> unconstrained latent pose variables, without any 3D inductive biases or
> concepts from multi-view geometry -- such as an explicit parameterization of
> poses as elements of SE(3). We introduce a new metric to quantify
> transferability, and through large-scale experiments, we demonstrate that
> XFactor significantly outperforms prior pose-free NVS transformers, and show
> that latent poses are highly correlated with real-world poses through probing
> experiments.

