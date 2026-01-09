---
layout: default
title: Measurement-Consistent Langevin Corrector: A Remedy for Latent Diffusion Inverse Solvers
---

# Measurement-Consistent Langevin Corrector: A Remedy for Latent Diffusion Inverse Solvers
**arXiv**：[2601.04791v1](https://arxiv.org/abs/2601.04791) · [PDF](https://arxiv.org/pdf/2601.04791.pdf)  
**作者**：Lee Hyoseok, Sohwi Lim, Eunju Cha, Tae-Hyun Oh  

**一句话要点**：提出测量一致朗格文校正器以稳定潜在扩散逆求解器

**关键词**：潜在扩散模型, 逆问题求解, 朗格文动力学, 图像恢复, 零样本学习

## 3 点简述
- 核心问题：现有潜在扩散逆求解器不稳定，产生伪影和质量下降。
- 方法要点：引入理论基础的即插即用校正模块，通过测量一致朗格文更新减少动态差异。
- 实验或效果：在多样图像恢复任务中验证有效性，并与现有求解器兼容。

## 摘要（原文）

> With recent advances in generative models, diffusion models have emerged as powerful priors for solving inverse problems in each domain. Since Latent Diffusion Models (LDMs) provide generic priors, several studies have explored their potential as domain-agnostic zero-shot inverse solvers. Despite these efforts, existing latent diffusion inverse solvers suffer from their instability, exhibiting undesirable artifacts and degraded quality. In this work, we first identify the instability as a discrepancy between the solver's and true reverse diffusion dynamics, and show that reducing this gap stabilizes the solver. Building on this, we introduce Measurement-Consistent Langevin Corrector (MCLC), a theoretically grounded plug-and-play correction module that remedies the LDM-based inverse solvers through measurement-consistent Langevin updates. Compared to prior approaches that rely on linear manifold assumptions, which often do not hold in latent space, MCLC operates without this assumption, leading to more stable and reliable behavior. We experimentally demonstrate the effectiveness of MCLC and its compatibility with existing solvers across diverse image restoration tasks. Additionally, we analyze blob artifacts and offer insights into their underlying causes. We highlight that MCLC is a key step toward more robust zero-shot inverse problem solvers.

