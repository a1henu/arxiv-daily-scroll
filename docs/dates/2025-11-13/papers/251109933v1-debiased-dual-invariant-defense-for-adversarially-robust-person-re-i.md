---
layout: default
title: Debiased Dual-Invariant Defense for Adversarially Robust Person Re-Identification
---

# Debiased Dual-Invariant Defense for Adversarially Robust Person Re-Identification
**arXiv**：[2511.09933v1](https://arxiv.org/abs/2511.09933) · [PDF](https://arxiv.org/pdf/2511.09933.pdf)  
**作者**：Yuhang Zhou, Yanxiang Zhao, Zhongyun Hua, Zhipu Liu, Zhaoquan Gu, Qing Liao, Leo Yu Zhang  

**一句话要点**：提出去偏双不变防御框架以增强行人重识别对抗鲁棒性

**关键词**：行人重识别, 对抗防御, 度量学习, 数据平衡, 对抗训练, 泛化能力

## 3 点简述
- 核心问题：行人重识别模型易受对抗攻击，现有防御未解决模型偏见和复合泛化需求。
- 方法要点：采用数据平衡和双对抗自元防御，结合扩散模型和度量对抗训练。
- 实验或效果：实验显示方法显著优于现有先进防御，提升对未知身份和攻击类型的泛化。

## 摘要（原文）

> Person re-identification (ReID) is a fundamental task in many real-world applications such as pedestrian trajectory tracking. However, advanced deep learning-based ReID models are highly susceptible to adversarial attacks, where imperceptible perturbations to pedestrian images can cause entirely incorrect predictions, posing significant security threats. Although numerous adversarial defense strategies have been proposed for classification tasks, their extension to metric learning tasks such as person ReID remains relatively unexplored. Moreover, the several existing defenses for person ReID fail to address the inherent unique challenges of adversarially robust ReID. In this paper, we systematically identify the challenges of adversarial defense in person ReID into two key issues: model bias and composite generalization requirements. To address them, we propose a debiased dual-invariant defense framework composed of two main phases. In the data balancing phase, we mitigate model bias using a diffusion-model-based data resampling strategy that promotes fairness and diversity in training data. In the bi-adversarial self-meta defense phase, we introduce a novel metric adversarial training approach incorporating farthest negative extension softening to overcome the robustness degradation caused by the absence of classifier. Additionally, we introduce an adversarially-enhanced self-meta mechanism to achieve dual-generalization for both unseen identities and unseen attack types. Experiments demonstrate that our method significantly outperforms existing state-of-the-art defenses.

