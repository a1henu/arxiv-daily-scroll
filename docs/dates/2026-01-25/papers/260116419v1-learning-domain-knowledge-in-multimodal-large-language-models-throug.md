---
layout: default
title: Learning Domain Knowledge in Multimodal Large Language Models through Reinforcement Fine-Tuning
---

# Learning Domain Knowledge in Multimodal Large Language Models through Reinforcement Fine-Tuning
**arXiv**：[2601.16419v1](https://arxiv.org/abs/2601.16419) · [PDF](https://arxiv.org/pdf/2601.16419.pdf)  
**作者**：Qinglong Cao, Yuntian Chen, Chao Ma, Xiaokang Yang  

**一句话要点**：提出强化微调框架，通过优化级整合领域知识以提升多模态大语言模型在遥感与医疗等专业领域的性能。

**关键词**：多模态大语言模型, 领域适应, 强化微调, 遥感图像, 医疗影像, 优化级整合

## 3 点简述
- 当前多模态大语言模型在遥感、医疗等专业领域表现有限，仅通过文本指令注入领域知识效果不佳。
- 提出强化微调框架，将领域知识编码为约束和奖励信号，直接整合到学习目标中。
- 在多个遥感与医疗数据集上实验，取得性能提升，达到领域任务的最先进水平。

## 摘要（原文）

> Multimodal large language models (MLLMs) have shown remarkable capabilities in multimodal perception and understanding tasks. However, their effectiveness in specialized domains, such as remote sensing and medical imaging, remains limited. A natural approach to domain adaptation is to inject domain knowledge through textual instructions, prompts, or auxiliary captions. Surprisingly, we find that such input-level domain knowledge injection yields little to no improvement on scientific multimodal tasks, even when the domain knowledge is explicitly provided. This observation suggests that current MLLMs fail to internalize domain-specific priors through language alone, and that domain knowledge must be integrated at the optimization level. Motivated by this insight, we propose a reinforcement fine-tuning framework that incorporates domain knowledge directly into the learning objective. Instead of treating domain knowledge as descriptive information, we encode it as domain-informed constraints and reward signals, shaping the model's behavior in the output space. Extensive experiments across multiple datasets in remote sensing and medical domains consistently demonstrate good performance gains, achieving state-of-the-art results on multimodal domain tasks. Our results highlight the necessity of optimization-level domain knowledge integration and reveal a fundamental limitation of textual domain conditioning in current MLLMs.

