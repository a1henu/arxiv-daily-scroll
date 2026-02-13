---
layout: default
title: AmbiBench: Benchmarking Mobile GUI Agents Beyond One-Shot Instructions in the Wild
---

# AmbiBench: Benchmarking Mobile GUI Agents Beyond One-Shot Instructions in the Wild
**arXiv**：[2602.11750v1](https://arxiv.org/abs/2602.11750) · [PDF](https://arxiv.org/pdf/2602.11750.pdf)  
**作者**：Jiazheng Sun, Mingxuan Li, Yingying Zhang, Jiayang Niu, Yachen Wu, Ruihan Jin, Shuyu Lei, Pengrongrui Tan, Zongyu Zhang, Ruoyi Wang, Jiachen Yang, Boyu Yang, Jiacheng Liu, Xin Peng  

**一句话要点**：提出AmbiBench基准以评估移动GUI代理在模糊指令下的意图对齐能力

**关键词**：移动GUI代理, 意图对齐, 模糊指令, 自动化评估, 认知差距理论

## 3 点简述
- 核心问题：现有基准假设用户指令完整明确，忽略代理在模糊指令下的意图对齐能力。
- 方法要点：基于认知差距理论，构建包含四种清晰度级别的任务数据集，并开发自动化评估框架MUSE。
- 实验或效果：实证结果揭示SoTA代理性能边界，量化主动交互收益，验证MUSE与人工评估强相关。

## 摘要（原文）

> Benchmarks are paramount for gauging progress in the domain of Mobile GUI Agents. In practical scenarios, users frequently fail to articulate precise directives containing full task details at the onset, and their expressions are typically ambiguous. Consequently, agents are required to converge on the user's true intent via active clarification and interaction during execution. However, existing benchmarks predominantly operate under the idealized assumption that user-issued instructions are complete and unequivocal. This paradigm focuses exclusively on assessing single-turn execution while overlooking the alignment capability of the agent. To address this limitation, we introduce AmbiBench, the first benchmark incorporating a taxonomy of instruction clarity to shift evaluation from unidirectional instruction following to bidirectional intent alignment. Grounded in Cognitive Gap theory, we propose a taxonomy of four clarity levels: Detailed, Standard, Incomplete, and Ambiguous. We construct a rigorous dataset of 240 ecologically valid tasks across 25 applications, subject to strict review protocols. Furthermore, targeting evaluation in dynamic environments, we develop MUSE (Mobile User Satisfaction Evaluator), an automated framework utilizing an MLLM-as-a-judge multi-agent architecture. MUSE performs fine-grained auditing across three dimensions: Outcome Effectiveness, Execution Quality, and Interaction Quality. Empirical results on AmbiBench reveal the performance boundaries of SoTA agents across different clarity levels, quantify the gains derived from active interaction, and validate the strong correlation between MUSE and human judgment. This work redefines evaluation standards, laying the foundation for next-generation agents capable of truly understanding user intent.

