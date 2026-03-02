---
layout: default
title: MT-PingEval: Evaluating Multi-Turn Collaboration with Private Information Games
---

# MT-PingEval: Evaluating Multi-Turn Collaboration with Private Information Games
**arXiv**：[2602.24188v1](https://arxiv.org/abs/2602.24188) · [PDF](https://arxiv.org/pdf/2602.24188.pdf)  
**作者**：Jacob Eisenstein, Fantine Huot, Adam Fisch, Jonathan Berant, Mirella Lapata  

**一句话要点**：提出MT-PingEval方法，通过私有信息游戏评估语言模型的多轮协作能力。

**关键词**：多轮协作评估, 私有信息游戏, 语言模型评估, 交互式缩放分析, 对话规划

## 3 点简述
- 核心问题：评估语言模型在多轮交互中的协作能力，特别是处理私有信息时的表现。
- 方法要点：设计协作游戏套件，采用交互式缩放分析，固定令牌预算分配至可变轮次。
- 实验或效果：发现模型在多轮协作中未超越非交互基线，表明其在规划和执行对话方面存在弱点。

## 摘要（原文）

> We present a scalable methodology for evaluating language models in multi-turn interactions, using a suite of collaborative games that require effective communication about private information. This enables an interactive scaling analysis, in which a fixed token budget is divided over a variable number of turns. We find that in many cases, language models are unable to use interactive collaboration to improve over the non-interactive baseline scenario in which one agent attempts to summarize its information and the other agent immediately acts -- despite substantial headroom. This suggests that state-of-the-art models still suffer from significant weaknesses in planning and executing multi-turn collaborative conversations. We analyze the linguistic features of these dialogues, assessing the roles of sycophancy, information density, and discourse coherence. While there is no single linguistic explanation for the collaborative weaknesses of contemporary language models, we note that humans achieve comparable task success at superior token efficiency by producing dialogues that are more coherent than those produced by most language models. The proactive management of private information is a defining feature of real-world communication, and we hope that MT-PingEval will drive further work towards improving this capability.

