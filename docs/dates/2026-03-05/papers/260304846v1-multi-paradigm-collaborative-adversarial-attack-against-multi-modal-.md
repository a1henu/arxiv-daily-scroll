---
layout: default
title: Multi-Paradigm Collaborative Adversarial Attack Against Multi-Modal Large Language Models
---

# Multi-Paradigm Collaborative Adversarial Attack Against Multi-Modal Large Language Models
**arXiv**：[2603.04846v1](https://arxiv.org/abs/2603.04846) · [PDF](https://arxiv.org/pdf/2603.04846.pdf)  
**作者**：Yuanbo Li, Tianyang Xu, Cong Hu, Tao Zhou, Xiao-Jun Wu, Josef Kittler  

**一句话要点**：提出多范式协同攻击框架以增强对抗样本对多模态大语言模型的迁移性

**关键词**：多模态大语言模型, 对抗攻击, 迁移性, 多范式协同优化, 特征聚合

## 3 点简述
- 现有攻击依赖单范式代理模型，特征表示受限，影响对抗扰动多样性。
- MPCAttack聚合视觉与语言语义表示，通过多范式协同优化策略进行联合对抗优化。
- 实验表明，MPCAttack在开源和闭源MLLMs的有目标与无目标攻击中均优于现有方法。

## 摘要（原文）

> The rapid progress of Multi-Modal Large Language Models (MLLMs) has significantly advanced downstream applications. However, this progress also exposes serious transferable adversarial vulnerabilities. In general, existing adversarial attacks against MLLMs typically rely on surrogate models trained within a single learning paradigm and perform independent optimisation in their respective feature spaces. This straightforward setting naturally restricts the richness of feature representations, delivering limits on the search space and thus impeding the diversity of adversarial perturbations. To address this, we propose a novel Multi-Paradigm Collaborative Attack (MPCAttack) framework to boost the transferability of adversarial examples against MLLMs. In principle, MPCAttack aggregates semantic representations, from both visual images and language texts, to facilitate joint adversarial optimisation on the aggregated features through a Multi-Paradigm Collaborative Optimisation (MPCO) strategy. By performing contrastive matching on multi-paradigm features, MPCO adaptively balances the importance of different paradigm representations and guides the global perturbation optimisation, effectively alleviating the representation bias. Extensive experimental results on multiple benchmarks demonstrate the superiority of MPCAttack, indicating that our solution consistently outperforms state-of-the-art methods in both targeted and untargeted attacks on open-source and closed-source MLLMs. The code is released at https://github.com/LiYuanBoJNU/MPCAttack.

