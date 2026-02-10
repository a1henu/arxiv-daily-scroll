---
layout: default
title: PISCO: Precise Video Instance Insertion with Sparse Control
---

# PISCO: Precise Video Instance Insertion with Sparse Control
**arXiv**：[2602.08277v1](https://arxiv.org/abs/2602.08277) · [PDF](https://arxiv.org/pdf/2602.08277.pdf)  
**作者**：Xiangbo Gao, Renjie Li, Xinghao Chen, Yuheng Wu, Suofei Feng, Qing Yin, Zhengzhong Tu  

**一句话要点**：提出PISCO视频扩散模型，通过稀疏关键帧控制实现精确视频实例插入

**关键词**：视频实例插入, 稀疏控制, 视频扩散模型, 几何感知条件, 分布保持时间掩码, 可变信息引导

## 3 点简述
- 核心问题：视频实例插入需在稀疏控制下保持时空精确性、物理一致性和原始动态
- 方法要点：引入可变信息引导和分布保持时间掩码，结合几何感知条件以稳定生成
- 实验或效果：在PISCO-Bench基准上优于基线，性能随控制信号增加单调提升

## 摘要（原文）

> The landscape of AI video generation is undergoing a pivotal shift: moving beyond general generation - which relies on exhaustive prompt-engineering and "cherry-picking" - towards fine-grained, controllable generation and high-fidelity post-processing. In professional AI-assisted filmmaking, it is crucial to perform precise, targeted modifications. A cornerstone of this transition is video instance insertion, which requires inserting a specific instance into existing footage while maintaining scene integrity. Unlike traditional video editing, this task demands several requirements: precise spatial-temporal placement, physically consistent scene interaction, and the faithful preservation of original dynamics - all achieved under minimal user effort. In this paper, we propose PISCO, a video diffusion model for precise video instance insertion with arbitrary sparse keyframe control. PISCO allows users to specify a single keyframe, start-and-end keyframes, or sparse keyframes at arbitrary timestamps, and automatically propagates object appearance, motion, and interaction. To address the severe distribution shift induced by sparse conditioning in pretrained video diffusion models, we introduce Variable-Information Guidance for robust conditioning and Distribution-Preserving Temporal Masking to stabilize temporal generation, together with geometry-aware conditioning for realistic scene adaptation. We further construct PISCO-Bench, a benchmark with verified instance annotations and paired clean background videos, and evaluate performance using both reference-based and reference-free perceptual metrics. Experiments demonstrate that PISCO consistently outperforms strong inpainting and video editing baselines under sparse control, and exhibits clear, monotonic performance improvements as additional control signals are provided. Project page: xiangbogaobarry.github.io/PISCO.

