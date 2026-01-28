---
layout: default
title: Riddle Quest : The Enigma of Words
---

# Riddle Quest : The Enigma of Words
**arXiv**：[2601.19273v1](https://arxiv.org/abs/2601.19273) · [PDF](https://arxiv.org/pdf/2601.19273.pdf)  
**作者**：Niharika Sri Parasa, Chaitali Diwan, Srinath Srinivasa  

**一句话要点**：提出基于类比的谜语生成与评估管道，用于测试语言模型的推理覆盖和歧义处理能力。

**关键词**：谜语生成, 类比推理, 语言模型评估, 歧义处理, 语义映射

## 3 点简述
- 核心问题：谜语作为语言谜题，需要模型处理间接线索和多种有效解释，以评估其推理覆盖和歧义处理。
- 方法要点：构建包含三元组创建、语义映射、风格化生成和验证器的管道，生成类比谜语并收集所有可能答案。
- 实验或效果：案例研究表明，大型语言模型常能猜出主要答案，但常遗漏其他有效解释，突显谜语作为轻量级评估工具的价值。

## 摘要（原文）

> Riddles are concise linguistic puzzles that describe an object or idea through indirect, figurative, or playful clues. They are a longstanding form of creative expression, requiring the solver to interpret hints, recognize patterns, and draw inferences to identify the answers. In this work, we introduce a simple pipeline for creating and evaluating analogy-based riddles. The system includes a triples creator that builds structured facts about a concept, a semantic mapper that selects attributes useful for analogy, a stylized generator that turns them into riddle clues, and a validator that collects all possible answers the riddle could point to. We use this validator to study whether large language models can recover the full answer set for different riddle types. Our case study shows that while models often guess the main intended answer, they frequently miss other valid interpretations. This highlights the value of riddles as a lightweight tool for examining reasoning coverage and ambiguity handling in language models.

