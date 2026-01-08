---
layout: default
title: Adaptive-Boundary-Clipping GRPO: Ensuring Bounded Ratios for Stable and Generalizable Training
---

# Adaptive-Boundary-Clipping GRPO: Ensuring Bounded Ratios for Stable and Generalizable Training
**arXiv**：[2601.03895v1](https://arxiv.org/abs/2601.03895) · [PDF](https://arxiv.org/pdf/2601.03895.pdf)  
**作者**：Chi Liu, Xin Chen  

**一句话要点**：提出自适应边界裁剪GRPO以增强强化学习稳定性和泛化性

**关键词**：强化学习, 大语言模型, 策略优化, 自适应裁剪, 数学推理

## 3 点简述
- 分析GRPO裁剪机制在特定场景下存在不足
- 引入非对称自适应边界裁剪改进原框架
- 在数学推理任务上表现优于标准GRPO并保持高熵

## 摘要（原文）

> Group Relative Policy Optimization (GRPO) has emerged as a popular algorithm for reinforcement learning with large language models (LLMs). However, upon analyzing its clipping mechanism, we argue that it is suboptimal in certain scenarios. With appropriate modifications, GRPO can be significantly enhanced to improve both flexibility and generalization. To this end, we propose Adaptive-Boundary-Clipping GRPO (ABC-GRPO), an asymmetric and adaptive refinement of the original GRPO framework. We demonstrate that ABC-GRPO achieves superior performance over standard GRPO on mathematical reasoning tasks using the Qwen3 LLMs. Moreover, ABC-GRPO maintains substantially higher entropy throughout training, thereby preserving the model's exploration capacity and mitigating premature convergence. The implementation code is available online to ease reproducibility https://github.com/chi2liu/ABC-GRPO.

