---
layout: default
title: CI4A: Semantic Component Interfaces for Agents Empowering Web Automation
---

# CI4A: Semantic Component Interfaces for Agents Empowering Web Automation
**arXiv**：[2601.14790v1](https://arxiv.org/abs/2601.14790) · [PDF](https://arxiv.org/pdf/2601.14790.pdf)  
**作者**：Zhi Qiu, Jiazheng Sun, Chenxiao Xia, Jun Zheng, Xin Peng  

**一句话要点**：提出CI4A语义组件接口，为智能体优化网页自动化交互，提升任务成功率。

**关键词**：网页自动化, 语义组件接口, 智能体交互, UI组件抽象, 基准测试升级

## 3 点简述
- 核心问题：大语言模型在细粒度网页组件操作上能力有限，需改进模型接地能力。
- 方法要点：设计CI4A语义封装机制，将UI组件交互逻辑抽象为统一工具原语供智能体调用。
- 实验或效果：基于CI4A的智能体在WebArena基准测试中达到86.3%任务成功率，显著优于现有方法。

## 摘要（原文）

> While Large Language Models demonstrate remarkable proficiency in high-level semantic planning, they remain limited in handling fine-grained, low-level web component manipulations. To address this limitation, extensive research has focused on enhancing model grounding capabilities through techniques such as Reinforcement Learning. However, rather than compelling agents to adapt to human-centric interfaces, we propose constructing interaction interfaces specifically optimized for agents. This paper introduces Component Interface for Agent (CI4A), a semantic encapsulation mechanism that abstracts the complex interaction logic of UI components into a set of unified tool primitives accessible to agents. We implemented CI4A within Ant Design, an industrial-grade front-end framework, covering 23 categories of commonly used UI components. Furthermore, we developed a hybrid agent featuring an action space that dynamically updates according to the page state, enabling flexible invocation of available CI4A tools. Leveraging the CI4A-integrated Ant Design, we refactored and upgraded the WebArena benchmark to evaluate existing SoTA methods. Experimental results demonstrate that the CI4A-based agent significantly outperforms existing approaches, achieving a new SoTA task success rate of 86.3%, alongside substantial improvements in execution efficiency.

