---
layout: default
title: Zero-shot adaptable task planning for autonomous construction robots: a comparative study of lightweight single and multi-AI agent systems
---

# Zero-shot adaptable task planning for autonomous construction robots: a comparative study of lightweight single and multi-AI agent systems
**arXiv**：[2601.14091v1](https://arxiv.org/abs/2601.14091) · [PDF](https://arxiv.org/pdf/2601.14091.pdf)  
**作者**：Hossein Naderi, Alireza Shojaei, Lifu Huang, Philip Agee, Kereshmeh Afsari, Abiola Akanmu  

**一句话要点**：提出基于轻量级基础模型的单/多智能体系统，以提升建筑机器人任务规划的零样本适应性和泛化能力。

**关键词**：建筑机器人, 任务规划, 零样本适应, 多智能体系统, 轻量级基础模型, 成本效益

## 3 点简述
- 核心问题：建筑机器人成本高、动态任务适应难，需提升任务规划的适应性和泛化性。
- 方法要点：使用轻量级开源LLMs和VLMs，设计一个单智能体和三个多智能体团队进行协作任务规划。
- 实验或效果：在Painter、Safety Inspector和Floor Tiling角色中评估，四智能体团队在多数指标上优于GPT-4o，成本效益高十倍，且多智能体团队泛化性更强。

## 摘要（原文）

> Robots are expected to play a major role in the future construction industry but face challenges due to high costs and difficulty adapting to dynamic tasks. This study explores the potential of foundation models to enhance the adaptability and generalizability of task planning in construction robots. Four models are proposed and implemented using lightweight, open-source large language models (LLMs) and vision language models (VLMs). These models include one single agent and three multi-agent teams that collaborate to create robot action plans. The models are evaluated across three construction roles: Painter, Safety Inspector, and Floor Tiling. Results show that the four-agent team outperforms the state-of-the-art GPT-4o in most metrics while being ten times more cost-effective. Additionally, teams with three and four agents demonstrate the improved generalizability. By discussing how agent behaviors influence outputs, this study enhances the understanding of AI teams and supports future research in diverse unstructured environments beyond construction.

