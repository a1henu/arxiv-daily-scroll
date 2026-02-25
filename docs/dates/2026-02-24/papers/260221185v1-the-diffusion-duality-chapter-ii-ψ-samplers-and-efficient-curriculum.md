---
layout: default
title: The Diffusion Duality, Chapter II: $Ψ$-Samplers and Efficient Curriculum
---

# The Diffusion Duality, Chapter II: $Ψ$-Samplers and Efficient Curriculum
**arXiv**：[2602.21185v1](https://arxiv.org/abs/2602.21185) · [PDF](https://arxiv.org/pdf/2602.21185.pdf)  
**作者**：Justin Deschenaux, Caglar Gulcehre, Subham Sekhar Sahoo  

**一句话要点**：提出预测-校正采样器与高效课程，提升均匀状态离散扩散模型的采样质量与训练效率。

**关键词**：离散扩散模型, 预测-校正采样器, 均匀状态扩散, 高效课程学习, 语言建模, 图像生成

## 3 点简述
- 均匀状态离散扩散模型在少步生成中表现优异，但传统采样器随步数增加质量停滞。
- 引入预测-校正采样器家族，适用于任意噪声过程，在语言和图像建模中超越祖先采样。
- 开发内存高效课程，减少高斯松弛训练阶段的时间和内存消耗，保持性能。

## 摘要（原文）

> Uniform-state discrete diffusion models excel at few-step generation and guidance due to their ability to self-correct, making them preferred over autoregressive or Masked diffusion models in these settings. However, their sampling quality plateaus with ancestral samplers as the number of steps increases. We introduce a family of Predictor-Corrector (PC) samplers for discrete diffusion that generalize prior methods and apply to arbitrary noise processes. When paired with uniform-state diffusion, our samplers outperform ancestral sampling on both language and image modeling, achieving lower generative perplexity at matched unigram entropy on OpenWebText and better FID/IS scores on CIFAR10. Crucially, unlike conventional samplers, our PC methods continue to improve with more sampling steps. Taken together, these findings call into question the assumption that Masked diffusion is the inevitable future of diffusion-based language modeling. Beyond sampling, we develop a memory-efficient curriculum for the Gaussian relaxation training phase, reducing training time by 25% and memory by 33% compared to Duo while maintaining comparable perplexity on OpenWebText and LM1B and strong downstream performance. We release code, checkpoints, and a video-tutorial on: https://s-sahoo.com/duo-ch2

