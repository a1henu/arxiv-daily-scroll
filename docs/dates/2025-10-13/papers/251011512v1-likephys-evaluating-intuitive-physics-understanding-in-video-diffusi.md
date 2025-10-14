---
layout: default
title: LikePhys: Evaluating Intuitive Physics Understanding in Video Diffusion Models via Likelihood Preference
---

# LikePhys: Evaluating Intuitive Physics Understanding in Video Diffusion Models via Likelihood Preference
**arXiv**：[2510.11512v1](https://arxiv.org/abs/2510.11512) · [PDF](https://arxiv.org/pdf/2510.11512.pdf)  
**作者**：Jianhao Yuan, Fabio Pizzati, Francesco Pinto, Lars Kunze, Ivan Laptev, Paul Newman, Philip Torr, Daniele De Martini  

**一句话要点**：提出LikePhys方法以评估视频扩散模型的直观物理理解能力

**关键词**：直观物理理解, 视频扩散模型, 似然评估, 物理基准, 训练免费方法

## 3 点简述
- 核心问题：难以在生成中分离物理正确性与视觉外观，导致评估困难
- 方法要点：使用去噪目标作为ELBO似然代理，区分物理有效与不可能视频
- 实验或效果：在12个场景基准上，PPE指标与人类偏好强对齐，优于基线

## 摘要（原文）

> Intuitive physics understanding in video diffusion models plays an essential
> role in building general-purpose physically plausible world simulators, yet
> accurately evaluating such capacity remains a challenging task due to the
> difficulty in disentangling physics correctness from visual appearance in
> generation. To the end, we introduce LikePhys, a training-free method that
> evaluates intuitive physics in video diffusion models by distinguishing
> physically valid and impossible videos using the denoising objective as an
> ELBO-based likelihood surrogate on a curated dataset of valid-invalid pairs. By
> testing on our constructed benchmark of twelve scenarios spanning over four
> physics domains, we show that our evaluation metric, Plausibility Preference
> Error (PPE), demonstrates strong alignment with human preference, outperforming
> state-of-the-art evaluator baselines. We then systematically benchmark
> intuitive physics understanding in current video diffusion models. Our study
> further analyses how model design and inference settings affect intuitive
> physics understanding and highlights domain-specific capacity variations across
> physical laws. Empirical results show that, despite current models struggling
> with complex and chaotic dynamics, there is a clear trend of improvement in
> physics understanding as model capacity and inference settings scale.

