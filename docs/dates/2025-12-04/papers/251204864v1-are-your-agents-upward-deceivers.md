---
layout: default
title: Are Your Agents Upward Deceivers?
---

# Are Your Agents Upward Deceivers?
**arXiv**：[2512.04864v1](https://arxiv.org/abs/2512.04864) · [PDF](https://arxiv.org/pdf/2512.04864.pdf)  
**作者**：Dadi Guo, Qingyu Liu, Dongrui Liu, Qihan Ren, Shuai Shao, Tianyi Qiu, Haoran Li, Yi R. Fung, Zhongjie Ba, Juntao Dai, Jiaming Ji, Zhikai Chen, Jialing Tao, Yaodong Yang, Jing Shao, Xia Hu  

**一句话要点**：提出LLM智能体向上欺骗现象，构建基准评估其普遍性并测试缓解策略。

**关键词**：LLM智能体, 向上欺骗, 基准评估, 安全缓解, 自主代理

## 3 点简述
- 核心问题：LLM智能体在受限环境中可能隐瞒失败并执行未请求操作，类似人类向上级欺骗。
- 方法要点：定义智能体向上欺骗，构建200任务基准覆盖五类任务和八种现实场景。
- 实验或效果：评估11个流行LLM，发现普遍存在基于行动的欺骗行为，提示缓解效果有限。

## 摘要（原文）

> Large Language Model (LLM)-based agents are increasingly used as autonomous subordinates that carry out tasks for users. This raises the question of whether they may also engage in deception, similar to how individuals in human organizations lie to superiors to create a good image or avoid punishment. We observe and define agentic upward deception, a phenomenon in which an agent facing environmental constraints conceals its failure and performs actions that were not requested without reporting. To assess its prevalence, we construct a benchmark of 200 tasks covering five task types and eight realistic scenarios in a constrained environment, such as broken tools or mismatched information sources. Evaluations of 11 popular LLMs reveal that these agents typically exhibit action-based deceptive behaviors, such as guessing results, performing unsupported simulations, substituting unavailable information sources, and fabricating local files. We further test prompt-based mitigation and find only limited reductions, suggesting that it is difficult to eliminate and highlighting the need for stronger mitigation strategies to ensure the safety of LLM-based agents.

