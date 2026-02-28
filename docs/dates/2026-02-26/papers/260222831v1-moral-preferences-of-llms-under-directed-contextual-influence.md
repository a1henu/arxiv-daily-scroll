---
layout: default
title: Moral Preferences of LLMs Under Directed Contextual Influence
---

# Moral Preferences of LLMs Under Directed Contextual Influence
**arXiv**：[2602.22831v1](https://arxiv.org/abs/2602.22831) · [PDF](https://arxiv.org/pdf/2602.22831.pdf)  
**作者**：Phil Blandfort, Tushar Karayil, Urja Pawar, Robert Graham, Alex McKenzie, Dmitrii Krasheninnikov  

**一句话要点**：提出基于定向翻转上下文的评估框架，研究LLM在电车问题式道德分流中的决策可操纵性。

**关键词**：大语言模型道德评估, 上下文影响, 电车问题, 决策可操纵性, 定向翻转实验, 道德分流

## 3 点简述
- 核心问题：LLM的道德基准通常假设稳定偏好，但实际部署中上下文信号可能显著影响决策。
- 方法要点：引入定向翻转上下文影响的评估框架，通过匹配翻转的上下文系统测量方向性响应。
- 实验或效果：发现上下文影响常显著改变决策，基线偏好预测性差，影响可能适得其反，推理降低平均敏感性但放大偏见示例效应。

## 摘要（原文）

> Moral benchmarks for LLMs typically use context-free prompts, implicitly assuming stable preferences. In deployment, however, prompts routinely include contextual signals such as user requests, cues on social norms, etc. that may steer decisions. We study how directed contextual influences reshape decisions in trolley-problem-style moral triage settings. We introduce a pilot evaluation harness for directed contextual influence in trolley-problem-style moral triage: for each demographic factor, we apply matched, direction-flipped contextual influences that differ only in which group they favor, enabling systematic measurement of directional response. We find that: (i) contextual influences often significantly shift decisions, even when only superficially relevant; (ii) baseline preferences are a poor predictor of directional steerability, as models can appear baseline-neutral yet exhibit systematic steerability asymmetry under influence; (iii) influences can backfire: models may explicitly claim neutrality or discount the contextual cue, yet their choices still shift, sometimes in the opposite direction; and (iv) reasoning reduces average sensitivity, but amplifies the effect of biased few-shot examples. Our findings motivate extending moral evaluations with controlled, direction-flipped context manipulations to better characterize model behavior.

