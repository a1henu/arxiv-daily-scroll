---
layout: default
title: Agentic Confidence Calibration
---

# Agentic Confidence Calibration
**arXiv**：[2601.15778v1](https://arxiv.org/abs/2601.15778) · [PDF](https://arxiv.org/pdf/2601.15778.pdf)  
**作者**：Jiaxin Zhang, Caiming Xiong, Chien-Sheng Wu  

**一句话要点**：提出Holistic Trajectory Calibration以解决AI代理在复杂任务中的过度自信问题

**关键词**：AI代理校准, 轨迹校准, 置信度校准, 过程特征提取, 泛化校准器, 多步任务可靠性

## 3 点简述
- 核心问题：现有校准方法无法处理代理系统在轨迹中的复合错误、外部工具不确定性和不透明失败模式。
- 方法要点：引入Agentic Confidence Calibration问题，提出HTC框架，提取代理轨迹的宏观动态和微观稳定性特征。
- 实验或效果：HTC在八个基准测试中超越基线，提供可解释性、可转移性和泛化性，在GAIA基准上实现最佳校准。

## 摘要（原文）

> AI agents are rapidly advancing from passive language models to autonomous systems executing complex, multi-step tasks. Yet their overconfidence in failure remains a fundamental barrier to deployment in high-stakes settings. Existing calibration methods, built for static single-turn outputs, cannot address the unique challenges of agentic systems, such as compounding errors along trajectories, uncertainty from external tools, and opaque failure modes. To address these challenges, we introduce, for the first time, the problem of Agentic Confidence Calibration and propose Holistic Trajectory Calibration (HTC), a novel diagnostic framework that extracts rich process-level features ranging from macro dynamics to micro stability across an agent's entire trajectory. Powered by a simple, interpretable model, HTC consistently surpasses strong baselines in both calibration and discrimination, across eight benchmarks, multiple LLMs, and diverse agent frameworks. Beyond performance, HTC delivers three essential advances: it provides interpretability by revealing the signals behind failure, enables transferability by applying across domains without retraining, and achieves generalization through a General Agent Calibrator (GAC) that achieves the best calibration (lowest ECE) on the out-of-domain GAIA benchmark. Together, these contributions establish a new process-centric paradigm for confidence calibration, providing a framework for diagnosing and enhancing the reliability of AI agents.

