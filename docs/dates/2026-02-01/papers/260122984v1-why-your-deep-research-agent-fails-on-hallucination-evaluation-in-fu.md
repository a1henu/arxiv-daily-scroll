---
layout: default
title: Why Your Deep Research Agent Fails? On Hallucination Evaluation in Full Research Trajectory
---

# Why Your Deep Research Agent Fails? On Hallucination Evaluation in Full Research Trajectory
**arXiv**：[2601.22984v1](https://arxiv.org/abs/2601.22984) · [PDF](https://arxiv.org/pdf/2601.22984.pdf)  
**作者**：Yuhao Zhan, Tianyu Fan, Linxuan Huang, Zirui Guo, Chao Huang  

**一句话要点**：提出PIES分类法与DeepHalluBench以评估深度研究代理在完整轨迹中的幻觉问题

**关键词**：深度研究代理, 幻觉评估, PIES分类法, DeepHalluBench, 轨迹分解, 系统性缺陷

## 3 点简述
- 核心问题：现有评估方法基于端到端，掩盖了规划等中间幻觉，导致诊断失败机制困难
- 方法要点：引入PIES分类法，按功能组件和错误属性分类幻觉，并构建细粒度评估框架
- 实验或效果：在六种先进代理上测试，发现系统均不可靠，并诊断出幻觉传播和认知偏差等系统性缺陷

## 摘要（原文）

> Diagnosing the failure mechanisms of Deep Research Agents (DRAs) remains a critical challenge. Existing benchmarks predominantly rely on end-to-end evaluation, obscuring critical intermediate hallucinations, such as flawed planning, that accumulate throughout the research trajectory. To bridge this gap, we propose a shift from outcome-based to process-aware evaluation by auditing the full research trajectory. We introduce the PIES Taxonomy to categorize hallucinations along functional components (Planning vs. Summarization) and error properties (Explicit vs. Implicit). We instantiate this taxonomy into a fine-grained evaluation framework that decomposes the trajectory to rigorously quantify these hallucinations. Leveraging this framework to isolate 100 distinctively hallucination-prone tasks including adversarial scenarios, we curate DeepHalluBench. Experiments on six state-of-theart DRAs reveal that no system achieves robust reliability. Furthermore, our diagnostic analysis traces the etiology of these failures to systemic deficits, specifically hallucination propagation and cognitive biases, providing foundational insights to guide future architectural optimization. Data and code are available at https://github.com/yuhao-zhan/DeepHalluBench.

