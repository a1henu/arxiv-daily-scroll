---
layout: default
title: Stable Language Guidance for Vision-Language-Action Models
---

# Stable Language Guidance for Vision-Language-Action Models
**arXiv**：[2601.04052v1](https://arxiv.org/abs/2601.04052) · [PDF](https://arxiv.org/pdf/2601.04052.pdf)  
**作者**：Zhihao Zhan, Yuhao Chen, Jiaying Zhou, Qinhan Lv, Hao Liu, Keze Wang, Liang Lin, Guangrun Wang  

**一句话要点**：提出Residual Semantic Steering以解决VLA模型对语言扰动脆弱的问题

**关键词**：视觉-语言-动作模型, 模态崩溃, 残差语义导向, 蒙特卡洛句法集成, 鲁棒性控制

## 3 点简述
- 核心问题：VLA模型存在模态崩溃，视觉先验压倒稀疏语言信号，导致对指令措辞过拟合
- 方法要点：引入RSS概率框架，通过蒙特卡洛句法集成和残差可供性导向，解耦物理可供性与语义执行
- 实验或效果：在多样化操作基准测试中实现最先进鲁棒性，对抗性语言扰动下保持性能

## 摘要（原文）

> Vision-Language-Action (VLA) models have demonstrated impressive capabilities in generalized robotic control; however, they remain notoriously brittle to linguistic perturbations. We identify a critical ``modality collapse'' phenomenon where strong visual priors overwhelm sparse linguistic signals, causing agents to overfit to specific instruction phrasings while ignoring the underlying semantic intent. To address this, we propose \textbf{Residual Semantic Steering (RSS)}, a probabilistic framework that disentangles physical affordance from semantic execution. RSS introduces two theoretical innovations: (1) \textbf{Monte Carlo Syntactic Integration}, which approximates the true semantic posterior via dense, LLM-driven distributional expansion, and (2) \textbf{Residual Affordance Steering}, a dual-stream decoding mechanism that explicitly isolates the causal influence of language by subtracting the visual affordance prior. Theoretical analysis suggests that RSS effectively maximizes the mutual information between action and intent while suppressing visual distractors. Empirical results across diverse manipulation benchmarks demonstrate that RSS achieves state-of-the-art robustness, maintaining performance even under adversarial linguistic perturbations.

