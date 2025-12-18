---
layout: default
title: Stock Pattern Assistant (SPA): A Deterministic and Explainable Framework for Structural Price Run Extraction and Event Correlation in Equity Markets
---

# Stock Pattern Assistant (SPA): A Deterministic and Explainable Framework for Structural Price Run Extraction and Event Correlation in Equity Markets
**arXiv**：[2512.15008v1](https://arxiv.org/abs/2512.15008) · [PDF](https://arxiv.org/pdf/2512.15008.pdf)  
**作者**：Sandeep Neela  

**一句话要点**：提出Stock Pattern Assistant框架，以确定性方法提取价格结构并关联事件，增强股市分析的可解释性。

**关键词**：股票模式提取, 可解释性框架, 事件关联, 确定性分析, 价格结构分解

## 3 点简述
- 核心问题：现有技术指标和预测模型缺乏透明度和可解释性，难以满足审计需求。
- 方法要点：基于日OHLCV数据和事件流，确定性提取单调价格运行，并通过对称窗口关联事件生成解释。
- 实验或效果：在四只股票上评估，展示稳定结构分解和上下文叙事，消融实验验证各组件对可解释性的贡献。

## 摘要（原文）

> Understanding how prices evolve over time often requires peeling back the layers of market noise to identify clear, structural behavior. Many of the tools commonly used for this purpose technical indicators, chart heuristics, or even sophisticated predictive models leave important questions unanswered. Technical indicators depend on platform-specific rules, and predictive systems typically offer little in terms of explanation. In settings that demand transparency or auditability, this poses a significant challenge. We introduce the Stock Pattern Assistant (SPA), a deterministic framework designed to extract monotonic price runs, attach relevant public events through a symmetric correlation window, and generate explanations that are factual, historical, and guardrailed. SPA relies only on daily OHLCV data and a normalized event stream, making the pipeline straight-forward to audit and easy to reproduce. To illustrate SPA's behavior in practice, we evaluate it across four equities-AAPL, NVDA, SCHW, and PGR-chosen to span a range of volatility regimes and sector characteristics. Although the evaluation period is modest, the results demonstrate how SPA consistently produces stable structural decompositions and contextual narratives. Ablation experiments further show how deterministic segmentation, event alignment, and constrained explanation each contribute to interpretability. SPA is not a forecasting system, nor is it intended to produce trading signals. Its value lies in offering a transparent, reproducible view of historical price structure that can complement analyst workflows, risk reviews, and broader explainable-AI pipelines.

