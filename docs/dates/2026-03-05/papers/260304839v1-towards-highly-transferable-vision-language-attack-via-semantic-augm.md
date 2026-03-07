---
layout: default
title: Towards Highly Transferable Vision-Language Attack via Semantic-Augmented Dynamic Contrastive Interaction
---

# Towards Highly Transferable Vision-Language Attack via Semantic-Augmented Dynamic Contrastive Interaction
**arXiv**：[2603.04839v1](https://arxiv.org/abs/2603.04839) · [PDF](https://arxiv.org/pdf/2603.04839.pdf)  
**作者**：Yuanbo Li, Tianyang Xu, Cong Hu, Tao Zhou, Xiao-Jun Wu, Josef Kittler  

**一句话要点**：提出语义增强动态对比攻击以提升视觉-语言预训练模型的对抗迁移性

**关键词**：视觉-语言预训练, 对抗攻击, 迁移性, 对比学习, 语义增强, 动态交互

## 3 点简述
- 现有攻击依赖静态跨模态交互，仅破坏正样本对，导致迁移性有限
- SADCA通过动态对抗图像-文本交互和对比学习机制增强语义不一致性
- 实验表明SADCA在多个数据集和模型上显著超越现有方法，提升对抗迁移性

## 摘要（原文）

> With the rapid advancement and widespread application of vision-language pre-training (VLP) models, their vulnerability to adversarial attacks has become a critical concern. In general, the adversarial examples can typically be designed to exhibit transferable power, attacking not only different models but also across diverse tasks. However, existing attacks on language-vision models mainly rely on static cross-modal interactions and focus solely on disrupting positive image-text pairs, resulting in limited cross-modal disruption and poor transferability. To address this issue, we propose a Semantic-Augmented Dynamic Contrastive Attack (SADCA) that enhances adversarial transferability through progressive and semantically guided perturbation. SADCA progressively disrupts cross-modal alignment through dynamic interactions between adversarial images and texts. This is accomplished by SADCA establishing a contrastive learning mechanism involving adversarial, positive and negative samples, to reinforce the semantic inconsistency of the obtained perturbations. Moreover, we empirically find that input transformations commonly used in traditional transfer-based attacks also benefit VLPs, which motivates a semantic augmentation module that increases the diversity and generalization of adversarial examples. Extensive experiments on multiple datasets and models demonstrate that SADCA significantly improves adversarial transferability and consistently surpasses state-of-the-art methods. The code is released at https://github.com/LiYuanBoJNU/SADCA.

