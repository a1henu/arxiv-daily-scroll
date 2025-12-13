---
layout: default
title: Long-LRM++: Preserving Fine Details in Feed-Forward Wide-Coverage Reconstruction
---

# Long-LRM++: Preserving Fine Details in Feed-Forward Wide-Coverage Reconstruction
**arXiv**：[2512.10267v1](https://arxiv.org/abs/2512.10267) · [PDF](https://arxiv.org/pdf/2512.10267.pdf)  
**作者**：Chen Ziwen, Hao Tan, Peng Wang, Zexiang Xu, Li Fuxin  

**一句话要点**：提出Long-LRM++模型，结合半显式场景表示与轻量解码器，实现实时高质量场景重建。

**关键词**：场景重建, 实时渲染, 高斯溅射, 隐式表示, 轻量解码器, 多视图输入

## 3 点简述
- 核心问题：现有方法在实时渲染与细节保留间存在权衡，如高斯溅射易模糊细节，隐式表示计算开销大。
- 方法要点：采用半显式场景表示，结合轻量解码器，减少计算复杂度，同时保持高渲染质量。
- 实验或效果：在DL3DV上匹配LaCT渲染质量，A100 GPU上实现14 FPS实时渲染，并支持64输入视图扩展。

## 摘要（原文）

> Recent advances in generalizable Gaussian splatting (GS) have enabled feed-forward reconstruction of scenes from tens of input views. Long-LRM notably scales this paradigm to 32 input images at $950\times540$ resolution, achieving 360° scene-level reconstruction in a single forward pass. However, directly predicting millions of Gaussian parameters at once remains highly error-sensitive: small inaccuracies in positions or other attributes lead to noticeable blurring, particularly in fine structures such as text. In parallel, implicit representation methods such as LVSM and LaCT have demonstrated significantly higher rendering fidelity by compressing scene information into model weights rather than explicit Gaussians, and decoding RGB frames using the full transformer or TTT backbone. However, this computationally intensive decompression process for every rendered frame makes real-time rendering infeasible. These observations raise key questions: Is the deep, sequential "decompression" process necessary? Can we retain the benefits of implicit representations while enabling real-time performance? We address these questions with Long-LRM++, a model that adopts a semi-explicit scene representation combined with a lightweight decoder. Long-LRM++ matches the rendering quality of LaCT on DL3DV while achieving real-time 14 FPS rendering on an A100 GPU, overcoming the speed limitations of prior implicit methods. Our design also scales to 64 input views at the $950\times540$ resolution, demonstrating strong generalization to increased input lengths. Additionally, Long-LRM++ delivers superior novel-view depth prediction on ScanNetv2 compared to direct depth rendering from Gaussians. Extensive ablation studies validate the effectiveness of each component in the proposed framework.

