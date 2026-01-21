---
layout: default
title: Learning Fine-Grained Correspondence with Cross-Perspective Perception for Open-Vocabulary 6D Object Pose Estimation
---

# Learning Fine-Grained Correspondence with Cross-Perspective Perception for Open-Vocabulary 6D Object Pose Estimation
**arXiv**：[2601.13565v1](https://arxiv.org/abs/2601.13565) · [PDF](https://arxiv.org/pdf/2601.13565.pdf)  
**作者**：Yu Qin, Shimeng Fan, Fan Yang, Zixuan Xue, Zijie Mai, Wenrui Chen, Kailun Yang, Zhiyong Li  

**一句话要点**：提出FiCoP框架，通过细粒度块级对应解决开放词汇6D物体姿态估计中的全局匹配模糊问题。

**关键词**：开放词汇6D姿态估计, 细粒度对应, 跨视角感知, 块级匹配, 机器人视觉, 开放世界场景

## 3 点简述
- 现有方法依赖全局匹配，在开放世界场景中易受背景干扰导致姿态估计模糊。
- FiCoP引入块到块关联矩阵作为结构先验，结合跨视角感知模块，实现噪声鲁棒的细粒度匹配。
- 在REAL275和Toyota-Light数据集上，平均召回率分别提升8.0%和6.1%，优于现有方法。

## 摘要（原文）

> Open-vocabulary 6D object pose estimation empowers robots to manipulate arbitrary unseen objects guided solely by natural language. However, a critical limitation of existing approaches is their reliance on unconstrained global matching strategies. In open-world scenarios, trying to match anchor features against the entire query image space introduces excessive ambiguity, as target features are easily confused with background distractors. To resolve this, we propose Fine-grained Correspondence Pose Estimation (FiCoP), a framework that transitions from noise-prone global matching to spatially-constrained patch-level correspondence. Our core innovation lies in leveraging a patch-to-patch correlation matrix as a structural prior to narrowing the matching scope, effectively filtering out irrelevant clutter to prevent it from degrading pose estimation. Firstly, we introduce an object-centric disentanglement preprocessing to isolate the semantic target from environmental noise. Secondly, a Cross-Perspective Global Perception (CPGP) module is proposed to fuse dual-view features, establishing structural consensus through explicit context reasoning. Finally, we design a Patch Correlation Predictor (PCP) that generates a precise block-wise association map, acting as a spatial filter to enforce fine-grained, noise-resilient matching. Experiments on the REAL275 and Toyota-Light datasets demonstrate that FiCoP improves Average Recall by 8.0% and 6.1%, respectively, compared to the state-of-the-art method, highlighting its capability to deliver robust and generalized perception for robotic agents operating in complex, unconstrained open-world environments. The source code will be made publicly available at https://github.com/zjjqinyu/FiCoP.

