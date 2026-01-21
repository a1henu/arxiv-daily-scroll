---
layout: default
title: SCRIPTMIND: Crime Script Inference and Cognitive Evaluation for LLM-based Social Engineering Scam Detection System
---

# SCRIPTMIND: Crime Script Inference and Cognitive Evaluation for LLM-based Social Engineering Scam Detection System
**arXiv**：[2601.13581v1](https://arxiv.org/abs/2601.13581) · [PDF](https://arxiv.org/pdf/2601.13581.pdf)  
**作者**：Heedou Kim, Changsik Kim, Sanghwa Shin, Jaewoo Kang  

**一句话要点**：提出ScriptMind框架，通过犯罪脚本推理和认知评估增强LLM在社交工程诈骗检测中的性能。

**关键词**：社交工程诈骗检测, 犯罪脚本推理, LLM微调, 认知模拟评估, 多轮对话分析

## 3 点简述
- 社交工程诈骗多轮个性化欺骗挑战传统检测方法，LLM潜力未充分挖掘。
- ScriptMind集成犯罪脚本推理任务、数据集和认知模拟评估，提升小LLM检测能力。
- 实验显示，11B小LLM微调后优于GPT-4o，提高检测准确性和用户认知警觉。

## 摘要（原文）

> Social engineering scams increasingly employ personalized, multi-turn deception, exposing the limits of traditional detection methods. While Large Language Models (LLMs) show promise in identifying deception, their cognitive assistance potential remains underexplored. We propose ScriptMind, an integrated framework for LLM-based scam detection that bridges automated reasoning and human cognition. It comprises three components: the Crime Script Inference Task (CSIT) for scam reasoning, the Crime Script-Aware Inference Dataset (CSID) for fine-tuning small LLMs, and the Cognitive Simulation-based Evaluation of Social Engineering Defense (CSED) for assessing real-time cognitive impact. Using 571 Korean phone scam cases, we built 22,712 structured scammer-sequence training instances. Experimental results show that the 11B small LLM fine-tuned with ScriptMind outperformed GPT-4o by 13%, achieving superior performance over commercial models in detection accuracy, false-positive reduction, scammer utterance prediction, and rationale quality. Moreover, in phone scam simulation experiments, it significantly enhanced and sustained users' suspicion levels, improving their cognitive awareness of scams. ScriptMind represents a step toward human-centered, cognitively adaptive LLMs for scam defense.

