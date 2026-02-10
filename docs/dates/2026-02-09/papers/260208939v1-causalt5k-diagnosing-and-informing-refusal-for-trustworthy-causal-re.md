---
layout: default
title: CausalT5K: Diagnosing and Informing Refusal for Trustworthy Causal Reasoning of Skepticism, Sycophancy, Detection-Correction, and Rung Collapse
---

# CausalT5K: Diagnosing and Informing Refusal for Trustworthy Causal Reasoning of Skepticism, Sycophancy, Detection-Correction, and Rung Collapse
**arXiv**：[2602.08939v1](https://arxiv.org/abs/2602.08939) · [PDF](https://arxiv.org/pdf/2602.08939.pdf)  
**作者**：Longling Geng, Andy Ouyang, Theodore Wu, Daphne Barretto, Matthew John Hayes, Rachael Cooper, Yuqiao Zeng, Sameer Vijay, Gia Ancone, Ankit Rai, Matthew Wolfman, Patrick Flanagan, Edward Y. Chang  

**一句话要点**：提出CausalT5K基准以诊断和提升LLM在因果推理中的可信赖性

**关键词**：因果推理基准, 阶梯塌陷检测, 奉承漂移抵抗, 明智拒绝生成, 可信赖AI, 诊断工具

## 3 点简述
- 核心问题：LLM在因果推理中存在奉承、阶梯塌陷和错误拒绝等失败，缺乏系统诊断基准。
- 方法要点：构建包含5000多个案例的诊断基准，测试阶梯塌陷检测、抗奉承漂移和明智拒绝生成能力。
- 实验或效果：初步实验揭示静态审计策略普遍失败，基准能揭示聚合精度不可见的失败模式。

## 摘要（原文）

> LLM failures in causal reasoning, including sycophancy, rung collapse, and miscalibrated refusal, are well-documented, yet progress on remediation is slow because no benchmark enables systematic diagnosis. We introduce CausalT5K, a diagnostic benchmark of over 5,000 cases across 10 domains that tests three critical capabilities: (1) detecting rung collapse, where models answer interventional queries with associational evidence; (2) resisting sycophantic drift under adversarial pressure; and (3) generating Wise Refusals that specify missing information when evidence is underdetermined. Unlike synthetic benchmarks, CausalT5K embeds causal traps in realistic narratives and decomposes performance into Utility (sensitivity) and Safety (specificity), revealing failure modes invisible to aggregate accuracy. Developed through a rigorous human-machine collaborative pipeline involving 40 domain experts, iterative cross-validation cycles, and composite verification via rule-based, LLM, and human scoring, CausalT5K implements Pearl's Ladder of Causation as research infrastructure. Preliminary experiments reveal a Four-Quadrant Control Landscape where static audit policies universally fail, a finding that demonstrates CausalT5K's value for advancing trustworthy reasoning systems. Repository: https://github.com/genglongling/CausalT5kBench

