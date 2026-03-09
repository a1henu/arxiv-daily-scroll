---
layout: default
title: Place-it-R1: Unlocking Environment-aware Reasoning Potential of MLLM for Video Object Insertion
---

# Place-it-R1: Unlocking Environment-aware Reasoning Potential of MLLM for Video Object Insertion
**arXiv**：[2603.06140v1](https://arxiv.org/abs/2603.06140) · [PDF](https://arxiv.org/pdf/2603.06140.pdf)  
**作者**：Bohai Gu, Taiyi Wu, Dazhao Du, Jian Liu, Shuai Yang, Xiaotong Zhao, Alan Zhao, Song Guo  

**一句话要点**：提出Place-it-R1框架，利用MLLM的环境感知推理能力实现物理一致的视频对象插入

**关键词**：视频对象插入, 多模态大语言模型, 环境感知推理, 扩散模型, 物理一致性, 链式思维

## 3 点简述
- 核心问题：现有视频编辑技术注重视觉保真度，但缺乏物理因果性，导致插入对象与环境物理不一致。
- 方法要点：采用Think-then-Place范式，通过MLLM的链式推理生成环境感知令牌和有效插入区域，引导扩散模型实现物理合理插入。
- 实验或效果：相比先进解决方案和商业模型，Place-it-R1在实验中实现了物理更一致的视频对象插入，并提供用户可选的灵活与标准模式。

## 摘要（原文）

> Modern video editing techniques have achieved high visual fidelity when inserting video objects. However, they focus on optimizing visual fidelity rather than physical causality, leading to edits that are physically inconsistent with their environment. In this work, we present Place-it-R$1$, an end-to-end framework for video object insertion that unlocks the environment-aware reasoning potential of Multimodal Large Language Models (MLLMs). Our framework leverages the Chain-of-Thought (CoT) reasoning of MLLMs to orchestrate video diffusion, following a Think-then-Place paradigm. To bridge cognitive reasoning and generative execution, we introduce three key innovations: First, MLLM performs physical scene understanding and interaction reasoning, generating environment-aware chain-of-thought tokens and inferring valid insertion regions to explicitly guide the diffusion toward physically plausible insertion. Then, we introduce MLLM-guided Spatial Direct Preference Optimization (DPO), where diffusion outputs are fed back to the MLLM for scoring, enabling visual naturalness. During inference, the MLLM iteratively triggers refinement cycles and elicits adaptive adjustments from the diffusion model, forming a closed-loop that progressively enhances editing quality. Furthermore, we provide two user-selectable modes: a plausibility-oriented flexible mode that permits environment modifications (\eg, generating support structures) to enhance physical plausibility, and a fidelity-oriented standard mode that preserves scene integrity for maximum fidelity, offering users explicit control over the plausibility-fidelity trade-off. Extensive experiments demonstrate Place-it-R1 achieves physically-coherent video object insertion compared with state-of-the-art solutions and commercial models.

