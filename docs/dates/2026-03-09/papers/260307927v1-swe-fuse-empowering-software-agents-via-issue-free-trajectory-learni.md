---
layout: default
title: SWE-Fuse: Empowering Software Agents via Issue-free Trajectory Learning and Entropy-aware RLVR Training
---

# SWE-Fuse: Empowering Software Agents via Issue-free Trajectory Learning and Entropy-aware RLVR Training
**arXiv**：[2603.07927v1](https://arxiv.org/abs/2603.07927) · [PDF](https://arxiv.org/pdf/2603.07927.pdf)  
**作者**：Xin-Cheng Wen, Binbin Chen, Haoxuan Lan, Hang Yu, Peng Di, Cuiyun Gao  

**一句话要点**：提出SWE-Fuse框架，通过无问题轨迹学习和熵感知RLVR训练提升软件代理解决现实软件问题的能力。

**关键词**：软件工程代理, 轨迹学习, 强化学习, 熵感知训练, 问题描述对齐, 测试时缩放

## 3 点简述
- 核心问题：现实数据集中问题描述与解决方案不对齐，误导LLM代理，限制其问题解决效果。
- 方法要点：融合问题描述引导和无问题样本，包括无问题轨迹学习模块和熵感知RLVR训练模块。
- 实验或效果：在SWE-bench Verified基准上，SWE-Fuse显著优于基线模型，结合测试时缩放进一步提升性能。

## 摘要（原文）

> Large language models (LLMs) have transformed the software engineering landscape. Recently, numerous LLM-based agents have been developed to address real-world software issue fixing tasks. Despite their state-of-the-art performance, Despite achieving state-of-the-art performance, these agents face a significant challenge: \textbf{Insufficient high-quality issue descriptions.} Real-world datasets often exhibit misalignments between issue descriptions and their corresponding solutions, introducing noise and ambiguity that mislead automated agents and limit their problem-solving effectiveness. We propose \textbf{\textit{SWE-Fuse}}, an issue-description-aware training framework that fuses issue-description-guided and issue-free samples for training SWE agents. It consists of two key modules: (1) An issue-free-driven trajectory learning module for mitigating potentially misleading issue descriptions while enabling the model to learn step-by-step debugging processes; and (2) An entropy-aware RLVR training module, which adaptively adjusts training dynamics through entropy-driven clipping. It applies relaxed clipping under high entropy to encourage exploration, and stricter clipping under low entropy to ensure training stability. We evaluate SWE-Fuse on the widely studied SWE-bench Verified benchmark shows to demonstrate its effectiveness in solving real-world software problems. Specifically, SWE-Fuse outperforms the best 8B and 32B baselines by 43.0\% and 60.2\% in solve rate, respectively. Furthermore, integrating SWE-Fuse with test-time scaling (TTS) enables further performance improvements, achieving solve rates of 49.8\% and 65.2\% under TTS@8 for the 8B and 32B models, respectively.

