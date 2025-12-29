---
layout: default
title: Fast Inference of Visual Autoregressive Model with Adjacency-Adaptive Dynamical Draft Trees
---

# Fast Inference of Visual Autoregressive Model with Adjacency-Adaptive Dynamical Draft Trees
**arXiv**：[2512.21857v1](https://arxiv.org/abs/2512.21857) · [PDF](https://arxiv.org/pdf/2512.21857.pdf)  
**作者**：Haodong Lei, Hongsong Wang, Xin Geng, Liang Wang, Pan Zhou  

**一句话要点**：提出邻接自适应动态草稿树以加速视觉自回归模型推理

**关键词**：视觉自回归模型, 推测解码, 动态草稿树, 图像生成加速, 邻接自适应

## 3 点简述
- 核心问题：视觉自回归模型推理慢，推测解码因图像区域预测难度差异导致接受率不一致
- 方法要点：基于邻接令牌状态和先验接受率动态调整草稿树深度和宽度，在简单区域加深、复杂区域加宽
- 实验或效果：在MS-COCO 2017和PartiPrompts上分别实现3.13倍和3.05倍加速，可与LANTERN等采样方法集成

## 摘要（原文）

> Autoregressive (AR) image models achieve diffusion-level quality but suffer from sequential inference, requiring approximately 2,000 steps for a 576x576 image. Speculative decoding with draft trees accelerates LLMs yet underperforms on visual AR models due to spatially varying token prediction difficulty. We identify a key obstacle in applying speculative decoding to visual AR models: inconsistent acceptance rates across draft trees due to varying prediction difficulties in different image regions. We propose Adjacency-Adaptive Dynamical Draft Trees (ADT-Tree), an adjacency-adaptive dynamic draft tree that dynamically adjusts draft tree depth and width by leveraging adjacent token states and prior acceptance rates. ADT-Tree initializes via horizontal adjacency, then refines depth/width via bisectional adaptation, yielding deeper trees in simple regions and wider trees in complex ones. The empirical evaluations on MS-COCO 2017 and PartiPrompts demonstrate that ADT-Tree achieves speedups of 3.13xand 3.05x, respectively. Moreover, it integrates seamlessly with relaxed sampling methods such as LANTERN, enabling further acceleration. Code is available at https://github.com/Haodong-Lei-Ray/ADT-Tree.

