---
layout: default
title: ArcFlow: Unleashing 2-Step Text-to-Image Generation via High-Precision Non-Linear Flow Distillation
---

# ArcFlow: Unleashing 2-Step Text-to-Image Generation via High-Precision Non-Linear Flow Distillation
**arXiv**：[2602.09014v1](https://arxiv.org/abs/2602.09014) · [PDF](https://arxiv.org/pdf/2602.09014.pdf)  
**作者**：Zihan Yang, Shuyuan Tu, Licheng Zhang, Qi Dai, Yu-Gang Jiang, Zuxuan Wu  

**一句话要点**：提出ArcFlow框架，通过非线性流蒸馏实现2步文本到图像生成，以解决现有蒸馏方法线性近似导致的轨迹匹配问题。

**关键词**：文本到图像生成, 扩散模型, 蒸馏训练, 非线性流, 快速推理, 轨迹近似

## 3 点简述
- 核心问题：扩散模型推理成本高，现有蒸馏方法使用线性捷径近似教师轨迹，难以匹配速度变化，导致生成质量下降。
- 方法要点：ArcFlow参数化速度场为连续动量过程混合，捕获速度演化，通过解析积分形成非线性轨迹，实现高精度教师轨迹近似。
- 实验或效果：基于Qwen-Image-20B和FLUX.1-dev模型，仅微调少于5%参数，在2步推理下实现40倍加速，无明显质量损失。

## 摘要（原文）

> Diffusion models have achieved remarkable generation quality, but they suffer from significant inference cost due to their reliance on multiple sequential denoising steps, motivating recent efforts to distill this inference process into a few-step regime. However, existing distillation methods typically approximate the teacher trajectory by using linear shortcuts, which makes it difficult to match its constantly changing tangent directions as velocities evolve across timesteps, thereby leading to quality degradation. To address this limitation, we propose ArcFlow, a few-step distillation framework that explicitly employs non-linear flow trajectories to approximate pre-trained teacher trajectories. Concretely, ArcFlow parameterizes the velocity field underlying the inference trajectory as a mixture of continuous momentum processes. This enables ArcFlow to capture velocity evolution and extrapolate coherent velocities to form a continuous non-linear trajectory within each denoising step. Importantly, this parameterization admits an analytical integration of this non-linear trajectory, which circumvents numerical discretization errors and results in high-precision approximation of the teacher trajectory. To train this parameterization into a few-step generator, we implement ArcFlow via trajectory distillation on pre-trained teacher models using lightweight adapters. This strategy ensures fast, stable convergence while preserving generative diversity and quality. Built on large-scale models (Qwen-Image-20B and FLUX.1-dev), ArcFlow only fine-tunes on less than 5% of original parameters and achieves a 40x speedup with 2 NFEs over the original multi-step teachers without significant quality degradation. Experiments on benchmarks show the effectiveness of ArcFlow both qualitatively and quantitatively.

