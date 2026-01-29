---
layout: default
title: UnlearnShield: Shielding Forgotten Privacy against Unlearning Inversion
---

# UnlearnShield: Shielding Forgotten Privacy against Unlearning Inversion
**arXiv**：[2601.20325v1](https://arxiv.org/abs/2601.20325) · [PDF](https://arxiv.org/pdf/2601.20325.pdf)  
**作者**：Lulu Xue, Shengshan Hu, Wei Lu, Ziqi Zhou, Yufei Song, Jianhong Cheng, Minghui Li, Yanjun Zhang, Leo Yu Zhang  

**一句话要点**：提出UnlearnShield以防御机器学习遗忘中的隐私泄露攻击

**关键词**：机器学习遗忘, 隐私保护, 反演攻击, 防御机制, 模型扰动, 余弦空间

## 3 点简述
- 核心问题：机器学习遗忘技术存在隐私漏洞，攻击者可通过反演重建被遗忘数据
- 方法要点：在余弦表示空间引入定向扰动，通过约束模块平衡模型准确性与遗忘效果
- 实验或效果：实验显示在隐私保护、准确性和遗忘效果间实现良好权衡

## 摘要（原文）

> Machine unlearning is an emerging technique that aims to remove the influence of specific data from trained models, thereby enhancing privacy protection. However, recent research has uncovered critical privacy vulnerabilities, showing that adversaries can exploit unlearning inversion to reconstruct data that was intended to be erased. Despite the severity of this threat, dedicated defenses remain lacking. To address this gap, we propose UnlearnShield, the first defense specifically tailored to counter unlearning inversion. UnlearnShield introduces directional perturbations in the cosine representation space and regulates them through a constraint module to jointly preserve model accuracy and forgetting efficacy, thereby reducing inversion risk while maintaining utility. Experiments demonstrate that it achieves a good trade-off among privacy protection, accuracy, and forgetting.

