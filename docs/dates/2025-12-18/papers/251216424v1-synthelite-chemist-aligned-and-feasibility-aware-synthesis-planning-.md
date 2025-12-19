---
layout: default
title: Synthelite: Chemist-aligned and feasibility-aware synthesis planning with LLMs
---

# Synthelite: Chemist-aligned and feasibility-aware synthesis planning with LLMs
**arXiv**：[2512.16424v1](https://arxiv.org/abs/2512.16424) · [PDF](https://arxiv.org/pdf/2512.16424.pdf)  
**作者**：Nguyen Xuan-Vu, Daniel Armstrong, Milena Wehrbach, Andres M Bran, Zlatko Jončev, Philippe Schwaller  

**一句话要点**：提出Synthelite框架，利用大语言模型进行化学合成规划，支持专家交互与可行性考量。

**关键词**：计算机辅助合成规划, 大语言模型, 逆合成分析, 专家交互, 化学可行性

## 3 点简述
- 现有计算机辅助合成规划框架缺乏与人类专家交互机制，限制化学家洞察整合。
- Synthelite利用大语言模型直接提出逆合成转化，通过自然语言提示允许专家干预。
- 实验显示Synthelite在约束任务中成功率高达95%，并能考虑化学可行性。

## 摘要（原文）

> Computer-aided synthesis planning (CASP) has long been envisioned as a complementary tool for synthetic chemists. However, existing frameworks often lack mechanisms to allow interaction with human experts, limiting their ability to integrate chemists' insights. In this work, we introduce Synthelite, a synthesis planning framework that uses large language models (LLMs) to directly propose retrosynthetic transformations. Synthelite can generate end-to-end synthesis routes by harnessing the intrinsic chemical knowledge and reasoning capabilities of LLMs, while allowing expert intervention through natural language prompts. Our experiments demonstrate that Synthelite can flexibly adapt its planning trajectory to diverse user-specified constraints, achieving up to 95\% success rates in both strategy-constrained and starting-material-constrained synthesis tasks. Additionally, Synthelite exhibits the ability to account for chemical feasibility during route design. We envision Synthelite to be both a useful tool and a step toward a paradigm where LLMs are the central orchestrators of synthesis planning.

