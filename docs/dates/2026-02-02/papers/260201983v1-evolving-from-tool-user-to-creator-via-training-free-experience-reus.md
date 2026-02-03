---
layout: default
title: Evolving from Tool User to Creator via Training-Free Experience Reuse in Multimodal Reasoning
---

# Evolving from Tool User to Creator via Training-Free Experience Reuse in Multimodal Reasoning
**arXiv**：[2602.01983v1](https://arxiv.org/abs/2602.01983) · [PDF](https://arxiv.org/pdf/2602.01983.pdf)  
**作者**：Xintian Shen, Jiawei Chen, Lihao Zheng, Hao Ma, Tao Wei, Kun Zhan  

**一句话要点**：提出UCT框架，通过无训练经验复用实现多模态推理中从工具使用者到创造者的转变。

**关键词**：工具集成推理, 经验复用, 无训练框架, 自适应工具创建, 多模态推理, 自进化代理

## 3 点简述
- 现有工具集成推理模型在开放性问题中工具固定且缺乏自优化，易受错误输出误导。
- UCT框架无训练地收集推理经验并提炼为可复用资产，支持自适应工具创建与自更新。
- 实验显示在数学和科学推理任务上性能显著提升，验证了代理的自进化能力。

## 摘要（原文）

> Existing Tool-Integrated Reasoning (TIR) models have effectively extended the question-answering capabilities of LLMs by incorporating external tools. However, real-world scenarios present numerous open-ended problems where fixed tools often fail to meet task requirements. Furthermore, the lack of self-optimization mechanisms means that erroneous tool outputs can mislead the LLM's responses. Additionally, the construction of existing tools entails significant manual effort, which consequently constrains their applicability. Recognizing that the reasoning traces of LLMs encapsulate implicit problem-solving capabilities, we propose UCT, a novel training-free framework that transforms agents from tool users to tool creators. This approach harvests reasoning experiences and distills them into reusable assets. This method transforms the agent from a mere tool user into a tool creator, enabling adaptive tool creation and self-updating during the inference process. We also introduce a memory consolidation mechanism to maintain the tool library, ensuring high reusability of retained experiential memory for subsequent reasoning tasks. This novel automated tool construction paradigm continuously improves tool quality during reasoning, allowing the overall agent system to progress without additional training. Extensive experiments demonstrate that our method serves as a novel paradigm for enhancing the capabilities of TIR models. In particular, the significant performance gains achieved +20.86%$\uparrow$ and +23.04%$\uparrow$ on benchmarks across multi-domain mathematical and scientific reasoning tasks validate the self-evolving capability of the agent.

