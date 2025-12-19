---
layout: default
title: Implementing a Sharia Chatbot as a Consultation Medium for Questions About Islam
---

# Implementing a Sharia Chatbot as a Consultation Medium for Questions About Islam
**arXiv**：[2512.16644v1](https://arxiv.org/abs/2512.16644) · [PDF](https://arxiv.org/pdf/2512.16644.pdf)  
**作者**：Wisnu Uriawan, Aria Octavian Hamza, Ade Ripaldi Nuralim, Adi Purnama, Ahmad Juaeni Yunus, Anissya Auliani Supriadi Putri  

**一句话要点**：提出基于强化学习与语义嵌入的伊斯兰教法咨询聊天机器人，以提升宗教知识获取与数字宣教。

**关键词**：伊斯兰教法聊天机器人, 强化学习, 语义嵌入, CRISP-DM方法论, 宗教咨询系统, 数字宣教

## 3 点简述
- 核心问题：开发一个符合伊斯兰教法的聊天机器人，用于咨询宗教问题，解决传统咨询方式的可及性与准确性限制。
- 方法要点：采用CRISP-DM方法论，集成Q-Learning强化学习和Sentence-Transformers语义嵌入，处理25,000个来自古兰经、圣训和教法裁决的问答对数据集。
- 实验或效果：原型系统在功能测试中达到87%的语义准确率，覆盖教法、信仰、礼拜和交易等主题，但存在静态学习和数据集依赖等局限性。

## 摘要（原文）

> This research presents the implementation of a Sharia-compliant chatbot as an interactive medium for consulting Islamic questions, leveraging Reinforcement Learning (Q-Learning) integrated with Sentence-Transformers for semantic embedding to ensure contextual and accurate responses. Utilizing the CRISP-DM methodology, the system processes a curated Islam QA dataset of 25,000 question-answer pairs from authentic sources like the Qur'an, Hadith, and scholarly fatwas, formatted in JSON for flexibility and scalability. The chatbot prototype, developed with a Flask API backend and Flutter-based mobile frontend, achieves 87% semantic accuracy in functional testing across diverse topics including fiqh, aqidah, ibadah, and muamalah, demonstrating its potential to enhance religious literacy, digital da'wah, and access to verified Islamic knowledge in the Industry 4.0 era. While effective for closed-domain queries, limitations such as static learning and dataset dependency highlight opportunities for future enhancements like continuous adaptation and multi-turn conversation support, positioning this innovation as a bridge between traditional Islamic scholarship and modern AI-driven consultation.

