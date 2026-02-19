---
layout: default
title: Error Propagation and Model Collapse in Diffusion Models: A Theoretical Study
---

# Error Propagation and Model Collapse in Diffusion Models: A Theoretical Study
**arXiv**：[2602.16601v1](https://arxiv.org/abs/2602.16601) · [PDF](https://arxiv.org/pdf/2602.16601.pdf)  
**作者**：Nail B. Khelifa, Richard E. Turner, Ramji Venkataramanan  

**一句话要点**：理论分析扩散模型中递归训练导致的误差传播与模型崩溃现象

**关键词**：扩散模型, 误差传播, 模型崩溃, 递归训练, 分布漂移, 理论分析

## 3 点简述
- 核心问题：递归使用合成数据训练导致模型性能退化，表现为与目标分布的渐进漂移
- 方法要点：在结合合成数据与新鲜样本的训练流程中，推导生成与目标分布间累积散度的上下界
- 实验或效果：通过合成数据和图像实验验证理论，展示不同漂移机制

## 摘要（原文）

> Machine learning models are increasingly trained or fine-tuned on synthetic data. Recursively training on such data has been observed to significantly degrade performance in a wide range of tasks, often characterized by a progressive drift away from the target distribution. In this work, we theoretically analyze this phenomenon in the setting of score-based diffusion models. For a realistic pipeline where each training round uses a combination of synthetic data and fresh samples from the target distribution, we obtain upper and lower bounds on the accumulated divergence between the generated and target distributions. This allows us to characterize different regimes of drift, depending on the score estimation error and the proportion of fresh data used in each generation. We also provide empirical results on synthetic data and images to illustrate the theory.

