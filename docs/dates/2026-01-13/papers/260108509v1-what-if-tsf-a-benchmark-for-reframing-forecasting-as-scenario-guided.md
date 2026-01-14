---
layout: default
title: What If TSF: A Benchmark for Reframing Forecasting as Scenario-Guided Multimodal Forecasting
---

# What If TSF: A Benchmark for Reframing Forecasting as Scenario-Guided Multimodal Forecasting
**arXiv**：[2601.08509v1](https://arxiv.org/abs/2601.08509) · [PDF](https://arxiv.org/pdf/2601.08509.pdf)  
**作者**：Jinkwan Jang, Hyunbin Jin, Hyungjin Park, Kyubyung Chae, Taesup Kim  

**一句话要点**：提出What If TSF基准，以评估模型在场景引导下的多模态时间序列预测能力。

**关键词**：时间序列预测, 多模态学习, 场景引导预测, 基准测试, 反事实分析

## 3 点简述
- 核心问题：现有时间序列预测方法多为单模态，且缺乏评估模型是否有效利用文本输入的基准。
- 方法要点：引入专家构建的合理或反事实场景，将预测重构为基于场景引导的多模态任务。
- 实验或效果：提供基准测试平台，用于严格评估模型在给定未来场景下的预测性能。

## 摘要（原文）

> Time series forecasting is critical to real-world decision making, yet most existing approaches remain unimodal and rely on extrapolating historical patterns. While recent progress in large language models (LLMs) highlights the potential for multimodal forecasting, existing benchmarks largely provide retrospective or misaligned raw context, making it unclear whether such models meaningfully leverage textual inputs. In practice, human experts incorporate what-if scenarios with historical evidence, often producing distinct forecasts from the same observations under different scenarios. Inspired by this, we introduce What If TSF (WIT), a multimodal forecasting benchmark designed to evaluate whether models can condition their forecasts on contextual text, especially future scenarios. By providing expert-crafted plausible or counterfactual scenarios, WIT offers a rigorous testbed for scenario-guided multimodal forecasting. The benchmark is available at https://github.com/jinkwan1115/WhatIfTSF.

