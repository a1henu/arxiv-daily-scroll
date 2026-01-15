---
layout: default
title: Improving Implicit Hate Speech Detection via a Community-Driven Multi-Agent Framework
---

# Improving Implicit Hate Speech Detection via a Community-Driven Multi-Agent Framework
**arXiv**：[2601.09342v1](https://arxiv.org/abs/2601.09342) · [PDF](https://arxiv.org/pdf/2601.09342.pdf)  
**作者**：Ewelina Gajewska, Katarzyna Budzynska, Jarosław A Chudziak  

**一句话要点**：提出基于社区驱动多智能体框架的隐式仇恨言论检测方法，以提升检测准确性与公平性。

**关键词**：隐式仇恨言论检测, 多智能体系统, 社会文化背景, 平衡准确率, ToxiGen数据集

## 3 点简述
- 核心问题：隐式仇恨言论检测因缺乏明确攻击性词汇而具挑战性，需融入社会文化背景。
- 方法要点：构建多智能体系统，包括中央仲裁智能体和代表特定群体的社区智能体，整合公开知识源。
- 实验或效果：在ToxiGen数据集上超越零/少样本提示等方法，使用平衡准确率评估，显著提升分类准确性和公平性。

## 摘要（原文）

> This work proposes a contextualised detection framework for implicitly hateful speech, implemented as a multi-agent system comprising a central Moderator Agent and dynamically constructed Community Agents representing specific demographic groups. Our approach explicitly integrates socio-cultural context from publicly available knowledge sources, enabling identity-aware moderation that surpasses state-of-the-art prompting methods (zero-shot prompting, few-shot prompting, chain-of-thought prompting) and alternative approaches on a challenging ToxiGen dataset. We enhance the technical rigour of performance evaluation by incorporating balanced accuracy as a central metric of classification fairness that accounts for the trade-off between true positive and true negative rates. We demonstrate that our community-driven consultative framework significantly improves both classification accuracy and fairness across all target groups.

