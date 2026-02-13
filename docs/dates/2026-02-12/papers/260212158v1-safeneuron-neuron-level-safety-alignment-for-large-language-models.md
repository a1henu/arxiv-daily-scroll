---
layout: default
title: SafeNeuron: Neuron-Level Safety Alignment for Large Language Models
---

# SafeNeuron: Neuron-Level Safety Alignment for Large Language Models
**arXiv**：[2602.12158v1](https://arxiv.org/abs/2602.12158) · [PDF](https://arxiv.org/pdf/2602.12158.pdf)  
**作者**：Zhaoxin Wang, Jiaming Liang, Fengbin Zhu, Weixiang Zhao, Junfeng Fang, Jiayi Ji, Handing Wang, Tat-Seng Chua  

**一句话要点**：提出SafeNeuron框架，通过神经元级安全对齐增强大语言模型鲁棒性

**关键词**：神经元级安全对齐, 大语言模型鲁棒性, 偏好优化, 安全表示冗余, 多模态模型

## 3 点简述
- 问题：现有安全对齐方法依赖稀疏参数，易受神经元级攻击，鲁棒性不足
- 方法：识别安全相关神经元，在偏好优化中冻结以强制构建冗余安全表示
- 效果：实验显示显著提升抗神经元剪枝攻击能力，保持通用能力，提供可解释分析

## 摘要（原文）

> Large language models (LLMs) and multimodal LLMs are typically safety-aligned before release to prevent harmful content generation. However, recent studies show that safety behaviors are concentrated in a small subset of parameters, making alignment brittle and easily bypassed through neuron-level attacks. Moreover, most existing alignment methods operate at the behavioral level, offering limited control over the model's internal safety mechanisms. In this work, we propose SafeNeuron, a neuron-level safety alignment framework that improves robustness by redistributing safety representations across the network. SafeNeuron first identifies safety-related neurons, then freezes these neurons during preference optimization to prevent reliance on sparse safety pathways and force the model to construct redundant safety representations. Extensive experiments across models and modalities demonstrate that SafeNeuron significantly improves robustness against neuron pruning attacks, reduces the risk of open-source models being repurposed as red-team generators, and preserves general capabilities. Furthermore, our layer-wise analysis reveals that safety behaviors are governed by stable and shared internal representations. Overall, SafeNeuron provides an interpretable and robust perspective for model alignment.

