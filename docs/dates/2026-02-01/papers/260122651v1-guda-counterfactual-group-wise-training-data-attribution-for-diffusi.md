---
layout: default
title: GUDA: Counterfactual Group-wise Training Data Attribution for Diffusion Models via Unlearning
---

# GUDA: Counterfactual Group-wise Training Data Attribution for Diffusion Models via Unlearning
**arXiv**：[2601.22651v1](https://arxiv.org/abs/2601.22651) · [PDF](https://arxiv.org/pdf/2601.22651.pdf)  
**作者**：Naoki Murata, Yuhta Takida, Chieh-Hsin Lai, Toshimitsu Uesaka, Bac Nguyen, Stefano Ermon, Yuki Mitsufuji  

**一句话要点**：提出GUDA方法，通过反学习实现扩散模型的组级训练数据归因，解决计算效率问题。

**关键词**：扩散模型, 训练数据归因, 反学习, 组级分析, 计算效率

## 3 点简述
- 核心问题：传统组级归因方法如LOGO重训练计算成本高，难以扩展。
- 方法要点：基于反学习近似反事实模型，利用ELBO差异量化组影响。
- 实验效果：在CIFAR-10和艺术风格归因中，GUDA比基线方法更可靠，速度提升百倍。

## 摘要（原文）

> Training-data attribution for vision generative models aims to identify which training data influenced a given output. While most methods score individual examples, practitioners often need group-level answers (e.g., artistic styles or object classes). Group-wise attribution is counterfactual: how would a model's behavior on a generated sample change if a group were absent from training? A natural realization of this counterfactual is Leave-One-Group-Out (LOGO) retraining, which retrains the model with each group removed; however, it becomes computationally prohibitive as the number of groups grows. We propose GUDA (Group Unlearning-based Data Attribution) for diffusion models, which approximates each counterfactual model by applying machine unlearning to a shared full-data model instead of training from scratch. GUDA quantifies group influence using differences in a likelihood-based scoring rule (ELBO) between the full model and each unlearned counterfactual. Experiments on CIFAR-10 and artistic style attribution with Stable Diffusion show that GUDA identifies primary contributing groups more reliably than semantic similarity, gradient-based attribution, and instance-level unlearning approaches, while achieving x100 speedup on CIFAR-10 over LOGO retraining.

