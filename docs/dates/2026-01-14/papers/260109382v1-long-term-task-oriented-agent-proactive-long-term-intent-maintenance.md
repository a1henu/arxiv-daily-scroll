---
layout: default
title: Long-term Task-oriented Agent: Proactive Long-term Intent Maintenance in Dynamic Environments
---

# Long-term Task-oriented Agent: Proactive Long-term Intent Maintenance in Dynamic Environments
**arXiv**：[2601.09382v1](https://arxiv.org/abs/2601.09382) · [PDF](https://arxiv.org/pdf/2601.09382.pdf)  
**作者**：Qinglong Shi, Donghai Wang, Hantao Zhou, Jiguo Li, Jun Xu, Jiuchong Gao, Jinghua Hao, Renqing He  

**一句话要点**：提出主动式任务导向智能体以在动态环境中维护用户长期意图

**关键词**：任务导向智能体, 长期意图维护, 动态环境适应, 数据合成, 基准评估, 监督学习

## 3 点简述
- 核心问题：现有大语言模型智能体多为被动响应，难以在动态环境中维持用户长期意图。
- 方法要点：通过意图条件监控和事件触发跟进，实现智能体主动适应环境变化。
- 实验或效果：构建ChronosBench基准，微调模型在复杂任务中达到85.19%完成率，验证数据驱动策略有效性。

## 摘要（原文）

> Current large language model agents predominantly operate under a reactive paradigm, responding only to immediate user queries within short-term sessions. This limitation hinders their ability to maintain long-term user's intents and dynamically adapt to evolving external environments. In this paper, we propose a novel interaction paradigm for proactive Task-oriented Agents capable of bridging the gap between relatively static user's needs and a dynamic environment. We formalize proactivity through two key capabilities, (i) Intent-Conditioned Monitoring: The agent autonomously formulates trigger conditions based on dialog history; (ii) Event-Triggered Follow-up: The agent actively engages the user upon detecting useful environmental updates. We introduce a high-quality data synthesis pipeline to construct complex, multi-turn dialog data in a dynamic environment. Furthermore, we attempt to address the lack of evaluation criteria of task-oriented interaction in a dynamic environment by proposing a new benchmark, namely ChronosBench. We evaluated some leading close-source and open-source models at present and revealed their flaws in long-term task-oriented interaction. Furthermore, our fine-tuned model trained using synthetic data for supervised learning achieves a task completion rate of 85.19% for complex tasks including shifts in user intent, outperforming other models under test. And the result validated the effectiveness of our data-driven strategy.

