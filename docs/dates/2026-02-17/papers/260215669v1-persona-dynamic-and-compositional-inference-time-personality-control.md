---
layout: default
title: PERSONA: Dynamic and Compositional Inference-Time Personality Control via Activation Vector Algebra
---

# PERSONA: Dynamic and Compositional Inference-Time Personality Control via Activation Vector Algebra
**arXiv**：[2602.15669v1](https://arxiv.org/abs/2602.15669) · [PDF](https://arxiv.org/pdf/2602.15669.pdf)  
**作者**：Xiachong Feng, Liang Zhao, Weihong Zhong, Yichong Huang, Yuxuan Gu, Lingpeng Kong, Xiaocheng Feng, Bing Qin  

**一句话要点**：提出PERSONA框架，通过激活向量代数实现动态组合的推理时人格控制

**关键词**：人格控制, 激活向量代数, 推理时控制, 动态组合, 训练免费框架

## 3 点简述
- 当前LLM人格控制方法依赖静态提示或昂贵微调，难以捕捉人格的动态组合特性
- PERSONA框架在激活空间中提取正交人格向量，支持代数操作以精确控制强度和组合
- 在PersonalityBench上平均得分9.60，接近监督微调上限9.61，无需梯度更新

## 摘要（原文）

> Current methods for personality control in Large Language Models rely on static prompting or expensive fine-tuning, failing to capture the dynamic and compositional nature of human traits. We introduce PERSONA, a training-free framework that achieves fine-tuning level performance through direct manipulation of personality vectors in activation space. Our key insight is that personality traits appear as extractable, approximately orthogonal directions in the model's representation space that support algebraic operations. The framework operates through three stages: Persona-Base extracts orthogonal trait vectors via contrastive activation analysis; Persona-Algebra enables precise control through vector arithmetic (scalar multiplication for intensity, addition for composition, subtraction for suppression); and Persona-Flow achieves context-aware adaptation by dynamically composing these vectors during inference. On PersonalityBench, our approach achieves a mean score of 9.60, nearly matching the supervised fine-tuning upper bound of 9.61 without any gradient updates. On our proposed Persona-Evolve benchmark for dynamic personality adaptation, we achieve up to 91% win rates across diverse model families. These results provide evidence that aspects of LLM personality are mathematically tractable, opening new directions for interpretable and efficient behavioral control.

