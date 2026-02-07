---
layout: default
title: Discrete diffusion samplers and bridges: Off-policy algorithms and applications in latent spaces
---

# Discrete diffusion samplers and bridges: Off-policy algorithms and applications in latent spaces
**arXiv**：[2602.05961v1](https://arxiv.org/abs/2602.05961) · [PDF](https://arxiv.org/pdf/2602.05961.pdf)  
**作者**：Arran Carter, Sanghyeok Choi, Kirill Tamogashev, Víctor Elvira, Nikolay Malkin  

**一句话要点**：提出离散扩散采样器与桥的离策略算法，应用于离散空间采样与桥接任务

**关键词**：离散扩散采样, 离策略训练, 施罗德桥, 隐空间采样, 后验采样

## 3 点简述
- 核心问题：离散空间采样效率低，未充分利用连续空间采样技术
- 方法要点：引入离策略训练技术，提升离散扩散采样器性能
- 实验或效果：在合成基准测试中表现提升，并应用于图像生成模型的离散隐空间后验采样

## 摘要（原文）

> Sampling from a distribution $p(x) \propto e^{-\mathcal{E}(x)}$ known up to a normalising constant is an important and challenging problem in statistics. Recent years have seen the rise of a new family of amortised sampling algorithms, commonly referred to as diffusion samplers, that enable fast and efficient sampling from an unnormalised density. Such algorithms have been widely studied for continuous-space sampling tasks; however, their application to problems in discrete space remains largely unexplored. Although some progress has been made in this area, discrete diffusion samplers do not take full advantage of ideas commonly used for continuous-space sampling. In this paper, we propose to bridge this gap by introducing off-policy training techniques for discrete diffusion samplers. We show that these techniques improve the performance of discrete samplers on both established and new synthetic benchmarks. Next, we generalise discrete diffusion samplers to the task of bridging between two arbitrary distributions, introducing data-to-energy Schrödinger bridge training for the discrete domain for the first time. Lastly, we showcase the application of the proposed diffusion samplers to data-free posterior sampling in the discrete latent spaces of image generative models.

