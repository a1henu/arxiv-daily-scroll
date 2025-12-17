---
layout: default
title: Improving the Accuracy of Amortized Model Comparison with Self-Consistency
---

# Improving the Accuracy of Amortized Model Comparison with Self-Consistency
**arXiv**：[2512.14308v1](https://arxiv.org/abs/2512.14308) · [PDF](https://arxiv.org/pdf/2512.14308.pdf)  
**作者**：Šimon Kucharský, Aayush Mishra, Daniel Habermann, Stefan T. Radev, Paul-Christian Bürkner  

**一句话要点**：提出自洽性训练以提升模型误设下摊销贝叶斯模型比较的准确性

**关键词**：摊销贝叶斯推断, 模型比较, 自洽性训练, 模型误设, 参数后验

## 3 点简述
- 核心问题：摊销贝叶斯推断在模型误设时因训练分布外数据导致神经代理行为不可预测
- 方法要点：利用自洽性训练增强基于参数后验的模型比较方法，提高鲁棒性
- 实验或效果：在合成和真实案例中，参数后验方法优于直接近似证据的方法，自洽性训练在似然可用时显著改善性能

## 摘要（原文）

> Amortized Bayesian inference (ABI) offers fast, scalable approximations to posterior densities by training neural surrogates on data simulated from the statistical model. However, ABI methods are highly sensitive to model misspecification: when observed data fall outside the training distribution (generative scope of the statistical models), neural surrogates can behave unpredictably. This makes it a challenge in a model comparison setting, where multiple statistical models are considered, of which at least some are misspecified. Recent work on self-consistency (SC) provides a promising remedy to this issue, accessible even for empirical data (without ground-truth labels). In this work, we investigate how SC can improve amortized model comparison conceptualized in four different ways. Across two synthetic and two real-world case studies, we find that approaches for model comparison that estimate marginal likelihoods through approximate parameter posteriors consistently outperform methods that directly approximate model evidence or posterior model probabilities. SC training improves robustness when the likelihood is available, even under severe model misspecification. The benefits of SC for methods without access of analytic likelihoods are more limited and inconsistent. Our results suggest practical guidance for reliable amortized Bayesian model comparison: prefer parameter posterior-based methods and augment them with SC training on empirical datasets to mitigate extrapolation bias under model misspecification.

