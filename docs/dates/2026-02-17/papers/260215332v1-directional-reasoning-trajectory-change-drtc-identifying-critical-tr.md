---
layout: default
title: Directional Reasoning Trajectory Change (DRTC): Identifying Critical Trace Segments in Reasoning Models
---

# Directional Reasoning Trajectory Change (DRTC): Identifying Critical Trace Segments in Reasoning Models
**arXiv**：[2602.15332v1](https://arxiv.org/abs/2602.15332) · [PDF](https://arxiv.org/pdf/2602.15332.pdf)  
**作者**：Waldemar Chang  

**一句话要点**：提出DRTC框架以识别语言模型长程推理中的关键转折点

**关键词**：推理模型解释, 因果干预, 轨迹分析, 长程推理, 决策点检测

## 3 点简述
- 核心问题：现有方法难以揭示模型推理中的因果转折点及触发上下文
- 方法要点：基于不确定性和分布偏移检测决策点，通过接收端干预测量轨迹变化
- 实验或效果：在四个模型上显示影响高度集中，学习到的跨度优于随机跨度

## 摘要（原文）

> Understanding how language models carry out long-horizon reasoning remains an open challenge. Existing interpretability methods often highlight tokens or spans correlated with an answer, but they rarely reveal where the model makes consequential reasoning turns, which earlier context causally triggers those turns, or whether the highlighted text actually steers the reasoning process. We introduce Directional Reasoning Trajectory Change (DRTC), a process-causal framework for interpreting long-form reasoning from a single on-policy rollout. DRTC detects pivot decision points using uncertainty and distribution-shift signals, then applies receiver-side interventions that preserve the realized rollout without resampling the continuation while blocking information flow from selected earlier chunks only at a pivot. It measures whether each intervention redirects the direction of the model's log-probability trajectory relative to the realized rollout direction, producing a signed per-chunk attribution score. We also compute turning-angle curvature changes on raw logits as a complementary diagnostic and introduce curvature signatures to summarize shared intervention-response geometry. Empirically, directional influence is sharply concentrated across four reasoning models (per-example \|DRTC\| shares yield Gini 0.50 to 0.58 and top-5 percent mass 0.23 to 0.28), and learned pivots induce stronger intervention magnitudes than matched random spans. In a scaling study on 500 MATH problems with R1-Distill-Qwen-1.5B, learned spans outperform matched random spans (median delta = 0.409, 355 of 500 positive; sign test p = 2.3e-21). Overall, DRTC provides a causally grounded, trajectory-level view of how specific context elements steer reasoning under on-policy dynamics.

