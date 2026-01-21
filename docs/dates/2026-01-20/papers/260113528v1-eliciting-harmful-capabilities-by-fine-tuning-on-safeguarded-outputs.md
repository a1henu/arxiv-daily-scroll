---
layout: default
title: Eliciting Harmful Capabilities by Fine-Tuning On Safeguarded Outputs
---

# Eliciting Harmful Capabilities by Fine-Tuning On Safeguarded Outputs
**arXiv**：[2601.13528v1](https://arxiv.org/abs/2601.13528) · [PDF](https://arxiv.org/pdf/2601.13528.pdf)  
**作者**：Jackson Kaunismaa, Avery Griffin, John Hughes, Christina Q. Knight, Mrinank Sharma, Erik Jones  

**一句话要点**：提出基于安全输出微调的诱导攻击，以在开源模型中激发有害能力

**关键词**：诱导攻击, 模型安全, 微调, 有害能力, 前沿模型, 开源模型

## 3 点简述
- 核心问题：前沿模型的安全防护可能被绕过，导致开源模型获得有害能力
- 方法要点：通过相邻领域提示获取安全输出，并微调开源模型以恢复有害能力
- 实验或效果：在危险化学品合成领域，攻击恢复约40%能力差距，效果随前沿模型能力和数据量提升

## 摘要（原文）

> Model developers implement safeguards in frontier models to prevent misuse, for example, by employing classifiers to filter dangerous outputs. In this work, we demonstrate that even robustly safeguarded models can be used to elicit harmful capabilities in open-source models through elicitation attacks. Our elicitation attacks consist of three stages: (i) constructing prompts in adjacent domains to a target harmful task that do not request dangerous information; (ii) obtaining responses to these prompts from safeguarded frontier models; (iii) fine-tuning open-source models on these prompt-output pairs. Since the requested prompts cannot be used to directly cause harm, they are not refused by frontier model safeguards. We evaluate these elicitation attacks within the domain of hazardous chemical synthesis and processing, and demonstrate that our attacks recover approximately 40% of the capability gap between the base open-source model and an unrestricted frontier model. We then show that the efficacy of elicitation attacks scales with the capability of the frontier model and the amount of generated fine-tuning data. Our work demonstrates the challenge of mitigating ecosystem level risks with output-level safeguards.

