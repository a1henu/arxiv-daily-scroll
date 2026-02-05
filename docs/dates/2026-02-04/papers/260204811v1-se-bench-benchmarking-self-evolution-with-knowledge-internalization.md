---
layout: default
title: SE-Bench: Benchmarking Self-Evolution with Knowledge Internalization
---

# SE-Bench: Benchmarking Self-Evolution with Knowledge Internalization
**arXiv**：[2602.04811v1](https://arxiv.org/abs/2602.04811) · [PDF](https://arxiv.org/pdf/2602.04811.pdf)  
**作者**：Jiarui Yuan, Tailin Jin, Weize Chen, Zeyuan Liu, Zhiyuan Liu, Maosong Sun  

**一句话要点**：提出SE-Bench基准以评测智能体通过知识内化实现自我进化的能力

**关键词**：自我进化, 知识内化, 基准评测, 强化学习, 监督微调, 智能体学习

## 3 点简述
- 核心问题：现有评测难以区分先验知识与新知识、推理复杂度与知识内化能力
- 方法要点：通过混淆NumPy库为伪新包，在封闭环境中训练和评估智能体知识内化
- 实验或效果：发现开卷训练抑制知识保留，标准强化学习存在内化差距，自博弈结合监督微调可行

## 摘要（原文）

> True self-evolution requires agents to act as lifelong learners that internalize novel experiences to solve future problems. However, rigorously measuring this foundational capability is hindered by two obstacles: the entanglement of prior knowledge, where ``new'' knowledge may appear in pre-training data, and the entanglement of reasoning complexity, where failures may stem from problem difficulty rather than an inability to recall learned knowledge. We introduce SE-Bench, a diagnostic environment that obfuscates the NumPy library and its API doc into a pseudo-novel package with randomized identifiers. Agents are trained to internalize this package and evaluated on simple coding tasks without access to documentation, yielding a clean setting where tasks are trivial with the new API doc but impossible for base models without it. Our investigation reveals three insights: (1) the Open-Book Paradox, where training with reference documentation inhibits retention, requiring "Closed-Book Training" to force knowledge compression into weights; (2) the RL Gap, where standard RL fails to internalize new knowledge completely due to PPO clipping and negative gradients; and (3) the viability of Self-Play for internalization, proving models can learn from self-generated, noisy tasks when coupled with SFT, but not RL. Overall, SE-Bench establishes a rigorous diagnostic platform for self-evolution with knowledge internalization. Our code and dataset can be found at https://github.com/thunlp/SE-Bench.

