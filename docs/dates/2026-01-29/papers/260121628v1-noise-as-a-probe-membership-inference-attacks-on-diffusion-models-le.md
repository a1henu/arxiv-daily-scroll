---
layout: default
title: Noise as a Probe: Membership Inference Attacks on Diffusion Models Leveraging Initial Noise
---

# Noise as a Probe: Membership Inference Attacks on Diffusion Models Leveraging Initial Noise
**arXiv**：[2601.21628v1](https://arxiv.org/abs/2601.21628) · [PDF](https://arxiv.org/pdf/2601.21628.pdf)  
**作者**：Puwei Lian, Yujun Cai, Songze Li, Bingkun Bao  

**一句话要点**：提出基于初始噪声语义注入的成员推断攻击，揭示扩散模型隐私漏洞

**关键词**：扩散模型, 成员推断攻击, 隐私安全, 噪声调度, 语义残留, 微调模型

## 3 点简述
- 核心问题：扩散模型在微调后易受成员推断攻击，现有方法依赖中间结果或辅助数据集
- 方法要点：利用噪声调度残留语义信息，通过初始噪声注入语义并分析生成结果推断成员关系
- 实验或效果：实验表明语义初始噪声能有效揭示成员信息，突显扩散模型隐私脆弱性

## 摘要（原文）

> Diffusion models have achieved remarkable progress in image generation, but their increasing deployment raises serious concerns about privacy. In particular, fine-tuned models are highly vulnerable, as they are often fine-tuned on small and private datasets. Membership inference attacks (MIAs) are used to assess privacy risks by determining whether a specific sample was part of a model's training data. Existing MIAs against diffusion models either assume obtaining the intermediate results or require auxiliary datasets for training the shadow model. In this work, we utilized a critical yet overlooked vulnerability: the widely used noise schedules fail to fully eliminate semantic information in the images, resulting in residual semantic signals even at the maximum noise step. We empirically demonstrate that the fine-tuned diffusion model captures hidden correlations between the residual semantics in initial noise and the original images. Building on this insight, we propose a simple yet effective membership inference attack, which injects semantic information into the initial noise and infers membership by analyzing the model's generation result. Extensive experiments demonstrate that the semantic initial noise can strongly reveal membership information, highlighting the vulnerability of diffusion models to MIAs.

