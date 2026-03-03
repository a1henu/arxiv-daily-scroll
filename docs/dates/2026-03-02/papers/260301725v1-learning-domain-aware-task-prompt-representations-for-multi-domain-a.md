---
layout: default
title: Learning Domain-Aware Task Prompt Representations for Multi-Domain All-in-One Image Restoration
---

# Learning Domain-Aware Task Prompt Representations for Multi-Domain All-in-One Image Restoration
**arXiv**：[2603.01725v1](https://arxiv.org/abs/2603.01725) · [PDF](https://arxiv.org/pdf/2603.01725.pdf)  
**作者**：Guanglu Dong, Chunlei Li, Chao Ren, Jingliang Hu, Yilei Shi, Xiao Xiang Zhu, Lichao Mou  

**一句话要点**：提出DATPRL-IR方法，通过领域感知任务提示表示学习实现多领域一体化图像恢复。

**关键词**：多领域图像恢复, 提示表示学习, 任务提示池, 领域感知, 一体化模型, 泛化能力

## 3 点简述
- 核心问题：现有一体化图像恢复方法局限于单一图像领域，如自然场景或遥感。
- 方法要点：构建任务和领域提示池，通过提示组合机制自适应生成领域感知任务表示。
- 实验或效果：在多个领域显著优于现有方法，并展现出强泛化能力。

## 摘要（原文）

> Recently, significant breakthroughs have been made in all-in-one image restoration (AiOIR), which can handle multiple restoration tasks with a single model. However, existing methods typically focus on a specific image domain, such as natural scene, medical imaging, or remote sensing. In this work, we aim to extend AiOIR to multiple domains and propose the first multi-domain all-in-one image restoration method, DATPRL-IR, based on our proposed Domain-Aware Task Prompt Representation Learning. Specifically, we first construct a task prompt pool containing multiple task prompts, in which task-related knowledge is implicitly encoded. For each input image, the model adaptively selects the most relevant task prompts and composes them into an instance-level task representation via a prompt composition mechanism (PCM). Furthermore, to endow the model with domain awareness, we introduce another domain prompt pool and distill domain priors from multimodal large language models into the domain prompts. PCM is utilized to combine the adaptively selected domain prompts into a domain representation for each input image. Finally, the two representations are fused to form a domain-aware task prompt representation which can make full use of both specific and shared knowledge across tasks and domains to guide the subsequent restoration process. Extensive experiments demonstrate that our DATPRL-IR significantly outperforms existing SOTA image restoration methods, while exhibiting strong generalization capabilities. Code is available at https://github.com/GuangluDong0728/DATPRL-IR.

