---
layout: default
title: Improving Diffusion Language Model Decoding through Joint Search in Generation Order and Token Space
---

# Improving Diffusion Language Model Decoding through Joint Search in Generation Order and Token Space
**arXiv**：[2601.20339v1](https://arxiv.org/abs/2601.20339) · [PDF](https://arxiv.org/pdf/2601.20339.pdf)  
**作者**：Yangyi Shen, Tianjian Feng, Jiaqi Han, Wen Wang, Tianlang Chen, Chunhua Shen, Jure Leskovec, Stefano Ermon  

**一句话要点**：提出Order-Token Search以提升扩散语言模型解码性能，通过联合搜索生成顺序和词元空间。

**关键词**：扩散语言模型, 解码方法, 联合搜索, 轨迹探索, 似然估计

## 3 点简述
- 核心问题：现有扩散语言模型解码方法局限于单一轨迹，限制了轨迹空间的探索。
- 方法要点：引入Order-Token Search，基于似然估计器评分去噪动作，实现稳定剪枝和高效轨迹探索。
- 实验或效果：在数学推理和编码基准测试中，性能优于基线，匹配或超越diffu-GRPO后训练的d1-LLaDA。

## 摘要（原文）

> Diffusion Language Models (DLMs) offer order-agnostic generation that can explore many possible decoding trajectories. However, current decoding methods commit to a single trajectory, limiting exploration in trajectory space. We introduce Order-Token Search to explore this space through jointly searching over generation order and token values. Its core is a likelihood estimator that scores denoising actions, enabling stable pruning and efficient exploration of diverse trajectories. Across mathematical reasoning and coding benchmarks, Order-Token Search consistently outperforms baselines on GSM8K, MATH500, Countdown, and HumanEval (3.1%, 3.8%, 7.9%, and 6.8% absolute over backbone), matching or surpassing diffu-GRPO post-trained d1-LLaDA. Our work establishes joint search as a key component for advancing decoding in DLMs.

