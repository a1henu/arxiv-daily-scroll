---
layout: default
title: SWE-Universe: Scale Real-World Verifiable Environments to Millions
---

# SWE-Universe: Scale Real-World Verifiable Environments to Millions
**arXiv**：[2602.02361v1](https://arxiv.org/abs/2602.02361) · [PDF](https://arxiv.org/pdf/2602.02361.pdf)  
**作者**：Mouxiang Chen, Lei Zhang, Yunlong Feng, Xuwu Wang, Wenting Zhao, Ruisheng Cao, Jiaxi Yang, Jiawei Chen, Mingze Li, Zeyao Ma, Hao Ge, Zongmeng Zhang, Zeyu Cui, Dayiheng Liu, Jingren Zhou, Jianling Sun, Junyang Lin, Binyuan Hui  

**一句话要点**：提出SWE-Universe框架以从GitHub拉取请求自动构建大规模真实软件工程验证环境

**关键词**：软件工程验证环境, 自动构建框架, 迭代自验证, 大规模数据集, 代理训练, 强化学习

## 3 点简述
- 核心问题：自动构建真实软件工程验证环境面临低产出、弱验证器和高成本挑战
- 方法要点：使用基于高效定制模型的构建代理，通过迭代自验证和循环黑客检测确保高保真任务生成
- 实验或效果：将多语言环境扩展至百万规模，应用于Qwen3-Max-Thinking在SWE-Bench Verified上得分75.3%

## 摘要（原文）

> We propose SWE-Universe, a scalable and efficient framework for automatically constructing real-world software engineering (SWE) verifiable environments from GitHub pull requests (PRs). To overcome the prevalent challenges of automatic building, such as low production yield, weak verifiers, and prohibitive cost, our framework utilizes a building agent powered by an efficient custom-trained model. This agent employs iterative self-verification and in-loop hacking detection to ensure the reliable generation of high-fidelity, verifiable tasks. Using this method, we scale the number of real-world multilingual SWE environments to a million scale (807,693). We demonstrate the profound value of our environments through large-scale agentic mid-training and reinforcement learning. Finally, we applied this technique to Qwen3-Max-Thinking and achieved a score of 75.3% on SWE-Bench Verified. Our work provides both a critical resource and a robust methodology to advance the next generation of coding agents.

