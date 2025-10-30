---
layout: default
title: VFXMaster: Unlocking Dynamic Visual Effect Generation via In-Context Learning
---

# VFXMaster: Unlocking Dynamic Visual Effect Generation via In-Context Learning
**arXiv**：[2510.25772v1](https://arxiv.org/abs/2510.25772) · [PDF](https://arxiv.org/pdf/2510.25772.pdf)  
**作者**：Baolu Li, Yiming Zhang, Qinghe Wang, Liqian Ma, Xiaoyu Shi, Xintao Wang, Pengfei Wan, Zhenfei Yin, Yunzhi Zhuge, Huchuan Lu, Xu Jia  

**一句话要点**：提出VFXMaster框架，通过上下文学习实现动态视觉效果的统一生成与泛化

**关键词**：视觉特效生成, 上下文学习, 视频生成, 效果泛化, 注意力机制

## 3 点简述
- 核心问题：现有方法依赖一LoRA一效果，资源密集且无法泛化到未见效果
- 方法要点：设计上下文条件策略和注意力掩码，实现效果属性解耦与注入
- 实验或效果：在多种效果类别上有效模仿，并展示对域外效果的出色泛化能力

## 摘要（原文）

> Visual effects (VFX) are crucial to the expressive power of digital media,
> yet their creation remains a major challenge for generative AI. Prevailing
> methods often rely on the one-LoRA-per-effect paradigm, which is
> resource-intensive and fundamentally incapable of generalizing to unseen
> effects, thus limiting scalability and creation. To address this challenge, we
> introduce VFXMaster, the first unified, reference-based framework for VFX video
> generation. It recasts effect generation as an in-context learning task,
> enabling it to reproduce diverse dynamic effects from a reference video onto
> target content. In addition, it demonstrates remarkable generalization to
> unseen effect categories. Specifically, we design an in-context conditioning
> strategy that prompts the model with a reference example. An in-context
> attention mask is designed to precisely decouple and inject the essential
> effect attributes, allowing a single unified model to master the effect
> imitation without information leakage. In addition, we propose an efficient
> one-shot effect adaptation mechanism to boost generalization capability on
> tough unseen effects from a single user-provided video rapidly. Extensive
> experiments demonstrate that our method effectively imitates various categories
> of effect information and exhibits outstanding generalization to out-of-domain
> effects. To foster future research, we will release our code, models, and a
> comprehensive dataset to the community.

