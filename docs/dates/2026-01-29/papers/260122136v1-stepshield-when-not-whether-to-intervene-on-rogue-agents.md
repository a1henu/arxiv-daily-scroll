---
layout: default
title: StepShield: When, Not Whether to Intervene on Rogue Agents
---

# StepShield: When, Not Whether to Intervene on Rogue Agents
**arXiv**：[2601.22136v1](https://arxiv.org/abs/2601.22136) · [PDF](https://arxiv.org/pdf/2601.22136.pdf)  
**作者**：Gloria Felicia, Michael Eniolade, Jinfeng He, Zitha Sasindran, Hemant Kumar, Milan Hussain Angati, Sandeep Bandarupalli  

**一句话要点**：提出StepShield基准以评估AI代理违规检测的时机，而非仅是否检测到。

**关键词**：代理安全基准, 早期干预评估, 时间指标, 代码代理轨迹, 经济影响分析

## 3 点简述
- 现有基准混淆早期干预与事后分析，无法衡量检测时机。
- StepShield包含9,213条代码代理轨迹，引入三个时间指标评估检测性能。
- 实验显示LLM法官比静态分析器在早期干预率上高2.3倍，并预测显著经济效益。

## 摘要（原文）

> Existing agent safety benchmarks report binary accuracy, conflating early intervention with post-mortem analysis. A detector that flags a violation at step 8 enables intervention; one that reports it at step 48 provides only forensic value. This distinction is critical, yet current benchmarks cannot measure it. We introduce StepShield, the first benchmark to evaluate when violations are detected, not just whether. StepShield contains 9,213 code agent trajectories, including 1,278 meticulously annotated training pairs and a 7,935-trajectory test set with a realistic 8.1% rogue rate. Rogue behaviors are grounded in real-world security incidents across six categories. We propose three novel temporal metrics: Early Intervention Rate (EIR), Intervention Gap, and Tokens Saved. Surprisingly, our evaluation reveals that an LLM-based judge achieves 59% EIR while a static analyzer achieves only 26%, a 2.3x performance gap that is entirely invisible to standard accuracy metrics. We further show that early detection has direct economic benefits: our cascaded HybridGuard detector reduces monitoring costs by 75% and projects to $108M in cumulative savings over five years at enterprise scale. By shifting the focus of evaluation from whether to when, StepShield provides a new foundation for building safer and more economically viable AI agents. The code and data are released under an Apache 2.0 license.

