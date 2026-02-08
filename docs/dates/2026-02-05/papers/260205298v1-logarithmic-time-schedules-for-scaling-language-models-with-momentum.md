---
layout: default
title: Logarithmic-time Schedules for Scaling Language Models with Momentum
---

# Logarithmic-time Schedules for Scaling Language Models with Momentum
**arXiv**：[2602.05298v1](https://arxiv.org/abs/2602.05298) · [PDF](https://arxiv.org/pdf/2602.05298.pdf)  
**作者**：Damien Ferbach, Courtney Paquette, Gauthier Gidel, Katie Everett, Elliot Paquette  

**一句话要点**：提出ADANA优化器，通过对数时间调度提升大规模语言模型训练效率。

**关键词**：优化器设计, 对数时间调度, 大规模语言模型训练, AdamW变体, 计算效率提升, 超参数调度

## 3 点简述
- 核心问题：AdamW优化器中超参数固定是否最优，针对语言数据幂律结构探索变体。
- 方法要点：设计对数时间调度，结合阻尼机制平衡稳定性和长记忆优势，实现ADANA优化器。
- 实验或效果：在45M至2.6B参数规模上，ADANA相比AdamW提升计算效率达40%，且随规模增大增益增强。

## 摘要（原文）

> In practice, the hyperparameters $(β_1, β_2)$ and weight-decay $λ$ in AdamW are typically kept at fixed values. Is there any reason to do otherwise? We show that for large-scale language model training, the answer is yes: by exploiting the power-law structure of language data, one can design time-varying schedules for $(β_1, β_2, λ)$ that deliver substantial performance gains.
>   We study logarithmic-time scheduling, in which the optimizer's gradient memory horizon grows with training time. Although naive variants of this are unstable, we show that suitable damping mechanisms restore stability while preserving the benefits of longer memory. Based on this, we present ADANA, an AdamW-like optimizer that couples log-time schedules with explicit damping to balance stability and performance. We empirically evaluate ADANA across transformer scalings (45M to 2.6B parameters), comparing against AdamW, Muon, and AdEMAMix.
>   When properly tuned, ADANA achieves up to 40% compute efficiency relative to a tuned AdamW, with gains that persist--and even improve--as model scale increases. We further show that similar benefits arise when applying logarithmic-time scheduling to AdEMAMix, and that logarithmic-time weight-decay alone can yield significant improvements. Finally, we present variants of ADANA that mitigate potential failure modes and improve robustness.

