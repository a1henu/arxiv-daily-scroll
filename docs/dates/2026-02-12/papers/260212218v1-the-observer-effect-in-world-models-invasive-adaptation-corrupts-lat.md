---
layout: default
title: The Observer Effect in World Models: Invasive Adaptation Corrupts Latent Physics
---

# The Observer Effect in World Models: Invasive Adaptation Corrupts Latent Physics
**arXiv**：[2602.12218v1](https://arxiv.org/abs/2602.12218) · [PDF](https://arxiv.org/pdf/2602.12218.pdf)  
**作者**：Christian Internò, Jumpei Yamaguchi, Loren Amdahl-Culleton, Markus Olhofer, David Klindt, Barbara Hammer  

**一句话要点**：提出非侵入式评估协议PhyIP，以解决自适应评估在物理世界模型中的潜在结构混淆问题。

**关键词**：世界模型评估, 线性表示假设, 非侵入式协议, 物理世界模型, 自监督学习, OOD泛化

## 3 点简述
- 核心问题：自适应评估可能改变自监督学习表示，混淆物理世界模型的内在能力。
- 方法要点：基于线性表示假设，通过冻结表示线性解码物理量进行非侵入式评估。
- 实验或效果：在流体动力学和轨道力学中，PhyIP在OOD测试中恢复物理结构，而自适应评估导致结构崩溃。

## 摘要（原文）

> Determining whether neural models internalize physical laws as world models, rather than exploiting statistical shortcuts, remains challenging, especially under out-of-distribution (OOD) shifts. Standard evaluations often test latent capability via downstream adaptation (e.g., fine-tuning or high-capacity probes), but such interventions can change the representations being measured and thus confound what was learned during self-supervised learning (SSL). We propose a non-invasive evaluation protocol, PhyIP. We test whether physical quantities are linearly decodable from frozen representations, motivated by the linear representation hypothesis. Across fluid dynamics and orbital mechanics, we find that when SSL achieves low error, latent structure becomes linearly accessible. PhyIP recovers internal energy and Newtonian inverse-square scaling on OOD tests (e.g., $ρ> 0.90$). In contrast, adaptation-based evaluations can collapse this structure ($ρ\approx 0.05$). These findings suggest that adaptation-based evaluation can obscure latent structures and that low-capacity probes offer a more accurate evaluation of physical world models.

