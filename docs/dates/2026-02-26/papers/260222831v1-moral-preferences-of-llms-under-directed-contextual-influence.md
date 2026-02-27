---
layout: default
title: Moral Preferences of LLMs Under Directed Contextual Influence
---

# Moral Preferences of LLMs Under Directed Contextual Influence
**arXiv**：[2602.22831v1](https://arxiv.org/abs/2602.22831) · [PDF](https://arxiv.org/pdf/2602.22831.pdf)  
**作者**：Phil Blandfort, Tushar Karayil, Urja Pawar, Robert Graham, Alex McKenzie, Dmitrii Krasheninnikov  

**一句话要点**：提出定向上下文影响评估框架，研究LLM在道德困境中的决策可操纵性。

**关键词**：大语言模型道德评估, 上下文影响, 道德困境, 定向操纵, 可操纵性不对称, 推理敏感性

## 3 点简述
- 核心问题：LLM道德基准常忽略上下文信号对决策的潜在影响。
- 方法要点：设计匹配翻转上下文，系统测量定向响应与可操纵性不对称。
- 实验效果：发现上下文显著改变决策，基线偏好无法预测可操纵性，推理降低平均敏感性但放大偏见示例影响。

## 摘要（原文）

> Moral benchmarks for LLMs typically use context-free prompts, implicitly assuming stable preferences. In deployment, however, prompts routinely include contextual signals such as user requests, cues on social norms, etc. that may steer decisions. We study how directed contextual influences reshape decisions in trolley-problem-style moral triage settings. We introduce a pilot evaluation harness for directed contextual influence in trolley-problem-style moral triage: for each demographic factor, we apply matched, direction-flipped contextual influences that differ only in which group they favor, enabling systematic measurement of directional response. We find that: (i) contextual influences often significantly shift decisions, even when only superficially relevant; (ii) baseline preferences are a poor predictor of directional steerability, as models can appear baseline-neutral yet exhibit systematic steerability asymmetry under influence; (iii) influences can backfire: models may explicitly claim neutrality or discount the contextual cue, yet their choices still shift, sometimes in the opposite direction; and (iv) reasoning reduces average sensitivity, but amplifies the effect of biased few-shot examples. Our findings motivate extending moral evaluations with controlled, direction-flipped context manipulations to better characterize model behavior.

