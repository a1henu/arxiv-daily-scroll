---
layout: default
title: One Hand to Rule Them All: Canonical Representations for Unified Dexterous Manipulation
---

# One Hand to Rule Them All: Canonical Representations for Unified Dexterous Manipulation
**arXiv**：[2602.16712v1](https://arxiv.org/abs/2602.16712) · [PDF](https://arxiv.org/pdf/2602.16712.pdf)  
**作者**：Zhenyu Wei, Yunchao Yao, Mingyu Ding  

**一句话要点**：提出参数化规范表示以统一灵巧手架构，实现跨手零样本泛化

**关键词**：灵巧手操作, 规范表示, 跨手泛化, 参数化建模, 零样本学习, URDF标准化

## 3 点简述
- 问题：现有灵巧手策略固定手设计，难以泛化到不同形态和结构的手。
- 方法：引入参数化规范表示，包括统一参数空间和规范URDF格式，支持条件学习和动作空间标准化。
- 效果：通过VAE编码和跨手零样本转移实验，如在三指LEAP手上达到81.9%成功率，验证了框架的有效性。

## 摘要（原文）

> Dexterous manipulation policies today largely assume fixed hand designs, severely restricting their generalization to new embodiments with varied kinematic and structural layouts. To overcome this limitation, we introduce a parameterized canonical representation that unifies a broad spectrum of dexterous hand architectures. It comprises a unified parameter space and a canonical URDF format, offering three key advantages. 1) The parameter space captures essential morphological and kinematic variations for effective conditioning in learning algorithms. 2) A structured latent manifold can be learned over our space, where interpolations between embodiments yield smooth and physically meaningful morphology transitions. 3) The canonical URDF standardizes the action space while preserving dynamic and functional properties of the original URDFs, enabling efficient and reliable cross-embodiment policy learning. We validate these advantages through extensive analysis and experiments, including grasp policy replay, VAE latent encoding, and cross-embodiment zero-shot transfer. Specifically, we train a VAE on the unified representation to obtain a compact, semantically rich latent embedding, and develop a grasping policy conditioned on the canonical representation that generalizes across dexterous hands. We demonstrate, through simulation and real-world tasks on unseen morphologies (e.g., 81.9% zero-shot success rate on 3-finger LEAP Hand), that our framework unifies both the representational and action spaces of structurally diverse hands, providing a scalable foundation for cross-hand learning toward universal dexterous manipulation.

