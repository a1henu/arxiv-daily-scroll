---
layout: default
title: Scaling Beyond Masked Diffusion Language Models
---

# Scaling Beyond Masked Diffusion Language Models
**arXiv**：[2602.15014v1](https://arxiv.org/abs/2602.15014) · [PDF](https://arxiv.org/pdf/2602.15014.pdf)  
**作者**：Subham Sekhar Sahoo, Jean-Marie Lemercier, Zhihan Yang, Justin Deschenaux, Jingyu Liu, John Thickstun, Ante Jukic  

**一句话要点**：研究离散扩散语言模型的缩放规律，挑战掩码扩散的主导地位并优化效率。

**关键词**：扩散语言模型, 缩放规律, 掩码扩散, 均匀状态扩散, 困惑度评估, 采样效率

## 3 点简述
- 核心问题：掩码扩散在语言建模基准上表现优异，但其缩放规律和跨算法比较的适用性未知。
- 方法要点：首次研究均匀状态和插值离散扩散方法的缩放规律，并优化掩码扩散的训练目标以提高效率。
- 实验或效果：在1.7B参数规模下，均匀状态扩散在GSM8K上优于自回归和掩码扩散模型，尽管验证困惑度较差。

## 摘要（原文）

> Diffusion language models are a promising alternative to autoregressive models due to their potential for faster generation. Among discrete diffusion approaches, Masked diffusion currently dominates, largely driven by strong perplexity on language modeling benchmarks. In this work, we present the first scaling law study of uniform-state and interpolating discrete diffusion methods. We also show that Masked diffusion models can be made approximately 12% more FLOPs-efficient when trained with a simple cross-entropy objective. We find that perplexity is informative within a diffusion family but can be misleading across families, where models with worse likelihood scaling may be preferable due to faster and more practical sampling, as reflected by the speed-quality Pareto frontier. These results challenge the view that Masked diffusion is categorically the future of diffusion language modeling and that perplexity alone suffices for cross-algorithm comparison. Scaling all methods to 1.7B parameters, we show that uniform-state diffusion remains competitive on likelihood-based benchmarks and outperforms autoregressive and Masked diffusion models on GSM8K, despite worse validation perplexity. We provide the code, model checkpoints, and video tutorials on the project page: http://s-sahoo.github.io/scaling-dllms

