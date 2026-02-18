---
layout: default
title: Automated Multi-Source Debugging and Natural Language Error Explanation for Dashboard Applications
---

# Automated Multi-Source Debugging and Natural Language Error Explanation for Dashboard Applications
**arXiv**：[2602.15362v1](https://arxiv.org/abs/2602.15362) · [PDF](https://arxiv.org/pdf/2602.15362.pdf)  
**作者**：Devendra Tata, Mona Rajhans  

**一句话要点**：提出自动化多源调试与自然语言错误解释系统，以解决仪表板应用中的调试挑战。

**关键词**：多源调试, 自然语言解释, 微服务架构, 错误关联, 大语言模型, 仪表板应用

## 3 点简述
- 核心问题：微服务架构导致错误调试困难，用户面对不透明错误信息。
- 方法要点：自动收集并关联浏览器、API、服务器等多源错误数据，利用大语言模型生成自然语言解释。
- 实验或效果：显著减少平均解决时间，提升用户体验，将错误代码转化为可操作见解。

## 摘要（原文）

> Modern web dashboards and enterprise applications increasingly rely on complex, distributed microservices architectures. While these architectures offer scalability, they introduce significant challenges in debugging and observability. When failures occur, they often manifest as opaque error messages to the end-user such as Something went wrong. This masks the underlying root cause which may reside in browser side exceptions, API contract violations, or server side logic failures. Existing monitoring tools capture these events in isolation but fail to correlate them effectively or provide intelligible explanations to non technical users. This paper proposes a novel system for Automated Multi Source Debugging and Natural Language Error Explanation. The proposed framework automatically collects and correlates error data from disparate sources such as browser, API, server logs and validates API contracts in real time, and utilizes Large Language Models to generate natural language explanations. This approach significantly reduces Mean Time to Resolution for support engineers and improves the user experience by transforming cryptic error codes into actionable insights.

