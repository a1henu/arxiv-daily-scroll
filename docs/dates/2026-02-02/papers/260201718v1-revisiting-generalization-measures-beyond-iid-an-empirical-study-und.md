---
layout: default
title: Revisiting Generalization Measures Beyond IID: An Empirical Study under Distributional Shift
---

# Revisiting Generalization Measures Beyond IID: An Empirical Study under Distributional Shift
**arXiv**：[2602.01718v1](https://arxiv.org/abs/2602.01718) · [PDF](https://arxiv.org/pdf/2602.01718.pdf)  
**作者**：Sora Nakai, Youssef Fadhloun, Kacem Mathlouthi, Kotaro Yoshida, Ganesh Talluri, Ioannis Mitliagkas, Hiroki Naganuma  

**一句话要点**：在分布偏移下评估泛化度量的鲁棒性，扩展大规模实验范围

**关键词**：泛化度量, 分布偏移, 深度学习, 鲁棒性评估, 大规模实验

## 3 点简述
- 核心问题：深度学习泛化能力预测在非IID分布下不稳定，需评估度量鲁棒性。
- 方法要点：训练超万种配置模型，评估40多种基于训练数据和模型的泛化度量。
- 实验或效果：发现分布偏移显著影响多数度量预测性能，少数度量相对稳定。

## 摘要（原文）

> Generalization remains a central yet unresolved challenge in deep learning, particularly the ability to predict a model's performance beyond its training distribution using quantities available prior to test-time evaluation. Building on the large-scale study of Jiang et al. (2020). and concerns by Dziugaite et al. (2020). about instability across training configurations, we benchmark the robustness of generalization measures beyond IID regime. We train small-to-medium models over 10,000 hyperparameter configurations and evaluate more than 40 measures computable from the trained model and the available training data alone. We significantly broaden the experimental scope along multiple axes: (i) extending the evaluation beyond the standard IID setting to include benchmarking for robustness across diverse distribution shifts, (ii) evaluating multiple architectures and training recipes, and (iii) newly incorporating calibration- and information-criteria-based measures to assess their alignment with both IID and OOD generalization. We find that distribution shifts can substantially alter the predictive performance of many generalization measures, while a smaller subset remains comparatively stable across settings.

