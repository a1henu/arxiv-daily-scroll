---
layout: default
title: Empowering Reliable Visual-Centric Instruction Following in MLLMs
---

# Empowering Reliable Visual-Centric Instruction Following in MLLMs
**arXiv**：[2601.03198v1](https://arxiv.org/abs/2601.03198) · [PDF](https://arxiv.org/pdf/2601.03198.pdf)  
**作者**：Weilei He, Feng Ju, Zhiyuan Fan, Rui Min, Minhao Cheng, Yi R. Fung  

**一句话要点**：提出VC-IFEval基准以评估多模态大语言模型的视觉指令跟随能力

**关键词**：多模态大语言模型, 视觉指令跟随, 基准评估, 数据集构建, 模型微调, 多模态约束

## 3 点简述
- 现有基准主要关注文本指令，忽视视觉模态的隐含约束，导致评估不全面。
- 引入VC-IFEval基准，系统整合视觉依赖约束，实现更严格细粒度的多模态指令跟随评估。
- 通过数据集微调模型，显著提升视觉指令跟随的准确性和遵循度，并提供模型性能新见解。

## 摘要（原文）

> Evaluating the instruction-following (IF) capabilities of Multimodal Large Language Models (MLLMs) is essential for rigorously assessing how faithfully model outputs adhere to user-specified intentions. Nevertheless, existing benchmarks for evaluating MLLMs' instruction-following capability primarily focus on verbal instructions in the textual modality. These limitations hinder a thorough analysis of instruction-following capabilities, as they overlook the implicit constraints embedded in the semantically rich visual modality. To address this gap, we introduce VC-IFEval, a new benchmark accompanied by a systematically constructed dataset that evaluates MLLMs' instruction-following ability under multimodal settings. Our benchmark systematically incorporates vision-dependent constraints into instruction design, enabling a more rigorous and fine-grained assessment of how well MLLMs align their outputs with both visual input and textual instructions. Furthermore, by fine-tuning MLLMs on our dataset, we achieve substantial gains in visual instruction-following accuracy and adherence. Through extensive evaluation across representative MLLMs, we provide new insights into the strengths and limitations of current models.

