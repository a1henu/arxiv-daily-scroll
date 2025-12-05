---
layout: default
title: Towards an AI Fluid Scientist: LLM-Powered Scientific Discovery in Experimental Fluid Mechanics
---

# Towards an AI Fluid Scientist: LLM-Powered Scientific Discovery in Experimental Fluid Mechanics
**arXiv**：[2512.04716v1](https://arxiv.org/abs/2512.04716) · [PDF](https://arxiv.org/pdf/2512.04716.pdf)  
**作者**：Haodong Feng, Lugang Ye, Dixia Fan  

**一句话要点**：提出AI流体科学家框架，实现实验流体力学全流程自主研究

**关键词**：实验流体力学, AI流体科学家, 多智能体系统, 涡激振动, 自主实验, 神经网络拟合

## 3 点简述
- 核心问题：AI在实验流体力学中应用局限，多集中于数值研究，缺乏端到端实验自动化。
- 方法要点：构建多智能体虚实交互系统，涵盖假设生成、实验设计、机器人执行、数据分析和论文撰写。
- 实验或效果：在串联圆柱体涡激振动和尾流诱导振动研究中，自动复现文献基准，发现新现象，神经网络拟合物理定律优于多项式31%。

## 摘要（原文）

> The integration of artificial intelligence into experimental fluid mechanics promises to accelerate discovery, yet most AI applications remain narrowly focused on numerical studies. This work proposes an AI Fluid Scientist framework that autonomously executes the complete experimental workflow: hypothesis generation, experimental design, robotic execution, data analysis, and manuscript preparation. We validate this through investigation of vortex-induced vibration (VIV) and wake-induced vibration (WIV) in tandem cylinders. Our work has four key contributions: (1) A computer-controlled circulating water tunnel (CWT) with programmatic control of flow velocity, cylinder position, and forcing parameters (vibration frequency and amplitude) with data acquisition (displacement, force, and torque). (2) Automated experiments reproduce literature benchmarks (Khalak and Williamson [1999] and Assi et al. [2013, 2010]) with frequency lock-in within 4% and matching critical spacing trends. (3) The framework with Human-in-the-Loop (HIL) discovers more WIV amplitude response phenomena, and uses a neural network to fit physical laws from data, which is 31% higher than that of polynomial fitting. (4) The framework with multi-agent with virtual-real interaction system executes hundreds of experiments end-to-end, which automatically completes the entire process of scientific research from hypothesis generation, experimental design, experimental execution, data analysis, and manuscript preparation. It greatly liberates human researchers and improves study efficiency, providing new paradigm for the development and research of experimental fluid mechanics.

