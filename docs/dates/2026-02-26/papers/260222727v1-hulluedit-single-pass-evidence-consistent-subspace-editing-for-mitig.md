---
layout: default
title: HulluEdit: Single-Pass Evidence-Consistent Subspace Editing for Mitigating Hallucinations in Large Vision-Language Models
---

# HulluEdit: Single-Pass Evidence-Consistent Subspace Editing for Mitigating Hallucinations in Large Vision-Language Models
**arXiv**：[2602.22727v1](https://arxiv.org/abs/2602.22727) · [PDF](https://arxiv.org/pdf/2602.22727.pdf)  
**作者**：Yangguang Lin, Quan Fang, Yufei Li, Jiachen Sun, Junyu Gao, Jitao Sang  

**一句话要点**：提出HulluEdit框架，通过正交子空间编辑单次干预缓解大视觉语言模型中的物体幻觉问题

**关键词**：大视觉语言模型, 物体幻觉缓解, 正交子空间编辑, 单次干预, 参考无关框架

## 3 点简述
- 核心问题：大视觉语言模型中的物体幻觉阻碍可靠部署，现有方法在效率与准确性间难以平衡
- 方法要点：将隐藏状态分解为视觉证据、冲突先验和残差不确定性正交子空间，选择性抑制幻觉模式
- 实验或效果：在POPE和CHAIR基准上实现最先进幻觉减少，保持MME通用能力，推理高效

## 摘要（原文）

> Object hallucination in Large Vision-Language Models (LVLMs) significantly hinders their reliable deployment. Existing methods struggle to balance efficiency and accuracy: they often require expensive reference models and multiple forward passes, or apply static edits that risk suppressing genuine visual evidence. To address this, we introduce HulluEdit, a single-pass, reference-free intervention framework. Our core innovation is orthogonal subspace editing: we decompose the hidden states of the model into orthogonal subspaces - visual evidence, conflicting priors, and residual uncertainty - enabling selective suppression of hallucinatory patterns without interfering with visual grounding. This approach mathematically guarantees that edits applied to the prior subspace leave the visual component entirely unaffected. Extensive experiments show that HulluEdit achieves state-of-the-art hallucination reduction on benchmarks including POPE and CHAIR across diverse architectures, while preserving general capabilities on MME and maintaining efficient inference. Our method consistently outperforms contrastive decoding and static subspace editing baselines, offering a new pathway toward more trustworthy LVLMs.

