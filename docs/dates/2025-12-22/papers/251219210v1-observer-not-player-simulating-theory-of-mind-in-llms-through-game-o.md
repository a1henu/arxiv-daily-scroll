---
layout: default
title: Observer, Not Player: Simulating Theory of Mind in LLMs through Game Observation
---

# Observer, Not Player: Simulating Theory of Mind in LLMs through Game Observation
**arXiv**：[2512.19210v1](https://arxiv.org/abs/2512.19210) · [PDF](https://arxiv.org/pdf/2512.19210.pdf)  
**作者**：Jerry Wang, Ting Yiu Liu  

**一句话要点**：提出基于游戏观察的交互框架，评估大语言模型在序列推理中的心智理论表现

**关键词**：心智理论评估, 序列游戏推理, 大语言模型基准测试, 交互式框架, 策略识别

## 3 点简述
- 核心问题：评估大语言模型是否能在简单策略游戏中展现类似心智的序列推理能力
- 方法要点：将模型设为观察者，通过基准测试和统一损失度量预测与真实策略的对齐
- 实验或效果：系统支持实时交互和可视化，量化模型在策略识别和推理中的表现

## 摘要（原文）

> We present an interactive framework for evaluating whether large language models (LLMs) exhibit genuine "understanding" in a simple yet strategic environment. As a running example, we focus on Rock-Paper-Scissors (RPS), which, despite its apparent simplicity, requires sequential reasoning, adaptation, and strategy recognition. Our system positions the LLM as an Observer whose task is to identify which strategies are being played and to articulate the reasoning behind this judgment. The purpose is not to test knowledge of Rock-Paper-Scissors itself, but to probe whether the model can exhibit mind-like reasoning about sequential behavior. To support systematic evaluation, we provide a benchmark consisting of both static strategies and lightweight dynamic strategies specified by well-prompted rules. We quantify alignment between the Observer's predictions and the ground-truth distributions induced by actual strategy pairs using three complementary signals: Cross-Entropy, Brier score, and Expected Value (EV) discrepancy. These metrics are further integrated into a unified score, the Union Loss, which balances calibration, sensitivity, and payoff alignment. Together with a Strategy Identification Rate (SIR) metric, our framework captures not only predictive accuracy but also whether the model can stably identify the latent strategies in play. The demo emphasizes interactivity, transparency, and reproducibility. Users can adjust LLM distributions in real time, visualize losses as they evolve, and directly inspect reasoning snippets to identify where and why failures occur. In doing so, our system provides a practical and interpretable proxy for mind-like inference in sequential games, offering insights into both the strengths and limitations of current LLM reasoning.

