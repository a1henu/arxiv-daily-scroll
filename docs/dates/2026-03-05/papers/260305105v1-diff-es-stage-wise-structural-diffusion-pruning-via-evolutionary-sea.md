---
layout: default
title: Diff-ES: Stage-wise Structural Diffusion Pruning via Evolutionary Search
---

# Diff-ES: Stage-wise Structural Diffusion Pruning via Evolutionary Search
**arXiv**：[2603.05105v1](https://arxiv.org/abs/2603.05105) · [PDF](https://arxiv.org/pdf/2603.05105.pdf)  
**作者**：Zongfang Liu, Shengkun Tang, Zongliang Wu, Xin Yuan, Zhiqiang Shen  

**一句话要点**：提出Diff-ES框架，通过进化搜索优化扩散模型的分阶段结构化剪枝，以平衡加速与图像质量。

**关键词**：扩散模型剪枝, 进化搜索, 结构化剪枝, 模型加速, 图像生成

## 3 点简述
- 扩散模型计算成本高，现有结构化剪枝方法难以平衡加速与质量，且依赖手动调优。
- Diff-ES利用进化搜索自动优化分阶段稀疏度计划，通过权重路由实现内存高效执行。
- 在DiT和SDXL上实验显示，Diff-ES在保持生成质量的同时实现实际加速，性能领先。

## 摘要（原文）

> Diffusion models have achieved remarkable success in high-fidelity image generation but remain computationally demanding due to their multi-step denoising process and large model sizes. Although prior work improves efficiency either by reducing sampling steps or by compressing model parameters, existing structured pruning approaches still struggle to balance real acceleration and image quality preservation. In particular, prior methods such as MosaicDiff rely on heuristic, manually tuned stage-wise sparsity schedules and stitch multiple independently pruned models during inference, which increases memory overhead. However, the importance of diffusion steps is highly non-uniform and model-dependent. As a result, schedules derived from simple heuristics or empirical observations often fail to generalize and may lead to suboptimal performance. To this end, we introduce \textbf{Diff-ES}, a stage-wise structural \textbf{Diff}usion pruning framework via \textbf{E}volutionary \textbf{S}earch, which optimizes the stage-wise sparsity schedule and executes it through memory-efficient weight routing without model duplication. Diff-ES divides the diffusion trajectory into multiple stages, automatically discovers an optimal stage-wise sparsity schedule via evolutionary search, and activates stage-conditioned weights dynamically without duplicating model parameters. Our framework naturally integrates with existing structured pruning methods for diffusion models including depth and width pruning. Extensive experiments on DiT and SDXL demonstrate that Diff-ES consistently achieves wall-clock speedups while incurring minimal degradation in generation quality, establishing state-of-the-art performance for structured diffusion model pruning.

