---
layout: default
title: Stop Testing Attacks, Start Diagnosing Defenses: The Four-Checkpoint Framework Reveals Where LLM Safety Breaks
---

# Stop Testing Attacks, Start Diagnosing Defenses: The Four-Checkpoint Framework Reveals Where LLM Safety Breaks
**arXiv**：[2602.09629v1](https://arxiv.org/abs/2602.09629) · [PDF](https://arxiv.org/pdf/2602.09629.pdf)  
**作者**：Hayfa Dhabhi, Kashyap Thimmaraju  

**一句话要点**：提出四检查点框架以诊断LLM安全防御的失效位置与原因

**关键词**：LLM安全, 越狱攻击, 防御诊断, 检查点框架, 加权攻击成功率

## 3 点简述
- 核心问题：现有研究仅展示越狱攻击成功，未解释防御失效的具体位置与原因。
- 方法要点：将LLM安全机制建模为顺序管道，基于处理阶段和检测水平定义四个检查点。
- 实验或效果：评估三个主流LLM，发现输出阶段防御最弱，加权攻击成功率揭示更高脆弱性。

## 摘要（原文）

> Large Language Models (LLMs) deploy safety mechanisms to prevent harmful outputs, yet these defenses remain vulnerable to adversarial prompts. While existing research demonstrates that jailbreak attacks succeed, it does not explain \textit{where} defenses fail or \textit{why}.
>   To address this gap, we propose that LLM safety operates as a sequential pipeline with distinct checkpoints. We introduce the \textbf{Four-Checkpoint Framework}, which organizes safety mechanisms along two dimensions: processing stage (input vs.\ output) and detection level (literal vs.\ intent). This creates four checkpoints, CP1 through CP4, each representing a defensive layer that can be independently evaluated. We design 13 evasion techniques, each targeting a specific checkpoint, enabling controlled testing of individual defensive layers.
>   Using this framework, we evaluate GPT-5, Claude Sonnet 4, and Gemini 2.5 Pro across 3,312 single-turn, black-box test cases. We employ an LLM-as-judge approach for response classification and introduce Weighted Attack Success Rate (WASR), a severity-adjusted metric that captures partial information leakage overlooked by binary evaluation.
>   Our evaluation reveals clear patterns. Traditional Binary ASR reports 22.6\% attack success. However, WASR reveals 52.7\%, a 2.3$\times$ higher vulnerability. Output-stage defenses (CP3, CP4) prove weakest at 72--79\% WASR, while input-literal defenses (CP1) are strongest at 13\% WASR. Claude achieves the strongest safety (42.8\% WASR), followed by GPT-5 (55.9\%) and Gemini (59.5\%).
>   These findings suggest that current defenses are strongest at input-literal checkpoints but remain vulnerable to intent-level manipulation and output-stage techniques. The Four-Checkpoint Framework provides a structured approach for identifying and addressing safety vulnerabilities in deployed systems.

