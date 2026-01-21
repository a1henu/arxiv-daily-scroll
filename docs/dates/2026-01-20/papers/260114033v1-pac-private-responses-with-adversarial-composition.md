---
layout: default
title: PAC-Private Responses with Adversarial Composition
---

# PAC-Private Responses with Adversarial Composition
**arXiv**：[2601.14033v1](https://arxiv.org/abs/2601.14033) · [PDF](https://arxiv.org/pdf/2601.14033.pdf)  
**作者**：Xiaochen Zhu, Mayuri Sridhar, Srinivas Devadas  

**一句话要点**：提出基于PAC隐私的对抗性查询响应算法，以保护API部署模型输出隐私。

**关键词**：PAC隐私, 对抗性查询组合, 互信息控制, 自适应噪声校准, 模型输出隐私, 蒸馏训练

## 3 点简述
- 核心问题：模型API部署中，标准权重隐私方法噪声过大，需直接保护输出隐私并应对对抗性查询组合。
- 方法要点：利用PAC隐私控制互信息，通过自适应噪声校准实现对抗性查询下的线性隐私保证累积。
- 实验或效果：在CIFAR-10等任务上，以极低隐私预算实现高精度，并支持蒸馏可发布隐私保护模型。

## 摘要（原文）

> Modern machine learning models are increasingly deployed behind APIs. This renders standard weight-privatization methods (e.g. DP-SGD) unnecessarily noisy at the cost of utility. While model weights may vary significantly across training datasets, model responses to specific inputs are much lower dimensional and more stable. This motivates enforcing privacy guarantees directly on model outputs.
>   We approach this under PAC privacy, which provides instance-based privacy guarantees for arbitrary black-box functions by controlling mutual information (MI). Importantly, PAC privacy explicitly rewards output stability with reduced noise levels. However, a central challenge remains: response privacy requires composing a large number of adaptively chosen, potentially adversarial queries issued by untrusted users, where existing composition results on PAC privacy are inadequate. We introduce a new algorithm that achieves adversarial composition via adaptive noise calibration and prove that mutual information guarantees accumulate linearly under adaptive and adversarial querying.
>   Experiments across tabular, vision, and NLP tasks show that our method achieves high utility at extremely small per-query privacy budgets. On CIFAR-10, we achieve 87.79% accuracy with a per-step MI budget of $2^{-32}$. This enables serving one million queries while provably bounding membership inference attack (MIA) success rates to 51.08% -- the same guarantee of $(0.04, 10^{-5})$-DP. Furthermore, we show that private responses can be used to label public data to distill a publishable privacy-preserving model; using an ImageNet subset as a public dataset, our model distilled from 210,000 responses achieves 91.86% accuracy on CIFAR-10 with MIA success upper-bounded by 50.49%, which is comparable to $(0.02,10^{-5})$-DP.

