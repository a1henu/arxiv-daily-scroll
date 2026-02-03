---
layout: default
title: SGHA-Attack: Semantic-Guided Hierarchical Alignment for Transferable Targeted Attacks on Vision-Language Models
---

# SGHA-Attack: Semantic-Guided Hierarchical Alignment for Transferable Targeted Attacks on Vision-Language Models
**arXiv**：[2602.01574v1](https://arxiv.org/abs/2602.01574) · [PDF](https://arxiv.org/pdf/2602.01574.pdf)  
**作者**：Haobo Wang, Weiqi Luo, Xiaojun Jia, Xiaochun Cao  

**一句话要点**：提出SGHA-Attack，通过语义引导分层对齐提升视觉语言模型目标攻击的跨模型迁移性

**关键词**：视觉语言模型, 对抗攻击, 迁移攻击, 语义对齐, 分层特征, 黑盒攻击

## 3 点简述
- 核心问题：现有目标迁移攻击依赖单一参考和最终层对齐，易过拟合代理模型，跨异构模型迁移效果差
- 方法要点：使用多目标参考和加权混合，在中间层进行全局与空间对齐，并同步视觉与文本特征
- 实验或效果：在开源和商业黑盒视觉语言模型上验证，攻击迁移性优于先前方法，对预处理和净化防御鲁棒

## 摘要（原文）

> Large vision-language models (VLMs) are vulnerable to transfer-based adversarial perturbations, enabling attackers to optimize on surrogate models and manipulate black-box VLM outputs. Prior targeted transfer attacks often overfit surrogate-specific embedding space by relying on a single reference and emphasizing final-layer alignment, which underutilizes intermediate semantics and degrades transfer across heterogeneous VLMs. To address this, we propose SGHA-Attack, a Semantic-Guided Hierarchical Alignment framework that adopts multiple target references and enforces intermediate-layer consistency. Concretely, we generate a visually grounded reference pool by sampling a frozen text-to-image model conditioned on the target prompt, and then carefully select the Top-K most semantically relevant anchors under the surrogate to form a weighted mixture for stable optimization guidance. Building on these anchors, SGHA-Attack injects target semantics throughout the feature hierarchy by aligning intermediate visual representations at both global and spatial granularities across multiple depths, and by synchronizing intermediate visual and textual features in a shared latent subspace to provide early cross-modal supervision before the final projection. Extensive experiments on open-source and commercial black-box VLMs show that SGHA-Attack achieves stronger targeted transferability than prior methods and remains robust under preprocessing and purification defenses.

