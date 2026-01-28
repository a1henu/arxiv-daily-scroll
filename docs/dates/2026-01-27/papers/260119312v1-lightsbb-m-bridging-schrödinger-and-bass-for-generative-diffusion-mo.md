---
layout: default
title: LightSBB-M: Bridging Schrödinger and Bass for Generative Diffusion Modeling
---

# LightSBB-M: Bridging Schrödinger and Bass for Generative Diffusion Modeling
**arXiv**：[2601.19312v1](https://arxiv.org/abs/2601.19312) · [PDF](https://arxiv.org/pdf/2601.19312.pdf)  
**作者**：Alexandre Alouadi, Pierre Henry-Labordère, Grégoire Loeper, Othmane Mazhar, Huyên Pham, Nizar Touzi  

**一句话要点**：提出LightSBB-M算法以高效求解Schrödinger-Bass桥问题，提升生成扩散模型性能。

**关键词**：Schrödinger桥, 扩散模型, 最优传输, 生成建模, 图像翻译, Wasserstein距离

## 3 点简述
- 核心问题：Schrödinger-Bass桥联合控制漂移和波动，是经典Schrödinger桥的扩展，但求解复杂。
- 方法要点：利用SBB目标的对偶表示，解析最优漂移和波动，引入可调参数beta在漂移和波动间插值。
- 实验或效果：在合成数据集上2-Wasserstein距离降低达32%，并在图像翻译任务中展示生成能力。

## 摘要（原文）

> The Schrodinger Bridge and Bass (SBB) formulation, which jointly controls drift and volatility, is an established extension of the classical Schrodinger Bridge (SB). Building on this framework, we introduce LightSBB-M, an algorithm that computes the optimal SBB transport plan in only a few iterations. The method exploits a dual representation of the SBB objective to obtain analytic expressions for the optimal drift and volatility, and it incorporates a tunable parameter beta greater than zero that interpolates between pure drift (the Schrodinger Bridge) and pure volatility (Bass martingale transport). We show that LightSBB-M achieves the lowest 2-Wasserstein distance on synthetic datasets against state-of-the-art SB and diffusion baselines with up to 32 percent improvement. We also illustrate the generative capability of the framework on an unpaired image-to-image translation task (adult to child faces in FFHQ). These findings demonstrate that LightSBB-M provides a scalable, high-fidelity SBB solver that outperforms existing SB and diffusion baselines across both synthetic and real-world generative tasks. The code is available at https://github.com/alexouadi/LightSBB-M.

