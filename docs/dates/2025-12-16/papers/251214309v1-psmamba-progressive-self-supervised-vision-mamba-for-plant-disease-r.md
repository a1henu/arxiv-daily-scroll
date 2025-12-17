---
layout: default
title: PSMamba: Progressive Self-supervised Vision Mamba for Plant Disease Recognition
---

# PSMamba: Progressive Self-supervised Vision Mamba for Plant Disease Recognition
**arXiv**：[2512.14309v1](https://arxiv.org/abs/2512.14309) · [PDF](https://arxiv.org/pdf/2512.14309.pdf)  
**作者**：Abdullah Al Mamun, Miaohua Zhang, David Ahmedt-Aristizabal, Zeeshan Hayder, Mohammad Awrangjeb  

**一句话要点**：提出PSMamba框架，通过渐进自监督和双学生分层蒸馏解决植物病害图像多尺度病变模式识别问题。

**关键词**：植物病害识别, 自监督学习, Vision Mamba, 分层蒸馏, 多尺度表示学习

## 3 点简述
- 核心问题：现有自监督学习框架难以捕捉植物病害图像中层次化、多尺度的病变模式。
- 方法要点：集成Vision Mamba高效序列建模，采用双学生分层蒸馏策略，包括全局教师和两个专门学生处理中尺度与局部视图。
- 实验或效果：在三个基准数据集上优于现有自监督方法，在领域偏移和细粒度场景中表现出更高的准确性和鲁棒性。

## 摘要（原文）

> Self-supervised Learning (SSL) has become a powerful paradigm for representation learning without manual annotations. However, most existing frameworks focus on global alignment and struggle to capture the hierarchical, multi-scale lesion patterns characteristic of plant disease imagery. To address this gap, we propose PSMamba, a progressive self-supervised framework that integrates the efficient sequence modelling of Vision Mamba (VM) with a dual-student hierarchical distillation strategy. Unlike conventional single teacher-student designs, PSMamba employs a shared global teacher and two specialised students: one processes mid-scale views to capture lesion distributions and vein structures, while the other focuses on local views to capture fine-grained cues such as texture irregularities and early-stage lesions. This multi-granular supervision facilitates the joint learning of contextual and detailed representations, with consistency losses ensuring coherent cross-scale alignment. Experiments on three benchmark datasets show that PSMamba consistently outperforms state-of-the-art SSL methods, delivering superior accuracy and robustness in both domain-shifted and fine-grained scenarios.

