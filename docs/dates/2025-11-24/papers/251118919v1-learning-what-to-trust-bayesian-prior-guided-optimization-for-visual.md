---
layout: default
title: Learning What to Trust: Bayesian Prior-Guided Optimization for Visual Generation
---

# Learning What to Trust: Bayesian Prior-Guided Optimization for Visual Generation
**arXiv**：[2511.18919v1](https://arxiv.org/abs/2511.18919) · [PDF](https://arxiv.org/pdf/2511.18919.pdf)  
**作者**：Ruiying Liu, Yuanzhi Liang, Haibin Huang, Tianshu Yu, Chi Zhang  

**一句话要点**：提出贝叶斯先验引导优化以解决视觉生成中奖励不确定性问题

**关键词**：视觉生成, 贝叶斯优化, 奖励模型, 语义对齐, 后训练优化

## 3 点简述
- 核心问题：文本与视觉对应关系模糊，导致奖励信号不确定和弱区分性
- 方法要点：通过语义先验锚建模奖励不确定性，自适应调节组间和组内信任
- 实验或效果：在图像和视频生成中，语义对齐、感知保真度和收敛速度均提升

## 摘要（原文）

> Group Relative Policy Optimization (GRPO) has emerged as an effective and lightweight framework for post-training visual generative models. However, its performance is fundamentally limited by the ambiguity of textual visual correspondence: a single prompt may validly describe diverse visual outputs, and a single image or video may support multiple equally correct interpretations. This many to many relationship leads reward models to generate uncertain and weakly discriminative signals, causing GRPO to underutilize reliable feedback and overfit noisy ones. We introduce Bayesian Prior-Guided Optimization (BPGO), a novel extension of GRPO that explicitly models reward uncertainty through a semantic prior anchor. BPGO adaptively modulates optimization trust at two levels: inter-group Bayesian trust allocation emphasizes updates from groups consistent with the prior while down-weighting ambiguous ones, and intra-group prior-anchored renormalization sharpens sample distinctions by expanding confident deviations and compressing uncertain scores. Across both image and video generation tasks, BPGO delivers consistently stronger semantic alignment, enhanced perceptual fidelity, and faster convergence than standard GRPO and recent variants.

