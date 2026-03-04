---
layout: default
title: AI-for-Science Low-code Platform with Bayesian Adversarial Multi-Agent Framework
---

# AI-for-Science Low-code Platform with Bayesian Adversarial Multi-Agent Framework
**arXiv**：[2603.03233v1](https://arxiv.org/abs/2603.03233) · [PDF](https://arxiv.org/pdf/2603.03233.pdf)  
**作者**：Zihang Zeng, Jiaquan Zhang, Pengze Li, Yuan Qi, Xi Chen  

**一句话要点**：提出贝叶斯对抗多智能体框架的低代码平台，以解决AI4S任务中LLM可靠性低和评估不确定性问题。

**关键词**：贝叶斯对抗多智能体, 低代码平台, AI for Science, LLM代码生成, 科学任务评估, 错误传播最小化

## 3 点简述
- 核心问题：LLM在科学代码生成中面临可靠性差、多智能体工作流错误传播和评估标准模糊的挑战。
- 方法要点：采用贝叶斯框架协调三个LLM智能体，通过对抗循环优化测试用例和代码，减少对LLM可靠性的依赖。
- 实验或效果：基准评估显示平台能生成鲁棒代码并最小化错误传播，在地球科学跨学科任务中表现优于竞争模型。

## 摘要（原文）

> Large Language Models (LLMs) demonstrate potentials for automating scientific code generation but face challenges in reliability, error propagation in multi-agent workflows, and evaluation in domains with ill-defined success metrics. We present a Bayesian adversarial multi-agent framework specifically designed for AI for Science (AI4S) tasks in the form of a Low-code Platform (LCP). Three LLM-based agents are coordinated under the Bayesian framework: a Task Manager that structures user inputs into actionable plans and adaptive test cases, a Code Generator that produces candidate solutions, and an Evaluator providing comprehensive feedback. The framework employs an adversarial loop where the Task Manager iteratively refines test cases to challenge the Code Generator, while prompt distributions are dynamically updated using Bayesian principles by integrating code quality metrics: functional correctness, structural alignment, and static analysis. This co-optimization of tests and code reduces dependence on LLM reliability and addresses evaluation uncertainty inherent to scientific tasks. LCP also streamlines human-AI collaboration by translating non-expert prompts into domain-specific requirements, bypassing the need for manual prompt engineering by practitioners without coding backgrounds. Benchmark evaluations demonstrate LCP's effectiveness in generating robust code while minimizing error propagation. The proposed platform is also tested on an Earth Science cross-disciplinary task and demonstrates strong reliability, outperforming competing models.

