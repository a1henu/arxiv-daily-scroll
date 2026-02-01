---
layout: default
title: DUET: Distilled LLM Unlearning from an Efficiently Contextualized Teacher
---

# DUET: Distilled LLM Unlearning from an Efficiently Contextualized Teacher
**arXiv**：[2601.21283v1](https://arxiv.org/abs/2601.21283) · [PDF](https://arxiv.org/pdf/2601.21283.pdf)  
**作者**：Yisheng Zhong, Zhengbang Yang, Zhuangdi Zhu  

**一句话要点**：提出DUET蒸馏遗忘方法，结合调优与上下文遗忘优势，高效移除LLM不良知识。

**关键词**：大语言模型遗忘, 蒸馏学习, 上下文遗忘, 知识移除, 高效训练

## 3 点简述
- LLM遗忘技术面临调优法计算重且易灾难性遗忘，上下文法轻量但易受攻击的局限。
- DUET通过蒸馏模仿提示引导的教师模型，拒绝不良知识生成并保留通用知识。
- 在基准测试中，DUET在遗忘和效用保持上表现更优，数据效率显著高于现有方法。

## 摘要（原文）

> LLM unlearning is a technique to remove the impacts of undesirable knowledge from the model without retraining from scratch, which is indispensable towards trustworthy AI. Existing unlearning methods face significant limitations: conventional tuning-based unlearning is computationally heavy and prone to catastrophic forgetting. In contrast, in-contextualized unlearning is lightweight for precise unlearning but vulnerable to prompt removal or reverse engineering attacks. In response, we propose Distilled Unlearning from an Efficient Teacher (DUET), a novel distillation-based unlearning method that combines the merits of these two lines of work. It learns a student model to imitate the behavior of a prompt-steered teacher that effectively refuses undesirable knowledge generation while preserving general domain knowledge. Extensive evaluations on existing benchmarks with our enriched evaluation protocols demonstrate that DUET achieves higher performance in both forgetting and utility preservation, while being orders of magnitude more data-efficient than state-of-the-art unlearning methods.

