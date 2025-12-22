---
layout: default
title: Generative Human-Object Interaction Detection via Differentiable Cognitive Steering of Multi-modal LLMs
---

# Generative Human-Object Interaction Detection via Differentiable Cognitive Steering of Multi-modal LLMs
**arXiv**：[2512.17640v1](https://arxiv.org/abs/2512.17640) · [PDF](https://arxiv.org/pdf/2512.17640.pdf)  
**作者**：Zhaolin Cai, Huiyu Duan, Zitong Xu, Fan Li, Zhi Liu, Jing Liu, Wei Shen, Xiongkuo Min, Guangtao Zhai  

**一句话要点**：提出GRASP-HO框架，通过可学习认知引导模块将人-物交互检测转化为开放词汇生成问题。

**关键词**：人-物交互检测, 开放词汇生成, 多模态大语言模型, 认知引导, 零样本泛化

## 3 点简述
- 核心问题：现有方法基于封闭世界假设，难以泛化到未见或模糊交互的长尾场景。
- 方法要点：设计轻量级认知引导模块，将细粒度视觉证据注入冻结多模态大语言模型进行推理。
- 实验或效果：在封闭集性能上达到最优，并展示强大的零样本泛化能力。

## 摘要（原文）

> Human-object interaction (HOI) detection aims to localize human-object pairs and the interactions between them. Existing methods operate under a closed-world assumption, treating the task as a classification problem over a small, predefined verb set, which struggles to generalize to the long-tail of unseen or ambiguous interactions in the wild. While recent multi-modal large language models (MLLMs) possess the rich world knowledge required for open-vocabulary understanding, they remain decoupled from existing HOI detectors since fine-tuning them is computationally prohibitive. To address these constraints, we propose \GRASP-HO}, a novel Generative Reasoning And Steerable Perception framework that reformulates HOI detection from the closed-set classification task to the open-vocabulary generation problem. To bridge the vision and cognitive, we first extract hybrid interaction representations, then design a lightweight learnable cognitive steering conduit (CSC) module to inject the fine-grained visual evidence into a frozen MLLM for effective reasoning. To address the supervision mismatch between classification-based HOI datasets and open-vocabulary generative models, we introduce a hybrid guidance strategy that coupling the language modeling loss and auxiliary classification loss, enabling discriminative grounding without sacrificing generative flexibility. Experiments demonstrate state-of-the-art closed-set performance and strong zero-shot generalization, achieving a unified paradigm that seamlessly bridges discriminative perception and generative reasoning for open-world HOI detection.

