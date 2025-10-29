---
layout: default
title: Generative View Stitching
---

# Generative View Stitching
**arXiv**：[2510.24718v1](https://arxiv.org/abs/2510.24718) · [PDF](https://arxiv.org/pdf/2510.24718.pdf)  
**作者**：Chonghyuk Song, Michal Stary, Boyuan Chen, George Kopanas, Vincent Sitzmann  

**一句话要点**：提出生成式视图缝合以解决相机引导视频生成中的碰撞与崩溃问题

**关键词**：视频生成, 扩散模型, 相机引导, 视图缝合, 时序一致性, 闭环机制

## 3 点简述
- 自回归视频扩散模型在长序列生成中稳定，但无法利用未来条件，导致相机轨迹碰撞后崩溃。
- GVS采用并行采样算法，扩展扩散缝合方法，兼容现成视频模型，无需专门训练。
- 引入全向指导增强时序一致性，实现闭环机制，在多种相机路径下生成稳定无碰撞视频。

## 摘要（原文）

> Autoregressive video diffusion models are capable of long rollouts that are
> stable and consistent with history, but they are unable to guide the current
> generation with conditioning from the future. In camera-guided video generation
> with a predefined camera trajectory, this limitation leads to collisions with
> the generated scene, after which autoregression quickly collapses. To address
> this, we propose Generative View Stitching (GVS), which samples the entire
> sequence in parallel such that the generated scene is faithful to every part of
> the predefined camera trajectory. Our main contribution is a sampling algorithm
> that extends prior work on diffusion stitching for robot planning to video
> generation. While such stitching methods usually require a specially trained
> model, GVS is compatible with any off-the-shelf video model trained with
> Diffusion Forcing, a prevalent sequence diffusion framework that we show
> already provides the affordances necessary for stitching. We then introduce
> Omni Guidance, a technique that enhances the temporal consistency in stitching
> by conditioning on both the past and future, and that enables our proposed
> loop-closing mechanism for delivering long-range coherence. Overall, GVS
> achieves camera-guided video generation that is stable, collision-free,
> frame-to-frame consistent, and closes loops for a variety of predefined camera
> paths, including Oscar Reutersv\"ard's Impossible Staircase. Results are best
> viewed as videos at https://andrewsonga.github.io/gvs.

