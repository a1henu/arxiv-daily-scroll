---
layout: default
title: Reflection Pretraining Enables Token-Level Self-Correction in Biological Sequence Models
---

# Reflection Pretraining Enables Token-Level Self-Correction in Biological Sequence Models
**arXiv**：[2512.20954v1](https://arxiv.org/abs/2512.20954) · [PDF](https://arxiv.org/pdf/2512.20954.pdf)  
**作者**：Xiang Zhang, Jiaqi Wei, Yuejin Yang, Zijie Qiu, Yuhan Chen, Zhiqiang Gao, Muhammad Abdul-Mageed, Laks V. S. Lakshmanan, Wanli Ouyang, Chenyu You, Siqi Sun  

**一句话要点**：提出反射预训练以增强生物序列模型的自校正能力

**关键词**：反射预训练, 生物序列模型, 链式思维, 语言表达力, 自校正, 蛋白质语言模型

## 3 点简述
- 生物序列模型因标记表达力有限，无法应用链式思维推理
- 通过反射预训练引入辅助思考标记，提升语言表达力
- 实验显示该方法显著提高蛋白质模型性能，实现自校正

## 摘要（原文）

> Chain-of-Thought (CoT) prompting has significantly advanced task-solving capabilities in natural language processing with large language models. Unlike standard prompting, CoT encourages the model to generate intermediate reasoning steps, non-answer tokens, that help guide the model toward more accurate final outputs. These intermediate steps enable more complex reasoning processes such as error correction, memory management, future planning, and self-reflection. However, applying CoT to non-natural language domains, such as protein and RNA language models, is not yet possible, primarily due to the limited expressiveness of their token spaces (e.g., amino acid tokens). In this work, we propose and define the concept of language expressiveness: the ability of a given language, using its tokens and grammar, to encode information. We show that the limited expressiveness of protein language severely restricts the applicability of CoT-style reasoning. To overcome this, we introduce reflection pretraining, for the first time in a biological sequence model, which enables the model to engage in intermediate reasoning through the generation of auxiliary "thinking tokens" beyond simple answer tokens. Theoretically, we demonstrate that our augmented token set significantly enhances biological language expressiveness, thereby improving the overall reasoning capacity of the model. Experimentally, our pretraining approach teaches protein models to self-correct and leads to substantial performance gains compared to standard pretraining.

