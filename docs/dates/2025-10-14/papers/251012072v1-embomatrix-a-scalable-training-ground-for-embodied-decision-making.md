---
layout: default
title: EmboMatrix: A Scalable Training-Ground for Embodied Decision-Making
---

# EmboMatrix: A Scalable Training-Ground for Embodied Decision-Making
**arXiv**：[2510.12072v1](https://arxiv.org/abs/2510.12072) · [PDF](https://arxiv.org/pdf/2510.12072.pdf)  
**作者**：Zixing Lei, Sheng Yin, Yichen Xiong, Yuanzhuo Ding, Wenhao Huang, Yuxi Wei, Qingyao Xu, Yiming Li, Weixin Li, Yunhong Wang, Siheng Chen  

**一句话要点**：提出EmboMatrix训练场以提升大语言模型的具身决策能力

**关键词**：具身决策, 大语言模型训练, 模拟环境, 多智能体数据引擎, 分布式仿真系统, 多级奖励架构

## 3 点简述
- 核心问题：大语言模型缺乏物理环境暴露，限制其具身决策理解。
- 方法要点：构建EmboMatrix训练场，集成任务模拟、交互和反馈信号。
- 实验效果：EmboBrain-7B在基准测试中超越DeepSeek-R1基线9.5%。

## 摘要（原文）

> Embodied decision-making enables agents to translate high-level goals into
> executable actions through continuous interactions within the physical world,
> forming a cornerstone of general-purpose embodied intelligence. Large language
> models (LLMs), with their general decision-making capabilities, offer a
> promising path to realize this potential; however, LLMs trained solely on
> language lack exposure to physical environments, limiting their true embodied
> understanding. To bridge this gap, we propose the concept of a training ground:
> a comprehensive infrastructure that provides task and scene simulation,
> embodied interaction, and feedback signals, offering a one-stop solution for
> LLM acquire genuine embodied decision-making skills. In this work, we present
> EmboMatrix, the first training ground of its kind, providing massive and
> diverse tasks with efficient simulation and precise rewards. EmboMatrix
> incorporates a series of novel techniques: a multi-agent data engine for
> large-scale task and scene generation, a distributed heterogeneous-hardware
> system for scalable simulation, and a multi-level reward architecture for
> precise supervision. Leveraging EmboMatrix, we cultivate EmboBrain, an LLM
> whose embodied decision-making abilities emerge from extensive embodied
> interactions. Experiments show that EmboBrain-7B surpasses the 671B DeepSeek-R1
> baseline by 9.5\% on two challenging embodied decision-making benchmarks,
> demonstrating the power of interactive, environment-grounded learning for
> building truly intelligent embodied agents.

