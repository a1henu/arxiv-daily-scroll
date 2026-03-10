---
layout: default
title: MJ1: Multimodal Judgment via Grounded Verification
---

# MJ1: Multimodal Judgment via Grounded Verification
**arXiv**：[2603.07990v1](https://arxiv.org/abs/2603.07990) · [PDF](https://arxiv.org/pdf/2603.07990.pdf)  
**作者**：Bhavesh Kumar, Dylan Feng, Leonard Tang  

**一句话要点**：提出MJ1多模态判断模型，通过结构化验证链和一致性奖励解决视觉证据基础不足问题。

**关键词**：多模态判断, 视觉基础验证, 强化学习训练, 结构化验证链, 反事实一致性奖励, MMRB2基准

## 3 点简述
- 多模态判断模型在决策时难以基于视觉证据进行基础验证。
- 采用强化学习训练，结合结构化验证链和反事实一致性奖励来强制视觉基础。
- 在MMRB2基准上，未训练时提升基础模型准确率，训练后以3B参数超越更大规模模型。

## 摘要（原文）

> Multimodal judges struggle to ground decisions in visual evidence. We present MJ1, a multimodal judge trained with reinforcement learning that enforces visual grounding through a structured grounded verification chain (observations $\rightarrow$ claims $\rightarrow$ verification $\rightarrow$ evaluation $\rightarrow$ scoring) and a counterfactual consistency reward that penalizes position bias. Even without training, our mechanism improves base-model accuracy on MMRB2 by +3.8 points on Image Editing and +1.7 on Multimodal Reasoning. After training, MJ1, with only 3B active parameters, achieves 77.0% accuracy on MMRB2 and surpasses orders-of-magnitude larger models like Gemini-3-Pro. These results show that grounded verification and consistency-based training substantially improve multimodal judgment without increasing model scale.

