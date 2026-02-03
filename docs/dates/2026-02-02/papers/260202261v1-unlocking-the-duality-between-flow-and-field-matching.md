---
layout: default
title: Unlocking the Duality between Flow and Field Matching
---

# Unlocking the Duality between Flow and Field Matching
**arXiv**：[2602.02261v1](https://arxiv.org/abs/2602.02261) · [PDF](https://arxiv.org/pdf/2602.02261.pdf)  
**作者**：Daniil Shlenskii, Alexander Varlamov, Nazar Buzun, Alexander Korotin  

**一句话要点**：揭示条件流匹配与交互场匹配的对偶性，统一生成模型框架并扩展表达能力

**关键词**：条件流匹配, 交互场匹配, 生成模型, 对偶性, 概率路径, 静电匹配

## 3 点简述
- 核心问题：探究条件流匹配（CFM）与交互场匹配（IFM）是否本质不同或为同一动态的两种描述
- 方法要点：证明CFM与正向IFM子类存在双射关系，并展示一般IFM更具表达力，包含静电匹配等
- 实验或效果：利用对偶性为正向IFM提供概率解释，并为CFM开发基于IFM的新技术

## 摘要（原文）

> Conditional Flow Matching (CFM) unifies conventional generative paradigms such as diffusion models and flow matching. Interaction Field Matching (IFM) is a newer framework that generalizes Electrostatic Field Matching (EFM) rooted in Poisson Flow Generative Models (PFGM). While both frameworks define generative dynamics, they start from different objects: CFM specifies a conditional probability path in data space, whereas IFM specifies a physics-inspired interaction field in an augmented data space. This raises a basic question: are CFM and IFM genuinely different, or are they two descriptions of the same underlying dynamics? We show that they coincide for a natural subclass of IFM that we call forward-only IFM. Specifically, we construct a bijection between CFM and forward-only IFM. We further show that general IFM is strictly more expressive: it includes EFM and other interaction fields that cannot be realized within the standard CFM formulation. Finally, we highlight how this duality can benefit both frameworks: it provides a probabilistic interpretation of forward-only IFM and yields novel, IFM-driven techniques for CFM.

