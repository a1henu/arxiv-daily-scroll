---
layout: default
title: A Tilted Seesaw: Revisiting Autoencoder Trade-off for Controllable Diffusion
---

# A Tilted Seesaw: Revisiting Autoencoder Trade-off for Controllable Diffusion
**arXiv**：[2601.21633v1](https://arxiv.org/abs/2601.21633) · [PDF](https://arxiv.org/pdf/2601.21633.pdf)  
**作者**：Pu Cao, Yiyang Ma, Feng Zhou, Xuedan Yin, Qing Song, Lu Yang  

**一句话要点**：揭示自编码器评估偏差对可控扩散模型的影响，提供可靠基准指导

**关键词**：可控扩散模型, 自编码器评估, 条件漂移, 重建保真度, 基准测试, 生成对抗网络

## 3 点简述
- 核心问题：ImageNet规模自编码器评估偏向生成指标，忽视重建保真度，可能损害可控扩散中的条件对齐。
- 方法要点：理论分析条件漂移现象，提出多维度条件漂移评估协议，验证重建指标与可控性的强相关性。
- 实验或效果：通过ControlNet实验证实可控性依赖于条件保持而非生成指标，为模型选择提供实证依据。

## 摘要（原文）

> In latent diffusion models, the autoencoder (AE) is typically expected to balance two capabilities: faithful reconstruction and a generation-friendly latent space (e.g., low gFID). In recent ImageNet-scale AE studies, we observe a systematic bias toward generative metrics in handling this trade-off: reconstruction metrics are increasingly under-reported, and ablation-based AE selection often favors the best-gFID configuration even when reconstruction fidelity degrades. We theoretically analyze why this gFID-dominant preference can appear unproblematic for ImageNet generation, yet becomes risky when scaling to controllable diffusion: AEs can induce condition drift, which limits achievable condition alignment. Meanwhile, we find that reconstruction fidelity, especially instance-level measures, better indicates controllability. We empirically validate the impact of tilted autoencoder evaluation on controllability by studying several recent ImageNet AEs. Using a multi-dimensional condition-drift evaluation protocol reflecting controllable generation tasks, we find that gFID is only weakly predictive of condition preservation, whereas reconstruction-oriented metrics are substantially more aligned. ControlNet experiments further confirm that controllability tracks condition preservation rather than gFID. Overall, our results expose a gap between ImageNet-centric AE evaluation and the requirements of scalable controllable diffusion, offering practical guidance for more reliable benchmarking and model selection.

