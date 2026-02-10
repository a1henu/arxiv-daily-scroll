---
layout: default
title: Closing the Confusion Loop: CLIP-Guided Alignment for Source-Free Domain Adaptation
---

# Closing the Confusion Loop: CLIP-Guided Alignment for Source-Free Domain Adaptation
**arXiv**：[2602.08730v1](https://arxiv.org/abs/2602.08730) · [PDF](https://arxiv.org/pdf/2602.08730.pdf)  
**作者**：Shanshan Wang, Ziying Feng, Xiaozheng Shen, Xun Yang, Pichao Wang, Zhenwei He, Xingyi Zhang  

**一句话要点**：提出CLIP引导对齐框架以解决源自由域适应中的类混淆问题

**关键词**：源自由域适应, 类混淆建模, CLIP引导, 伪标签优化, 对比学习, 细粒度识别

## 3 点简述
- 核心问题：源自由域适应中，源模型在目标域存在不对称动态类混淆，导致伪标签噪声和判别力差。
- 方法要点：通过检测混淆对、构建CLIP引导的混淆感知提示和对比对齐特征，显式建模并缓解类混淆。
- 实验或效果：在多个数据集上优于现有方法，尤其在易混淆和细粒度场景中提升显著。

## 摘要（原文）

> Source-Free Domain Adaptation (SFDA) tackles the problem of adapting a pre-trained source model to an unlabeled target domain without accessing any source data, which is quite suitable for the field of data security. Although recent advances have shown that pseudo-labeling strategies can be effective, they often fail in fine-grained scenarios due to subtle inter-class similarities. A critical but underexplored issue is the presence of asymmetric and dynamic class confusion, where visually similar classes are unequally and inconsistently misclassified by the source model. Existing methods typically ignore such confusion patterns, leading to noisy pseudo-labels and poor target discrimination. To address this, we propose CLIP-Guided Alignment(CGA), a novel framework that explicitly models and mitigates class confusion in SFDA. Generally, our method consists of three parts: (1) MCA: detects first directional confusion pairs by analyzing the predictions of the source model in the target domain; (2) MCC: leverages CLIP to construct confusion-aware textual prompts (e.g. a truck that looks like a bus), enabling more context-sensitive pseudo-labeling; and (3) FAM: builds confusion-guided feature banks for both CLIP and the source model and aligns them using contrastive learning to reduce ambiguity in the representation space. Extensive experiments on various datasets demonstrate that CGA consistently outperforms state-of-the-art SFDA methods, with especially notable gains in confusion-prone and fine-grained scenarios. Our results highlight the importance of explicitly modeling inter-class confusion for effective source-free adaptation. Our code can be find at https://github.com/soloiro/CGA

