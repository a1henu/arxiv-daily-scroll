---
layout: default
title: Plug-and-Play Fidelity Optimization for Diffusion Transformer Acceleration via Cumulative Error Minimization
---

# Plug-and-Play Fidelity Optimization for Diffusion Transformer Acceleration via Cumulative Error Minimization
**arXiv**：[2512.23258v1](https://arxiv.org/abs/2512.23258) · [PDF](https://arxiv.org/pdf/2512.23258.pdf)  
**作者**：Tong Shao, Yusen Fu, Guoying Sun, Jingde Kong, Zhuotao Tian, Jingyong Su  

**一句话要点**：提出CEM插件通过累积误差最小化优化扩散Transformer加速的生成保真度

**关键词**：扩散Transformer加速, 缓存误差优化, 动态规划算法, 生成保真度, 模型无关插件, 量化模型集成

## 3 点简述
- 核心问题：扩散Transformer迭代去噪导致推理慢，基于缓存的加速方法存在计算误差，固定缓存策略无法适应误差变化
- 方法要点：CEM预定义误差先验，结合动态规划算法优化缓存策略，最小化累积误差，提升保真度
- 实验或效果：在九个生成模型和量化方法上验证，CEM显著提升加速模型的生成保真度，在多个模型上超越原始性能

## 摘要（原文）

> Although Diffusion Transformer (DiT) has emerged as a predominant architecture for image and video generation, its iterative denoising process results in slow inference, which hinders broader applicability and development. Caching-based methods achieve training-free acceleration, while suffering from considerable computational error. Existing methods typically incorporate error correction strategies such as pruning or prediction to mitigate it. However, their fixed caching strategy fails to adapt to the complex error variations during denoising, which limits the full potential of error correction. To tackle this challenge, we propose a novel fidelity-optimization plugin for existing error correction methods via cumulative error minimization, named CEM. CEM predefines the error to characterize the sensitivity of model to acceleration jointly influenced by timesteps and cache intervals. Guided by this prior, we formulate a dynamic programming algorithm with cumulative error approximation for strategy optimization, which achieves the caching error minimization, resulting in a substantial improvement in generation fidelity. CEM is model-agnostic and exhibits strong generalization, which is adaptable to arbitrary acceleration budgets. It can be seamlessly integrated into existing error correction frameworks and quantized models without introducing any additional computational overhead. Extensive experiments conducted on nine generation models and quantized methods across three tasks demonstrate that CEM significantly improves generation fidelity of existing acceleration models, and outperforms the original generation performance on FLUX.1-dev, PixArt-$α$, StableDiffusion1.5 and Hunyuan. The code will be made publicly available.

