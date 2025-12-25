---
layout: default
title: Language-Guided Grasp Detection with Coarse-to-Fine Learning for Robotic Manipulation
---

# Language-Guided Grasp Detection with Coarse-to-Fine Learning for Robotic Manipulation
**arXiv**：[2512.21065v1](https://arxiv.org/abs/2512.21065) · [PDF](https://arxiv.org/pdf/2512.21065.pdf)  
**作者**：Zebin Jiang, Tianle Jin, Xiangtong Yao, Alois Knoll, Hu Cao  

**一句话要点**：提出语言引导抓取检测方法，通过粗到细学习解决机器人抓取中语义对齐不足的问题。

**关键词**：语言引导抓取, 粗到细学习, 跨模态融合, 机器人操作, 视觉语义对齐, 动态卷积

## 3 点简述
- 现有语言引导抓取方法依赖浅层融合，导致语义对齐弱和视觉推理与语言意图不一致。
- 采用基于CLIP的层次跨模态融合和语言条件动态卷积头，实现细粒度视觉语义对齐和指令自适应预测。
- 在OCID-VLG和Grasp-Anything++数据集上超越现有方法，并在真实机器人平台验证有效性。

## 摘要（原文）

> Grasping is one of the most fundamental challenging capabilities in robotic manipulation, especially in unstructured, cluttered, and semantically diverse environments. Recent researches have increasingly explored language-guided manipulation, where robots not only perceive the scene but also interpret task-relevant natural language instructions. However, existing language-conditioned grasping methods typically rely on shallow fusion strategies, leading to limited semantic grounding and weak alignment between linguistic intent and visual grasp reasoning.In this work, we propose Language-Guided Grasp Detection (LGGD) with a coarse-to-fine learning paradigm for robotic manipulation. LGGD leverages CLIP-based visual and textual embeddings within a hierarchical cross-modal fusion pipeline, progressively injecting linguistic cues into the visual feature reconstruction process. This design enables fine-grained visual-semantic alignment and improves the feasibility of the predicted grasps with respect to task instructions. In addition, we introduce a language-conditioned dynamic convolution head (LDCH) that mixes multiple convolution experts based on sentence-level features, enabling instruction-adaptive coarse mask and grasp predictions. A final refinement module further enhances grasp consistency and robustness in complex scenes.Experiments on the OCID-VLG and Grasp-Anything++ datasets show that LGGD surpasses existing language-guided grasping methods, exhibiting strong generalization to unseen objects and diverse language queries. Moreover, deployment on a real robotic platform demonstrates the practical effectiveness of our approach in executing accurate, instruction-conditioned grasp actions. The code will be released publicly upon acceptance.

