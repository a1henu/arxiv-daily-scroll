---
layout: default
title: Infusion: Shaping Model Behavior by Editing Training Data via Influence Functions
---

# Infusion: Shaping Model Behavior by Editing Training Data via Influence Functions
**arXiv**：[2602.09987v1](https://arxiv.org/abs/2602.09987) · [PDF](https://arxiv.org/pdf/2602.09987.pdf)  
**作者**：J Rosser, Robert Kirk, Edward Grefenstette, Jakob Foerster, Laura Ruis  

**一句话要点**：提出Infusion框架，通过编辑训练数据以诱导模型行为，应用于数据投毒任务。

**关键词**：影响函数, 数据投毒, 训练数据编辑, 模型行为诱导, 跨架构迁移

## 3 点简述
- 核心问题：如何通过编辑训练数据来系统性地塑造模型行为，而非仅用影响函数解释行为。
- 方法要点：利用可扩展的影响函数近似计算训练文档的微小扰动，通过参数偏移诱导目标行为变化。
- 实验或效果：在CIFAR-10上，仅编辑0.2%训练数据即可与插入显式行为示例的基线竞争，且投毒效果可跨架构迁移。

## 摘要（原文）

> Influence functions are commonly used to attribute model behavior to training documents. We explore the reverse: crafting training data that induces model behavior. Our framework, Infusion, uses scalable influence-function approximations to compute small perturbations to training documents that induce targeted changes in model behavior through parameter shifts. We evaluate Infusion on data poisoning tasks across vision and language domains. On CIFAR-10, we show that making subtle edits via Infusion to just 0.2% (100/45,000) of the training documents can be competitive with the baseline of inserting a small number of explicit behavior examples. We also find that Infusion transfers across architectures (ResNet $\leftrightarrow$ CNN), suggesting a single poisoned corpus can affect multiple independently trained models. In preliminary language experiments, we characterize when our approach increases the probability of target behaviors and when it fails, finding it most effective at amplifying behaviors the model has already learned. Taken together, these results show that small, subtle edits to training data can systematically shape model behavior, underscoring the importance of training data interpretability for adversaries and defenders alike. We provide the code here: https://github.com/jrosseruk/infusion.

