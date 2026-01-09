---
layout: default
title: From Rays to Projections: Better Inputs for Feed-Forward View Synthesis
---

# From Rays to Projections: Better Inputs for Feed-Forward View Synthesis
**arXiv**：[2601.05116v1](https://arxiv.org/abs/2601.05116) · [PDF](https://arxiv.org/pdf/2601.05116.pdf)  
**作者**：Zirui Wu, Zeren Jiang, Martin R. Oswald, Jie Song  

**一句话要点**：提出投影条件化以提升前馈视图合成的鲁棒性和一致性

**关键词**：视图合成, 投影条件化, 掩码自编码, 几何一致性, 前馈模型, 图像翻译

## 3 点简述
- 现有方法使用Plücker射线图编码相机，导致预测对相机变换敏感，几何一致性差。
- 提出投影条件化，用目标视图投影线索替代原始相机参数，将任务重构为图像到图像翻译问题。
- 引入掩码自编码预训练策略，利用大规模未校准数据，在视图一致性基准上优于基线，达到SOTA质量。

## 摘要（原文）

> Feed-forward view synthesis models predict a novel view in a single pass with minimal 3D inductive bias. Existing works encode cameras as Plücker ray maps, which tie predictions to the arbitrary world coordinate gauge and make them sensitive to small camera transformations, thereby undermining geometric consistency. In this paper, we ask what inputs best condition a model for robust and consistent view synthesis. We propose projective conditioning, which replaces raw camera parameters with a target-view projective cue that provides a stable 2D input. This reframes the task from a brittle geometric regression problem in ray space to a well-conditioned target-view image-to-image translation problem. Additionally, we introduce a masked autoencoding pretraining strategy tailored to this cue, enabling the use of large-scale uncalibrated data for pretraining. Our method shows improved fidelity and stronger cross-view consistency compared to ray-conditioned baselines on our view-consistency benchmark. It also achieves state-of-the-art quality on standard novel view synthesis benchmarks.

