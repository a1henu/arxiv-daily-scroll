---
layout: default
title: Agentic LLMs as Powerful Deanonymizers: Re-identification of Participants in the Anthropic Interviewer Dataset
---

# Agentic LLMs as Powerful Deanonymizers: Re-identification of Participants in the Anthropic Interviewer Dataset
**arXiv**：[2601.05918v1](https://arxiv.org/abs/2601.05918) · [PDF](https://arxiv.org/pdf/2601.05918.pdf)  
**作者**：Tianshi Li  

**一句话要点**：展示智能体化大语言模型作为高效去匿名化工具，在Anthropic访谈数据集中重新识别科学家参与者

**关键词**：去匿名化攻击, 大语言模型代理, 隐私保护, 数据发布伦理, 交叉引用识别

## 3 点简述
- 核心问题：公开的丰富定性访谈数据在智能体化大语言模型时代面临隐私泄露风险
- 方法要点：利用现成大语言模型代理，通过自然语言提示进行网络搜索和交叉引用
- 实验效果：在24个科学家访谈中成功关联6个到具体科学工作，部分可唯一识别受访者

## 摘要（原文）

> On December 4, 2025, Anthropic released Anthropic Interviewer, an AI tool for running qualitative interviews at scale, along with a public dataset of 1,250 interviews with professionals, including 125 scientists, about their use of AI for research. Focusing on the scientist subset, I show that widely available LLMs with web search and agentic capabilities can link six out of twenty-four interviews to specific scientific works, recovering associated authors and, in some cases, uniquely identifying the interviewees. My contribution is to show that modern LLM-based agents make such re-identification attacks easy and low-effort: off-the-shelf tools can, with a few natural-language prompts, search the web, cross-reference details, and propose likely matches, effectively lowering the technical barrier. Existing safeguards can be bypassed by breaking down the re-identification into benign tasks. I outline the attack at a high level, discuss implications for releasing rich qualitative data in the age of LLM agents, and propose mitigation recommendations and open problems. I have notified Anthropic of my findings.

