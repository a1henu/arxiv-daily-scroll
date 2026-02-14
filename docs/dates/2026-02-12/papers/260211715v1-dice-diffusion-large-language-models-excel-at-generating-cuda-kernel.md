---
layout: default
title: DICE: Diffusion Large Language Models Excel at Generating CUDA Kernels
---

# DICE: Diffusion Large Language Models Excel at Generating CUDA Kernels
**arXiv**：[2602.11715v1](https://arxiv.org/abs/2602.11715) · [PDF](https://arxiv.org/pdf/2602.11715.pdf)  
**作者**：Haolei Bai, Lingcheng Kong, Xueyi Chen, Jianmian Wang, Zhiqiang Tao, Huan Wang  

**一句话要点**：提出DICE扩散大语言模型，通过CuKe数据集和BiC-RL框架解决CUDA内核生成难题。

**关键词**：扩散大语言模型, CUDA内核生成, 强化学习, 代码生成, 并行生成

## 3 点简述
- 核心问题：扩散大语言模型在CUDA内核生成中面临数据稀缺和专业化挑战。
- 方法要点：构建CuKe数据集，并设计BiC-RL框架进行两阶段强化学习优化。
- 实验或效果：在KernelBench上，DICE超越同类模型，实现CUDA内核生成的新SOTA。

## 摘要（原文）

> Diffusion large language models (dLLMs) have emerged as a compelling alternative to autoregressive (AR) LLMs, owing to their capacity for parallel token generation. This paradigm is particularly well-suited for code generation, where holistic structural planning and non-sequential refinement are critical. Despite this potential, tailoring dLLMs for CUDA kernel generation remains challenging, obstructed not only by the high specialization but also by the severe lack of high-quality training data. To address these challenges, we construct CuKe, an augmented supervised fine-tuning dataset optimized for high-performance CUDA kernels. On top of it, we propose a bi-phase curated reinforcement learning (BiC-RL) framework consisting of a CUDA kernel infilling stage and an end-to-end CUDA kernel generation stage. Leveraging this training framework, we introduce DICE, a series of diffusion large language models designed for CUDA kernel generation, spanning three parameter scales, 1.7B, 4B, and 8B. Extensive experiments on KernelBench demonstrate that DICE significantly outperforms both autoregressive and diffusion LLMs of comparable scale, establishing a new state-of-the-art for CUDA kernel generation.

