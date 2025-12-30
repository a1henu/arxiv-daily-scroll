---
layout: default
title: Task-oriented Learnable Diffusion Timesteps for Universal Few-shot Learning of Dense Tasks
---

# Task-oriented Learnable Diffusion Timesteps for Universal Few-shot Learning of Dense Tasks
**arXiv**：[2512.23210v1](https://arxiv.org/abs/2512.23210) · [PDF](https://arxiv.org/pdf/2512.23210.pdf)  
**作者**：Changgyoon Oh, Jongoh Jeong, Jegyeong Cho, Kuk-Jin Yoon  

**一句话要点**：提出任务感知扩散时间步选择与特征整合方法，以优化少样本密集预测任务的通用学习性能。

**关键词**：扩散模型, 少样本学习, 密集预测, 时间步选择, 特征整合, 通用学习

## 3 点简述
- 核心问题：现有扩散模型在密集预测任务中，时间步特征选择依赖经验直觉，导致性能次优且偏向特定任务。
- 方法要点：引入任务感知时间步选择模块和特征整合模块，自适应选择并整合扩散时间步特征，提升少样本学习效果。
- 实验或效果：在Taskonomy数据集上验证，该方法在少样本密集预测场景中表现出优越性能，支持通用任务学习。

## 摘要（原文）

> Denoising diffusion probabilistic models have brought tremendous advances in generative tasks, achieving state-of-the-art performance thus far. Current diffusion model-based applications exploit the power of learned visual representations from multistep forward-backward Markovian processes for single-task prediction tasks by attaching a task-specific decoder. However, the heuristic selection of diffusion timestep features still heavily relies on empirical intuition, often leading to sub-optimal performance biased towards certain tasks. To alleviate this constraint, we investigate the significance of versatile diffusion timestep features by adaptively selecting timesteps best suited for the few-shot dense prediction task, evaluated on an arbitrary unseen task. To this end, we propose two modules: Task-aware Timestep Selection (TTS) to select ideal diffusion timesteps based on timestep-wise losses and similarity scores, and Timestep Feature Consolidation (TFC) to consolidate the selected timestep features to improve the dense predictive performance in a few-shot setting. Accompanied by our parameter-efficient fine-tuning adapter, our framework effectively achieves superiority in dense prediction performance given only a few support queries. We empirically validate our learnable timestep consolidation method on the large-scale challenging Taskonomy dataset for dense prediction, particularly for practical universal and few-shot learning scenarios.

