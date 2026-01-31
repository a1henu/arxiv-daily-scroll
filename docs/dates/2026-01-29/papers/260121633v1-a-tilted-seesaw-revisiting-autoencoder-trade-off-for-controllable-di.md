---
layout: default
title: A Tilted Seesaw: Revisiting Autoencoder Trade-off for Controllable Diffusion
---

# A Tilted Seesaw: Revisiting Autoencoder Trade-off for Controllable Diffusion
**arXiv**：[2601.21633v1](https://arxiv.org/abs/2601.21633) · [PDF](https://arxiv.org/pdf/2601.21633.pdf)  
**作者**：Pu Cao, Yiyang Ma, Feng Zhou, Xuedan Yin, Qing Song, Lu Yang  

**一句话要点**：揭示自编码器评估偏差对可控扩散模型的影响，提出基于重建保真度的可靠基准方法

**关键词**：可控扩散模型, 自编码器评估, 条件漂移, 重建保真度, 基准方法, 生成对抗网络

## 3 点简述
- 核心问题：ImageNet规模自编码器评估偏向生成指标，忽视重建保真度，导致可控扩散中条件漂移风险
- 方法要点：理论分析条件漂移机制，提出多维度条件保持评估协议，强调实例级重建指标的重要性
- 实验或效果：实证验证重建指标与可控性对齐，ControlNet实验确认条件保持优于gFID预测

## 摘要（原文）

> In latent diffusion models, the autoencoder (AE) is typically expected to balance two capabilities: faithful reconstruction and a generation-friendly latent space (e.g., low gFID). In recent ImageNet-scale AE studies, we observe a systematic bias toward generative metrics in handling this trade-off: reconstruction metrics are increasingly under-reported, and ablation-based AE selection often favors the best-gFID configuration even when reconstruction fidelity degrades. We theoretically analyze why this gFID-dominant preference can appear unproblematic for ImageNet generation, yet becomes risky when scaling to controllable diffusion: AEs can induce condition drift, which limits achievable condition alignment. Meanwhile, we find that reconstruction fidelity, especially instance-level measures, better indicates controllability. We empirically validate the impact of tilted autoencoder evaluation on controllability by studying several recent ImageNet AEs. Using a multi-dimensional condition-drift evaluation protocol reflecting controllable generation tasks, we find that gFID is only weakly predictive of condition preservation, whereas reconstruction-oriented metrics are substantially more aligned. ControlNet experiments further confirm that controllability tracks condition preservation rather than gFID. Overall, our results expose a gap between ImageNet-centric AE evaluation and the requirements of scalable controllable diffusion, offering practical guidance for more reliable benchmarking and model selection.

