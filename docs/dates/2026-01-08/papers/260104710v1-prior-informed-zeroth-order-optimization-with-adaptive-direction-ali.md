---
layout: default
title: Prior-Informed Zeroth-Order Optimization with Adaptive Direction Alignment for Memory-Efficient LLM Fine-Tuning
---

# Prior-Informed Zeroth-Order Optimization with Adaptive Direction Alignment for Memory-Efficient LLM Fine-Tuning
**arXiv**：[2601.04710v1](https://arxiv.org/abs/2601.04710) · [PDF](https://arxiv.org/pdf/2601.04710.pdf)  
**作者**：Feihu Jin, Shipeng Cen, Ying Tan  

**一句话要点**：提出基于先验信息的零阶优化方法，通过自适应方向对齐提升大语言模型微调的内存效率与收敛速度。

**关键词**：零阶优化, 大语言模型微调, 内存效率, 梯度估计, 自适应方向对齐, 先验信息扰动

## 3 点简述
- 核心问题：大语言模型微调中反向传播内存开销大，传统零阶优化梯度估计方差高导致收敛慢。
- 方法要点：引入先验信息扰动，动态计算引导向量以对齐梯度方向，减少估计方差。
- 实验或效果：在OPT-13B等模型上，优于传统零阶优化和多数梯度基线，实现效率与精度的平衡。

## 摘要（原文）

> Fine-tuning large language models (LLMs) has achieved remarkable success across various NLP tasks, but the substantial memory overhead during backpropagation remains a critical bottleneck, especially as model scales grow. Zeroth-order (ZO) optimization alleviates this issue by estimating gradients through forward passes and Gaussian sampling, avoiding the need for backpropagation. However, conventional ZO methods suffer from high variance in gradient estimation due to their reliance on random perturbations, leading to slow convergence and suboptimal performance. We propose a simple plug-and-play method that incorporates prior-informed perturbations to refine gradient estimation. Our method dynamically computes a guiding vector from Gaussian samples, which directs perturbations toward more informative directions, significantly accelerating convergence compared to standard ZO approaches. We further investigate a greedy perturbation strategy to explore the impact of prior knowledge on gradient estimation. Theoretically, we prove that our gradient estimator achieves stronger alignment with the true gradient direction, enhancing optimization efficiency. Extensive experiments across LLMs of varying scales and architectures demonstrate that our proposed method could seamlessly integrate into existing optimization methods, delivering faster convergence and superior performance. Notably, on the OPT-13B model, our method outperforms traditional ZO optimization across all 11 benchmark tasks and surpasses gradient-based baselines on 9 out of 11 tasks, establishing a robust balance between efficiency and accuracy.

