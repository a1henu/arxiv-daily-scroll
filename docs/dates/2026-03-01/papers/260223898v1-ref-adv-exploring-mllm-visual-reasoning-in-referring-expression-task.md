---
layout: default
title: Ref-Adv: Exploring MLLM Visual Reasoning in Referring Expression Tasks
---

# Ref-Adv: Exploring MLLM Visual Reasoning in Referring Expression Tasks
**arXiv**：[2602.23898v1](https://arxiv.org/abs/2602.23898) · [PDF](https://arxiv.org/pdf/2602.23898.pdf)  
**作者**：Qihua Dong, Kuo Yang, Lin Ju, Handong Zhao, Yitian Zhang, Yizhou Wang, Huimin Zeng, Jianglin Lu, Yun Fu  

**一句话要点**：提出Ref-Adv基准以解决多模态大语言模型在指代表达理解任务中视觉推理和基础能力的不足

**关键词**：指代表达理解, 多模态大语言模型, 视觉推理, 基准测试, 捷径抑制, 否定推理

## 3 点简述
- 指代表达理解任务现有基准存在表达简短、干扰少和冗余描述等捷径问题
- Ref-Adv通过配对非平凡表达与必要信息并引入硬干扰和否定推理来抑制捷径
- 实验显示模型在Ref-Adv上性能显著下降，揭示其对捷径的依赖和视觉推理差距

## 摘要（原文）

> Referring Expression Comprehension (REC) links language to region level visual perception. Standard benchmarks (RefCOCO, RefCOCO+, RefCOCOg) have progressed rapidly with multimodal LLMs but remain weak tests of visual reasoning and grounding: (i) many expressions are very short, leaving little reasoning demand; (ii) images often contain few distractors, making the target easy to find; and (iii) redundant descriptors enable shortcut solutions that bypass genuine text understanding and visual reasoning. We introduce Ref-Adv, a modern REC benchmark that suppresses shortcuts by pairing linguistically nontrivial expressions with only the information necessary to uniquely identify the target. The dataset contains referring expressions on real images, curated with hard distractors and annotated with reasoning facets including negation. We conduct comprehensive ablations (word order perturbations and descriptor deletion sufficiency) to show that solving Ref-Adv requires reasoning beyond simple cues, and we evaluate a broad suite of contemporary multimodal LLMs on Ref-Adv. Despite strong results on RefCOCO, RefCOCO+, and RefCOCOg, models drop markedly on Ref-Adv, revealing reliance on shortcuts and gaps in visual reasoning and grounding. We provide an in depth failure analysis and aim for Ref-Adv to guide future work on visual reasoning and grounding in MLLMs.

