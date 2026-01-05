---
layout: default
title: An Agentic Framework for Neuro-Symbolic Programming
---

# An Agentic Framework for Neuro-Symbolic Programming
**arXiv**：[2601.00743v1](https://arxiv.org/abs/2601.00743) · [PDF](https://arxiv.org/pdf/2601.00743.pdf)  
**作者**：Aliakbar Nafar, Chetan Chigurupati, Danial Kamali, Hamid Karimian, Parisa Kordjamshidi  

**一句话要点**：提出AgenticDomiKnowS框架，通过代理工作流将自由形式任务描述转换为神经符号程序，以简化开发过程。

**关键词**：神经符号编程, 代理工作流, 符号约束集成, 深度学习框架, 人机交互, 程序生成

## 3 点简述
- 核心问题：将符号约束集成到深度学习模型中耗时且具挑战性，现有框架依赖用户精通特定语法。
- 方法要点：使用代理工作流独立创建和测试DomiKnowS组件，支持可选人机交互以优化中间输出。
- 实验或效果：使经验用户和非用户快速构建神经符号程序，开发时间从数小时缩短至10-15分钟。

## 摘要（原文）

> Integrating symbolic constraints into deep learning models could make them more robust, interpretable, and data-efficient. Still, it remains a time-consuming and challenging task. Existing frameworks like DomiKnowS help this integration by providing a high-level declarative programming interface, but they still assume the user is proficient with the library's specific syntax. We propose AgenticDomiKnowS (ADS) to eliminate this dependency. ADS translates free-form task descriptions into a complete DomiKnowS program using an agentic workflow that creates and tests each DomiKnowS component separately. The workflow supports optional human-in-the-loop intervention, enabling users familiar with DomiKnowS to refine intermediate outputs. We show how ADS enables experienced DomiKnowS users and non-users to rapidly construct neuro-symbolic programs, reducing development time from hours to 10-15 minutes.

