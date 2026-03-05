---
layout: default
title: SWE-CI: Evaluating Agent Capabilities in Maintaining Codebases via Continuous Integration
---

# SWE-CI: Evaluating Agent Capabilities in Maintaining Codebases via Continuous Integration
**arXiv**：[2603.03823v1](https://arxiv.org/abs/2603.03823) · [PDF](https://arxiv.org/pdf/2603.03823.pdf)  
**作者**：Jialong Chen, Xander Xu, Hu Wei, Chuan Chen, Bing Zhao  

**一句话要点**：提出SWE-CI基准，基于持续集成评估LLM代理在长期代码维护中的能力。

**关键词**：代码生成评估, 持续集成基准, 软件维护, LLM代理, 长期演化

## 3 点简述
- 核心问题：现有基准如SWE-bench仅评估静态一次性修复，无法反映真实软件开发中的长期迭代和需求变化。
- 方法要点：构建首个基于持续集成循环的仓库级基准，包含100个任务，模拟平均233天和71次提交的代码演化历史。
- 实验或效果：要求代理通过多轮分析和编码迭代解决任务，评估其在长期演化中维持代码质量的能力。

## 摘要（原文）

> Large language model (LLM)-powered agents have demonstrated strong capabilities in automating software engineering tasks such as static bug fixing, as evidenced by benchmarks like SWE-bench. However, in the real world, the development of mature software is typically predicated on complex requirement changes and long-term feature iterations -- a process that static, one-shot repair paradigms fail to capture. To bridge this gap, we propose \textbf{SWE-CI}, the first repository-level benchmark built upon the Continuous Integration loop, aiming to shift the evaluation paradigm for code generation from static, short-term \textit{functional correctness} toward dynamic, long-term \textit{maintainability}. The benchmark comprises 100 tasks, each corresponding on average to an evolution history spanning 233 days and 71 consecutive commits in a real-world code repository. SWE-CI requires agents to systematically resolve these tasks through dozens of rounds of analysis and coding iterations. SWE-CI provides valuable insights into how well agents can sustain code quality throughout long-term evolution.

