---
layout: default
title: Tortoise and Hare Guidance: Accelerating Diffusion Model Inference with Multirate Integration
---

# Tortoise and Hare Guidance: Accelerating Diffusion Model Inference with Multirate Integration
**arXiv**：[2511.04117v1](https://arxiv.org/abs/2511.04117) · [PDF](https://arxiv.org/pdf/2511.04117.pdf)  
**作者**：Yunghee Lee, Byeonghyun Pak, Junwha Hong, Hoseong Kim  

**一句话要点**：提出Tortoise and Hare Guidance以加速扩散模型推理并保持高保真生成

**关键词**：扩散模型, 推理加速, 多速率积分, 分类器自由引导, 训练免费方法, 图像生成

## 3 点简述
- 核心问题：扩散模型推理速度慢，传统求解器未充分利用额外引导项的冗余
- 方法要点：将CFG ODE重构为多速率系统，分别用细/粗网格积分噪声估计和额外引导
- 实验或效果：减少函数评估次数达30%，生成保真度损失极小，优于现有训练免费加速器

## 摘要（原文）

> In this paper, we propose Tortoise and Hare Guidance (THG), a training-free
> strategy that accelerates diffusion sampling while maintaining high-fidelity
> generation. We demonstrate that the noise estimate and the additional guidance
> term exhibit markedly different sensitivity to numerical error by reformulating
> the classifier-free guidance (CFG) ODE as a multirate system of ODEs. Our
> error-bound analysis shows that the additional guidance branch is more robust
> to approximation, revealing substantial redundancy that conventional solvers
> fail to exploit. Building on this insight, THG significantly reduces the
> computation of the additional guidance: the noise estimate is integrated with
> the tortoise equation on the original, fine-grained timestep grid, while the
> additional guidance is integrated with the hare equation only on a coarse grid.
> We also introduce (i) an error-bound-aware timestep sampler that adaptively
> selects step sizes and (ii) a guidance-scale scheduler that stabilizes large
> extrapolation spans. THG reduces the number of function evaluations (NFE) by up
> to 30% with virtually no loss in generation fidelity ($\Delta$ImageReward
> $\leq$ 0.032) and outperforms state-of-the-art CFG-based training-free
> accelerators under identical computation budgets. Our findings highlight the
> potential of multirate formulations for diffusion solvers, paving the way for
> real-time high-quality image synthesis without any model retraining. The source
> code is available at https://github.com/yhlee-add/THG.

