---
layout: default
title: Eroding the Truth-Default: A Causal Analysis of Human Susceptibility to Foundation Model Hallucinations and Disinformation in the Wild
---

# Eroding the Truth-Default: A Causal Analysis of Human Susceptibility to Foundation Model Hallucinations and Disinformation in the Wild
**arXiv**：[2601.22871v1](https://arxiv.org/abs/2601.22871) · [PDF](https://arxiv.org/pdf/2601.22871.pdf)  
**作者**：Alexander Loth, Martin Kappes, Marc-Oliver Pahl  

**一句话要点**：提出JudgeGPT与RogueGPT框架，通过因果分析揭示人类对基础模型幻觉与虚假信息的认知机制

**关键词**：基础模型幻觉, 虚假信息检测, 结构因果模型, 认知机制分析, 可信人工智能

## 3 点简述
- 核心问题：基础模型生成内容与人类文本难以区分，威胁可信网络信息生态
- 方法要点：构建双轴框架分离真实性判断与来源归因，采用结构因果模型分析检测机制
- 实验效果：发现熟悉度影响检测能力，GPT-4输出存在绕过来源监控的流畅性陷阱

## 摘要（原文）

> As foundation models (FMs) approach human-level fluency, distinguishing synthetic from organic content has become a key challenge for Trustworthy Web Intelligence.
>   This paper presents JudgeGPT and RogueGPT, a dual-axis framework that decouples "authenticity" from "attribution" to investigate the mechanisms of human susceptibility. Analyzing 918 evaluations across five FMs (including GPT-4 and Llama-2), we employ Structural Causal Models (SCMs) as a principal framework for formulating testable causal hypotheses about detection accuracy.
>   Contrary to partisan narratives, we find that political orientation shows a negligible association with detection performance ($r=-0.10$). Instead, "fake news familiarity" emerges as a candidate mediator ($r=0.35$), suggesting that exposure may function as adversarial training for human discriminators. We identify a "fluency trap" where GPT-4 outputs (HumanMachineScore: 0.20) bypass Source Monitoring mechanisms, rendering them indistinguishable from human text.
>   These findings suggest that "pre-bunking" interventions should target cognitive source monitoring rather than demographic segmentation to ensure trustworthy information ecosystems.

