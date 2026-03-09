---
layout: default
title: When One Modality Rules Them All: Backdoor Modality Collapse in Multimodal Diffusion Models
---

# When One Modality Rules Them All: Backdoor Modality Collapse in Multimodal Diffusion Models
**arXiv**：[2603.06508v1](https://arxiv.org/abs/2603.06508) · [PDF](https://arxiv.org/pdf/2603.06508.pdf)  
**作者**：Qitong Wang, Haoran Dai, Haotian Zhang, Christopher Rasmussen, Binghui Wang  

**一句话要点**：提出后门模态坍缩现象，揭示多模态扩散模型中攻击依赖单一模态的脆弱性

**关键词**：多模态扩散模型, 后门攻击, 模态坍缩, 脆弱性分析, 触发模态归因, 跨触发交互

## 3 点简述
- 核心问题：多模态扩散模型的后门攻击可能退化，过度依赖部分模态，导致其他模态冗余
- 方法要点：引入触发模态归因和跨触发交互两个新指标，量化后门模态坍缩行为
- 实验或效果：实验显示攻击常呈现“赢者通吃”动态，跨模态交互可忽略或负向，挑战协同脆弱性直觉

## 摘要（原文）

> While diffusion models have revolutionized visual content generation, their rapid adoption has underscored the critical need to investigate vulnerabilities, e.g., to backdoor attacks. In multimodal diffusion models, it is natural to expect that attacking multiple modalities simultaneously (e.g., text and image) would yield complementary effects and strengthen the overall backdoor. In this paper, we challenge this assumption by investigating the phenomenon of Backdoor Modality Collapse, a scenario where the backdoor mechanism degenerates to rely predominantly on a subset of modalities, rendering others redundant. To rigorously quantify this behavior, we introduce two novel metrics: Trigger Modality Attribution (TMA) and Cross-Trigger Interaction (CTI). Through extensive experiments across diverse training configurations in multimodal conditional diffusion, we consistently observe a ``winner-takes-all'' dynamic in backdoor behavior. Our results reveal that (1) attacks often collapse into subset-modality dominance, and (2) cross-modal interaction is negligible or even negative, contradicting the intuition of synergistic vulnerability. These findings highlight a critical blind spot in current assessments, suggesting that high attack success rates often mask a fundamental reliance on a subset of modalities. This establishes a principled foundation for mechanistic analysis and future defense development.

