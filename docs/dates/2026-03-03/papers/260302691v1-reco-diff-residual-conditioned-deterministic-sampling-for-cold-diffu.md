---
layout: default
title: ReCo-Diff: Residual-Conditioned Deterministic Sampling for Cold Diffusion in Sparse-View CT
---

# ReCo-Diff: Residual-Conditioned Deterministic Sampling for Cold Diffusion in Sparse-View CT
**arXiv**：[2603.02691v1](https://arxiv.org/abs/2603.02691) · [PDF](https://arxiv.org/pdf/2603.02691.pdf)  
**作者**：Yong Eun Choi, Hyoung Suk Park, Kiwan Jeon, Hyun-Cheol Park, Sung Ho Kang  

**一句话要点**：提出ReCo-Diff框架，通过残差条件化采样提升稀疏视图CT重建的准确性与稳定性。

**关键词**：稀疏视图CT重建, 冷扩散模型, 残差条件化采样, 确定性采样, 图像重建, 医学成像

## 3 点简述
- 现有冷扩散采样策略依赖启发式控制，易受误差累积影响，导致重建不稳定。
- ReCo-Diff利用观测残差进行自引导采样，在确定性采样中实现连续测量感知校正。
- 实验表明，该方法在严重稀疏条件下优于基线，提高了重建精度和鲁棒性。

## 摘要（原文）

> Cold and generalized diffusion models have recently shown strong potential for sparse-view CT reconstruction by explicitly modeling deterministic degradation processes. However, existing sampling strategies often rely on ad hoc sampling controls or fixed schedules, which remain sensitive to error accumulation and sampling instability. We propose ReCo-Diff, a residual-conditioned diffusion framework that leverages observation residuals through residual-conditioned self-guided sampling. At each sampling step, ReCo-Diff first produces a null (unconditioned) baseline reconstruction and then conditions subsequent predictions on the observation residual between the predicted image and the measured sparse-view input. This residual-driven guidance provides continuous, measurement-aware correction while preserving a deterministic sampling schedule, without requiring heuristic interventions. Experimental results demonstrate that ReCo-Diff consistently outperforms existing cold diffusion sampling baselines, achieving higher reconstruction accuracy, improved stability, and enhanced robustness under severe sparsity.

