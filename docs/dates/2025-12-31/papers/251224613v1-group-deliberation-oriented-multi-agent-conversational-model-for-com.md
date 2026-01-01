---
layout: default
title: Group Deliberation Oriented Multi-Agent Conversational Model for Complex Reasoning
---

# Group Deliberation Oriented Multi-Agent Conversational Model for Complex Reasoning
**arXiv**：[2512.24613v1](https://arxiv.org/abs/2512.24613) · [PDF](https://arxiv.org/pdf/2512.24613.pdf)  
**作者**：Zheyu Shi, Dong Qiu, Shanlong Yu  

**一句话要点**：提出面向群体审议的多智能体对话模型以解决复杂推理任务中单一大语言模型的局限性。

**关键词**：多智能体对话模型, 复杂推理, 检索增强, 协作训练, 多跳推理

## 3 点简述
- 核心问题：单一大语言模型在复杂推理任务中表现受限，需提升多跳推理准确性和一致性。
- 方法要点：采用三层角色架构（生成、验证、整合），结合自博弈机制和检索增强模块，设计复合奖励函数进行协作训练。
- 实验或效果：在HotpotQA、2WikiMultihopQA和MeetingBank数据集上，多跳推理准确率提升14.3%至19.2%，一致性提升21.5%。

## 摘要（原文）

> This paper proposes a group deliberation oriented multi-agent conversational model to address the limitations of single large language models in complex reasoning tasks. The model adopts a three-level role division architecture consisting of generation, verification, and integration. An opinion generation agent produces diverse reasoning perspectives, an evidence verification agent retrieves external knowledge and quantifies factual support, and a consistency arbitration agent integrates logically coherent conclusions. A self-game mechanism is introduced to expand multi-path reasoning trajectories, while a retrieval enhancement module dynamically supplements external knowledge. A composite reward function combining factual consistency and logical coherence is designed, and an improved proximal policy optimization strategy is applied for collaborative training. Experimental results show that the proposed model improves multi-hop reasoning accuracy by 16.8 percent on HotpotQA, 14.3 percent on 2WikiMultihopQA, and 19.2 percent on MeetingBank, while improving consistency by 21.5 percent. The model achieves higher reasoning efficiency than mainstream multi-agent approaches, providing an effective and stable solution for complex reasoning tasks.

