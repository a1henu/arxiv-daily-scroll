---
layout: default
title: HALO: A Unified Vision-Language-Action Model for Embodied Multimodal Chain-of-Thought Reasoning
---

# HALO: A Unified Vision-Language-Action Model for Embodied Multimodal Chain-of-Thought Reasoning
**arXiv**：[2602.21157v1](https://arxiv.org/abs/2602.21157) · [PDF](https://arxiv.org/pdf/2602.21157.pdf)  
**作者**：Quanxin Shou, Fangqi Zhu, Shawn Chen, Puxin Yan, Zhengyang Yan, Yikun Miao, Xiaoyi Pang, Zicong Hong, Ruikai Shi, Hao Huang, Jie Zhang, Song Guo  

**一句话要点**：提出HALO统一视觉-语言-动作模型，通过具身多模态思维链推理提升机器人长视野任务性能

**关键词**：视觉-语言-动作模型, 具身多模态思维链推理, 混合Transformer架构, 机器人操作, 长视野任务, 泛化能力

## 3 点简述
- 核心问题：现有VLA模型在长视野或分布外场景中缺乏多模态推理和动作前瞻机制，导致性能受限。
- 方法要点：采用混合Transformer架构，通过文本任务推理、视觉子目标预测和增强动作预测实现统一的多模态思维链推理。
- 实验或效果：在模拟和真实环境中超越基线策略34.1%，并展示出强泛化能力。

## 摘要（原文）

> Vision-Language-Action (VLA) models have shown strong performance in robotic manipulation, but often struggle in long-horizon or out-of-distribution scenarios due to the lack of explicit mechanisms for multimodal reasoning and anticipating how the world will evolve under action. Recent works introduce textual chain-of-thought or visual subgoal prediction within VLA models to reason, but still fail to offer a unified human-like reasoning framework for joint textual reasoning, visual foresight, and action prediction. To this end, we propose HALO, a unified VLA model that enables embodied multimodal chain-of-thought (EM-CoT) reasoning through a sequential process of textual task reasoning, visual subgoal prediction for fine-grained guidance, and EM-CoT-augmented action prediction. We instantiate HALO with a Mixture-of-Transformers (MoT) architecture that decouples semantic reasoning, visual foresight, and action prediction into specialized experts while allowing seamless cross-expert collaboration. To enable HALO learning at scale, we introduce an automated pipeline to synthesize EM-CoT training data along with a carefully crafted training recipe. Extensive experiments demonstrate that: (1) HALO achieves superior performance in both simulated and real-world environments, surpassing baseline policy pi_0 by 34.1% on RoboTwin benchmark; (2) all proposed components of the training recipe and EM-CoT design help improve task success rate; and (3) HALO exhibits strong generalization capabilities under aggressive unseen environmental randomization with our proposed EM-CoT reasoning.

