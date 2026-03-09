---
layout: default
title: Contrastive-to-Self-Supervised: A Two-Stage Framework for Script Similarity Learning
---

# Contrastive-to-Self-Supervised: A Two-Stage Framework for Script Similarity Learning
**arXiv**：[2603.06180v1](https://arxiv.org/abs/2603.06180) · [PDF](https://arxiv.org/pdf/2603.06180.pdf)  
**作者**：Claire Roman, Philippe Meyer  

**一句话要点**：提出两阶段框架以解决文字系统相似性学习中的历史关系不确定性问题

**关键词**：文字系统相似性学习, 对比学习, 师生蒸馏, 字形识别, 无监督发现

## 3 点简述
- 核心问题：文字系统历史关系不确定，难以直接学习相似性度量
- 方法要点：先在有标签人造字母上训练对比学习编码器，再通过师生蒸馏扩展到历史文字
- 实验或效果：在多样文字系统上实现少样本字形识别和有意义的聚类，无需真实进化关系

## 摘要（原文）

> Learning similarity metrics for glyphs and writing systems faces a fundamental challenge: while individual graphemes within invented alphabets can be reliably labeled, the historical relationships between different scripts remain uncertain and contested. We propose a two-stage framework that addresses this epistemological constraint. First, we train an encoder with contrastive loss on labeled invented alphabets, establishing a teacher model with robust discriminative features. Second, we extend to historically attested scripts through teacher-student distillation, where the student learns unsupervised representations guided by the teacher's knowledge but free to discover latent cross-script similarities. The asymmetric setup enables the student to learn deformation-invariant embeddings while inheriting discriminative structure from clean examples. Our approach bridges supervised contrastive learning and unsupervised discovery, enabling both hard boundaries between distinct systems and soft similarities reflecting potential historical influences. Experiments on diverse writing systems demonstrate effective few-shot glyph recognition and meaningful script clustering without requiring ground-truth evolutionary relationships.

