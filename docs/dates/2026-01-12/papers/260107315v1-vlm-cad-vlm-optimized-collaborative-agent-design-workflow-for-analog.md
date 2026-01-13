---
layout: default
title: VLM-CAD: VLM-Optimized Collaborative Agent Design Workflow for Analog Circuit Sizing
---

# VLM-CAD: VLM-Optimized Collaborative Agent Design Workflow for Analog Circuit Sizing
**arXiv**：[2601.07315v1](https://arxiv.org/abs/2601.07315) · [PDF](https://arxiv.org/pdf/2601.07315.pdf)  
**作者**：Guanyuan Pan, Yugui Lin, Tiansheng Zhou, Pietro Liò, Shuai Wang, Yaqi Wang  

**一句话要点**：提出VLM-CAD工作流以解决模拟电路尺寸优化中利用不足和可解释性差的问题

**关键词**：模拟电路尺寸优化, 视觉语言模型, 可解释性优化, 协作代理设计, 贝叶斯优化, 电路图分析

## 3 点简述
- 模拟混合信号电路尺寸优化存在高维设计空间复杂权衡，现有方法未充分利用电路图且缺乏可解释性
- VLM-CAD集成Image2Net生成结构化JSON描述，结合ExTuRBO方法进行协作优化和双粒度敏感性分析
- 在放大器尺寸优化实验中，使用180nm至45nm工艺模型，实现100%成功率，总运行时间低于43分钟

## 摘要（原文）

> Analog mixed-signal circuit sizing involves complex trade-offs within high-dimensional design spaces. Existing automatic analog circuit sizing approaches often underutilize circuit schematics and lack the explainability required for industry adoption. To tackle these challenges, we propose a Vision Language Model-optimized collaborative agent design workflow (VLM-CAD), which analyzes circuits, optimizes DC operating points, performs inference-based sizing and executes external sizing optimization. We integrate Image2Net to annotate circuit schematics and generate a structured JSON description for precise interpretation by Vision Language Models. Furthermore, we propose an Explainable Trust Region Bayesian Optimization method (ExTuRBO) that employs collaborative warm-starting from agent-generated seeds and offers dual-granularity sensitivity analysis for external sizing optimization, supporting a comprehensive final design report. Experiment results on amplifier sizing tasks using 180nm, 90nm, and 45nm Predictive Technology Models demonstrate that VLM-CAD effectively balances power and performance, achieving a 100% success rate in optimizing an amplifier with a complementary input and a class-AB output stage, while maintaining total runtime under 43 minutes across all experiments.

