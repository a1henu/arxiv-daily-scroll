---
layout: default
title: GenTract: Generative Global Tractography
---

# GenTract: Generative Global Tractography
**arXiv**：[2511.13183v1](https://arxiv.org/abs/2511.13183) · [PDF](https://arxiv.org/pdf/2511.13183.pdf)  
**作者**：Alec Sargood, Lemuel Puglisi, Elinor Thompson, Mirco Musolesi, Daniel C. Alexander  

**一句话要点**：提出GenTract生成模型以解决脑白质纤维束成像中的误差累积与计算成本问题

**关键词**：生成模型, 全局纤维束成像, 扩散磁共振成像, 纤维束轨迹推断, 计算效率优化

## 3 点简述
- 局部纤维束成像方法易累积误差，全局方法计算昂贵，影响脑白质路径推断。
- GenTract作为首个生成模型，直接从dMRI学习映射生成完整、解剖合理的纤维束。
- 在低分辨率和噪声数据上，GenTract精度比次优方法高一个数量级，表现优异。

## 摘要（原文）

> Tractography is the process of inferring the trajectories of white-matter pathways in the brain from diffusion magnetic resonance imaging (dMRI). Local tractography methods, which construct streamlines by following local fiber orientation estimates stepwise through an image, are prone to error accumulation and high false positive rates, particularly on noisy or low-resolution data. In contrast, global methods, which attempt to optimize a collection of streamlines to maximize compatibility with underlying fiber orientation estimates, are computationally expensive. To address these challenges, we introduce GenTract, the first generative model for global tractography. We frame tractography as a generative task, learning a direct mapping from dMRI to complete, anatomically plausible streamlines. We compare both diffusion-based and flow matching paradigms and evaluate GenTract's performance against state-of-the-art baselines. Notably, GenTract achieves precision 2.1x higher than the next-best method, TractOracle. This advantage becomes even more pronounced in challenging low-resolution and noisy settings, where it outperforms the closest competitor by an order of magnitude. By producing tractograms with high precision on research-grade data while also maintaining reliability on imperfect, lower-resolution data, GenTract represents a promising solution for global tractography.

