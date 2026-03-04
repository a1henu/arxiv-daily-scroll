---
layout: default
title: Scores Know Bobs Voice: Speaker Impersonation Attack
---

# Scores Know Bobs Voice: Speaker Impersonation Attack
**arXiv**：[2603.02781v1](https://arxiv.org/abs/2603.02781) · [PDF](https://arxiv.org/pdf/2603.02781.pdf)  
**作者**：Chanwoo Hwang, Sunpill Kim, Yong Kiam Tan, Tianchi Liu, Seunghun Paik, Dongsoo Kim, Mondal Soumik, Khin Mi Mi Aung, Jae Hong Seo  

**一句话要点**：提出特征对齐的反演生成攻击框架，以提升说话人识别系统在分数模拟攻击中的查询效率。

**关键词**：说话人识别系统, 分数模拟攻击, 生成模型反演, 特征对齐, 查询效率优化, 子空间投影攻击

## 3 点简述
- 核心问题：现有攻击在原始波形或生成模型潜在空间优化时，因缺乏说话人判别几何对齐，导致查询效率低。
- 方法要点：通过特征对齐反演策略，同步合成模型潜在空间与说话人嵌入特征空间，使潜在更新直接提升分数。
- 实验效果：方法显著减少查询次数，平均比先前方法少10倍，子空间投影攻击仅用50次查询达到91.65%成功率。

## 摘要（原文）

> Advances in deep learning have enabled the widespread deployment of speaker recognition systems (SRSs), yet they remain vulnerable to score-based impersonation attacks. Existing attacks that operate directly on raw waveforms require a large number of queries due to the difficulty of optimizing in high-dimensional audio spaces. Latent-space optimization within generative models offers improved efficiency, but these latent spaces are shaped by data distribution matching and do not inherently capture speaker-discriminative geometry. As a result, optimization trajectories often fail to align with the adversarial direction needed to maximize victim scores.
>   To address this limitation, we propose an inversion-based generative attack framework that explicitly aligns the latent space of the synthesis model with the discriminative feature space of SRSs. We first analyze the requirements of an inverse model for score-based attacks and introduce a feature-aligned inversion strategy that geometrically synchronizes latent representations with speaker embeddings. This alignment ensures that latent updates directly translate into score improvements. Moreover, it enables new attack paradigms, including subspace-projection-based attacks, which were previously infeasible due to the absence of a faithful feature-to-audio mapping.
>   Experiments show that our method significantly improves query efficiency, achieving competitive attack success rates with on average 10x fewer queries than prior approaches. In particular, the enabled subspace-projection-based attack attains up to 91.65% success using only 50 queries. These findings establish feature-aligned inversion as a key tool for evaluating the robustness of modern SRSs against score-based impersonation threats.

