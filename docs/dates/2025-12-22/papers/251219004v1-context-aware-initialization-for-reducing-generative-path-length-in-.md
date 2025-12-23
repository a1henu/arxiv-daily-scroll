---
layout: default
title: Context-Aware Initialization for Reducing Generative Path Length in Diffusion Language Models
---

# Context-Aware Initialization for Reducing Generative Path Length in Diffusion Language Models
**arXiv**：[2512.19004v1](https://arxiv.org/abs/2512.19004) · [PDF](https://arxiv.org/pdf/2512.19004.pdf)  
**作者**：Tongyuan Miao, Gary Huang, Kai Jun Han, Annie Jiang  

**一句话要点**：提出上下文感知初始化以减少扩散语言模型的生成路径长度

**关键词**：扩散语言模型, 上下文感知初始化, 生成路径优化, 推理加速, 提示条件先验

## 3 点简述
- 核心问题：扩散大语言模型推理时需多次去噪迭代，导致效率低下
- 方法要点：通过轻量辅助模型注入提示条件先验，缩短生成轨迹
- 实验或效果：在GSM8K上减少约35%函数评估，但可能影响最终准确性

## 摘要（原文）

> Diffusion Large Language Models (DLLMs) enable fully parallel token decoding but often remain impractical at inference time due to the many denoising iterations required to refine an information-free, fully masked initialization into coherent text. Most existing acceleration methods focus on traversing this generative trajectory more efficiently via improved solvers or sampling strategies. We advance a complementary perspective: shorten the trajectory itself by starting closer to the target distribution through context-aware initialization.
>   We propose a training-free interface that injects prompt-conditioned priors from a lightweight auxiliary model into the diffusion initialization, and instantiate it with two mechanisms: discrete token injection and representation-level embedding interpolation. Because injected priors can be imperfect and unmask-only decoding can over-commit early, we also introduce a simple confidence-based remasking mechanism as a form of prior skepticism. Preliminary evidence on GSM8K suggests that context-aware initialization can substantially reduce denoising iterations (about 35\% fewer function evaluations in our setting), while also exposing a key open challenge: naive warm-starting can degrade final accuracy relative to strong diffusion baselines. We use these findings to motivate a research agenda around calibration, revision mechanisms, and representation alignment for reliable warm-started diffusion decoding.

