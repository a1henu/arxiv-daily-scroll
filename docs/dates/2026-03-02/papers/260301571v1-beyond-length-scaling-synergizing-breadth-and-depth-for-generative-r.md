---
layout: default
title: Beyond Length Scaling: Synergizing Breadth and Depth for Generative Reward Models
---

# Beyond Length Scaling: Synergizing Breadth and Depth for Generative Reward Models
**arXiv**：[2603.01571v1](https://arxiv.org/abs/2603.01571) · [PDF](https://arxiv.org/pdf/2603.01571.pdf)  
**作者**：Qiyuan Zhang, Yufei Wang, Tianhe Wu, Can Xu, Qingfeng Sun, Kai Zheng, Xue Liu, Chen Ma  

**一句话要点**：提出Mix-GRM框架，通过协同广度与深度推理机制提升生成奖励模型的评估可靠性。

**关键词**：生成奖励模型, 链式思维推理, 广度与深度协同, 监督微调, 强化学习, 任务对齐

## 3 点简述
- 核心问题：现有生成奖励模型依赖无结构长度扩展，忽视广度与深度推理机制的不同效能。
- 方法要点：将原始推理重构为广度与深度链式思维，采用监督微调和强化学习进行优化。
- 实验或效果：在五个基准测试中实现新最优，平均超越开源模型8.2%，揭示推理机制与任务的对齐重要性。

## 摘要（原文）

> Recent advancements in Generative Reward Models (GRMs) have demonstrated that scaling the length of Chain-of-Thought (CoT) reasoning considerably enhances the reliability of evaluation. However, current works predominantly rely on unstructured length scaling, ignoring the divergent efficacy of different reasoning mechanisms: Breadth-CoT (B-CoT, i.e., multi-dimensional principle coverage) and Depth-CoT (D-CoT, i.e., substantive judgment soundness). To address this, we introduce Mix-GRM, a framework that reconfigures raw rationales into structured B-CoT and D-CoT through a modular synthesis pipeline, subsequently employing Supervised Fine-Tuning (SFT) and Reinforcement Learning with Verifiable Rewards (RLVR) to internalize and optimize these mechanisms. Comprehensive experiments demonstrate that Mix-GRM establishes a new state-of-the-art across five benchmarks, surpassing leading open-source RMs by an average of 8.2\%. Our results reveal a clear divergence in reasoning: B-CoT benefits subjective preference tasks, whereas D-CoT excels in objective correctness tasks. Consequently, misaligning the reasoning mechanism with the task directly degrades performance. Furthermore, we demonstrate that RLVR acts as a switching amplifier, inducing an emergent polarization where the model spontaneously allocates its reasoning style to match task demands. The synthesized data and models are released at \href{https://huggingface.co/collections/DonJoey/mix-grm}{Hugging Face}, and the code is released at \href{https://github.com/Don-Joey/Mix-GRM}{Github}.

