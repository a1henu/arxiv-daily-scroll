---
layout: default
title: FFP-300K: Scaling First-Frame Propagation for Generalizable Video Editing
---

# FFP-300K: Scaling First-Frame Propagation for Generalizable Video Editing
**arXiv**：[2601.01720v1](https://arxiv.org/abs/2601.01720) · [PDF](https://arxiv.org/pdf/2601.01720.pdf)  
**作者**：Xijie Huang, Chengming Xu, Donghao Luo, Xiaobin Hu, Peng Tang, Xu Peng, Jiangning Zhang, Chengjie Wang, Yanwei Fu  

**一句话要点**：提出FFP-300K数据集与自适应时空RoPE框架，以解决视频编辑中首帧传播的运行时依赖问题

**关键词**：视频编辑, 首帧传播, 大规模数据集, 自适应位置编码, 自蒸馏训练, 时空稳定性

## 3 点简述
- 核心问题：现有首帧传播方法依赖运行时引导，源于训练数据不足，如视频短、分辨率低、任务多样性缺乏
- 方法要点：构建FFP-300K大规模数据集，并设计自适应时空RoPE框架，通过自蒸馏策略实现无引导传播
- 实验或效果：在EditVerseBench基准上显著优于现有模型，PickScore和VLM分数提升约0.2和0.3

## 摘要（原文）

> First-Frame Propagation (FFP) offers a promising paradigm for controllable video editing, but existing methods are hampered by a reliance on cumbersome run-time guidance. We identify the root cause of this limitation as the inadequacy of current training datasets, which are often too short, low-resolution, and lack the task diversity required to teach robust temporal priors. To address this foundational data gap, we first introduce FFP-300K, a new large-scale dataset comprising 300K high-fidelity video pairs at 720p resolution and 81 frames in length, constructed via a principled two-track pipeline for diverse local and global edits. Building on this dataset, we propose a novel framework designed for true guidance-free FFP that resolves the critical tension between maintaining first-frame appearance and preserving source video motion. Architecturally, we introduce Adaptive Spatio-Temporal RoPE (AST-RoPE), which dynamically remaps positional encodings to disentangle appearance and motion references. At the objective level, we employ a self-distillation strategy where an identity propagation task acts as a powerful regularizer, ensuring long-term temporal stability and preventing semantic drift. Comprehensive experiments on the EditVerseBench benchmark demonstrate that our method significantly outperforming existing academic and commercial models by receiving about 0.2 PickScore and 0.3 VLM score improvement against these competitors.

