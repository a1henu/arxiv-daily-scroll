---
layout: default
title: Agentic Rubrics as Contextual Verifiers for SWE Agents
---

# Agentic Rubrics as Contextual Verifiers for SWE Agents
**arXiv**：[2601.04171v1](https://arxiv.org/abs/2601.04171) · [PDF](https://arxiv.org/pdf/2601.04171.pdf)  
**作者**：Mohit Raghavendra, Anisha Gunjal, Bing Liu, Yunzhong He  

**一句话要点**：提出Agentic Rubrics作为软件工程代理的上下文验证器，以替代代码执行验证。

**关键词**：软件工程代理, 上下文验证, 评分标准, 测试时间扩展, 代码库交互, 补丁评估

## 3 点简述
- 核心问题：软件工程代理验证依赖代码执行，难以扩展且环境设置开销大。
- 方法要点：专家代理与代码库交互生成上下文驱动的评分标准，无需测试执行即可评估补丁。
- 实验或效果：在SWE-Bench Verified上，Agentic Rubrics在Qwen3-Coder-30B-A3B上得分54.2%，优于基线至少3.5个百分点。

## 摘要（原文）

> Verification is critical for improving agents: it provides the reward signal for Reinforcement Learning and enables inference-time gains through Test-Time Scaling (TTS). Despite its importance, verification in software engineering (SWE) agent settings often relies on code execution, which can be difficult to scale due to environment setup overhead. Scalable alternatives such as patch classifiers and heuristic methods exist, but they are less grounded in codebase context and harder to interpret. To this end, we explore Agentic Rubrics: an expert agent interacts with the repository to create a context-grounded rubric checklist, and candidate patches are then scored against it without requiring test execution. On SWE-Bench Verified under parallel TTS evaluation, Agentic Rubrics achieve a score of 54.2% on Qwen3-Coder-30B-A3B and 40.6% on Qwen3-32B, with at least a +3.5 percentage-point gain over the strongest baseline in our comparison set. We further analyze rubric behavior, showing that rubric scores are consistent with ground-truth tests while also flagging issues that tests do not capture. Our ablations show that agentic context gathering is essential for producing codebase-specific, unambiguous criteria. Together, these results suggest that Agentic Rubrics provide an efficient, scalable, and granular verification signal for SWE agents.

