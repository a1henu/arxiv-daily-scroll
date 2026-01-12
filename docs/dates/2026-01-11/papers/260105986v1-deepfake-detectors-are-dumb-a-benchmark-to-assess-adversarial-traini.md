---
layout: default
title: Deepfake detectors are DUMB: A benchmark to assess adversarial training robustness under transferability constraints
---

# Deepfake detectors are DUMB: A benchmark to assess adversarial training robustness under transferability constraints
**arXiv**：[2601.05986v1](https://arxiv.org/abs/2601.05986) · [PDF](https://arxiv.org/pdf/2601.05986.pdf)  
**作者**：Adrian Serrano, Erwan Umlil, Ronan Thomas  

**一句话要点**：扩展DUMB方法评估深度伪造检测器在对抗训练下的鲁棒性，聚焦迁移约束与跨数据集场景

**关键词**：深度伪造检测, 对抗训练, 鲁棒性评估, 迁移攻击, 跨数据集分析, DUMB方法

## 3 点简述
- 核心问题：真实环境中深度伪造检测器面临对抗攻击，现有对抗训练在有限知识和数据分布不匹配下的有效性未知
- 方法要点：基于DUMB/DUMBer框架，评估检测器在迁移约束和跨数据集配置下的鲁棒性，涵盖攻击者与防御者视角
- 实验或效果：测试五种检测器、三种攻击和两个数据集，发现对抗训练在分布内增强鲁棒性，但跨数据集可能降低，需案例感知防御

## 摘要（原文）

> Deepfake detection systems deployed in real-world environments are subject to adversaries capable of crafting imperceptible perturbations that degrade model performance. While adversarial training is a widely adopted defense, its effectiveness under realistic conditions -- where attackers operate with limited knowledge and mismatched data distributions - remains underexplored. In this work, we extend the DUMB -- Dataset soUrces, Model architecture and Balance - and DUMBer methodology to deepfake detection. We evaluate detectors robustness against adversarial attacks under transferability constraints and cross-dataset configuration to extract real-world insights. Our study spans five state-of-the-art detectors (RECCE, SRM, XCeption, UCF, SPSL), three attacks (PGD, FGSM, FPBA), and two datasets (FaceForensics++ and Celeb-DF-V2). We analyze both attacker and defender perspectives mapping results to mismatch scenarios. Experiments show that adversarial training strategies reinforce robustness in the in-distribution cases but can also degrade it under cross-dataset configuration depending on the strategy adopted. These findings highlight the need for case-aware defense strategies in real-world applications exposed to adversarial attacks.

