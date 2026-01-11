---
layout: default
title: Hán Dān Xué Bù (Mimicry) or Qīng Chū Yú Lán (Mastery)? A Cognitive Perspective on Reasoning Distillation in Large Language Models
---

# Hán Dān Xué Bù (Mimicry) or Qīng Chū Yú Lán (Mastery)? A Cognitive Perspective on Reasoning Distillation in Large Language Models
**arXiv**：[2601.05019v1](https://arxiv.org/abs/2601.05019) · [PDF](https://arxiv.org/pdf/2601.05019.pdf)  
**作者**：Yueqing Hu, Xinyang Peng, Shuting Peng, Hanqi Wang, Tianhong Wang  

**一句话要点**：揭示推理蒸馏导致功能对齐崩溃，提出人类认知是强化学习涌现属性而非被动模仿

**关键词**：推理蒸馏, 功能对齐崩溃, 监督微调, 认知结构, 大语言模型, 强化学习

## 3 点简述
- 核心问题：推理蒸馏训练使学生模型模仿推理轨迹，但未能传递认知结构
- 方法要点：通过14个模型测试邯郸学步假设，发现监督微调引发功能对齐崩溃
- 实验效果：教师模型保持人类难度对齐，学生模型对齐显著退化并出现负迁移

## 摘要（原文）

> Recent Large Reasoning Models trained via reinforcement learning exhibit a "natural" alignment with human cognitive costs. However, we show that the prevailing paradigm of reasoning distillation -- training student models to mimic these traces via Supervised Fine-Tuning (SFT) -- fails to transmit this cognitive structure. Testing the "Hán Dān Xué Bù" (Superficial Mimicry) hypothesis across 14 models, we find that distillation induces a "Functional Alignment Collapse": while teacher models mirror human difficulty scaling ($\bar{r}=0.64$), distilled students significantly degrade this alignment ($\bar{r}=0.34$), often underperforming their own pre-distillation baselines ("Negative Transfer"). Our analysis suggests that SFT induces a "Cargo Cult" effect, where students ritualistically replicate the linguistic form of reasoning (verbosity) without internalizing the teacher's dynamic resource allocation policy. Consequently, reasoning distillation decouples computational cost from cognitive demand, revealing that human-like cognition is an emergent property of active reinforcement, not passive imitation.

