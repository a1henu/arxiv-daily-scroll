---
layout: default
title: Causal World Modeling for Robot Control
---

# Causal World Modeling for Robot Control
**arXiv**：[2601.21998v1](https://arxiv.org/abs/2601.21998) · [PDF](https://arxiv.org/pdf/2601.21998.pdf)  
**作者**：Lin Li, Qihang Zhang, Yiming Luo, Shuai Yang, Ruilin Wang, Fei Han, Mingrui Yu, Zelin Gao, Nan Xue, Xing Zhu, Yujun Shen, Yinghao Xu  

**一句话要点**：提出LingBot-VA自回归扩散框架，通过视频世界建模提升机器人控制性能

**关键词**：视频世界建模, 机器人控制, 自回归扩散, 共享潜在空间, 闭环滚动, 异步推理

## 3 点简述
- 核心问题：视频世界建模与视觉语言预训练作为机器人学习新基础，需理解动作与视觉动态的因果关系
- 方法要点：采用共享潜在空间、闭环滚动机制和异步推理管道，同时学习帧预测与策略执行
- 实验或效果：在仿真基准和真实场景中展示长时程操作、数据效率和强泛化能力

## 摘要（原文）

> This work highlights that video world modeling, alongside vision-language pre-training, establishes a fresh and independent foundation for robot learning. Intuitively, video world models provide the ability to imagine the near future by understanding the causality between actions and visual dynamics. Inspired by this, we introduce LingBot-VA, an autoregressive diffusion framework that learns frame prediction and policy execution simultaneously. Our model features three carefully crafted designs: (1) a shared latent space, integrating vision and action tokens, driven by a Mixture-of-Transformers (MoT) architecture, (2) a closed-loop rollout mechanism, allowing for ongoing acquisition of environmental feedback with ground-truth observations, (3) an asynchronous inference pipeline, parallelizing action prediction and motor execution to support efficient control. We evaluate our model on both simulation benchmarks and real-world scenarios, where it shows significant promise in long-horizon manipulation, data efficiency in post-training, and strong generalizability to novel configurations. The code and model are made publicly available to facilitate the community.

