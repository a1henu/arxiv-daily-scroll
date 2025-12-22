---
layout: default
title: RecipeMasterLLM: Revisiting RoboEarth in the Era of Large Language Models
---

# RecipeMasterLLM: Revisiting RoboEarth in the Era of Large Language Models
**arXiv**：[2512.17309v1](https://arxiv.org/abs/2512.17309) · [PDF](https://arxiv.org/pdf/2512.17309.pdf)  
**作者**：Asil Kaan Bozcuoglu, Ziyuan Liu  

**一句话要点**：提出RecipeMasterLLM，利用大语言模型自动化生成机器人动作本体以增强RoboEarth知识获取。

**关键词**：大语言模型, 机器人知识图谱, 动作本体生成, 检索增强生成, 云机器人

## 3 点简述
- 核心问题：RoboEarth知识获取依赖人工构建，效率低且难以适应动态环境。
- 方法要点：基于微调LLM和检索增强生成，根据用户提示自动生成OWL动作本体。
- 实验或效果：未知，但预期能提升知识获取自动化水平和动作描述准确性。

## 摘要（原文）

> RoboEarth was a pioneering initiative in cloud robotics, establishing a foundational framework for robots to share and exchange knowledge about actions, objects, and environments through a standardized knowledge graph. Initially, this knowledge was predominantly hand-crafted by engineers using RDF triples within OWL Ontologies, with updates, such as changes in an object's pose, being asserted by the robot's control and perception routines. However, with the advent and rapid development of Large Language Models (LLMs), we believe that the process of knowledge acquisition can be significantly automated. To this end, we propose RecipeMasterLLM, a high-level planner, that generates OWL action ontologies based on a standardized knowledge graph in response to user prompts. This architecture leverages a fine-tuned LLM specifically trained to understand and produce action descriptions consistent with the RoboEarth standardized knowledge graph. Moreover, during the Retrieval-Augmented Generation (RAG) phase, environmental knowledge is supplied to the LLM to enhance its contextual understanding and improve the accuracy of the generated action descriptions.

