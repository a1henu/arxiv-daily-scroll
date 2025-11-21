---
layout: default
title: FT-NCFM: An Influence-Aware Data Distillation Framework for Efficient VLA Models
---

# FT-NCFM: An Influence-Aware Data Distillation Framework for Efficient VLA Models
**arXiv**：[2511.16233v1](https://arxiv.org/abs/2511.16233) · [PDF](https://arxiv.org/pdf/2511.16233.pdf)  
**作者**：Kewei Chen, Yayu Long, Shuai Li, Mingsheng Shang  

**一句话要点**：提出FT-NCFM数据蒸馏框架以解决VLA模型数据冗余问题

**关键词**：视觉语言动作模型, 数据蒸馏, 因果归因, 模型无关数据, 训练效率, 核心集优化

## 3 点简述
- 核心问题：VLA模型依赖大规模冗余数据，阻碍广泛应用
- 方法要点：结合因果归因和程序化对比验证，合成信息密集数据
- 实验效果：用5%蒸馏数据训练，成功率85-90%，训练时间减少80%

## 摘要（原文）

> The powerful generalization of Vision-Language-Action (VLA) models is bottlenecked by their heavy reliance on massive, redundant, and unevenly valued datasets, hindering their widespread application. Existing model-centric optimization paths, such as model compression (which often leads to performance degradation) or policy distillation (whose products are model-dependent and lack generality), fail to fundamentally address this data-level challenge. To this end, this paper introduces FT-NCFM, a fundamentally different, data-centric generative data distillation framework. Our framework employs a self-contained Fact-Tracing (FT) engine that combines causal attribution with programmatic contrastive verification to assess the intrinsic value of samples. Guided by these assessments, an adversarial NCFM process synthesizes a model-agnostic, information-dense, and reusable data asset. Experimental results on several mainstream VLA benchmarks show that models trained on just 5% of our distilled coreset achieve a success rate of 85-90% compared with training on the full dataset, while reducing training time by over 80%. Our work demonstrates that intelligent data distillation is a highly promising new path for building efficient, high-performance VLA models.

