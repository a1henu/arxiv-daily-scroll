---
layout: default
title: Beyond Reward Margin: Rethinking and Resolving Likelihood Displacement in Diffusion Models via Video Generation
---

# Beyond Reward Margin: Rethinking and Resolving Likelihood Displacement in Diffusion Models via Video Generation
**arXiv**：[2511.19049v1](https://arxiv.org/abs/2511.19049) · [PDF](https://arxiv.org/pdf/2511.19049.pdf)  
**作者**：Ruojun Xu, Yu Kai, Xuhua Ren, Jiaxiang Cheng, Bing Ma, Tianxiang Zheng, Qinhlin Lu  

**一句话要点**：提出PG-DPO以解决扩散模型中似然位移问题，提升视频生成偏好对齐

**关键词**：扩散模型, 直接偏好优化, 似然位移, 视频生成, 偏好对齐, 优化冲突

## 3 点简述
- 核心问题：DPO在扩散模型中导致似然位移，降低生成质量
- 方法要点：引入PG-DPO，结合ARS和IPR缓解优化冲突与次优最大化
- 实验或效果：PG-DPO在定量和定性评估中优于现有方法

## 摘要（原文）

> Direct Preference Optimization (DPO) has shown promising results in aligning generative outputs with human preferences by distinguishing between chosen and rejected samples. However, a critical limitation of DPO is likelihood displacement, where the probabilities of chosen samples paradoxically decrease during training, undermining the quality of generation. Although this issue has been investigated in autoregressive models, its impact within diffusion-based models remains largely unexplored. This gap leads to suboptimal performance in tasks involving video generation. To address this, we conduct a formal analysis of DPO loss through updating policy within the diffusion framework, which describes how the updating of specific training samples influences the model's predictions on other samples. Using this tool, we identify two main failure modes: (1) Optimization Conflict, which arises from small reward margins between chosen and rejected samples, and (2) Suboptimal Maximization, caused by large reward margins. Informed by these insights, we introduce a novel solution named Policy-Guided DPO (PG-DPO), combining Adaptive Rejection Scaling (ARS) and Implicit Preference Regularization (IPR) to effectively mitigate likelihood displacement. Experiments show that PG-DPO outperforms existing methods in both quantitative metrics and qualitative evaluations, offering a robust solution for improving preference alignment in video generation tasks.

