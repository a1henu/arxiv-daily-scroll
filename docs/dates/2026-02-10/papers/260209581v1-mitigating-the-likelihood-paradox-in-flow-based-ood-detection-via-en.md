---
layout: default
title: Mitigating the Likelihood Paradox in Flow-based OOD Detection via Entropy Manipulation
---

# Mitigating the Likelihood Paradox in Flow-based OOD Detection via Entropy Manipulation
**arXiv**：[2602.09581v1](https://arxiv.org/abs/2602.09581) · [PDF](https://arxiv.org/pdf/2602.09581.pdf)  
**作者**：Donghwan Kim, Hyunsoo Yoon  

**一句话要点**：提出基于熵操纵的方法以缓解流模型在分布外检测中的似然悖论

**关键词**：流模型, 分布外检测, 似然悖论, 熵操纵, 语义相似性, 无额外训练

## 3 点简述
- 核心问题：流模型等生成模型常对分布外输入分配过高似然，导致检测失效
- 方法要点：基于语义相似性操纵输入熵，对相似度低的输入施加更强扰动
- 实验或效果：在标准基准上实现AUROC一致提升，优于基于似然的基线方法

## 摘要（原文）

> Deep generative models that can tractably compute input likelihoods, including normalizing flows, often assign unexpectedly high likelihoods to out-of-distribution (OOD) inputs. We mitigate this likelihood paradox by manipulating input entropy based on semantic similarity, applying stronger perturbations to inputs that are less similar to an in-distribution memory bank. We provide a theoretical analysis showing that entropy control increases the expected log-likelihood gap between in-distribution and OOD samples in favor of the in-distribution, and we explain why the procedure works without any additional training of the density model. We then evaluate our method against likelihood-based OOD detectors on standard benchmarks and find consistent AUROC improvements over baselines, supporting our explanation.

