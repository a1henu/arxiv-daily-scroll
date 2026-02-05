---
layout: default
title: Relational Scene Graphs for Object Grounding of Natural Language Commands
---

# Relational Scene Graphs for Object Grounding of Natural Language Commands
**arXiv**：[2602.04635v1](https://arxiv.org/abs/2602.04635) · [PDF](https://arxiv.org/pdf/2602.04635.pdf)  
**作者**：Julia Kuhn, Francesco Verdoja, Tsvetomila Mihaylova, Ville Kyrki  

**一句话要点**：提出基于关系场景图的方法，以增强大语言模型对自然语言指令中目标物体的定位能力。

**关键词**：自然语言理解, 3D场景图, 物体定位, 空间关系, 大语言模型, 视觉语言模型

## 3 点简述
- 核心问题：现有3D场景图缺乏显式空间关系，影响机器人理解依赖这些关系的自然语言指令。
- 方法要点：结合大语言模型与视觉语言模型，生成开放或封闭词汇的空间关系边，构建关系场景图。
- 实验或效果：研究表明显式空间关系提升物体定位性能，开放词汇关系生成可行但优势有限。

## 摘要（原文）

> Robots are finding wider adoption in human environments, increasing the need for natural human-robot interaction. However, understanding a natural language command requires the robot to infer the intended task and how to decompose it into executable actions, and to ground those actions in the robot's knowledge of the environment, including relevant objects, agents, and locations. This challenge can be addressed by combining the capabilities of Large language models (LLMs) to understand natural language with 3D scene graphs (3DSGs) for grounding inferred actions in a semantic representation of the environment. However, many 3DSGs lack explicit spatial relations between objects, even though humans often rely on these relations to describe an environment. This paper investigates whether incorporating open- or closed-vocabulary spatial relations into 3DSGs can improve the ability of LLMs to interpret natural language commands. To address this, we propose an LLM-based pipeline for target object grounding from open-vocabulary language commands and a vision language model (VLM)-based pipeline to add open-vocabulary spatial edges to 3DSGs from images captured while mapping. Finally, two LLMs are evaluated in a study assessing their performance on the downstream task of target object grounding. Our study demonstrates that explicit spatial relations improve the ability of LLMs to ground objects. Moreover, open-vocabulary relation generation with VLMs proves feasible from robot-captured images, but their advantage over closed-vocabulary relations is found to be limited.

