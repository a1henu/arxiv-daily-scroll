---
layout: default
title: Next-Gen CAPTCHAs: Leveraging the Cognitive Gap for Scalable and Diverse GUI-Agent Defense
---

# Next-Gen CAPTCHAs: Leveraging the Cognitive Gap for Scalable and Diverse GUI-Agent Defense
**arXiv**：[2602.09012v1](https://arxiv.org/abs/2602.09012) · [PDF](https://arxiv.org/pdf/2602.09012.pdf)  
**作者**：Jiacheng Liu, Yaxin Luo, Jiacheng Cui, Xinyi Shang, Xiaohan Zhao, Zhiqiang Shen  

**一句话要点**：提出Next-Gen CAPTCHAs框架，利用认知差距为GUI代理时代提供可扩展防御。

**关键词**：CAPTCHA防御, GUI代理安全, 认知差距, 可扩展基准, 动态任务生成

## 3 点简述
- 核心问题：传统CAPTCHA因GUI代理进化而失效，高级模型在复杂逻辑谜题上通过率高达90%。
- 方法要点：基于数据生成管道构建可扩展基准，设计动态任务以利用人机在交互感知和决策中的认知差距。
- 实验或效果：系统能生成近乎无限的CAPTCHA实例，重新建立生物用户与人工代理的鲁棒区分。

## 摘要（原文）

> The rapid evolution of GUI-enabled agents has rendered traditional CAPTCHAs obsolete. While previous benchmarks like OpenCaptchaWorld established a baseline for evaluating multimodal agents, recent advancements in reasoning-heavy models, such as Gemini3-Pro-High and GPT-5.2-Xhigh have effectively collapsed this security barrier, achieving pass rates as high as 90% on complex logic puzzles like "Bingo". In response, we introduce Next-Gen CAPTCHAs, a scalable defense framework designed to secure the next-generation web against the advanced agents. Unlike static datasets, our benchmark is built upon a robust data generation pipeline, allowing for large-scale and easily scalable evaluations, notably, for backend-supported types, our system is capable of generating effectively unbounded CAPTCHA instances. We exploit the persistent human-agent "Cognitive Gap" in interactive perception, memory, decision-making, and action. By engineering dynamic tasks that require adaptive intuition rather than granular planning, we re-establish a robust distinction between biological users and artificial agents, offering a scalable and diverse defense mechanism for the agentic era.

