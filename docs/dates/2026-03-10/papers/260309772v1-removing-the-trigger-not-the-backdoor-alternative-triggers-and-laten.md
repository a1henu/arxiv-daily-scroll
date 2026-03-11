---
layout: default
title: Removing the Trigger, Not the Backdoor: Alternative Triggers and Latent Backdoors
---

# Removing the Trigger, Not the Backdoor: Alternative Triggers and Latent Backdoors
**arXiv**：[2603.09772v1](https://arxiv.org/abs/2603.09772) · [PDF](https://arxiv.org/pdf/2603.09772.pdf)  
**作者**：Gorka Abad, Ermes Franch, Stefanos Koffas, Stjepan Picek  

**一句话要点**：揭示后门攻击中替代触发器的存在，提出特征空间防御方向

**关键词**：后门攻击, 替代触发器, 特征空间, 机器学习安全, 防御策略

## 3 点简述
- 核心问题：传统后门防御仅移除已知触发器，但替代触发器可激活相同后门
- 方法要点：通过对比干净与触发表示估计后门方向，开发特征引导攻击
- 实验或效果：理论证明替代触发器存在，实证显示防御后后门仍潜伏

## 摘要（原文）

> Current backdoor defenses assume that neutralizing a known trigger removes the backdoor. We show this trigger-centric view is incomplete: \emph{alternative triggers}, patterns perceptually distinct from training triggers, reliably activate the same backdoor. We estimate the alternative trigger backdoor direction in feature space by contrasting clean and triggered representations, and then develop a feature-guided attack that jointly optimizes target prediction and directional alignment. First, we theoretically prove that alternative triggers exist and are an inevitable consequence of backdoor training. Then, we verify this empirically. Additionally, defenses that remove training triggers often leave backdoors intact, and alternative triggers can exploit the latent backdoor feature-space. Our findings motivate defenses targeting backdoor directions in representation space rather than input-space triggers.

