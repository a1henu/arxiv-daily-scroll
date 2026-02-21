---
layout: default
title: ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment
---

# ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment
**arXiv**：[2602.17560v1](https://arxiv.org/abs/2602.17560) · [PDF](https://arxiv.org/pdf/2602.17560.pdf)  
**作者**：Hongjue Zhao, Haosen Sun, Jiangtao Kong, Xiaochang Li, Qineng Wang, Liwei Jiang, Qi Zhu, Tarek Abdelzaher, Yejin Choi, Manling Li, Huajie Shao  

**一句话要点**：提出基于常微分方程的ODESteer框架，以统一理论指导大语言模型对齐中的激活操控。

**关键词**：大语言模型对齐, 激活操控, 常微分方程框架, 屏障函数, 多步自适应操控, 模型对齐基准

## 3 点简述
- 核心问题：现有激活操控方法缺乏统一理论框架，且单步操控难以捕捉复杂激活分布模式。
- 方法要点：将激活加法解释为常微分方程一阶近似，基于控制理论设计屏障函数指导多步自适应操控。
- 实验或效果：在TruthfulQA等基准上实现显著提升，如TruthfulQA提升5.7%，验证了理论框架的有效性。

## 摘要（原文）

> Activation steering, or representation engineering, offers a lightweight approach to align large language models (LLMs) by manipulating their internal activations at inference time. However, current methods suffer from two key limitations: \textit{(i)} the lack of a unified theoretical framework for guiding the design of steering directions, and \textit{(ii)} an over-reliance on \textit{one-step steering} that fail to capture complex patterns of activation distributions. In this work, we propose a unified ordinary differential equations (ODEs)-based \textit{theoretical} framework for activation steering in LLM alignment. We show that conventional activation addition can be interpreted as a first-order approximation to the solution of an ODE. Based on this ODE perspective, identifying a steering direction becomes equivalent to designing a \textit{barrier function} from control theory. Derived from this framework, we introduce ODESteer, a kind of ODE-based steering guided by barrier functions, which shows \textit{empirical} advancement in LLM alignment. ODESteer identifies steering directions by defining the barrier function as the log-density ratio between positive and negative activations, and employs it to construct an ODE for \textit{multi-step and adaptive} steering. Compared to state-of-the-art activation steering methods, ODESteer achieves consistent empirical improvements on diverse LLM alignment benchmarks, a notable $5.7\%$ improvement over TruthfulQA, $2.5\%$ over UltraFeedback, and $2.4\%$ over RealToxicityPrompts. Our work establishes a principled new view of activation steering in LLM alignment by unifying its theoretical foundations via ODEs, and validating it empirically through the proposed ODESteer method.

