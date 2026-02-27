---
layout: default
title: CGSA: Class-Guided Slot-Aware Adaptation for Source-Free Object Detection
---

# CGSA: Class-Guided Slot-Aware Adaptation for Source-Free Object Detection
**arXiv**：[2602.22621v1](https://arxiv.org/abs/2602.22621) · [PDF](https://arxiv.org/pdf/2602.22621.pdf)  
**作者**：Boyang Dai, Zeng Fan, Zihao Qi, Meng Lou, Yizhou Yu  

**一句话要点**：提出CGSA框架，通过类引导的槽感知适应解决无源域自适应目标检测问题。

**关键词**：无源域自适应目标检测, 对象中心学习, 槽感知适应, DETR检测器, 跨域适应, 隐私敏感场景

## 3 点简述
- 核心问题：无源域自适应目标检测中忽视跨域数据的对象级结构线索。
- 方法要点：集成层次槽感知模块和类引导槽对比模块，促进域不变适应。
- 实验或效果：在多个跨域数据集上优于先前方法，验证了对象中心设计的有效性。

## 摘要（原文）

> Source-Free Domain Adaptive Object Detection (SF-DAOD) aims to adapt a detector trained on a labeled source domain to an unlabeled target domain without retaining any source data. Despite recent progress, most popular approaches focus on tuning pseudo-label thresholds or refining the teacher-student framework, while overlooking object-level structural cues within cross-domain data. In this work, we present CGSA, the first framework that brings Object-Centric Learning (OCL) into SF-DAOD by integrating slot-aware adaptation into the DETR-based detector. Specifically, our approach integrates a Hierarchical Slot Awareness (HSA) module into the detector to progressively disentangle images into slot representations that act as visual priors. These slots are then guided toward class semantics via a Class-Guided Slot Contrast (CGSC) module, maintaining semantic consistency and prompting domain-invariant adaptation. Extensive experiments on multiple cross-domain datasets demonstrate that our approach outperforms previous SF-DAOD methods, with theoretical derivations and experimental analysis further demonstrating the effectiveness of the proposed components and the framework, thereby indicating the promise of object-centric design in privacy-sensitive adaptation scenarios. Code is released at https://github.com/Michael-McQueen/CGSA.

