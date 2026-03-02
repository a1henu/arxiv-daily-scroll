---
layout: default
title: MPU: Towards Secure and Privacy-Preserving Knowledge Unlearning for Large Language Models
---

# MPU: Towards Secure and Privacy-Preserving Knowledge Unlearning for Large Language Models
**arXiv**：[2602.23798v1](https://arxiv.org/abs/2602.23798) · [PDF](https://arxiv.org/pdf/2602.23798.pdf)  
**作者**：Tiantong Wang, Xinyu Yan, Tiantong Wu, Yurong Hao, Yong Jiang, Fei Huang, Wei Yang Bryan Lim  

**一句话要点**：提出MPU框架以解决大语言模型知识遗忘中的双重隐私约束问题

**关键词**：知识遗忘, 隐私保护, 大语言模型, 扰动副本, 本地计算, 聚合更新

## 3 点简述
- 核心问题：大语言模型知识遗忘面临服务器参数与客户端遗忘集均不可共享的双重隐私约束
- 方法要点：通过服务器端生成随机扰动副本，客户端本地执行遗忘，服务器聚合更新以减轻扰动影响
- 实验或效果：在七种遗忘算法上，MPU在10%噪声下性能退化低于1%，部分算法在1%噪声下优于无噪声基线

## 摘要（原文）

> Machine unlearning for large language models often faces a privacy dilemma in which strict constraints prohibit sharing either the server's parameters or the client's forget set. To address this dual non-disclosure constraint, we propose MPU, an algorithm-agnostic privacy-preserving Multiple Perturbed Copies Unlearning framework that primarily introduces two server-side modules: Pre-Process for randomized copy generation and Post-Process for update aggregation. In Pre-Process, the server distributes multiple perturbed and reparameterized model instances, allowing the client to execute unlearning locally on its private forget set without accessing the server's exact original parameters. After local unlearning, the server performs Post-Process by inverting the reparameterization and aggregating updates with a harmonic denoising procedure to alleviate the impact of perturbation. Experiments with seven unlearning algorithms show that MPU achieves comparable unlearning performance to noise-free baselines, with most algorithms' average degradation well below 1% under 10% noise, and can even outperform the noise-free baseline for some algorithms under 1% noise. Code is available at https://github.com/Tristan-SHU/MPU.

