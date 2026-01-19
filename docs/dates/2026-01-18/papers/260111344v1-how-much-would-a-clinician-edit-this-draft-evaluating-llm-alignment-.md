---
layout: default
title: How Much Would a Clinician Edit This Draft? Evaluating LLM Alignment for Patient Message Response Drafting
---

# How Much Would a Clinician Edit This Draft? Evaluating LLM Alignment for Patient Message Response Drafting
**arXiv**：[2601.11344v1](https://arxiv.org/abs/2601.11344) · [PDF](https://arxiv.org/pdf/2601.11344.pdf)  
**作者**：Parker Seegmiller, Joseph Gatto, Sarah E. Greer, Ganza Belise Isingizwe, Rohan Ray, Timothy E. Burdick, Sarah Masud Preum  

**一句话要点**：提出主题编辑负载评估框架，以解决LLM在患者消息回复草拟中与临床医生对齐的不确定性。

**关键词**：患者消息回复草拟, LLM对齐评估, 临床工作流集成, 主题编辑负载, 检索增强生成, 监督微调

## 3 点简述
- 核心问题：评估LLM草拟患者消息回复时与临床医生对齐的编辑负载，关注节省临床工作时间的实际效果。
- 方法要点：开发临床医生回复主题分类法，构建内容与主题层面的编辑负载评估框架，结合主题提示、检索增强生成等技术进行模型适配。
- 实验或效果：大规模评估显示LLM在部分主题生成能力强，但在提问等主题对齐困难，主题驱动适配策略能提升多数主题表现。

## 摘要（原文）

> Large language models (LLMs) show promise in drafting responses to patient portal messages, yet their integration into clinical workflows raises various concerns, including whether they would actually save clinicians time and effort in their portal workload. We investigate LLM alignment with individual clinicians through a comprehensive evaluation of the patient message response drafting task. We develop a novel taxonomy of thematic elements in clinician responses and propose a novel evaluation framework for assessing clinician editing load of LLM-drafted responses at both content and theme levels. We release an expert-annotated dataset and conduct large-scale evaluations of local and commercial LLMs using various adaptation techniques including thematic prompting, retrieval-augmented generation, supervised fine-tuning, and direct preference optimization. Our results reveal substantial epistemic uncertainty in aligning LLM drafts with clinician responses. While LLMs demonstrate capability in drafting certain thematic elements, they struggle with clinician-aligned generation in other themes, particularly question asking to elicit further information from patients. Theme-driven adaptation strategies yield improvements across most themes. Our findings underscore the necessity of adapting LLMs to individual clinician preferences to enable reliable and responsible use in patient-clinician communication workflows.

