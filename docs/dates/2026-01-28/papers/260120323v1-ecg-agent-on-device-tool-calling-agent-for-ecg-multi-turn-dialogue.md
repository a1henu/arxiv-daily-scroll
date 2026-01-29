---
layout: default
title: ECG-Agent: On-Device Tool-Calling Agent for ECG Multi-Turn Dialogue
---

# ECG-Agent: On-Device Tool-Calling Agent for ECG Multi-Turn Dialogue
**arXiv**：[2601.20323v1](https://arxiv.org/abs/2601.20323) · [PDF](https://arxiv.org/pdf/2601.20323.pdf)  
**作者**：Hyunseung Chung, Jungwoo Oh, Daeun Kyung, Jiho Kim, Yeonsu Kwon, Min-Gyu Kim, Edward Choi  

**一句话要点**：提出ECG-Agent，首个基于LLM的工具调用代理，用于解决心电图多轮对话中的实时设备效率和精确测量理解问题。

**关键词**：心电图多轮对话, 工具调用代理, 设备端效率, PQRST间隔理解, 多模态大语言模型

## 3 点简述
- 现有心电图多模态大模型缺乏多轮对话能力、设备端效率和PQRST间隔等精确测量理解。
- 开发ECG-Agent，支持工具调用，并构建ECG-MTD数据集用于多轮对话训练与评估。
- 实验显示ECG-Agent在响应准确性上优于基线模型，设备端代理在多项评估中表现接近大型代理。

## 摘要（原文）

> Recent advances in Multimodal Large Language Models have rapidly expanded to electrocardiograms, focusing on classification, report generation, and single-turn QA tasks. However, these models fall short in real-world scenarios, lacking multi-turn conversational ability, on-device efficiency, and precise understanding of ECG measurements such as the PQRST intervals. To address these limitations, we introduce ECG-Agent, the first LLM-based tool-calling agent for multi-turn ECG dialogue. To facilitate its development and evaluation, we also present ECG-Multi-Turn-Dialogue (ECG-MTD) dataset, a collection of realistic user-assistant multi-turn dialogues for diverse ECG lead configurations. We develop ECG-Agents in various sizes, from on-device capable to larger agents. Experimental results show that ECG-Agents outperform baseline ECG-LLMs in response accuracy. Furthermore, on-device agents achieve comparable performance to larger agents in various evaluations that assess response accuracy, tool-calling ability, and hallucinations, demonstrating their viability for real-world applications.

