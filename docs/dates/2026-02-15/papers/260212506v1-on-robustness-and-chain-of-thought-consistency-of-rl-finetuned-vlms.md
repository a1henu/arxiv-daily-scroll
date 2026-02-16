---
layout: default
title: On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs
---

# On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs
**arXiv**：[2602.12506v1](https://arxiv.org/abs/2602.12506) · [PDF](https://arxiv.org/pdf/2602.12506.pdf)  
**作者**：Rosie Zhao, Anshul Shah, Xiaoyu Zhu, Xinke Deng, Zhongyu Jiang, Yang Yang, Joerg Liebelt, Arnab Mondal  

**一句话要点**：揭示RL微调视觉语言模型在鲁棒性与思维链一致性上的局限性

**关键词**：视觉语言模型, 强化学习微调, 鲁棒性分析, 思维链一致性, 文本扰动, 模型不确定性

## 3 点简述
- 核心问题：RL微调VLMs在视觉推理任务中易受误导性文本扰动影响，导致鲁棒性下降和思维链不忠实
- 方法要点：通过文本扰动实验和熵度量分析模型不确定性，并探讨对抗增强与忠实性奖励的改进策略
- 实验或效果：发现RL微调存在准确性-忠实性权衡，单纯对抗增强无法完全恢复鲁棒性，需联合评估正确性、鲁棒性和推理忠实性

## 摘要（原文）

> Reinforcement learning (RL) fine-tuning has become a key technique for enhancing large language models (LLMs) on reasoning-intensive tasks, motivating its extension to vision language models (VLMs). While RL-tuned VLMs improve on visual reasoning benchmarks, they remain vulnerable to weak visual grounding, hallucinations, and over-reliance on textual cues. We show that simple, controlled textual perturbations--misleading captions or incorrect chain-of-thought (CoT) traces--cause substantial drops in robustness and confidence, and that these effects are more pronounced when CoT consistency is taken into account across open-source multimodal reasoning models. Entropy-based metrics further show that these perturbations reshape model uncertainty and probability mass on the correct option, exposing model-specific trends in miscalibration. To better understand these vulnerabilities, we further analyze RL fine-tuning dynamics and uncover an accuracy-faithfulness trade-off: fine-tuning raises benchmark accuracy, but can simultaneously erode the reliability of the accompanying CoT and its robustness to contextual shifts. Although adversarial augmentation improves robustness, it does not by itself prevent faithfulness drift. Incorporating a faithfulness-aware reward can restore alignment between answers and reasoning, but when paired with augmentation, training risks collapsing onto shortcut strategies and robustness remains elusive. Together, these findings highlight the limitations of accuracy-only evaluations and motivate training and assessment protocols that jointly emphasize correctness, robustness, and the faithfulness of visually grounded reasoning.

