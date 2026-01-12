---
layout: default
title: The Molecular Structure of Thought: Mapping the Topology of Long Chain-of-Thought Reasoning
---

# The Molecular Structure of Thought: Mapping the Topology of Long Chain-of-Thought Reasoning
**arXiv**：[2601.06002v1](https://arxiv.org/abs/2601.06002) · [PDF](https://arxiv.org/pdf/2601.06002.pdf)  
**作者**：Qiguang Chen, Yantao Du, Ziniu Li, Jinhao Liu, Songyao Duan, Jiarui Guo, Minghao Liu, Jiaheng Liu, Tong Yang, Ge Zhang, Libo Qin, Wanxiang Che, Wenhao Huang  

**一句话要点**：提出Mole-Syn方法，通过分子结构类比指导长链思维推理的有效合成，提升大语言模型性能与强化学习稳定性。

**关键词**：长链思维推理, 分子结构类比, 熵收敛, 分布转移图, 大语言模型微调, 强化学习稳定性

## 3 点简述
- 核心问题：大语言模型难以从人类或非长链思维模型模仿中学习有效的长链思维推理轨迹。
- 方法要点：将长链思维轨迹视为分子结构，分析三种交互类型，并基于熵收敛理论识别稳定结构。
- 实验或效果：Mole-Syn方法在基准测试中提升性能，增强强化学习训练的稳定性。

## 摘要（原文）

> Large language models (LLMs) often fail to learn effective long chain-of-thought (Long CoT) reasoning from human or non-Long-CoT LLMs imitation. To understand this, we propose that effective and learnable Long CoT trajectories feature stable molecular-like structures in unified view, which are formed by three interaction types: Deep-Reasoning (covalent-like), Self-Reflection (hydrogen-bond-like), and Self-Exploration (van der Waals-like). Analysis of distilled trajectories reveals these structures emerge from Long CoT fine-tuning, not keyword imitation. We introduce Effective Semantic Isomers and show that only bonds promoting fast entropy convergence support stable Long CoT learning, while structural competition impairs training. Drawing on these findings, we present Mole-Syn, a distribution-transfer-graph method that guides synthesis of effective Long CoT structures, boosting performance and RL stability across benchmarks.

