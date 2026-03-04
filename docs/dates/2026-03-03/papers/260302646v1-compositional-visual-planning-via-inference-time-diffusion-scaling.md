---
layout: default
title: Compositional Visual Planning via Inference-Time Diffusion Scaling
---

# Compositional Visual Planning via Inference-Time Diffusion Scaling
**arXiv**：[2603.02646v1](https://arxiv.org/abs/2603.02646) · [PDF](https://arxiv.org/pdf/2603.02646.pdf)  
**作者**：Yixin Zhang, Yunhao Luo, Utkarsh Aashu Mishra, Woo Chul Shin, Yongxin Chen, Danfei Xu  

**一句话要点**：提出基于Tweedie估计边界对齐的推理时扩散缩放方法，以解决长时程视觉规划中的不稳定问题。

**关键词**：视觉规划, 扩散模型, 长时程任务, 推理时优化, 边界对齐, 因子图

## 3 点简述
- 核心问题：扩散模型在长时程机器人规划中因计算限制和训练数据不足导致全局计划不一致。
- 方法要点：通过链式因子图建模重叠视频块，在推理时对Tweedie估计进行同步和异步消息传递以强制边界对齐。
- 实验或效果：无需额外训练，在未见起始-目标组合上显著优于基线，提升规划稳定性。

## 摘要（原文）

> Diffusion models excel at short-horizon robot planning, yet scaling them to long-horizon tasks remains challenging due to computational constraints and limited training data. Existing compositional approaches stitch together short segments by separately denoising each component and averaging overlapping regions. However, this suffers from instability as the factorization assumption breaks down in noisy data space, leading to inconsistent global plans. We propose that the key to stable compositional generation lies in enforcing boundary agreement on the estimated clean data (Tweedie estimates) rather than on noisy intermediate states. Our method formulates long-horizon planning as inference over a chain-structured factor graph of overlapping video chunks, where pretrained short-horizon video diffusion models provide local priors. At inference time, we enforce boundary agreement through a novel combination of synchronous and asynchronous message passing that operates on Tweedie estimates, producing globally consistent guidance without requiring additional training. Our training-free framework demonstrates significant improvements over existing baselines, effectively generalizing to unseen start-goal combinations that were not present in the original training data. Project website: https://comp-visual-planning.github.io/

