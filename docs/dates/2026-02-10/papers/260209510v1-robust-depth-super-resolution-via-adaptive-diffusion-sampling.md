---
layout: default
title: Robust Depth Super-Resolution via Adaptive Diffusion Sampling
---

# Robust Depth Super-Resolution via Adaptive Diffusion Sampling
**arXiv**：[2602.09510v1](https://arxiv.org/abs/2602.09510) · [PDF](https://arxiv.org/pdf/2602.09510.pdf)  
**作者**：Kun Wang, Yun Zhu, Pan Zhou, Na Zhao  

**一句话要点**：提出AdaDS框架，通过自适应扩散采样实现鲁棒的深度超分辨率

**关键词**：深度超分辨率, 扩散模型, 鲁棒性, 自适应采样, 零样本泛化

## 3 点简述
- 核心问题：传统深度超分辨率方法在严重或未知退化下易产生伪影，缺乏鲁棒性。
- 方法要点：利用高斯平滑的收缩性质，自适应选择扩散反向轨迹起点并注入噪声，以生成先验主导恢复。
- 实验或效果：在真实和合成基准测试中，AdaFS展现零样本泛化优势和对多种退化模式的强韧性。

## 摘要（原文）

> We propose AdaDS, a generalizable framework for depth super-resolution that robustly recovers high-resolution depth maps from arbitrarily degraded low-resolution inputs. Unlike conventional approaches that directly regress depth values and often exhibit artifacts under severe or unknown degradation, AdaDS capitalizes on the contraction property of Gaussian smoothing: as noise accumulates in the forward process, distributional discrepancies between degraded inputs and their pristine high-quality counterparts diminish, ultimately converging to isotropic Gaussian prior. Leveraging this, AdaDS adaptively selects a starting timestep in the reverse diffusion trajectory based on estimated refinement uncertainty, and subsequently injects tailored noise to position the intermediate sample within the high-probability region of the target posterior distribution. This strategy ensures inherent robustness, enabling generative prior of a pre-trained diffusion model to dominate recovery even when upstream estimations are imperfect. Extensive experiments on real-world and synthetic benchmarks demonstrate AdaDS's superior zero-shot generalization and resilience to diverse degradation patterns compared to state-of-the-art methods.

