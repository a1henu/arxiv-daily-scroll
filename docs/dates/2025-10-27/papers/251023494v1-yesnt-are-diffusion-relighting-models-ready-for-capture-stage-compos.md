---
layout: default
title: Yesnt: Are Diffusion Relighting Models Ready for Capture Stage Compositing? A Hybrid Alternative to Bridge the Gap
---

# Yesnt: Are Diffusion Relighting Models Ready for Capture Stage Compositing? A Hybrid Alternative to Bridge the Gap
**arXiv**：[2510.23494v1](https://arxiv.org/abs/2510.23494) · [PDF](https://arxiv.org/pdf/2510.23494.pdf)  
**作者**：Elisabeth Jüttner, Leona Krath, Stefan Korfhage, Hannah Dröge, Matthias B. Hullin, Markus Plack  

**一句话要点**：提出混合重光照框架以解决体积视频重光照的时序不稳定问题

**关键词**：体积视频重光照, 扩散模型, 时序稳定性, 混合框架, 高斯不透明度场, 光流引导

## 3 点简述
- 核心问题：扩散模型在序列重光照中产生随机噪声和不稳定性，视频扩散模型受限于内存和规模
- 方法要点：结合扩散先验与时间正则化，使用光流引导聚合材料属性，并基于高斯不透明度场渲染间接效果
- 实验或效果：在真实和合成捕获上实现比纯扩散基线更稳定的重光照，并扩展到更长序列

## 摘要（原文）

> Volumetric video relighting is essential for bringing captured performances
> into virtual worlds, but current approaches struggle to deliver temporally
> stable, production-ready results. Diffusion-based intrinsic decomposition
> methods show promise for single frames, yet suffer from stochastic noise and
> instability when extended to sequences, while video diffusion models remain
> constrained by memory and scale. We propose a hybrid relighting framework that
> combines diffusion-derived material priors with temporal regularization and
> physically motivated rendering. Our method aggregates multiple stochastic
> estimates of per-frame material properties into temporally consistent shading
> components, using optical-flow-guided regularization. For indirect effects such
> as shadows and reflections, we extract a mesh proxy from Gaussian Opacity
> Fields and render it within a standard graphics pipeline. Experiments on real
> and synthetic captures show that this hybrid strategy achieves substantially
> more stable relighting across sequences than diffusion-only baselines, while
> scaling beyond the clip lengths feasible for video diffusion. These results
> indicate that hybrid approaches, which balance learned priors with physically
> grounded constraints, are a practical step toward production-ready volumetric
> video relighting.

