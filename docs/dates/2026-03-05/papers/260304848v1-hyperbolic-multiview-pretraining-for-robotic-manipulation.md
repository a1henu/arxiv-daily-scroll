---
layout: default
title: Hyperbolic Multiview Pretraining for Robotic Manipulation
---

# Hyperbolic Multiview Pretraining for Robotic Manipulation
**arXiv**：[2603.04848v1](https://arxiv.org/abs/2603.04848) · [PDF](https://arxiv.org/pdf/2603.04848.pdf)  
**作者**：Jin Yang, Ping Wei, Yixin Chen  

**一句话要点**：提出HyperMVP框架，通过双曲多视图预训练提升机器人操作任务的鲁棒性。

**关键词**：双曲空间学习, 多视图预训练, 机器人操作, 3D感知, 自监督学习

## 3 点简述
- 现有方法局限于欧几里得嵌入空间，难以建模结构关系，影响机器人空间感知。
- 扩展掩码自编码器范式，设计GeoLink编码器学习多视图双曲表示，并引入3D-MOV数据集支持预训练。
- 在COLOSSEUM、RLBench和真实场景中评估，HyperMVP在多种任务和扰动设置下优于基线方法。

## 摘要（原文）

> 3D-aware visual pretraining has proven effective in improving the performance of downstream robotic manipulation tasks. However, existing methods are constrained to Euclidean embedding spaces, whose flat geometry limits their ability to model structural relations among embeddings. As a result, they struggle to learn structured embeddings that are essential for robust spatial perception in robotic applications. To this end, we propose HyperMVP, a self-supervised framework for \underline{Hyper}bolic \underline{M}ulti\underline{V}iew \underline{P}retraining. Hyperbolic space offers geometric properties well suited for capturing structural relations. Methodologically, we extend the masked autoencoder paradigm and design a GeoLink encoder to learn multiview hyperbolic representations. The pretrained encoder is then finetuned with visuomotor policies on manipulation tasks. In addition, we introduce 3D-MOV, a large-scale dataset comprising multiple types of 3D point clouds to support pretraining. We evaluate HyperMVP on COLOSSEUM, RLBench, and real-world scenarios, where it consistently outperforms strong baselines across diverse tasks and perturbation settings. Our results highlight the potential of 3D-aware pretraining in a non-Euclidean space for learning robust and generalizable robotic manipulation policies.

