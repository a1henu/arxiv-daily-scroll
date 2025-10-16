---
layout: default
title: MMLongCite: A Benchmark for Evaluating Fidelity of Long-Context Vision-Language Models
---

# MMLongCite: A Benchmark for Evaluating Fidelity of Long-Context Vision-Language Models
**arXiv**：[2510.13276v1](https://arxiv.org/abs/2510.13276) · [PDF](https://arxiv.org/pdf/2510.13276.pdf)  
**作者**：Keyan Zhou, Zecheng Tang, Lingfeng Ming, Guanghao Zhou, Qiguang Chen, Dan Qiao, Zheming Yang, Libo Qin, Minghui Qiu, Juntao Li, Min Zhang  

**一句话要点**：提出MMLongCite基准以评估长上下文视觉语言模型的忠实性

**关键词**：长上下文评估, 视觉语言模型, 多模态基准, 忠实性分析, 上下文长度影响

## 3 点简述
- 核心问题：长上下文窗口不保证有效利用，影响多模态应用。
- 方法要点：构建涵盖多模态和长度区间的综合基准。
- 实验或效果：评估显示模型忠实性有限，分析长度和内容位置影响。

## 摘要（原文）

> The rapid advancement of large vision language models (LVLMs) has led to a
> significant expansion of their context windows. However, an extended context
> window does not guarantee the effective utilization of the context, posing a
> critical challenge for real-world applications. Current evaluations of such
> long-context faithfulness are predominantly focused on the text-only domain,
> while multimodal assessments remain limited to short contexts. To bridge this
> gap, we introduce MMLongCite, a comprehensive benchmark designed to evaluate
> the fidelity of LVLMs in long-context scenarios. MMLongCite comprises 8
> distinct tasks spanning 6 context length intervals and incorporates diverse
> modalities, including text, images, and videos. Our evaluation of
> state-of-the-art LVLMs reveals their limited faithfulness in handling long
> multimodal contexts. Furthermore, we provide an in-depth analysis of how
> context length and the position of crucial content affect the faithfulness of
> these models.

