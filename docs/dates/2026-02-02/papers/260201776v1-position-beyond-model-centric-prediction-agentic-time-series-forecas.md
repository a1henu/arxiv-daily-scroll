---
layout: default
title: Position: Beyond Model-Centric Prediction -- Agentic Time Series Forecasting
---

# Position: Beyond Model-Centric Prediction -- Agentic Time Series Forecasting
**arXiv**：[2602.01776v1](https://arxiv.org/abs/2602.01776) · [PDF](https://arxiv.org/pdf/2602.01776.pdf)  
**作者**：Mingyue Cheng, Xiaoyu Tao, Qi Liu, Ze Guo, Enhong Chen  

**一句话要点**：提出代理时间序列预测以解决自适应多轮预测中的模型中心化局限

**关键词**：时间序列预测, 代理系统, 自适应预测, 工作流设计, 强化学习

## 3 点简述
- 核心问题：传统时间序列预测为模型中心化、静态单次预测，不适应自适应多轮场景。
- 方法要点：将预测重构为代理过程，包含感知、规划、行动、反思和记忆组件。
- 实验或效果：未知，但讨论了基于工作流、代理强化学习和混合代理工作流三种实现范式。

## 摘要（原文）

> Time series forecasting has traditionally been formulated as a model-centric, static, and single-pass prediction problem that maps historical observations to future values. While this paradigm has driven substantial progress, it proves insufficient in adaptive and multi-turn settings where forecasting requires informative feature extraction, reasoning-driven inference, iterative refinement, and continual adaptation over time. In this paper, we argue for agentic time series forecasting (ATSF), which reframes forecasting as an agentic process composed of perception, planning, action, reflection, and memory. Rather than focusing solely on predictive models, ATSF emphasizes organizing forecasting as an agentic workflow that can interact with tools, incorporate feedback from outcomes, and evolve through experience accumulation. We outline three representative implementation paradigms -- workflow-based design, agentic reinforcement learning, and a hybrid agentic workflow paradigm -- and discuss the opportunities and challenges that arise when shifting from model-centric prediction to agentic forecasting. Together, this position aims to establish agentic forecasting as a foundation for future research at the intersection of time series forecasting.

