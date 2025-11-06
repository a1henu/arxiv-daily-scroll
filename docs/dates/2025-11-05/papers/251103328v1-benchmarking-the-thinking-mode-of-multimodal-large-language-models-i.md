---
layout: default
title: Benchmarking the Thinking Mode of Multimodal Large Language Models in Clinical Tasks
---

# Benchmarking the Thinking Mode of Multimodal Large Language Models in Clinical Tasks
**arXiv**：[2511.03328v1](https://arxiv.org/abs/2511.03328) · [PDF](https://arxiv.org/pdf/2511.03328.pdf)  
**作者**：Jindong Hong, Tianjie Chen, Lingjie Luo, Chuanyang Zheng, Ting Xu, Haibao Yu, Jianing Qiu, Qianzhong Chen, Suning Huang, Yan Xu, Yong Gui, Yijun He, Jiankai Sun  

**一句话要点**：评估多模态大语言模型在临床任务中思维模式对性能的影响

**关键词**：多模态大语言模型, 临床任务评估, 思维模式, 医学图像解释, 视觉问答

## 3 点简述
- 核心问题：评估MLLMs的思维模式在临床任务中是否显著提升模型性能与可靠性。
- 方法要点：比较Seed1.5-VL和Gemini-2.5-Flash在思维模式与非思维模式下的表现。
- 实验或效果：思维模式对多数任务改进有限，复杂医疗任务表现仍不理想。

## 摘要（原文）

> A recent advancement in Multimodal Large Language Models (MLLMs) research is
> the emergence of "reasoning MLLMs" that offer explicit control over their
> internal thinking processes (normally referred as the "thinking mode")
> alongside the standard "non-thinking mode". This capability allows these models
> to engage in a step-by-step process of internal deliberation before generating
> a final response. With the rapid transition to and adoption of these
> "dual-state" MLLMs, this work rigorously evaluated how the enhanced reasoning
> processes of these MLLMs impact model performance and reliability in clinical
> tasks. This paper evaluates the active "thinking mode" capabilities of two
> leading MLLMs, Seed1.5-VL and Gemini-2.5-Flash, for medical applications. We
> assessed their performance on four visual medical tasks using VQA-RAD and
> ROCOv2 datasets. Our findings reveal that the improvement from activating the
> thinking mode remains marginal compared to the standard non-thinking mode for
> the majority of the tasks. Their performance on complex medical tasks such as
> open-ended VQA and medical image interpretation remains suboptimal,
> highlighting the need for domain-specific medical data and more advanced
> methods for medical knowledge integration.

